# Pen hover

## Overview&#x20;

All drawing tablets detect the position of the pen - **even if the pen is not touching the tablet**.

If you think about it, this is how the tablet MUST work, because the EMR sensor (aka the digitizer) is below the surface (plastic or glass) that the pen touches. So, obviously the pen is **always** detected at a distance.

This explains why we are able to place a sheet of paper or a plastic cover over the tablet, and the pen will still be detected correctly.&#x20;

## Benefits of hover

* You can reposition the pointer without drawing or clicking.
* You can see where your drawing stroke is going to be before you start the stroke
* For some art styles it is very important: [https://youtu.be/ZpcKfipVy24 ](https://youtu.be/ZpcKfipVy24)

## Hover height

The maximum distance the tablet can detect the pen is about 10mm for a modern tablet.

## Controlling the maximum hover height

There is no user control over the maximum hover height. It's something locked into the code of the  driver.

However, [**OpenTabletDriver**](../drivers/opentabletdriver/) does have plugins that let you control the hover height.



