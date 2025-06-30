# Pen pressure

## Overview

**Pressure** is the physical force being exerted on its tip. Remember that it is the pen that measure the pressure, not the tablet surface.&#x20;

## Key concepts

The **Initial Activation Force** (IAF) is the smallest amount of pressure that an EMR pen will detect and report.&#x20;

The **maximum pressure** the maximum amount of pressure that an EMR pen can detect and report.&#x20;

The **pressure range** is the range of physical force the pen is capable of sensing and outputting as pressure. In other words its lower bound is the IAF and its upper bound is the maximum pressure.

* A wide pressure range is very desirable. It contributes a lot to a good pressure experience. A wider pressure range is even more important than the number of pressure levels.

## Units

When dealing with the pressure (i.e. the force applied to the tip), the standard unit used in **gram force** abbreviated as **gf**.

You may occasionally this force described as **grams** and see the unit **g** used. This is technically incorrect, since grams are a unit of mass, not force.

## Initial activation force (IAF)

A lower IAF is good because it allows you to draw finer details better.

* Most modern EMR pens have an IAF of around 3gf - and a consider 3gf to be a very good IAF
* Modern professional pens have an IAF of <= 1gf - this is considered an excellent IAF
* Between 4gf and 6gf - I consider this to be OK and tolerable IAF.&#x20;
* Anything higher than 6gf I consider bad.

## IAF through the years

Very low IAF is not new. Wacom has been making pens for decades that have excellent low IAF. Their professional pen have had low IAF for a long time.

Here are some examples from Kuuube's measurements (using Open Tablet Driver) from his [Wacom Tablet Mastersheet](https://docs.google.com/spreadsheets/d/125LNzGmidy1gagwYUt12tRhrNdrWFHhWon7kxWY7iWU/edit?gid=1134075895#gid=1134075895).

<table><thead><tr><th width="315.79998779296875">Pen</th><th width="141.800048828125">IAF</th><th>Tablet launch year</th></tr></thead><tbody><tr><td>Wacom Pro Pen 2 (KP-504E) IAF</td><td>&#x3C;1gf</td><td>2017</td></tr><tr><td>Wacom Pro Pen Slim (KP-301E) IAF</td><td>&#x3C;1gf</td><td>?</td></tr><tr><td>Wacom Intuos4/5 Grip Pen (KP-501E)</td><td>&#x3C;1gf</td><td>2009 and 2012</td></tr><tr><td>Wacom Intuos3 Grip Pen (ZP-501E)</td><td>&#x3C;1gf</td><td>2004</td></tr><tr><td>Wacom Intuos2 Grip Pen (XP-501E)</td><td>&#x3C;1gf</td><td>2001</td></tr><tr><td>Wacom Intuos1 Grip Pen (GP-300E)</td><td>&#x3C;1gf</td><td>1998</td></tr></tbody></table>

## The importance of low IAF

Some people REALLY need that EXCELLENT IAF of <1gf.&#x20;

Others like (myself included) work fine with a 3gf IAF. I definitely notice the difference but it doesn't effect me with the kind of art I create.

## Pressure levels

Conceptually, a drawing tablet takes the pressure range and divides the range up into segments - each segment is a pressure level.

The number of pressure levels NOT decided by the pen. It is ultimately determined by the tablet itself. It can be the case that a tablet decides to have 4K pressure levels with one pen model but 8K pressure levels with another pen model.

## How many pressure levels do you need?

These days tablet brands say that they can handle 8K (8192) levels of pressure. Some tablets even claim to support 16K pressure levels.

<mark style="color:red;">**Don't get caught up in hype about pressure levels**</mark>.&#x20;

I claim you only need 2048 levels of pressure (and probably even less than that). As a quick example watch this 35 second video: [https://youtu.be/V-79hS5sRQw](https://youtu.be/V-79hS5sRQw)&#x20;

{% embed url="https://youtu.be/V-79hS5sRQw" %}

## Disabling pressure

Sometimes it is useful to disable pen pressure. For options on how to do so go here: [**Disable pen pressure**](disable-pen-pressure.md).

## Notes

* Pens - even if they are of the same model - differ a little in their pressure sensitivity
* Pressure sensors are subject to wear. Over time, you may find that a pen is less sensitive to pressure than it used to be. Though in practice, I have never experienced this in any noticable way myself.

## How EMR pens measure pressure

There are two different techniques. The newer technique involved a pressure sensor in the pen. More here: [EMR pressure detection](../technology/emr/emr-pressure-detection.md)

## OBSOLETE Rating scale for IAF and max pressure

IGNORE THIS SECTION. It is being updated and replaced with a new rating scale.

To get a broad view into how different pens handle IAF and max pressure, consult this document: [**Pen pressure range comparison**](pen-pressure-range-comparison.md)

