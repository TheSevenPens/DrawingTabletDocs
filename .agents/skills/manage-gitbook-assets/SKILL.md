---
name: manage-gitbook-assets
description: Renames generically-named markdown images based on the referring document, handles README images smartly, and moves orphaned assets to an unused folder.
---

# Manage Gitbook Assets

This skill contains tools to automatically organize, rename, and clean up images in the `.gitbook/assets` directory of this repository.

## Capabilities

The skill provides three python scripts located in `scripts/`, plus a shared
`assetrefs.py` module that all three use to parse image references:

1. **`rename_images.py`**
   - Scans all `.md` files to find image references.
   - Identifies "generic" image filenames in `.gitbook/assets` (like `image-000123.jpg`) that are uniquely referenced by a single markdown file.
   - Renames the file using the format `[document_basename]-[index].[ext]` (e.g., `tablet-evaluation-1.jpg`).
   - Updates the markdown link.

2. **`rename_readme_images.py`**
   - Processes images uniquely referenced by `README.md` files.
   - Renames them using their **parent directory's name** instead of "README" (e.g., `catalog/pens/README.md` -> `pens-[index].jpg`).
   - Updates the markdown link.

3. **`cleanup_orphans.py`**
   - Scans all `.md` files for image references.
   - Identifies images in `.gitbook/assets` that are not referenced by *any* markdown file.
   - Moves these orphaned images to `.gitbook/assets/unused/` to reduce clutter.
   - **Defaults to a dry run.** It reports what it would do and changes nothing. Pass `--apply` to actually move files.
   - Skips an orphan whose name already exists in `unused/`, rather than overwriting a different file that happens to share the name.
   - Reports **stranded** files: images sitting in `unused/` that markdown actually references. Those are left alone, since moving them would break the references pointing at the `unused/` path.

### `assetrefs.py`

Shared reference parsing, used by all three scripts so they agree on what
counts as a reference.

The scripts previously each carried their own copy of the regex
`!\[.*?\]\((.*?)\)`, which stops at the first closing parenthesis. Markdown
wraps paths containing spaces in angle brackets, and many assets here are named
like `image-000209 (1).png`, so that regex truncated them to
`image-000209 (1`. A file whose reference was mis-parsed looked unreferenced,
which meant `cleanup_orphans.py` could quarantine an image that was in use.

`assetrefs.py` also provides `resolve()`, which resolves a reference relative to
the markdown file containing it. `cleanup_orphans.py` matches on resolved paths
rather than basenames, because this repo has same-named files in different
folders — `assets/image (9).png` and `assets/unused/image (9).png` are different
images.

## Instructions for Agents

When a user asks you to clean up, organize, or manage the Gitbook assets, follow these steps:

1. Always run the scripts from the repository root: `c:\Users\seven\Documents\GitHub\DrawingTabletDocs`
2. First run `python .agents/skills/manage-gitbook-assets/scripts/rename_images.py`
3. Next run `python .agents/skills/manage-gitbook-assets/scripts/rename_readme_images.py`
4. Run `python .agents/skills/manage-gitbook-assets/scripts/cleanup_orphans.py` to see the dry-run report.
5. Review the report with the user, then run it again with `--apply` to move the orphans.
6. Check the script outputs to summarize the changes made to the user.
