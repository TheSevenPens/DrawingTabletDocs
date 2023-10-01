# Pen hover

## Overview&#x20;

In the context of drawing tablets, it means that the pen's position can be detected even if the pen doesn't touch the tablet and whether you can see the brush outline/cursor while the pen hovers.

All drawing tablets support pen hover.

## Benefits of hover

* You can reposition the pointer without drawing or clicking.
* You can see where your drawing stroke is going to be before you start the stroke

## Importance of hover

For some people seeing the brush outline/cursor during hover is very important, but for others it is isn't very important. This video demonstrates why it is important: [https://youtu.be/ZpcKfipVy24 ](https://youtu.be/ZpcKfipVy24)

## Hover height

The maximum distance the tablet can detect the pen is about 10mm for a modern tablet.

## Controlling the maximum hover height

There is no user control over the maximum hover height. It's something locked into the code of the  driver.

However, [**OpenTabletDriver**](../drivers/opentabletdriver/) does have plugins that let you control the hover height.



