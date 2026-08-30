"""Shared image-reference extraction for the gitbook asset scripts.

All three scripts previously used the regex:

    r'!\\[.*?\\]\\((.*?)\\)'

which stops at the FIRST closing parenthesis. Markdown wraps paths that
contain spaces in angle brackets, and many assets in this repo have names
like `image-000209 (1).png`, so that regex truncated them:

    ![](<../.gitbook/assets/image-000209 (1).png>)
                                            ^ match ended here

producing the basename `image-000209 (1` instead of `image-000209 (1).png`.
A file whose reference was mis-parsed looked unreferenced, so
cleanup_orphans.py would quarantine an image that was actually in use.

extract_references() below handles the angle-bracket form first, then the
plain form, then HTML <img src="...">.
"""

import re
import urllib.parse
import os

# ![alt](<path with spaces>)  -- must be tried before the plain form
RE_MD_ANGLE = re.compile(r'!\[[^\]]*\]\(\s*<([^>]+)>\s*\)')
# ![alt](path-without-spaces). Allows one level of balanced parens so that
# percent-encoded names keep their suffix, e.g. image%20(9).png
RE_MD_PLAIN = re.compile(r'!\[[^\]]*\]\(\s*((?:[^()<>\s]|\([^()]*\))+)\s*\)')
# <img src="path"> / <img src='path'>
RE_HTML = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']')


def extract_references(content):
    """Yield (start, end, url) for every image reference in `content`.

    start/end are the offsets of the url itself, so callers can splice a
    replacement in without re-matching.
    """
    refs = []
    for rx in (RE_MD_ANGLE, RE_MD_PLAIN, RE_HTML):
        for m in rx.finditer(content):
            refs.append((m.start(1), m.end(1), m.group(1)))
    refs.sort(key=lambda r: r[0])
    return refs


def extract_urls(content):
    """Just the urls, in document order."""
    return [u for _, _, u in extract_references(content)]


def clean_url(url):
    """Percent-decode and strip any #fragment or ?query."""
    return urllib.parse.unquote(url).split('#')[0].split('?')[0]


def basename_of(url):
    """Lowercased basename of a reference, for case-insensitive matching."""
    return os.path.basename(clean_url(url)).lower()


def resolve(md_path, url, repo_root):
    """Resolve a reference to an absolute path, or None if it is external.

    Path-aware resolution matters because this repo has same-named files in
    different folders -- `assets/image (9).png` and
    `assets/unused/image (9).png` are different images. Matching on basename
    alone conflates them.
    """
    u = clean_url(url)
    if u.startswith(('http://', 'https://', 'data:', 'mailto:')):
        return None
    if u.startswith('/'):
        return os.path.normpath(os.path.join(str(repo_root), u.lstrip('/')))
    return os.path.normpath(os.path.join(os.path.dirname(str(md_path)), u))
