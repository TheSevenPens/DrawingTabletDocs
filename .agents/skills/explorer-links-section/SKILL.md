---
name: explorer-links-section
description: Generates the standard "## Core links" and "## Other links" sections for a catalog notes page from DrawTabData. Core links lists each model's DrawTabData Explorer page, which is where the page's specs live, and the manufacturer's product page, store page and user manual, with one bullet per model on pages that cover several; Other links starts with a table of reviews.
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
- `--family` also sets the series link in Core links on a page with several models.
- With `--write`, it replaces the page's `## Core links` section where it is. A page without one gets it near the top: after the page's first section, or before it when the page starts with `## Other links`. Bullets in Core links that link to nothing from DrawTabData (hand-added links) are kept, below the generated ones.
- With `--write`, it also replaces the generated part of `## Other links` (the intro line and the reviews table) and keeps the hand-written links below it. With no links section yet, it inserts one after `## Overview`; `--after <heading>` picks a different section to insert after.
- A page still in an older layout (`## Official resources`, `## Links`) is converted: the sections are renamed and merged.

It reads DrawTabData from `$DRAWTABDATA_DIR` if that's set. Otherwise it uses a `../DrawTabData/data` clone, or `../DrawTabDataExplorer/data-repo/data`, the data submodule of a DrawTabDataExplorer clone next to this repo. Pull first, so the links match the live Explorer.

## What it generates

Two sections, from the tablets' `Model.Links` in DrawTabData. Don't hand-write Explorer links, product pages, store pages, manuals or reviews in the notes: add them to DrawTabData, then rerun.

### Core links

A bulleted list near the top of the page, so the key links are easy to find. Its layout depends on how many models the page covers.

**One model:**

1. **DrawTabData Explorer** — always first: a "<Model ID> specs" link to `https://thesevenpens.github.io/DrawTabDataExplorer/entity/<EntityId>`.
2. The manufacturer's own links: product page, store page, user manual (and product information).

```markdown
## Core links

* DrawTabData Explorer: [G930L specs](https://thesevenpens.github.io/DrawTabDataExplorer/entity/huion.tablet.g930l)
* [Product page](https://www.huion.com/products/inspiroy-giano)
* [Store page](https://store.huion.com/products/inspiroy-giano)
* [User manual](https://www.huion.com/manual/inspiroy-giano)
```

**Several models:** one bullet per model, so a reader finds their model first.

1. A first bullet with the links that cover every model (usually the product page), then "Series specs in DrawTabData Explorer", linking the family.
2. One bullet per model, in the order given: the model's name in bold and its ID, then its own links with short labels (Store, Manual, Product info) and, last, its Explorer page as "Specs". Links are separated by " · ".

```markdown
## Core links

* [Product page](https://www.wacom.com/en-us/products/pen-tablets/wacom-intuos-pro) · [Series specs in DrawTabData Explorer](https://thesevenpens.github.io/DrawTabDataExplorer/entity/wacom.tabletfamily.wacom_intuospro_2025)
* **Intuos Pro 2025 Small** (PTK-470): [Store](https://estore.wacom.com/en-us/wacom-intuos-pro-small-s-ptk470k0a.html) · [Manual](https://101.wacom.com/UserHelp/en/TOC/PTK470.html) · [Specs](https://thesevenpens.github.io/DrawTabDataExplorer/entity/wacom.tablet.ptk470)
* **Intuos Pro 2025 Medium** (PTK-670): [Store](https://estore.wacom.com/en-us/wacom-intuos-pro-medium-m-ptk670k0a.html) · [Manual](http://101.wacom.com/UserHelp/en/TOC/PTK670.html) · [Specs](https://thesevenpens.github.io/DrawTabDataExplorer/entity/wacom.tablet.ptk670)
* **Intuos Pro 2025 Large** (PTK-870): [Store](https://estore.wacom.com/en-us/wacom-intuos-pro-large-l-ptk870k0a.html) · [Manual](https://101.wacom.com/UserHelp/en/TOC/PTK870.html) · [Specs](https://thesevenpens.github.io/DrawTabDataExplorer/entity/wacom.tablet.ptk870)
```

The model names come from `Model.Name` in DrawTabData; to change one, fix it there. A link that covers some but not all of the models goes on each of those models' bullets.

### Other links

An intro line linking the model's family in the Explorer, then one table of reviews, newest first, with the columns Source | Link | Date. Hand-written links that aren't data (tutorials, setup videos, reddit threads, general-topic videos) go below the table, in the same section; the script keeps them. A page with no reviews has no table.

On a page with several models, a review that applies to only some of them names those model IDs after the link. DEAD links (per the link check) and links back to the page itself are left out.

Reviews come from trusted reviewers: Brad Colbow, Teoh on Tech, Parka Blogs, Aaron Rutten, Seven Pens, Gartzia Artz (Spanish), EyekooDrawsStuff and David Revoy. Other reviews the author chose for a page also count. A Seven Pens video that discusses one model in depth counts as a review. Tutorials, setup videos, reddit threads and general-topic videos are not data; they stay in the notes under `## Other links`, below the reviews table.

## Also on each notes page

Link each model ID in the page's Models table to its Explorer page: `https://thesevenpens.github.io/DrawTabDataExplorer/entity/<EntityId>`.
