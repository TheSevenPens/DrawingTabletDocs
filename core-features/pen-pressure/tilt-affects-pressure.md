# Tilt affects pressure

{% hint style="info" %}
This section has nothing to do with using tilt to draw strokes. This refers only to how the tilt of the pen affects pressure detection.
{% endhint %}

## Overview

The pen's physical tilt angle affects how pressure behaves.&#x20;

* When holding the pen vertically, the pen is the most sensitive to pressure.&#x20;
* When holding the pen tilted, the pen is less sensitive to pressure.

This is a NORMAL behavior of drawing tablet pens.

## Why this happens

Inside the pen, force from the nib is transmitted to a pressure sensor.

* When vertical, all the force on the tip of the nib hits the pressure sensor
* When tilted:
  * some of the force hits the pressure sensor
  * some of the force is transmitted to the barrel of the pen and thus is not detected

For more information about how pressure is detected: [EMR pressure detection](../../technology/emr/emr-pressure-detection.md)

## How you might notice it

When you draw a stroke with the pen held vertically you might see a thicker stroke, while at an angle you will notice a slightly thinner stroke.&#x20;

## This can be useful

Most pens are "over-reactive" at low physical pressure and give very blobby strokes at very low pressure. If you encounter those, you can tilt the pen more to minimize those blobby artifacts. More here: See: [Pen pressure instability at low pressure](drawing-at-low-physical-pressure.md)&#x20;



