---
name: explorer-links-section
description: Generates the standard "## Official resources" and "## Links" sections for a catalog notes page from DrawTabData. Official resources lists the manufacturer's product page, store page and user manual; Links starts with the row that links each model's DrawTabData Explorer page, which is where the page's specs live.
---

# Explorer links section

Catalog notes pages (`catalog/drawtabs/**/*-notes.md`) don't carry spec tables. Specs are data, and data lives in DrawTabData, shown in the [DrawTabData Explorer](https://thesevenpens.github.io/DrawTabDataExplorer/). The Explorer is the single source of truth: each notes page links to it from its `## Links` section instead of copying the specs. To fix a spec, fix it in DrawTabData.

The notes page holds usage notes: the author's own comments about specs (opinions, measurements, comparisons, context the Explorer can't show) stay in the page's prose sections, under "## Notes on specs" for spec-related context. Don't restate a value the Explorer already shows.

## Running it

From the repo root:

```bash
python .agents/skills/explorer-links-section/scripts/links_section.py catalog/drawtabs/wacom/wacom-intuos-pro-2017/wacom-pthx60-notes.md wacom.tablet.pth460 wacom.tablet.pth660 wacom.tablet.pth860 --write
```

- Pass the page, then the Explorer entity IDs of the models the page covers, in order.
- Without `--write`, it prints the sections instead of writing them.
- `--family <familyEntityId>` overrides the family link in the intro line. By default it uses the first model's family.
- With `--write`, it replaces the page's existing `## Links` section, or inserts one after `## Overview`. `--after <heading>` picks a different section to insert after.
- With `--write`, it also replaces the page's `## Official resources` section, and puts it near the top: after the page's first section, or before it when the page starts with `## Links` or `## Other links`.

It reads DrawTabData from `$DRAWTABDATA_DIR` if that's set. Otherwise it uses a `../DrawTabData/data` clone, or `../DrawTabDataExplorer/data-repo/data`, the data submodule of a DrawTabDataExplorer clone next to this repo. Pull first, so the links match the live Explorer.

## What it generates

Two sections, from the tablets' `Model.Links` in DrawTabData. Don't hand-write product pages, store pages, manuals or reviews in the notes: add them to DrawTabData, then rerun.

### Official resources

A bulleted list of the manufacturer's own links, near the top of the page so they're easy to find: product page, store page, user manual (and product information). A page with no manufacturer links has no Official resources section.

```markdown
## Official resources

* [Product page](https://www.huion.com/products/inspiroy-giano)
* [Store page](https://store.huion.com/products/inspiroy-giano)
* [User manual](https://www.huion.com/manual/inspiroy-giano)
```

### Links

One table with the columns Source | Link | Date:

1. **DrawTabData Explorer** — always the first row: one "<Model ID> specs" link per model, to `https://thesevenpens.github.io/DrawTabDataExplorer/entity/<EntityId>`.
2. Reviews, newest first.

The manufacturer's links are not repeated here; they're in Official resources.

On a page with several models, a link that applies to only some of them names those model IDs after the link, in either section. DEAD links (per the link check) and links back to the page itself are left out.

Reviews come from trusted reviewers: Brad Colbow, Teoh on Tech, Parka Blogs, Aaron Rutten, Seven Pens, Gartzia Artz (Spanish), EyekooDrawsStuff and David Revoy. Other reviews the author chose for a page also count. A Seven Pens video that discusses one model in depth counts as a review. Tutorials, setup videos, reddit threads and general-topic videos are not data; they stay in the notes under `## Other links`.

## Also on each notes page

Link each model ID in the page's Models table to its Explorer page: `https://thesevenpens.github.io/DrawTabDataExplorer/entity/<EntityId>`.
