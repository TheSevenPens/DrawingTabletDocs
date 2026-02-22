# IAF

## Overview

The **Initial Activation Force** (IAF) is the smallest amount of pressure that an EMR pen will detect.

In more simple terms: IAF is how hard you have to press to draw. High IAF means you have to press harder to draw with the pen. Low IAF means you don't have to press as hard.

Generally, people want lower IAF.

## Details

* IAF is measured in "gram-force" units (gf). Though you may see it very often described in "grams".
* IAF is determined by the pen hardware, not the tablet.
* More info: [Pen pressure](./)

## Video

{% embed url="https://www.youtube.com/watch?v=ADirKEMoczU" %}

## Initial activation force (IAF)

A lower IAF is good because it allows you to draw finer details better. To give you a better sense of what these values mean, I've ranked IAF below based on feedback I've received and what works for me.

<table><thead><tr><th width="154.5999755859375">IAF Rating</th><th width="134.79998779296875">IAF Range</th><th>Comments</th></tr></thead><tbody><tr><td>EXCELLENT</td><td>&#x3C;=1gf</td><td>Many modern Wacom pens have an IAF of &#x3C;= 1gf</td></tr><tr><td>GREAT</td><td>1gf to 2gf</td><td>Only a couple of pens are in this range</td></tr><tr><td>GOOD</td><td>2gf to 3.5gf</td><td>Most modern EMR pens have an IAF of around 3gf.</td></tr><tr><td>OK</td><td>3.5gf and 5gf</td><td>This is tolerable. Something that would be typical of a consumer-level pen.</td></tr><tr><td>BAD</td><td>≥ 5gf</td><td>Most people would not enjoy using such a pen.</td></tr></tbody></table>

Note that, some people have much stronger opinions about IAF. For example, some people think any IAF greater than 2gf is BAD IAF.

## IAF through the years

Very low IAF is not new. Wacom has been making pens for decades that have excellent low IAF. Their professional pens have had low IAF for a long time.

Here are some examples from Kuuube's measurements (using Open Tablet Driver) from his [Wacom Tablet Mastersheet](https://docs.google.com/spreadsheets/d/125LNzGmidy1gagwYUt12tRhrNdrWFHhWon7kxWY7iWU/edit?gid=1134075895#gid=1134075895).

<table><thead><tr><th width="315.79998779296875">Pen</th><th width="92.2000732421875">IAF</th><th>Tablet launch year</th></tr></thead><tbody><tr><td>Wacom Pro Pen 2 (KP-504E) IAF</td><td>&#x3C;1gf</td><td>2017</td></tr><tr><td>Wacom Pro Pen Slim (KP-301E) IAF</td><td>&#x3C;1gf</td><td>?</td></tr><tr><td>Wacom Intuos4/5 Grip Pen (KP-501E)</td><td>&#x3C;1gf</td><td>2009 and 2012</td></tr><tr><td>Wacom Intuos3 Grip Pen (ZP-501E)</td><td>&#x3C;1gf</td><td>2004</td></tr><tr><td>Wacom Intuos2 Grip Pen (XP-501E)</td><td>&#x3C;1gf</td><td>2001</td></tr><tr><td>Wacom Intuos1 Grip Pen (GP-300E)</td><td>&#x3C;1gf</td><td>1998</td></tr></tbody></table>

## The importance of low IAF

Some people REALLY need that EXCELLENT IAF of <1gf.

Others like (myself included) work fine with a 3gf IAF. I definitely notice the difference but it doesn't affect me with the kind of art I create.

## Changing the IAF

* Lowering IAF - See [Lowering the IAF](../../guides/customizing/decreasing-iaf.md)
* Increasing IAF - See [Increasing IAF](../../guides/customizing/increasing-iaf.md)

## A higher IAF can be useful

Given that there's so much focus on having a “low IAF”, it would be natural to think that always having a low IAF is good and that it is always preferable to have a lower IAF rather than a higher one. The overall sentiment is generally true but there are some exceptions and things to keep in mind.

### False pressure detection

First, as the pressure sensing mechanism in a pen gets more sensitive to enable a very low IAF, it can have unintended effects. For example those pens with super low IAF may actually say that they are detecting pressure when they are clearly not touching the tablet. Sometimes this can take the form of spurious pressure readings or it can happen more frequently and the pen can effectively draw while hovering.

### Effectively increasing IAF with the pressure curve

To compensate for these kinds of effects, you might encounter a tablet that has a pressure dead zone deliberately created by the manufacturer. This dead zone ignores a little bit of that lower pressure so that these kinds of strange artifacts are avoided.

* Note that depending on which tablet you have the pressure dead zone might be visible to you in the pressure curve that you see in the tablet driver.
* And also the dead zone might be implemented in the driver but it is not shown to you.
* And of course some tablet drivers don't implement a default dead zone at all.

More here: [Pressure curve dead zones](pen-pressure-curves/pressure-curve-dead-zones.md)

## Wispy tails on strokes

Another thing that happens when you're dealing with very low initial activation force is that it can affect the shape of your strokes at the very beginning or end. For example it can often leave little wispy tails at the beginning or end of a stroke. So in some cases you might want to create a little bit of a dead zone in your driver to avoid those wispy tails.

In some pens I've also noticed that having an extremely low IAF can cause the pen to register pressure for just one moment longer after you lift the pen off the tablet. I suspect this is due to the mechanics of a nib that is moving the pen having to overcome some friction. And so for just a moment as you lift off the tablet the very sensitive pressure mechanism is still detecting the nib pushing into it. This can create the same wispy tail effect.

## How IAF is measured

This video from XP-Pen demonstrates it [https://www.youtube.com/watch?v=QLmkI2vgfBg](https://www.youtube.com/watch?v=QLmkI2vgfBg)
