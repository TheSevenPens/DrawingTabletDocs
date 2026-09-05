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
| `visitors_3mo` | Unique human visitors over the trailing 3 months, from GitBook Insights. See *Refreshing traffic data* below. |
| `priority` | Revision priority: `high`, `medium`, `low`. Assigned from `visitors_3mo` — see *How priority is assigned*. |
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
  | awk -F/ '{sec = (NF>1 ? $1 : "(root)"); print $0 "\t" sec "\t0\t\t\t"}' \
  >> .docquality/doc-review-log.tsv
```

## How priority is assigned

Traffic on this site is extremely top-heavy, so priority follows the cumulative
share of visitors rather than a fixed visitor threshold:

| Priority | Rule | Docs | Share of traffic |
| --- | --- | --- | --- |
| `high` | Docs making up the top 50% of all traffic | 48 | 50% |
| `medium` | The next 30% | 141 | 30% |
| `low` | Everything else | 531 | 20% |

Re-derive rather than hand-edit: the numbers are the source of truth, and a doc's
band should move when its traffic does.

## Refreshing traffic data

`visitors_3mo` comes from the GitBook Insights API, filtered to `page_view`
events from non-bot visitors over `last3Months`:

```
POST /orgs/-LBUpLETf4LFiwdypBiE/sites/site_5ZpyS/insights/events/aggregate
{
  "range": "last3Months",
  "groupBy": [{"column": "urlPath"}],
  "select":  [{"column": "visitorsCount"}],
  "where":   [{"column": "eventType",  "values": ["page_view"]},
              {"column": "visitorBot", "values": [""]}],
  "order":   {"by": {"column": "visitorsCount"}, "direction": "desc"},
  "limit": 1000
}
```

Results are URL paths, not file paths. Mapping back to the repo: strip the
`/drawtab` prefix, then try `<rest>.md` and `<rest>/README.md`. Roughly 200 URLs
per pull match neither — these are pre-restructure paths still receiving traffic
through redirects, and are worth reviewing separately as a redirect-health signal.

Last pulled: 2026-09-04 (225,572 visitors across 947 URLs; 98.2% attributed).
