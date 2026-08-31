# Calibrating pressure

## Overview

For other calibration types, see [Calibrating a drawing tablet](calibrating-color.md).

Use a pressure curve to tune a pen's pressure response in three ways.

These adjustments work independently. Some may be unnecessary for your needs.

## Which pressure curve

You can use these techniques with any pressure curve, including driver and app curves. Use the driver curve, because these adjustments affect the pen's overall behavior.

## Tuning maximum physical pressure

Some pens just require too much force to hit 100% pressure. The solution is to adjust the upper right of the pressure curve and move it slightly to the left. See: [Lowering maximum physical pressure](lowering-max-physical-pressure.md)

If the maximum pressure already works for you, then there is nothing to do.

Raising the maximum physical pressure is NOT POSSIBLE.

## Adjusting the pressure response

First, adjust the maximum physical pressure if needed.

Understand these concepts:

* **Reported pressure** — the pressure percentage shown by the driver.
* **Perceptual pressure** — the pressure percentage your hand and brain perceive.

### STEP 1: Synchronize maximum reported and perceptual pressure

In the pressure curve editor, press down until the pressure reaches nearly 100%. Aim for at least 95%.

<figure><img src="../../.gitbook/assets/image (1).png" alt="" width="375"><figcaption></figcaption></figure>

Ideally, close your eyes and press down. When you open them, the driver should show the maximum reported pressure.

At this point your perceptual pressure and the reported pressure are in close agreement.

### STEP 2: Train your hand and brain to recognize perceptual 50% pressure

Press down until your brain perceives half the pressure from step 1.

Now check the pressure reported by the driver. It may not correspond to 50%. It may read 70% or 80%.

At this stage perceptual 50% clearly does not match the reported pressure. We will fix that in the next step.

### STEP 3: Match perceptual 50% with reported 50%

Keep pressing at your perceptual 50%. Then adjust the pressure curve incrementally. The driver should eventually report 50% for perceptual 50%.

<figure><img src="../../.gitbook/assets/image (2).png" alt="" width="375"><figcaption></figcaption></figure>

Here is the curve for one of my pens.

<figure><img src="../../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure>

### Tweaking the curve

Treat this curve as a good starting point. It is not necessarily the definitive answer. Experiment from there.

## Raising the IAF

Sometimes, a low IAF causes problems:

* The pen may draw when it is not touching the tablet
* The pen may produce hooks when you start a stroke

Move the lower-left corner of the pressure curve to increase the IAF. See [Raising IAF](raising-iaf.md).
