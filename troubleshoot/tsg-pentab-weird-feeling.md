# TSG: It feels "weird" to draw with a pen tablet

## Overview

Users of pen tablets (screenless) tablets often complain that drawing with one feels "weird". This can manifest as:

* A subtle feeling of "wrongness" even when drawing straight lines
* A feeling like the pen isn't matching what their hands are doing
* Strokes that look or feel "distorted"

Before you buy a pen display (screen tablet), explore what options you have.

## The most likely problem: mismatched aspect ratios

The vast majority of times someone mentions this with a pen tablet, its because there is a mismatch of aspect ratios between their pen tablet's active area and their monitor's display.

How to fix:

* First, in the tablet driver, configure the tablet to use a single monitor instead of mapping to multiple monitors
* Second, In the tablet driver, configure to the tablet to use "force proportions". [See Matching aspect ratios with Force Proportions](../guides/customizing/force-proportions.md)

