# Pen pressure

## Overview

**Pressure** is the physical force being exerted on its tip.&#x20;

## Key concepts

* The **Initial Activation Force** (IAF) is the smallest amount of pressure that an EMR pen will detect and report.  More here: [**Initial Activation Force**](initial-activation-force-iaf.md)
* The **maximum pressure** the maximum amount of pressure that an EMR pen can detect and report.&#x20;
* The **pressure range** is the range of physical force the pen is capable of sensing and outputting as pressure. In other words its lower bound is the IAF and its upper bound is the maximum pressure. More here: [**Pen pressure range**](pen-pressure-range.md)
* A tablet splits up the pressure range into a number of segments that are called **pressure levels**. Pressure levels. More here: [**Pen pressure levels**](pen-pressure-levels.md)

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

There are two different techniques. The newer technique involved a pressure sensor in the pen. More here: [EMR pressure detection](../technology/emr/emr-pressure-detection.md)

## Notes

* Pens - even if they are of the same model - differ a little in their pressure sensitivity
* Pressure sensors are subject to wear. Over time, you may find that a pen is less sensitive to pressure than it used to be. Though in practice, I have never experienced this in any noticable way myself.

