---
name: explorer-spec-tables
description: Generates the standard "## Specs" section (GitBook tabs, one column per model) for a catalog notes page from DrawTabData, so the notes' specs always match the DrawTabData Explorer.
---

# Explorer spec tables

Catalog notes pages (`catalog/drawtabs/**/*-notes.md`) don't hand-copy manufacturer specs. Each page has a `## Specs` section generated from DrawTabData, the data behind the [DrawTabData Explorer](https://thesevenpens.github.io/DrawTabDataExplorer/). To fix a spec, fix it in DrawTabData, then rerun this script. Don't edit the generated tables by hand.

Specs are data, and data lives in DrawTabData and the generated Specs section. The notes page holds usage notes: the author's own comments about specs (opinions, measurements, comparisons, context that doesn't fit a table) stay in the page's prose sections, under "## Notes on specs" for spec-related context. Don't repeat in the notes a value the Specs section already shows.

## Running it

From the repo root:

```bash
python .agents/skills/explorer-spec-tables/scripts/spec_tables.py catalog/drawtabs/wacom/wacom-intuos-pro-2017/wacom-pthx60-notes.md wacom.tablet.pth460 wacom.tablet.pth660 wacom.tablet.pth860 --write
```

- Pass the page, then the Explorer entity IDs of the models the page covers, in column order.
- Without `--write`, it prints the section instead of writing it.
- `--family <familyEntityId>` overrides the family link. By default it uses the first model's family.
- With `--write`, it replaces the page's existing `## Specs` section, or inserts one right after `## Models`. For a single-model page with no Models section, pass `--after Overview` (or another section heading) to choose where it goes. `--after END` appends it to a page that has no `## ` headings at all.

It reads DrawTabData from `$DRAWTABDATA_DIR` if that's set. Otherwise it uses `../DrawTabDataExplorer/data-repo/data`, the data submodule of a DrawTabDataExplorer clone next to this repo. Pull that clone and update its submodule first, so the tables match the live Explorer.

## What it generates

An intro line linking the Explorer family page, then GitBook tabs. Each tab is a table with one column per model, and each column header links to that model's Explorer page.

| Tab | Rows | Shown for |
|---|---|---|
| Model | Name, Released, Status | all |
| Display | Resolution, Aspect ratio, Pixel density, Panel, Lamination, Anti-glare, Color gamut, Color depth, Brightness, Peak brightness, Viewing angle, Refresh rate, Response time | pen displays, standalone |
| Digitizer | Active area, Diagonal, Aspect ratio, Pen technology, Pressure levels, Tilt, Accuracy (center), Accuracy (corner), Report rate, Density, Max hover | all |
| Pen | Included pen (Model.IncludedPen), Compatible pens (data/pen-compat, matched on brand and model ID), one per line, each linked to its Explorer page | all |
| Other inputs | Buttons, Dials, Touch rings, Touch strips, Touch | all |
| Physical | Size, Weight; plus VESA mount, Legs, Included stand on pen displays and standalone | all |
| Connectivity | Ports, Attached cable, Bluetooth; plus Wi-Fi on standalone | all |
| In the box | Contents: one item per line, from Model.IncludedInBox | all |
| Computer | OS, Processor, RAM, Storage | standalone |

Rows are fixed, so every page looks the same:
- "—" means DrawTabData has no value. Fill it in DrawTabData, not in the page.
- "None" means DrawTabData records that the tablet explicitly has none, e.g. an empty port list.

Sizes (including the active area diagonal, computed from its width and height) show mm with inches in parentheses. Accuracy shows ± mm. Aspect ratio shows the common ratio when it is exact (16:9), "≈16:9 (1.772:1)" when it is within 0.05 of one, and the plain ratio otherwise, using the same ratios and thresholds as DrawTabData. Pixel density is display pixels across the active area width, in PPI. Color gamut lists every gamut DrawTabData has, one per line. Density shows LPmm with LPI in parentheses.

## Also on each notes page

Link each model ID in the page's Models table to its Explorer page: `https://thesevenpens.github.io/DrawTabDataExplorer/entity/<EntityId>`.
