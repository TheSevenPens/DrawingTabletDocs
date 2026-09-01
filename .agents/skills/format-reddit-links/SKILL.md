---
name: format-reddit-links
description: Rewrites bare Reddit post URLs in the docs into the house format - bold "r/subreddit - Post Title" link text with the post date trailing after the link.
---

# Format Reddit Links

Turns raw Reddit URLs into readable links. A bare URL like

```
* [https://www.reddit.com/r/wacom/comments/sm7e3z/photoshop\_2022\_slider\_delay/](https://www.reddit.com/r/wacom/comments/sm7e3z/photoshop_2022_slider_delay/)
```

becomes

```
* [**r/wacom - Photoshop 2022 slider delay**](https://www.reddit.com/r/wacom/comments/sm7e3z/photoshop_2022_slider_delay/) 2022-02-06
```

The canonical hand-written examples of this format live in `guides/touch/README.md`.

## The format

`[**r/{subreddit} - {Post Title}**](url) YYYY-MM-DD`

- Link text is bold, and holds the subreddit and the exact post title.
- Subreddit casing is whatever Reddit reports (`XPpen`, `ClipStudio`, `Windowsink`) — not the lowercase spelling that appears in the URL.
- The date sits **outside** the link, after the closing paren.

### Dates are local time, not UTC

This matters and is easy to get wrong. The docs date posts the way Reddit displays them to you, in local time. Post `s3go3g` is `2022-01-14 02:22` UTC but is dated `2022-01-13` in the docs; the prose in `catalog/drawtabs/xencelabs/xencelabs-lph2412ua-notes.md` independently dates post `14y8xl7` to July 12 where UTC says the 13th.

Formatting `created_utc` with `toISOString()` shifts roughly a third of all posts a day early. The fetch snippet in the script already does the local-time conversion — don't replace it with `toISOString()`.

## Capabilities

One script, in `scripts/`:

**`format_reddit_links.py`** — scans every `.md` file in the repo and rewrites bare Reddit post links.

- **Defaults to a dry run.** Reports what it would do and changes nothing. Pass `--apply` to write.
- `--list` also prints every proposed link, for review before applying.
- `--missing` reports post URLs whose metadata isn't cached yet, and prints a ready-to-paste browser snippet to fetch them.

It only touches **raw** links — ones where the visible text is just the URL again. A link someone already gave a human-written label is left alone, so running this can't clobber hand-written text.

### `scripts/posts.tsv`

The metadata cache: `post_id`, `subreddit`, `date`, `title`, tab separated. Seeded with the 65 posts already linked from the docs.

This is the thing that makes re-runs cheap. Anything already cached is formatted **offline with no network at all** — so the usual case, adding links to posts the docs already reference elsewhere, is a single command. Only genuinely new posts need the browser step.

## Fetching metadata for new posts

Reddit is blocked from `curl`, `WebFetch`, the in-app browser, and `WebSearch`. All four were tested; all four fail. The only route that works is **Claude in Chrome** driving the user's real logged-in Chrome.

Given that, the fetch is built to be done once for many posts rather than per-post: one call to `https://www.reddit.com/api/info.json?raw_json=1&id=t3_aaa,t3_bbb,...` returns up to **100 posts at once**. Never visit posts one at a time.

Two quirks worth knowing:

- `javascript_tool` output truncates at roughly 1KB. The snippet therefore stashes results on `window.__rows` and hands them back in slices via `__chunk(0)`, `__chunk(1)`, and so on.
- Deleted posts return the title `[deleted by user]` but a still-accurate `created_utc`. The script recovers a title from the URL slug for these. A URL with no slug (`/comments/13ikmph/`) or a comment permalink (`/comments/<id>/comment/<id>/`) has nothing to recover from — those are reported as skipped and left alone.

## Deliberately out of scope

- **Bare subreddit links** (`https://www.reddit.com/r/huion/`) are not posts. They have no title or date, and several already carry their own annotations like "(16K members as of Oct 2023)". The script reports them as skipped and never rewrites them.
- **Links that already have a date** after them keep that date rather than getting a second one. The existing date wins, since it may have been checked by hand.

## Instructions for Agents

Always run from the repository root: `c:\Users\seven\Documents\GitHub\DrawingTabletDocs`

1. Dry run to see the scope:

   `python .agents/skills/format-reddit-links/scripts/format_reddit_links.py --list`

2. If it reports posts needing metadata, get the fetch snippet:

   `python .agents/skills/format-reddit-links/scripts/format_reddit_links.py --missing`

   Then, using **Claude in Chrome** (not the in-app browser — Reddit is blocked there):
   - `select_browser`, then navigate to any `reddit.com` page.
   - Run the printed snippet with `javascript_tool`.
   - Read the rows back with `__chunk(0)`, `__chunk(1)`, ... until you have them all.
   - Append those TSV rows to `scripts/posts.tsv`.
   - Close the tab when finished.

   If there are no missing posts, skip this entirely — the run is offline.

3. Review the proposed links with the user, then apply:

   `python .agents/skills/format-reddit-links/scripts/format_reddit_links.py --apply`

4. Confirm the diff is one changed line per link (`git diff --stat` should show equal insertions and deletions, and no line-ending churn), then summarize the changes for the user.
