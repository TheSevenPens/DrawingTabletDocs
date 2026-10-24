---
name: explorer-links-section
description: Generates the standard "## Core links" and "## Other links" sections for a catalog notes page from DrawTabData. Core links lists each model's DrawTabData Explorer page, which is where the page's specs live, then the manufacturer's product page, store page and user manual; Other links starts with a table of reviews.
---

# Explorer links section

Catalog notes pages (`catalog/drawtabs/**/*-notes.md`) don't carry spec tables. Specs are data, and data lives in DrawTabData, shown in the [DrawTabData Explorer](https://thesevenpens.github.io/DrawTabDataExplorer/). The Explorer is the single source of truth: each notes page links to it from its `## Core links` section instead of copying the specs. To fix a spec, fix it in DrawTabData.

The notes page holds usage notes: the author's own comments about specs (opinions, measurements, comparisons, context the Explorer can't show) stay in the page's prose sections, under "## Notes on specs" for spec-related context. Don't restate a value the Explorer already shows.

## Running it

From the repo root:

```bash
python .agents/skills/explorer-links-section/scripts/links_section.py catalog/drawtabs/wacom/wacom-intuos-pro-2017/wacom-pthx60-notes.md wacom.tablet.pth460 wacom.tablet.pth660 wacom.tablet.pth860 --write
```

- Pass the page, then the Explorer entity IDs of the models the page covers, in order.
- Without `--write`, it prints the sections instead of writing them.
- `--family <familyEntityId>` overrides the family link in the Other links intro line. By default it uses the first model's family.
- With `--write`, it replaces the page's `## Core links` section and puts it near the top: after the page's first section, or before it when the page starts with `## Other links`.
- With `--write`, it also replaces the generated part of `## Other links` (the intro line and the reviews table) and keeps the hand-written links below it. With no links section yet, it inserts one after `## Overview`; `--after <heading>` picks a different section to insert after.
- A page still in an older layout (`## Official resources`, `## Links`) is converted: the sections are renamed and merged.

It reads DrawTabData from `$DRAWTABDATA_DIR` if that's set. Otherwise it uses a `../DrawTabData/data` clone, or `../DrawTabDataExplorer/data-repo/data`, the data submodule of a DrawTabDataExplorer clone next to this repo. Pull first, so the links match the live Explorer.

## What it generates

Two sections, from the tablets' `Model.Links` in DrawTabData. Don't hand-write Explorer links, product pages, store pages, manuals or reviews in the notes: add them to DrawTabData, then rerun.

### Core links

A bulleted list near the top of the page, so the key links are easy to find:

1. **DrawTabData Explorer** — always first: one "<Model ID> specs" link per model, to `https://thesevenpens.github.io/DrawTabDataExplorer/entity/<EntityId>`.
2. The manufacturer's own links: product page, store page, user manual (and product information).

```markdown
## Core links

* DrawTabData Explorer: [G930L specs](https://thesevenpens.github.io/DrawTabDataExplorer/entity/huion.tablet.g930l)
* [Product page](https://www.huion.com/products/inspiroy-giano)
* [Store page](https://store.huion.com/products/inspiroy-giano)
* [User manual](https://www.huion.com/manual/inspiroy-giano)
```

### Other links

An intro line linking the model's family in the Explorer, then one table of reviews, newest first, with the columns Source | Link | Date. Hand-written links that aren't data (tutorials, setup videos, reddit threads, general-topic videos) go below the table, in the same section; the script keeps them. A page with no reviews has no table.

On a page with several models, a link that applies to only some of them names those model IDs after the link, in either section. DEAD links (per the link check) and links back to the page itself are left out.

Reviews come from trusted reviewers: Brad Colbow, Teoh on Tech, Parka Blogs, Aaron Rutten, Seven Pens, Gartzia Artz (Spanish), EyekooDrawsStuff and David Revoy. Other reviews the author chose for a page also count. A Seven Pens video that discusses one model in depth counts as a review. Tutorials, setup videos, reddit threads and general-topic videos are not data; they stay in the notes under `## Other links`, below the reviews table.

## Also on each notes page

Link each model ID in the page's Models table to its Explorer page: `https://thesevenpens.github.io/DrawTabDataExplorer/entity/<EntityId>`.
