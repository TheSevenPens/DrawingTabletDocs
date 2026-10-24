"""Generate the standard "## Core links" and "## Other links" sections for a catalog notes page from DrawTabData's
Model.Links.

"## Core links" is a bulleted list near the top: each model's DrawTabData Explorer page, which is where the page's specs
live, and the manufacturer's own links (product page, store page, user manual). A page with several models gets one
bullet per model, after a bullet with the links shared by all of them and the series' Explorer page. "## Other links" starts with a table of
reviews, newest first, followed by any hand-written links (tutorials, reddit threads) the section already holds.

Usage (from the repo root):
  python .agents/skills/explorer-links-section/scripts/links_section.py <notes-page.md> <entityId> [<entityId> ...] [--family <familyEntityId>] [--after <heading>] [--write]

Without --write, prints the sections. With --write, replaces the page's "## Core links" section in place, keeping
bullets that link to nothing from DrawTabData (or, with none yet, puts it after the page's first section, or before it
when that is "## Other links"), and replaces the generated part of "## Other links",
keeping its hand-written links. A legacy "## Links" or "## Official resources" section is folded in. With no links
section yet, "## Other links" goes after the section named by --after (default: Overview); with no reviews and no
hand-written links, there is no "## Other links".

Data comes from a local DrawTabData checkout: $DRAWTABDATA_DIR if set, otherwise a DrawTabData clone or the
data-repo submodule of a DrawTabDataExplorer clone next to this repo.
"""
import glob, json, os, re, sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
DATA = os.environ.get('DRAWTABDATA_DIR') or next(
    (d for d in (os.path.join(REPO_ROOT, '..', 'DrawTabData', 'data'),
                 os.path.join(REPO_ROOT, '..', 'DrawTabDataExplorer', 'data-repo', 'data')) if os.path.isdir(d)),
    os.path.join(REPO_ROOT, '..', 'DrawTabData', 'data'))
EXPLORER = 'https://thesevenpens.github.io/DrawTabDataExplorer/entity/'


def load(kind, key):
    out = {}
    for f in glob.glob(os.path.join(DATA, kind, '*.json')):
        for r in json.load(open(f, encoding='utf-8'))[key]:
            out[r['Meta']['EntityId'] if 'Meta' in r else r['EntityId']] = r
    return out


TABLETS = load('tablets', 'DrawingTablets')
FAMILIES = load('tablet-families', 'TabletFamilies')

MANUFACTURER = [
    ('MANUFACTURERPRODUCTINFO', 'Product page'),
    ('STORE', 'Store page'),
    ('MANUFACTURERUSERMANUAL', 'User manual'),
    ('PRODUCTINFO', 'Product information'),
    ('USERMANUAL', 'User manual'),
]
# the short labels on a model's own bullet in "## Core links", where the model name already says which tablet
SHORT = {
    'MANUFACTURERPRODUCTINFO': 'Product page',
    'STORE': 'Store',
    'MANUFACTURERUSERMANUAL': 'Manual',
    'PRODUCTINFO': 'Product info',
    'USERMANUAL': 'Manual',
}
DOCS_SITE = 'docs.sevenpens.com/drawtab/'


def cell(text):
    """Text that is safe inside a markdown table cell and link text."""
    return text.replace('|', '\\|').replace('[', '\\[').replace(']', '\\]').replace('\n', ' ')


def live(link):
    return (link.get('Check') or {}).get('Status') != 'DEAD'


def collect(tablets, types, page=''):
    """URL -> (first link record seen, model IDs it is attached to), in first-seen order.

    Skips DEAD links and links to this same page on the published docs site.
    """
    own = DOCS_SITE + page.replace('\\', '/').removesuffix('.md') if page else None
    out = {}
    for t in tablets:
        for link in t['Model'].get('Links', []):
            if own and own in link['URL']:
                continue
            if link.get('Type') in types and live(link):
                rec = out.setdefault(link['URL'], (link, []))
                if t['Model']['Id'] not in rec[1]:
                    rec[1].append(t['Model']['Id'])
    return out


def which(models, tablets):
    """' (PTH-460, PTH-660)' when a link covers only some of the page's models."""
    return '' if len(tablets) == 1 or len(models) == len(tablets) else f" ({', '.join(models)})"


def core(entity_ids, page='', family_id=None):
    """The "## Core links" section, as bullets.

    One model: the Explorer specs link, then the manufacturer's links. Several models: a first bullet with the links
    that cover every model and the series' Explorer page, then one bullet per model with its own links and specs.
    """
    tablets = [TABLETS[e] for e in entity_ids]
    if len(tablets) == 1:
        bullets = [f'* DrawTabData Explorer: [{cell(tablets[0]["Model"]["Id"])} specs]({EXPLORER}{entity_ids[0]})']
        for type_, label in MANUFACTURER:
            for url, (link, models) in collect(tablets, {type_}, page).items():
                bullets.append(f'* [{cell(label)}]({url})')
        return '\n'.join(['## Core links', ''] + bullets) + '\n'
    family_id = family_id or tablets[0]['Model'].get('Family')
    shared, own = [], {t['Model']['Id']: [] for t in tablets}
    for type_, label in MANUFACTURER:
        for url, (link, models) in collect(tablets, {type_}, page).items():
            if len(models) == len(tablets):
                shared.append(f'[{cell(label)}]({url})')
            else:
                for m in models:
                    own[m].append((SHORT[type_], url))
    if family_id in FAMILIES:
        shared.append(f'[Series specs in DrawTabData Explorer]({EXPLORER}{family_id})')
    bullets = [f'* {" · ".join(shared)}'] if shared else []
    for e, t in zip(entity_ids, tablets):
        model_id, name = t['Model']['Id'], t['Model'].get('Name') or ''
        title = f'**{cell(model_id)}**' if not name or model_id in name else f'**{cell(name)}** ({cell(model_id)})'
        links, seen = [], {}
        for label, url in own[model_id] + [('Specs', f'{EXPLORER}{e}')]:
            seen[label] = seen.get(label, 0) + 1
            links.append(f'[{label}{f" {seen[label]}" if seen[label] > 1 else ""}]({url})')
        bullets.append(f'* {title}: {" · ".join(links)}')
    return '\n'.join(['## Core links', ''] + bullets) + '\n'


def known_urls(entity_ids):
    """URLs the generator owns for these models: every Model.Links URL (dead or not) and Explorer pages."""
    return {link['URL'] for e in entity_ids for link in TABLETS[e]['Model'].get('Links', [])}


def hand_added_core(src, entity_ids):
    """Bullets of an existing "## Core links" section that link to none of the generated URLs."""
    m = re.search(section_re('Core links'), src, flags=re.M | re.S)
    if not m:
        return []
    known = known_urls(entity_ids)
    kept = []
    for line in m.group(0).splitlines()[1:]:
        if not re.match(r'^\s*[*-] ', line):
            continue
        urls = re.findall(r'\]\(((?:[^()\s]|\([^()\s]*\))+)\)', line)  # a URL may hold one level of ()
        if urls and not any(u in known or u.startswith(EXPLORER) for u in urls):
            kept.append(line)
    return kept


def reviews_table(entity_ids, family_id=None, page=''):
    """The generated part of "## Other links": an intro line and a table of reviews, newest first, or ''."""
    tablets = [TABLETS[e] for e in entity_ids]
    family_id = family_id or tablets[0]['Model'].get('Family')
    where = f'[DrawTabData Explorer]({EXPLORER}{family_id})' if family_id else '[DrawTabData Explorer](https://thesevenpens.github.io/DrawTabDataExplorer/)'
    reviews = list(collect(tablets, {'REVIEW'}, page).items())
    reviews.sort(key=lambda kv: kv[1][0].get('PublishDate') or '', reverse=True)
    if not reviews:
        return ''
    lines = []
    for url, (link, models) in reviews:
        author = link.get('Author') or ''
        title = link.get('Title') or (f'Review by {author}' if author else 'Review')
        lines.append(f'| {cell(author)} | [{cell(title)}]({url}){which(models, tablets)} | {link.get("PublishDate") or ""} |')
    parts = [f'The reviews in this table come from the {where}. To add or fix a link, change it in DrawTabData.', '',
             '| Source | Link | Date |', '| --- | --- | --- |'] + lines
    return '\n'.join(parts) + '\n'


def section_re(heading):
    return r'^## ' + re.escape(heading) + r'\s*$.*?(?=^## |\Z)'


# the generated part at the top of a links section: the intro line, then the table
GENERATED = re.compile(r'\A\s*(?:(?:These links|The reviews in this table) come from the \[DrawTabData Explorer\][^\n]*\n+)?(?:\|[^\n]*(?:\n|\Z))*')


def hand_written(src, heading):
    """(span, content) of a section: its hand-written links below the generated part, or (None, '')."""
    m = re.search(section_re(heading), src, flags=re.M | re.S)
    if not m:
        return None, ''
    body = m.group(0).split('\n', 1)[1] if '\n' in m.group(0) else ''
    return m.span(), GENERATED.sub('', body, count=1).strip('\n')


def write(page, entity_ids, core_text, reviews, after='Overview'):
    crlf = b'\r\n' in open(page, 'rb').read()  # keep the file's existing line endings
    src = open(page, encoding='utf-8').read()
    extra = hand_added_core(src, entity_ids)
    if extra:
        core_text = core_text.rstrip('\n') + '\n' + '\n'.join(extra) + '\n'
    # an existing "## Core links" stays where it is: mark its place, then fill it in last
    MARK = '\0CORE\0\n'
    m = re.search(section_re('Core links'), src, flags=re.M | re.S)
    if m:
        src = src[:m.start()] + MARK + src[m.end():]
    src = re.sub(section_re('Official resources'), '', src, flags=re.M | re.S)
    # "## Other links": the reviews table, then any hand-written links from "## Other links" or a legacy "## Links",
    # merged into one section where the first of them was
    found = [hand_written(src, h) for h in ('Links', 'Other links')]
    spans = sorted(span for span, _ in found if span)
    for start, end in reversed(spans):
        src = src[:start] + src[end:]
    body = '\n\n'.join(x.strip('\n') for x in [reviews] + [text for _, text in found] if x.strip())
    if spans:
        at = spans[0][0]
    elif body:
        m = re.search(section_re(after), src, flags=re.M | re.S)
        if not m:
            sys.exit(f'No links section to replace and no "## {after}" section to insert after')
        head = src[:m.end()].rstrip('\n') + '\n\n'
        src, at = head + src[m.end():], len(head)
    else:
        at = len(src)
    new = src[:at] + (f'## Other links\n\n{body}\n\n' if body else '') + src[at:]
    if MARK in new:
        new = new.replace(MARK, core_text + '\n')
    else:
        # a new "## Core links" goes near the top: after the first section, or before it when it is a links section
        heads = list(re.finditer(r'^## .*$', new, flags=re.M))
        if not heads:
            at = len(new)
        elif re.match(r'^## Other links\s*$', heads[0].group(0)):
            at = heads[0].start()
        else:
            at = heads[1].start() if len(heads) > 1 else len(new)
        new = new[:at] + core_text + '\n' + new[at:]
    new = re.sub(r'\n{3,}', '\n\n', new).rstrip('\n') + '\n'
    open(page, 'w', encoding='utf-8', newline='\r\n' if crlf else '\n').write(new)


if __name__ == '__main__':
    args = sys.argv[1:]
    do_write = '--write' in args
    args = [a for a in args if a != '--write']
    fam = None
    if '--family' in args:
        i = args.index('--family'); fam = args[i + 1]; del args[i:i + 2]
    after = 'Overview'
    if '--after' in args:
        i = args.index('--after'); after = args[i + 1]; del args[i:i + 2]
    page, ids = args[0], args[1:]
    core_text = core(ids, page, fam)
    reviews = reviews_table(ids, fam, page)
    if do_write:
        write(page, ids, core_text, reviews, after)
        print('wrote', page)
    else:
        print(core_text + ('\n## Other links\n\n' + reviews if reviews else ''))
