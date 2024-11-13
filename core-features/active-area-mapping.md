# Active area mapping

## Overview

Translating the position of the pen on the EMR sensor (AKA “the digitizer”) to a position on display is called **mapping**.

The tablet firmware reports the position of the pen on the EMR sensor using coordinates that are relative to the EMR sensor.&#x20;

The tablet driver takes coordinates from the tablet and then maps them coordinate on the display.

## Basic cases to consider

### CASE 1  a pen display

The simplest case to consider is a pen display. In this scenario the EMR sensor is directly underneath the display and both are inside the plastic shell of the tablet

In this case the active areas physical size and aspect ratio matches that of the display perfectly.

and in this case the transformation is very simple because the EMR sensor and the display have the same aspect ratio.

### Case 2 a pen tablet with one monitor

this is a somewhat more challenging case.

Because the EMR sensor and the display in the monitor need not be the same size and need not have the same aspect ratio.

But still it is possible to transform the coordinates from the tablet to a coordinate on that display.

### Case 3 a pen tablet with multiple monitors

This is a little bit of a weird case. But we have to account for it because so many people have multiple monitors with their computers.

Tablet drivers allow users to handle the situation in multiple ways.

* The tablet driver can map the EMR census coordinates to a single display.
* Another option is that the tablet driver can map the sensor coordinates to a virtual coordinate system that includes multiple displays.

&#x20;



