---
name: explorer-spec-tables
description: Generates the standard "## Specs" section (GitBook tabs, one column per model) for a catalog notes page from DrawTabData, so the notes' specs always match the DrawTabData Explorer.
---

# Explorer spec tables

Catalog notes pages (`catalog/drawtabs/**/*-notes.md`) don't hand-copy manufacturer specs. Each page has a `## Specs` section generated from DrawTabData, the data behind the [DrawTabData Explorer](https://thesevenpens.github.io/DrawTabDataExplorer/). To fix a spec, fix it in DrawTabData, then rerun this script. Don't edit the generated tables by hand.

The author's own comments about specs (opinions, measurements, comparisons) stay in the page's prose sections, not in the Specs section.

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
| Model | Name, Released, Status, Included pen | all |
| Display | Resolution, Panel, Lamination, Anti-glare, sRGB, Color depth, Brightness, Refresh rate, Response time | pen displays, standalone |
| Digitizer | Active area, Pen technology, Pressure levels, Tilt, Report rate, Density, Max hover | all |
| Other inputs | Buttons, Dials, Touch rings, Touch strips, Touch | all |
| Physical | Size, Weight; plus VESA mount, Legs, Included stand on pen displays and standalone | all |
| Connectivity | Ports, Attached cable, Bluetooth; plus Wi-Fi on standalone | all |
| Computer | OS, Processor, RAM, Storage | standalone |

Rows are fixed, so every page looks the same:
- "—" means DrawTabData has no value. Fill it in DrawTabData, not in the page.
- "None" means DrawTabData records that the tablet explicitly has none, e.g. an empty port list.

Sizes show mm with inches in parentheses. Density shows LPmm with LPI in parentheses.

## Also on each notes page

Link each model ID in the page's Models table to its Explorer page: `https://thesevenpens.github.io/DrawTabDataExplorer/entity/<EntityId>`.
