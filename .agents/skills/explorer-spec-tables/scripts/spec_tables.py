"""Generate the standard "## Specs" section for a catalog notes page from DrawTabData.

Usage (from the repo root):
  python .agents/skills/explorer-spec-tables/scripts/spec_tables.py <notes-page.md> <entityId> [<entityId> ...] [--family <familyEntityId>] [--after <heading>] [--write]

Without --write, prints the section. With --write, replaces the page's existing "## Specs"
section (up to the next "## " heading) or inserts it after the "## Models" section (or the
section named by --after, e.g. --after Overview for single-model pages; --after END appends it
to a page that has no "## " headings).

Data comes from a local DrawTabData checkout: $DRAWTABDATA_DIR if set, otherwise the
data-repo submodule of a DrawTabDataExplorer clone next to this repo.
"""
import json, glob, os, re, sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
DATA = os.environ.get('DRAWTABDATA_DIR') or os.path.join(REPO_ROOT, '..', 'DrawTabDataExplorer', 'data-repo', 'data')
EXPLORER = 'https://thesevenpens.github.io/DrawTabDataExplorer/entity/'


def load(kind, key):
    out = {}
    for f in glob.glob(os.path.join(DATA, kind, '*.json')):
        for r in json.load(open(f, encoding='utf-8'))[key]:
            out[r['Meta']['EntityId'] if 'Meta' in r else r['EntityId']] = r
    return out


TABLETS = load('tablets', 'DrawingTablets')
PENS = load('pens', 'Pens')
FAMILIES = load('tablet-families', 'TabletFamilies')

DASH = '—'


def g(t, path):
    for k in path.split('.'):
        t = t.get(k) if isinstance(t, dict) else None
    return None if t in (None, '', []) else t


def num(v, dp=1):
    v = float(v)
    return f'{v:.{dp}f}'.rstrip('0').rstrip('.')


def mm_in(*vals):
    if any(v is None for v in vals):
        return DASH
    mm = ' × '.join(num(v) for v in vals)
    inch = ' × '.join(num(float(v) / 25.4) for v in vals)
    return f'{mm} mm ({inch} in)'


def yes_no(v):
    return {'YES': 'Yes', 'NO': 'No'}.get(v, v or DASH)


def pen_eid(p):
    return p['Meta']['EntityId'] if 'Meta' in p else p['EntityId']


# pen-compat files are grouped by pen: {Brand, PenId, TabletIds}. TabletIds are Model.Id values within that brand.
PEN_BY_ID = {(p.get('Brand'), p.get('PenId')): p for p in PENS.values()}
COMPAT = {}
for _f in glob.glob(os.path.join(DATA, 'pen-compat', '*.json')):
    with open(_f, encoding='utf-8') as _fh:
        for _row in json.load(_fh)['PenCompat']:
            _pen = PEN_BY_ID.get((_row['Brand'], _row['PenId']))
            for _tid in _row['TabletIds']:
                COMPAT.setdefault((_row['Brand'], _tid), []).append(pen_eid(_pen) if _pen else _row['PenId'])


def pen_links(ids):
    if not ids:
        return DASH
    out = []
    for pid in ids:
        p = PENS.get(pid)
        label = f"{p['PenName']} ({p['PenId']})" if p else pid
        out.append(f'[{label}]({EXPLORER}{pid})')
    return '<br>'.join(out)


def pens(t):
    return pen_links(g(t, 'Model.IncludedPen') or [])


def compatible_pens(t):
    return pen_links(COMPAT.get((t['Model'].get('Brand'), t['Model'].get('Id')), []))


def tilt(t):
    v = g(t, 'Digitizer.Tilt')
    return DASH if v is None else ('None' if str(v) == '0' else f'±{v}°')


def density(t):
    v = g(t, 'Digitizer.Density')
    return DASH if v is None else f'{num(v)} LPmm ({round(float(v) * 25.4)} LPI)'


def diagonal(t):
    """Active area diagonal, computed the same way as the Explorer's DigitizerDiagonal field."""
    w, h = g(t, 'Digitizer.Dimensions.Width'), g(t, 'Digitizer.Dimensions.Height')
    if w is None or h is None:
        return DASH
    d = (float(w) ** 2 + float(h) ** 2) ** 0.5
    return f'{num(d)} mm ({num(d / 25.4)} in)'


# Same ratios and thresholds as DrawTabData's lib/aspect-ratio.ts, so the page agrees with the Explorer.
POPULAR_RATIOS = [('16:9', 16 / 9), ('16:10', 16 / 10), ('3:2', 3 / 2), ('4:3', 4 / 3), ('5:4', 5 / 4), ('1:1', 1)]


def aspect_ratio(w, h):
    """'16:9' when exact, '≈16:9 (1.772:1)' when close, else '1.432:1'."""
    if w is None or h is None or float(w) <= 0 or float(h) <= 0:
        return DASH
    ratio = max(float(w), float(h)) / min(float(w), float(h))
    name, target = min(POPULAR_RATIOS, key=lambda r: abs(ratio - r[1]))
    diff = abs(ratio - target)
    if diff <= 0.005:
        return name
    if diff <= 0.05:
        return f'≈{name} ({ratio:.3f}:1)'
    return f'{ratio:.3f}:1'


def ppi(t):
    """Pixel density, computed like the Explorer's DisplayDensity (px/mm), shown as PPI."""
    px, mm = g(t, 'Display.PixelDimensions.Width'), g(t, 'Digitizer.Dimensions.Width')
    if px is None or mm is None or float(mm) <= 0:
        return DASH
    return f'{round(float(px) / float(mm) * 25.4)} PPI'


GAMUTS = [('SRGB', 'sRGB'), ('ADOBERGB', 'Adobe RGB'), ('DCIP3', 'DCI-P3'), ('DISPLAYP3', 'Display P3'), ('NTSC', 'NTSC'), ('REC709', 'Rec. 709')]


def gamuts(t):
    have = g(t, 'Display.ColorGamuts') or {}
    out = [f'{label} {num(have[k])}%' for k, label in GAMUTS if have.get(k) not in (None, '')]
    return '<br>'.join(out) if out else DASH


def viewing_angle(t):
    h, v = g(t, 'Display.ViewingAngleHorizontal'), g(t, 'Display.ViewingAngleVertical')
    if h is None and v is None:
        return DASH
    return f"{f'{num(h)}°' if h is not None else DASH} horizontal<br>{f'{num(v)}°' if v is not None else DASH} vertical"


def accuracy(path):
    return lambda t: DASH if g(t, path) is None else f'±{num(g(t, path), 2)} mm'


def unit(path, suffix):
    return lambda t: DASH if g(t, path) is None else f'{num(g(t, path))} {suffix}'


def plain(path, fmt=str):
    return lambda t: DASH if g(t, path) is None else fmt(g(t, path))


PEN_TECH = {'PASSIVE_EMR': 'Passive EMR', 'ACTIVE_EMR': 'Active EMR', 'AES': 'AES', 'MPP': 'MPP', 'USI': 'USI'}
STATUS = {'DISCONTINUED': 'Discontinued', 'AVAILABLE': 'Available', 'ACTIVE': 'Available', 'ANNOUNCED': 'Announced'}
ANTIGLARE = {'AGFILM': 'AG film', 'ETCHEDGLASS': 'Etched glass', 'FILM': 'Film'}

DIGITIZER = [
    ('Active area', lambda t: mm_in(g(t, 'Digitizer.Dimensions.Width'), g(t, 'Digitizer.Dimensions.Height'))),
    ('Diagonal', diagonal),
    ('Aspect ratio', lambda t: aspect_ratio(g(t, 'Digitizer.Dimensions.Width'), g(t, 'Digitizer.Dimensions.Height'))),
    ('Pen technology', plain('Digitizer.Type', lambda v: PEN_TECH.get(v, v))),
    ('Pressure levels', plain('Digitizer.PressureLevels')),
    ('Tilt', tilt),
    ('Accuracy (center)', accuracy('Digitizer.AccuracyCenter')),
    ('Accuracy (corner)', accuracy('Digitizer.AccuracyCorner')),
    ('Report rate', unit('Digitizer.ReportRate', 'Hz')),
    ('Density', density),
    ('Max hover', unit('Digitizer.MaxHover', 'mm')),
]
OTHER_INPUTS = [
    ('Buttons', plain('OtherInputs.Buttons')),
    ('Dials', plain('OtherInputs.Dials')),
    ('Touch rings', plain('OtherInputs.TouchRings')),
    ('Touch strips', plain('OtherInputs.TouchStrips')),
    ('Touch', lambda t: yes_no(g(t, 'OtherInputs.Touch'))),
]
DISPLAY = [
    ('Resolution', lambda t: DASH if g(t, 'Display.PixelDimensions.Width') is None else f"{g(t, 'Display.PixelDimensions.Width')} × {g(t, 'Display.PixelDimensions.Height')}"),
    ('Aspect ratio', lambda t: aspect_ratio(g(t, 'Display.PixelDimensions.Width'), g(t, 'Display.PixelDimensions.Height'))),
    ('Pixel density', ppi),
    ('Panel', plain('Display.PanelTech')),
    ('Lamination', lambda t: yes_no(g(t, 'Display.Lamination'))),
    ('Anti-glare', plain('Display.AntiGlare', lambda v: ANTIGLARE.get(v, v))),
    ('Color gamut', gamuts),
    ('Color depth', unit('Display.ColorBitDepth', 'bits per channel')),
    ('Brightness', unit('Display.Brightness', 'cd/m²')),
    ('Peak brightness', unit('Display.BrightnessPeak', 'cd/m²')),
    ('Viewing angle', viewing_angle),
    ('Refresh rate', unit('Display.RefreshRate', 'Hz')),
    ('Response time', unit('Display.ResponseTime', 'ms')),
]
STANDALONE = [
    ('OS', plain('Standalone.OS')),
    ('Processor', plain('Standalone.Processor')),
    ('RAM', unit('Standalone.RAM', 'GB')),
    ('Storage', unit('Standalone.Storage', 'GB')),
]
PHYSICAL = [
    ('Size', lambda t: mm_in(g(t, 'Physical.Dimensions.Width'), g(t, 'Physical.Dimensions.Height'), g(t, 'Physical.Dimensions.Depth'))),
    ('Weight', unit('Physical.Weight', 'g')),
]


def vesa(t):
    v = g(t, 'Physical.VesaMount')
    if v is None:
        return DASH
    pat = g(t, 'Physical.VesaPattern')
    pat = ', '.join(pat) if isinstance(pat, list) else pat
    return yes_no(v) + (f" ({pat.replace('x', '×')})" if v == 'YES' and pat else '')


PHYSICAL_DISPLAY = PHYSICAL + [
    ('VESA mount', vesa),
    ('Legs', lambda t: yes_no(g(t, 'Physical.Legs'))),
    ('Included stand', lambda t: yes_no(g(t, 'Physical.IncludedStand'))),
]
MODEL = [
    ('Name', plain('Model.Name')),
    ('Released', lambda t: g(t, 'Model.ReleaseDate') or g(t, 'Model.ReleaseYear') or DASH),
    ('Status', plain('Model.Status', lambda v: STATUS.get(v, v.title()))),
]
PEN = [
    ('Included pen', pens),
    ('Compatible pens', compatible_pens),
]

PORT_LABELS = {
    'USB_C': 'USB-C', 'MICRO_USB': 'Micro-USB', 'MINI_USB': 'Mini-USB', 'USB_A': 'USB-A', 'USB_B': 'USB-B',
    'LIGHTNING': 'Lightning', 'HDMI': 'HDMI', 'MINI_HDMI': 'Mini HDMI', 'DISPLAYPORT': 'DisplayPort',
    'MINI_DISPLAYPORT': 'Mini DisplayPort', 'DVI': 'DVI', 'VGA': 'VGA', 'DC_POWER': 'DC power',
    'AUDIO_3_5MM': '3.5 mm audio', 'SERIAL': 'Serial', 'ADB': 'ADB', 'PROPRIETARY': 'Proprietary',
}


def port_list(items):
    """[] means explicitly none; None means unknown."""
    if items is None:
        return DASH
    if not items:
        return 'None'
    out = []
    for p in items:
        p = p if isinstance(p, dict) else {'Type': p}
        label = PORT_LABELS.get(p['Type'], p['Type'])
        out.append(f"{label} ({p['Detail']})" if p.get('Detail') else label)
    return '<br>'.join(out)


def conn(t, key):
    c = t.get('Connectivity') or {}
    return c.get(key)


def bluetooth(t):
    v = conn(t, 'Bluetooth')
    if v is None:
        return DASH
    ver = conn(t, 'BluetoothVersion')
    return yes_no(v) + (f' ({ver})' if v == 'YES' and ver else '')


CONNECTIVITY = [
    ('Ports', lambda t: port_list(conn(t, 'Ports'))),
    ('Attached cable', lambda t: port_list(conn(t, 'AttachedCable'))),
    ('Bluetooth', bluetooth),
]
CONNECTIVITY_STANDALONE = CONNECTIVITY + [('Wi-Fi', lambda t: conn(t, 'Wifi') or DASH)]


def in_box(t):
    items = g(t, 'Model.IncludedInBox')
    return '<br>'.join(str(i).replace('|', r'\|') for i in items) if items else DASH


IN_THE_BOX = [('Contents', in_box)]


def table(tablets, rows):
    head = '| | ' + ' | '.join(f"[{t['Model']['Id']}]({EXPLORER}{t['Meta']['EntityId']})" for t in tablets) + ' |'
    sep = '| --- | ' + ' | '.join('---' for _ in tablets) + ' |'
    body = [f'| {label} | ' + ' | '.join(str(fn(t)) for t in tablets) + ' |' for label, fn in rows]
    return '\n'.join([head, sep] + body)


def section(entity_ids, family_id=None):
    tablets = [TABLETS[e] for e in entity_ids]
    types = {t['Model']['Type'] for t in tablets}
    standalone = 'STANDALONE' in types
    tabs = [('Model', MODEL)]
    if types & {'PENDISPLAY', 'STANDALONE'}:
        tabs.append(('Display', DISPLAY))
    tabs += [('Digitizer', DIGITIZER), ('Pen', PEN), ('Other inputs', OTHER_INPUTS),
             ('Physical', PHYSICAL_DISPLAY if types & {'PENDISPLAY', 'STANDALONE'} else PHYSICAL),
             ('Connectivity', CONNECTIVITY_STANDALONE if standalone else CONNECTIVITY),
             ('In the box', IN_THE_BOX)]
    if standalone:
        tabs.append(('Computer', STANDALONE))
    family_id = family_id or tablets[0]['Model'].get('Family')
    where = f'[DrawTabData Explorer]({EXPLORER}{family_id})' if family_id else '[DrawTabData Explorer](https://thesevenpens.github.io/DrawTabDataExplorer/)'
    parts = ['## Specs', '',
             f'These specs come from the {where}. Click a model ID to see its full record there.', '',
             '{% tabs %}']
    for title, rows in tabs:
        parts += [f'{{% tab title="{title}" %}}', table(tablets, rows), '{% endtab %}', '']
    parts[-1] = '{% endtabs %}'
    return '\n'.join(parts) + '\n'


def write(page, text, after='Models'):
    crlf = b'\r\n' in open(page, 'rb').read()  # keep the file's existing line endings
    src = open(page, encoding='utf-8').read()
    m = re.search(r'^## Specs\s*$.*?(?=^## |\Z)', src, flags=re.M | re.S)
    if m:
        new = src[:m.start()] + text + '\n' + src[m.end():]
    elif after == 'END':
        new = src.rstrip('\n') + '\n\n' + text
    else:
        m = re.search(rf'^## {re.escape(after)}\s*$.*?(?=^## |\Z)', src, flags=re.M | re.S)
        if not m:
            sys.exit(f'No "## Specs" section to replace and no "## {after}" section to insert after (use --after)')
        new = src[:m.end()] + text + '\n' + src[m.end():]
    open(page, 'w', encoding='utf-8', newline='\r\n' if crlf else '\n').write(new)


if __name__ == '__main__':
    args = sys.argv[1:]
    do_write = '--write' in args
    args = [a for a in args if a != '--write']
    fam, after = None, 'Models'
    if '--family' in args:
        i = args.index('--family'); fam = args[i + 1]; del args[i:i + 2]
    if '--after' in args:
        i = args.index('--after'); after = args[i + 1]; del args[i:i + 2]
    page, ids = args[0], args[1:]
    text = section(ids, fam)
    if do_write:
        write(page, text, after)
        print('wrote', page)
    else:
        print(text)
