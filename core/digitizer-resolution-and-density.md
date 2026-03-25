# Digitizer resolution and density

## Background on tablet digitizers

The digitizer is the mechanism inside all EMR drawing tablets that:

* Can send power to the pen through an electromagnetic signal
* Senses a returning electromagnetic signal from the pen

From the returning electromagnetic signal the digitizer can get information about:

* The pen position
* The amount of pen tilt
* How much pressure is being applied
* The status of the buttons

Digitizers are capable of distinguishing the position of the pen with **very high precision**.

## Terminology

When dealing with this topic it's good to start off with clearing up two terms. Not everyone follows exactly what is described below, but even if they don't, it's good if we agree for the purposes of this document what these terms mean.

For any rectangle that is composed of or can be decomposed into smaller elements:

* **Resolution** refers to the dimensions - that is the width and height of the area given in some unit. For example: 1920 pixels by 1080 pixels.
* **Density** refers to how many elements are packed into a given length. For example: Pixels-per-Inch, or Lines-per-Inch.

## Digitizer density

You'll often see the density of a tablet's digitizer given in this unit: LPI (Lines per Inch).

A typical modern value is 5280 LPI. For every inch on the digitizer, the tablet can detect 5280 distinct positions.

It's easier to deal with this density when we use centimeters or millimeters.

So, 5280 LPI = 200 LPmm

NOTE: It is very common to see the density labelled as resolution.

## Digitizer resolution

The resolution of digitizers is almost NEVER listed anywhere. But of course, if you know the dimensions of the active area and the density, then the resolution is easy to calculate.

Here's an example: the Wacom Intuos Pro 2025 M has these specs.

| Spec | Imperial | Metric |
| --- | --- | --- |
| Dimensions | 10.4 x 5.8 inches | 263mm x 148mm |
| LPI | 5280 LPI | 200 LPmm |

So the resolution of the digitizer in terms of addressable elements is 52600 x 29600.

Though in practice nobody ever discusses digitizer resolution in these units.

## Relation to a display

All drawing tablets have to be used with some form of display. This takes the form of either a display in a separate monitor or a display embedded in the drawing tablet itself.

Displays have their own native resolution and size, so they have a pixel density.

Here are some common examples:

| Display | PPI |
| --- | --- |
| 27" 4K display | 166 |
| 27" 8K display | 326 |
| 16" 4K display | 283 |
| Samsung Galaxy S21 series | ~500 |
| 6th and 7th generation iPad minis | 326 |

Overall, drawing tablet digitizers are 10x more dense than even the best available displays. Even very old digitizers have a density of 2640 LPI (100 LPmm).

## Implications on buying a drawing tablet

You don't need to worry about this LPI specification when selecting a drawing tablet. You will not be able to tell the difference between 2640 LPI and 5280 LPI.

My advice is: Do not pay attention to LPI or LPmm when making a purchase decision.

## Position data sent to the computer

Even if the digitizer has an incredibly high resolution, it's a good question to ask what exact data is being sent to the computer.

The answer is simple: the digitizer sends its coordinates using the highest resolution available.

## Somewhat related but VERY important: Force proportions

Resolution and density are not important when talking about tablets. But there's another topic that involves both the tablet's digitizer and a display which you should pay a lot of attention to. This is very important for the quality of your drawing and what it will feel like to you.

Specifically, you should make sure that you enable force proportions in the tablet driver. See: [Matching aspect ratios with Force Proportions](../guides/customizing/force-proportions.md).
