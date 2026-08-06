# Pressure

## Overview

**Pressure** is the physical force being exerted on the pen tip. The pen and tablet translates that physical pressure into a logical number that sent to the tablet (i.e. the pressure level).

## Key concepts

* **The pen senses pressure**, not the tablet. The pen communicates the pressure it detects to the tablet.
* The [pressure range](pen-pressure-range.md) is the range of physical force the pen can sense.&#x20;
  * The lower bound of this range is the [Initial Activation Force (IAF)](iaf.md)&#x20;
  * The upper bound of this range is the [maximum physical pressure](maximum-physical-pressure.md)
* A tablet splits the pressure range into logical segments called [Pen pressure levels](pen-pressure-levels.md).
* The [Pen pressure response](pen-pressure-response.md) is the pen hardware's pressure behavior. It describes how a specific pen maps physical pressure to the logical pressure number sent to your computer.
* A [Pen pressure curve](pressure-curves/) processes the pressure response of a pen. You can use it to solve or mitigate some pressure problems, or to achieve certain creative effects.

## "Under pressure" video series

If you'd prefer to watch, I built the "Under Pressure" video series on YouTube that goes deep into how pressure works. It explores all these concepts in great detail.

{% embed url="https://www.youtube.com/playlist?list=PLp1wHemgDmJ2kCUS7-fzfxt4d7FETdSui" %}

## Relationship between the pen and the tablet

* The pressure sensing mechanism is in the pen, not the tablet.
* Tablets do play a role in processing pressure. They
  * Determine the number of pressure levels
  * Translate the pressure information from the pen into those levels
  * May process the pressure data before it is sent to the computer

## Units

When dealing with the pressure (i.e. the force applied to the tip), the standard unit used is **gram force** abbreviated as **gf**.

You may occasionally see this force described as **grams** and see the unit **g** used. This is technically incorrect, since grams are a unit of mass, not force.

## Disabling pressure

Sometimes it is useful to disable pen pressure. For options, go here: [Disabling pen pressure](disable-pen-pressure.md).

## How EMR pens measure pressure

There are two different techniques. The newer one uses a pressure sensor in the pen. More here: [EMR pressure detection](../../tech/emr/emr-pressure-detection.md).

## Notes

* Pens, even of the same model, differ a little in their pressure sensitivity.
* Pressure sensors are subject to wear. Over time, a pen may become less sensitive than it used to be. In practice, I have never noticed this in a meaningful way.
