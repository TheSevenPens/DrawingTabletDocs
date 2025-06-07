# Hover jitter

## Overview

In some cases for some tablets you may see that the pen position may jitter or shake when the pen his hovering. This does not interfere with drawing but may be irritating to some people.&#x20;

## Explanation

The Pen hover feature involves detecting the position of the pen, even though the pen is not touching the tablet. This raises an interesting challenge for drawing tablets. The further the pen is away from the tablet the less reliably the position of the pen can be determined. This increased distance means that nearby electromagnetic noise starts to "drown out" the signal from the pen.&#x20;

The result is that the reported pen position can "jump around" a bit during hover.

## Hover height vs hover jitter

Especially at the upper end of the hover range. Pens can often be detected even further away that the hover distance provided in the manufacturer specs, and in these locations you may encounter the most vigorous jitter.

## Prevalence

Specific digitizers families may be prone to hover jitter.
