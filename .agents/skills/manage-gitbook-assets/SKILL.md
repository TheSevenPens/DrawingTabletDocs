---
name: manage-gitbook-assets
description: Renames generically-named markdown images based on the referring document, handles README images smartly, and moves orphaned assets to an unused folder.
---

# Manage Gitbook Assets

This skill contains tools to automatically organize, rename, and clean up images in the `.gitbook/assets` directory of this repository.

## Capabilities

The skill provides three python scripts located in `scripts/`:

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

## Instructions for Agents

When a user asks you to clean up, organize, or manage the Gitbook assets, follow these steps:

1. Always run the scripts from the repository root: `c:\Users\seven\Documents\GitHub\DrawingTabletDocs`
2. First run `python .agents/skills/manage-gitbook-assets/scripts/rename_images.py`
3. Next run `python .agents/skills/manage-gitbook-assets/scripts/rename_readme_images.py`
4. Finally run `python .agents/skills/manage-gitbook-assets/scripts/cleanup_orphans.py`
5. Check the script outputs to summarize the changes made to the user.
