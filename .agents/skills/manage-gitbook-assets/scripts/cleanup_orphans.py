"""Report, and optionally quarantine, unreferenced images in .gitbook/assets.

Defaults to a DRY RUN. Pass --apply to actually move files.

    python cleanup_orphans.py            # report only
    python cleanup_orphans.py --apply    # move orphans into assets/unused/

Two things this script is careful about:

1. Reference parsing. Image references are extracted via assetrefs.py, which
   handles the `![](<path with spaces>)` form. The previous regex truncated
   those, so a referenced file could look orphaned and get quarantined.

2. Path-aware matching. A reference is resolved relative to the markdown file
   that contains it, then compared against the real asset path. Matching on
   basename alone conflates same-named files in different folders -- this repo
   has both `assets/image (9).png` and `assets/unused/image (9).png`, and they
   are different images.

It also reports STRANDED files: images sitting in assets/unused/ that markdown
actually references. Those are not orphans and are left alone; moving them
would break the references that point at the unused/ path.
"""

import os
import shutil
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import assetrefs

REPO_ROOT = Path(__file__).resolve().parents[4]
ASSETS_DIR = REPO_ROOT / ".gitbook" / "assets"
UNUSED_DIR = ASSETS_DIR / "unused"


def get_markdown_files():
    md_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'scripts-output']
        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)
    return md_files


def referenced_paths(md_files):
    """Set of absolute, normalized paths that markdown actually points at."""
    seen = set()
    for md in md_files:
        try:
            content = md.read_text(encoding='utf-8')
        except Exception:
            continue
        for url in assetrefs.extract_urls(content):
            p = assetrefs.resolve(md, url, REPO_ROOT)
            if p:
                seen.add(os.path.normcase(p))
    return seen


def main():
    apply_changes = '--apply' in sys.argv

    md_files = get_markdown_files()
    print(f"Scanning {len(md_files)} markdown files...")
    referenced = referenced_paths(md_files)
    print(f"Found {len(referenced)} distinct referenced paths.\n")

    top_level = sorted(p for p in ASSETS_DIR.iterdir() if p.is_file())
    quarantined = sorted(p for p in UNUSED_DIR.iterdir() if p.is_file()) if UNUSED_DIR.exists() else []

    orphans = [p for p in top_level if os.path.normcase(str(p)) not in referenced]
    stranded = [p for p in quarantined if os.path.normcase(str(p)) in referenced]

    # An orphan whose name already exists in unused/ cannot be moved without
    # clobbering a different file that happens to share the name.
    existing = {p.name.lower() for p in quarantined}
    collisions = [p for p in orphans if p.name.lower() in existing]
    movable = [p for p in orphans if p.name.lower() not in existing]

    print(f"top-level assets : {len(top_level)}")
    print(f"unused/ assets   : {len(quarantined)}")
    print(f"orphans          : {len(orphans)}")
    print(f"  movable        : {len(movable)}")
    print(f"  name collision : {len(collisions)}  (left in place, would overwrite)")
    print(f"stranded in unused/ (referenced, left alone): {len(stranded)}\n")

    for p in collisions:
        print(f"  COLLISION  {p.name}")
    for p in stranded:
        print(f"  STRANDED   unused/{p.name}")

    if not apply_changes:
        print(f"\nDRY RUN. {len(movable)} file(s) would move to {UNUSED_DIR}.")
        print("Re-run with --apply to move them.")
        return

    UNUSED_DIR.mkdir(exist_ok=True)
    moved = 0
    for p in movable:
        try:
            shutil.move(str(p), str(UNUSED_DIR / p.name))
            moved += 1
        except Exception as e:
            print(f"Error moving {p.name}: {e}")
    print(f"\nMoved {moved} orphaned image(s) to {UNUSED_DIR}")


if __name__ == '__main__':
    main()
