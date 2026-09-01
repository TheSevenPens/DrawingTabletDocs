# -*- coding: utf-8 -*-
"""Rewrite bare Reddit post URLs in the docs to the house link format.

    * [**r/{subreddit} - {Post Title}**](url) YYYY-MM-DD

Post titles and dates come from `posts.tsv`, a cache next to this script.
Anything already in the cache needs no network, so re-runs are usually
offline. Only genuinely new links require the browser fetch step --
run with `--missing` to get the snippet for those.

Dry run by default. Pass --apply to write.
"""
import re
import sys
import os
import io
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "posts.tsv")

# Matches a Reddit post URL and pulls out the id and the title slug.
# The slug is optional: some links are bare (/comments/13ikmph/) and some
# are comment permalinks (/comments/<id>/comment/<commentid>/).
POST_RE = re.compile(r"reddit\.com/r/([^/]+)/comments/([a-z0-9]+)(?:/([^/?#]*))?")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
# A redundant "r/wacom - " sitting just before the link; the new link text
# already carries the subreddit, so absorb it rather than leaving it doubled.
PREFIX_RE = re.compile(r"r/\w+\s*-\s*$", re.I)
DATE_RE = re.compile(r"^\s*(\d{4}-\d{2}-\d{2})")

DELETED = "[deleted by user]"


def load_cache():
    posts = {}
    if not os.path.exists(CACHE):
        return posts
    for line in io.open(CACHE, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t", 3)
        if len(parts) != 4:
            continue
        pid, sub, date, title = parts
        posts[pid] = (sub, date, title)
    return posts


def slug_title(slug):
    """Recover a readable title from a URL slug.

    Only used for posts Reddit reports as deleted, where the live title is
    gone but the slug still preserves the original wording. Capitalization
    is approximate -- slugs are lowercased by Reddit.
    """
    s = slug.replace("_", " ").strip()
    return s[:1].upper() + s[1:] if s else ""


def esc(t):
    """Escape characters that would break out of the [...] link text."""
    return (t.replace("\\", "\\\\")
             .replace("[", "\\[")
             .replace("]", "\\]")
             .replace("*", "\\*"))


def md_files(root="."):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", ".gitbook", ".agents", "node_modules")]
        for fn in sorted(filenames):
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn).replace("\\", "/")


def plan(posts):
    """Work out every rewrite. Returns (edits_by_file, skipped, missing)."""
    edits_by_file, skipped, missing = {}, [], {}

    for path in md_files():
        orig = io.open(path, encoding="utf-8").read()
        edits = []
        for m in LINK_RE.finditer(orig):
            text, url = m.group(1), m.group(2)
            if "reddit.com" not in url:
                continue
            # Only touch "raw" links, where the visible text is just the URL.
            # Links that already have a human-written label are left alone.
            if text.replace("\\", "").rstrip("/") != url.replace("\\", "").rstrip("/"):
                continue

            pm = POST_RE.search(url)
            if not pm:
                # A subreddit homepage (/r/huion/), not a post. There is no
                # title or date for these, so they are out of scope.
                skipped.append((path, url, "subreddit link, not a post"))
                continue

            pid = pm.group(2)
            slug = (pm.group(3) or "").replace("\\", "")
            if pid not in posts:
                missing.setdefault(pid, []).append(path)
                continue

            sub, date, title = posts[pid]
            if title == DELETED:
                if not slug or slug == "comment":
                    skipped.append((path, url,
                                    "deleted post, no slug to recover title"))
                    continue
                title = slug_title(slug)

            start, end = m.start(), m.end()
            line_start = orig.rfind("\n", 0, start) + 1

            pfx = PREFIX_RE.search(orig[line_start:start])
            if pfx:
                start = line_start + pfx.start()

            # Keep a date that is already there rather than appending a second
            # one. The existing date wins: it may have been checked by hand.
            dm = DATE_RE.match(orig[end:end + 12])
            if dm:
                end += dm.end()
                date = dm.group(1)

            new = "[**r/%s - %s**](%s) %s" % (
                sub, esc(title), url.replace("\\", ""), date)

            # Don't glue the link onto the preceding word.
            if start > line_start and orig[start - 1] not in " \t(":
                new = " " + new

            edits.append((start, end, new))

        if edits:
            edits_by_file[path] = (orig, edits)

    return edits_by_file, skipped, missing


def apply_edits(orig, edits):
    buf, last = [], 0
    for start, end, new in edits:
        buf.append(orig[last:start])
        buf.append(new)
        last = end
    buf.append(orig[last:])
    return "".join(buf)


FETCH_JS = """\
// Paste into the Claude in Chrome javascript tool, on any reddit.com page.
// Reddit blocks curl / WebFetch / the in-app browser, so a logged-in real
// Chrome is the only route that works. One call covers up to 100 posts.
const ids='%s';
const r = await fetch('https://www.reddit.com/api/info.json?raw_json=1&id='+ids,{credentials:'include'});
if(!r.ok) throw new Error('HTTP '+r.status);
const j = await r.json();
// Local time, NOT toISOString(): the docs date posts the way reddit shows
// them to you. Using UTC shifts roughly a third of them a day early.
const L = d => d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
window.__rows = j.data.children.map(c => [c.data.id, c.data.subreddit,
    L(new Date(c.data.created_utc*1000)),
    c.data.title.replace(/\\s+/g,' ').trim()].join('\\t'));
window.__chunk = n => window.__rows.slice(n*8, n*8+8).join('\\n');
'GOT '+window.__rows.length+' rows; read them with __chunk(0), __chunk(1), ... up to '+Math.ceil(window.__rows.length/8)"""


def main():
    args = sys.argv[1:]
    apply_mode = "--apply" in args
    posts = load_cache()

    os.chdir(os.path.join(HERE, "..", "..", "..", ".."))  # repo root

    edits_by_file, skipped, missing = plan(posts)
    n_edits = sum(len(e) for _, e in edits_by_file.values())

    if "--missing" in args:
        if not missing:
            print("No uncached posts. Everything can be formatted offline.")
            return 0
        ids = ",".join("t3_" + p for p in sorted(missing))
        print("%d post(s) not in posts.tsv:\n" % len(missing))
        for pid in sorted(missing):
            print("  %-10s %s" % (pid, missing[pid][0]))
        print("\n" + "-" * 70)
        print(FETCH_JS % ids)
        print("-" * 70)
        print("\nAppend the resulting TSV rows to:\n  %s" % CACHE)
        return 0

    print("MODE: %s" % ("APPLY" if apply_mode else "DRY RUN"))
    print("cached posts: %d" % len(posts))
    print("links to rewrite: %d in %d file(s)" % (n_edits, len(edits_by_file)))

    if "--list" in args:
        print("\n--- proposed link text ---")
        for path, (orig, edits) in sorted(edits_by_file.items()):
            for _, _, new in edits:
                print(new.strip())

    if skipped:
        print("\nskipped (%d):" % len(skipped))
        for reason, n in Counter(r for _, _, r in skipped).items():
            print("   %-42s %d" % (reason, n))

    if missing:
        print("\n%d post(s) need metadata -- re-run with --missing for the "
              "fetch snippet:" % len(missing))
        for pid in sorted(missing):
            print("   %-10s %s" % (pid, missing[pid][0]))

    if apply_mode:
        for path, (orig, edits) in edits_by_file.items():
            # newline="" preserves the file's existing line endings; this repo
            # stores LF in the working tree and git normalizes on checkout.
            io.open(path, "w", encoding="utf-8", newline="").write(
                apply_edits(orig, edits))
        print("\nWrote %d file(s)." % len(edits_by_file))
    elif n_edits:
        print("\nNothing written. Re-run with --apply to write.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
