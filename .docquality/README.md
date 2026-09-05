# Doc quality tracking

Working files for tracking documentation review status. **Not published content** —
this folder is a dot-directory, so GitBook's git sync ignores it (same as `.agents/`).

## `doc-review-log.tsv`

One row per content doc in the repo. Tab-separated so it opens cleanly in a
spreadsheet and stays greppable / diffable in git.

| Column | Meaning |
| --- | --- |
| `path` | Repo-relative path to the doc. |
| `section` | Top-level folder, for filtering and bulk priority assignment. |
| `priority` | Revision priority: `high`, `medium`, `low`. Blank = not yet triaged. |
| `last_revised` | Date (`YYYY-MM-DD`) of the last *thoughtful content revision*. Blank = never revised under this process. Typo fixes, link fixes, and GitBook sync commits do not count. |
| `notes` | Free text — what was done, or what still needs doing. |

Excluded from the log: `SUMMARY.md` (table of contents, not content) and
everything under `.agents/`.

### Regenerating after adding docs

Append new files without disturbing existing rows:

```bash
comm -13 <(cut -f1 .docquality/doc-review-log.tsv | tail -n +2 | sort) \
         <(find . -name '*.md' -not -path './.git/*' -not -path './.agents/*' \
              -not -path './.docquality/*' -not -name 'SUMMARY.md' \
            | sed 's|^\./||' | sort) \
  | awk -F/ '{sec = (NF>1 ? $1 : "(root)"); print $0 "\t" sec "\t\t\t"}' \
  >> .docquality/doc-review-log.tsv
```
