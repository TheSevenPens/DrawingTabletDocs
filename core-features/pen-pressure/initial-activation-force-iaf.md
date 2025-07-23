# Initial activation force (IAF)

## Overview

The **Initial Activation Force** (IAF) is the smallest amount of pressure that an EMR pen will detect and report.&#x20;

More info: [**Pen pressure**](./)&#x20;

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

## Tweaking the IAF

The IAF is a physical property of the pen, so that physical behaviors can't be lowered or raised. However by using a pressure curve with a dead zone, you can effectively increase the IAF.  More here: [**Pen pressure dead zone**](pen-pressure-dead-zone.md)

## A higher IAF can be useful

Given that there's so much focus on having a “low IAF”, it would be natural to think that always having a low IAF is good and that it is always preferable to have a lower IAF rather than a higher one. The overall sentiment is generally true but there are some exceptions and things to keep in mind.

### False pressure detection

First, as the pressure sensing mechanism in a pen gets more sensitive to enable a very low IAF, it can have unintended effects. For example those pens with super low IAF may actually say that they are detecting pressure when they are clearly not touching the tablet. Sometimes this can take the form of spurious pressure readings or it can happen more frequently and the pen can effectively draw while hovering.

### Effectively increasing IAF with the pressure curve

To compensate for these kinds of effects you, You might encounter a tablet that has a pressure dead zone deliberately created by the manufacturer. This dead zone ignores a little bit of that lower pressure so that these kinds of strange artifacts are avoided.

* Note that depending on which tablet you have the pressure dead zone might be visible to you in the pressure curve that you see in the tablet driver.
* And also the dead zone might be implemented in the driver but it is not shown to you.
* And of course some tell the drivers don't implement default dead zone at all.

More here: [**Pen pressure dead zone**](pen-pressure-dead-zone.md)

## Wispy tails on strokes

another thing that happens when you're dealing with very low initial activation force is that it can affect the shape of your strokes at the very beginning or ends. For example it can often leave little wispy tails at the beginning or end of a stroke.  So in some cases you might want to create a little bit of a dead zone in your driver to avoid those wispy tails.

In some pens I've also noticed that having an extremely low IAF can cause the pen to register pressure for just one moment longer after you lift the pen off the tablet. I suspect this is due to the mechanics of a nib that is moving the pen having to overcome some friction. And so for just a moment as you lift off the tablet the very sensitive pressure mechanism is still detecting the nib pushing into it. This can create the same wispy tail effect.

## How IAF is measured

This video from XP-Pen demonstrates it [https://www.youtube.com/watch?v=QLmkI2vgfBg](https://www.youtube.com/watch?v=QLmkI2vgfBg)



.
