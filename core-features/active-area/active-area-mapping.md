# Active area mapping

## Overview

Mapping is how the tablet driver translated the position of the pen on the EMR sensor (AKA “the digitizer”) to a position on display.



### Mapping for pen displays

For pen displays, mapping is relatively straightforward because essentially the digitizer and the display are embedded in the same device.

## Mapping for pen tablets

Active area mapping is a surprisingly complex topic, because it has to work in a number of different situations (single monitor, multiple monitors, etc.) AND is highly configurable AND and can even change dynamically at the press of a button.

For pen tablets (screenless tablets) mapping is the most complex, since the digitizer and the display are separate devices.

### Dealing with mismatched aspect ratios

Because the tablet's active area and the display may have different aspect ratios, distortion can be introduced unless you enable Force Proportions: [Match aspect ratios with Force proportions](../../guides/customizing/matching-aspect-ratios.md)

## Display Toggle for pen tablets and multiple monitors

When multiple monitors are being used, you can have the tablet switch between mapping to each monitor at the click of a button. See: [Display toggle](display-toggle.md)

