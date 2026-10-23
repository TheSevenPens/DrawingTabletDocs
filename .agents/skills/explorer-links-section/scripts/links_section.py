"""Generate the standard "## Links" section for a catalog notes page from DrawTabData's Model.Links.

The first row always links each model's DrawTabData Explorer page, which is where the page's specs live.

Usage (from the repo root):
  python .agents/skills/explorer-links-section/scripts/links_section.py <notes-page.md> <entityId> [<entityId> ...] [--family <familyEntityId>] [--after <heading>] [--write]

Without --write, prints the section. With --write, replaces the page's existing "## Links" section (up to the next
"## " heading), or inserts it after the section named by --after (default: Overview).

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

MANUFACTURER = [
    ('MANUFACTURERPRODUCTINFO', 'Product page'),
    ('STORE', 'Store page'),
    ('MANUFACTURERUSERMANUAL', 'User manual'),
    ('PRODUCTINFO', 'Product information'),
    ('USERMANUAL', 'User manual'),
]
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


def section(entity_ids, family_id=None, page=''):
    tablets = [TABLETS[e] for e in entity_ids]
    family_id = family_id or tablets[0]['Model'].get('Family')
    where = f'[DrawTabData Explorer]({EXPLORER}{family_id})' if family_id else '[DrawTabData Explorer](https://thesevenpens.github.io/DrawTabDataExplorer/)'
    parts = ['## Links', '', f'These links come from the {where}. To add or fix a link, change it in DrawTabData.', '']

    def row(source, text, url, date, models):
        return f'| {cell(source)} | [{cell(text)}]({url}){which(models, tablets)} | {date or ""} |'

    explorer = ', '.join(f'[{cell(t["Model"]["Id"])} specs]({EXPLORER}{e})' for e, t in zip(entity_ids, tablets))
    maker = [f'| DrawTabData Explorer | {explorer} |  |']
    for type_, label in MANUFACTURER:
        for url, (link, models) in collect(tablets, {type_}, page).items():
            maker.append(row(link.get('Author') or '', label, url, link.get('PublishDate'), models))
    reviews = list(collect(tablets, {'REVIEW'}, page).items())
    reviews.sort(key=lambda kv: kv[1][0].get('PublishDate') or '', reverse=True)
    lines = []
    for url, (link, models) in reviews:
        author = link.get('Author') or ''
        title = link.get('Title') or (f'Review by {author}' if author else 'Review')
        lines.append(row(author, title, url, link.get('PublishDate'), models))
    # one table: the Explorer, then the manufacturer's links, then reviews newest first
    parts += ['| Source | Link | Date |', '| --- | --- | --- |'] + maker + lines + ['']
    return '\n'.join(parts).rstrip('\n') + '\n'


def write(page, text, after='Overview'):
    crlf = b'\r\n' in open(page, 'rb').read()  # keep the file's existing line endings
    src = open(page, encoding='utf-8').read()
    m = re.search(r'^## Links\s*$.*?(?=^## |\Z)', src, flags=re.M | re.S)
    if m:
        new = src[:m.start()] + text + '\n' + src[m.end():]
    else:
        m = re.search(r'^## ' + re.escape(after) + r'\s*$.*?(?=^## |\Z)', src, flags=re.M | re.S)
        if not m:
            sys.exit(f'No "## Links" section to replace and no "## {after}" section to insert after')
        new = src[:m.end()].rstrip('\n') + '\n\n' + text + '\n' + src[m.end():]
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
    text = section(ids, fam, page)
    if do_write:
        write(page, text, after)
        print('wrote', page)
    else:
        print(text)
