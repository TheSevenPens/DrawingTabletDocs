# Hover jitter

## Overview

In some cases, on some tablets, the pen position may jitter or shake while the pen is hovering. This does not interfere with drawing, but it may be irritating.

## Explanation

The pen hover feature involves detecting the position of the pen even though it is not touching the tablet. This creates an interesting challenge. The farther the pen is from the tablet, the less reliably its position can be determined. At greater distances, nearby electromagnetic noise starts to "drown out" the signal from the pen.

The result is that the reported pen position can "jump around" a bit during hover.

## Hover height vs hover jitter

Especially at the upper end of the hover range, pens can often be detected even farther away than the hover distance listed in the manufacturer specs. In those locations, you may encounter the strongest jitter.

## Prevalence

Specific digitizer families may be prone to hover jitter.
