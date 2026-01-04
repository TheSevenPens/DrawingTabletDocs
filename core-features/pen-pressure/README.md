# Pen pressure

## Overview

**Pressure** is the physical force being exerted on its tip.&#x20;

## Key concepts

* **The pen senses pressure**, not the tablet. The pen communicates the pressure it detects to the tablet.
* The [**Initial Activation Force**](iaf.md) is the smallest amount of pressure that an EMR pen will detect and report.  More here:&#x20;
* The [**Pen pressure range**](pen-pressure-range.md) is the range of physical force the pen is capable of sensing and outputting as pressure. In other words its lower bound is the IAF and its upper bound is the **maximum pressure**.&#x20;
* A tablet splits up the pressure range into a number of segments that are called [**Pen pressure levels**](pen-pressure-levels.md).
* The [**pen pressure response**](pen-pressure-response.md) is the pen hardware's "pressure behavior" - how a specific pen maps the physical pressure (how hard you are pressing down) to a logical pressure number that is sent to your computer. &#x20;
* A [**pressure curve**](pen-pressure-curves/) is a way of modifying or processing the pressure pressure response of a pen. You can do this to solve solve or mitigate some kinds of pressure problems or to achieve certain kinds of creative effects.
* A [**pressure dead zone**](pen-pressure-dead-zone.md) is a ways of using a a pressure curve to effectively increase the IAF.
* The vast majority of drawing tablet pens are too-sensitive to small changes in physical pressure near the IAF. This means there is some [**pressure instability at low pressure**](drawing-at-low-physical-pressure.md). You can address this by using [**pressure curves**](pen-pressure-curves/) or **pressure smoothing**.
* [**Tilt affects pressure**](tilt-affects-pressure.md). The pen is more sensitive when it is held - perpendicular to the tablet surface.

## "Under pressure" video series

If you'd prefer to watch, I built the "Under Pressure" video series on YouTube that goes deep into how pressure works. It explores all these concepts in great detail.

{% embed url="https://www.youtube.com/playlist?list=PLp1wHemgDmJ2kCUS7-fzfxt4d7FETdSui" %}

## Relationship between the pen and the tablet

* The pressure sensing mechanism is in the Pen, not the tablet.
* Tablets do play a role in processing pressure. Tablets
  * Determine the number of pressure levels
  * Translate the pressure information from the pen into those levels
  * May process the pressure data before it is sent to the computer

## Units

When dealing with the pressure (i.e. the force applied to the tip), the standard unit used in **gram force** abbreviated as **gf**.

You may occasionally this force described as **grams** and see the unit **g** used. This is technically incorrect, since grams are a unit of mass, not force.

## Disabling pressure

Sometimes it is useful to disable pen pressure. For options on how to do so go here: [**Disable pen pressure**](disable-pen-pressure.md).

## How EMR pens measure pressure

There are two different techniques. The newer technique involved a pressure sensor in the pen. More here: [EMR pressure detection](../../technology/emr/emr-pressure-detection.md)

## Notes

* Pens - even if they are of the same model - differ a little in their pressure sensitivity
* Pressure sensors are subject to wear. Over time, you may find that a pen is less sensitive to pressure than it used to be. Though in practice, I have never experienced this in any noticable way myself.

