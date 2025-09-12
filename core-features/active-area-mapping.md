# Active area mapping

## Overview

Mapping is how the tablet driver translated the position of the pen on the EMR sensor (AKA “the digitizer”) to a position on display.



### Mapping for pen displays

For pen displays, mapping is relatively straightforward because essentially the digitizer and the display are embedded in the same device.

## Mapping for pen tablets

Active area mapping is a surprisingly complex topic, because it has to work in a number of different situations (single monitor, multiple monitors, etc.) AND is highly configurable AND and can even change dynamically at the press of a button.

For pen tablets (screenless tablets) mapping is the most complex, since the digitizer and the display are separate devices.

### Dealing with mismatched aspect ratios

Because the tablet's active area and the display may have different aspect ratios, distortion can be introduced unless you enable Force Proportions: [Match aspect ratios with Force proportions](../guides/customizing-your-experience/match-aspect-ratios-with-force-proportions.md)

## Display Toggle for pen tablets and multiple monitors

With a pen tablet, you may have multiple monitors. Mapping to both will either create a lot of distortion. You can avoid the distortion with force proportions, but then you lose a lot of active area on the tablet. An alternative is to setup your pen tablet to swap between which monitor it is mapped to by pressing a tablet or pen button. This is called "Display Toggle".&#x20;
