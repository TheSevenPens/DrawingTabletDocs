# Hover

## Overview

All drawing tablets detect the position of the pen, **even when the pen is not touching the tablet**.

This is how the tablet must work, because the EMR sensor, also called the digitizer, sits below the surface that the pen touches. So the pen is **always** detected at a distance.

This explains why we are able to place a sheet of paper or a plastic cover over the tablet, and the pen will still be detected correctly.

## Benefits of hover

* You can reposition the pointer without drawing or clicking.
* You can see where your stroke will go before you start it.
* For some art styles it is very important: [https://youtu.be/ZpcKfipVy24](https://youtu.be/ZpcKfipVy24)

## Some people don't like hover

This is rare, but a small number of people do not like seeing the pointer move as they move the pen over the tablet surface.

## Hover height

The maximum distance a modern EMR tablet can detect the pen is about 10 mm.

## What influences the hover height

Even though the typical hover height is 10 mm, the EMR sensor itself can detect the pen at a much greater distance, sometimes around 20 mm. But the greater the distance, the less accurately the pen position can be determined. For that reason, tablet drivers enforce a lower maximum hover height.

## Controlling the maximum hover height

Drivers from tablet manufacturers offer no user control over the maximum hover height. That value is locked into the driver. However, [OpenTabletDriver](../../guides/drivers/opentabletdriver/) has plugins that let you control hover height.

## Turning off hover

With a drawing tablet, hover is an intrinsic part of how the tablet works. There is no way to disable it. In some apps, you may be able to hide the pointer when using the pen, which can achieve a similar effect.
