# Diagonal wobble

## Overview

Diagonal wobble is a regular displacement of the tablet's interpretation of the pen's position.

You might also see this referred to as "jitter."

## Companion video

I covered wobble extensively in this video about pen display accuracy: [https://youtu.be/M4rEk\_RNBrM](https://youtu.be/M4rEk_RNBrM)

## Appearance

If you slowly draw a line on a tablet with a ruler, the wobble will be apparent on diagonal lines. The diagram below exaggerates the wobble.

<figure><img src="../.gitbook/assets/image-000163.jpg" alt=""><figcaption></figcaption></figure>

## Characteristics

* The wobble can happen with any kind of pen movement, whether straight lines or curves.
* As the name suggests, the wobble is most apparent when the pen moves at an angle.
  * A 45-degree angle exhibits the most wobble.
  * A 0-degree or 90-degree angle exhibits no wobble.
  * Angles between 0 and 90 exhibit more wobble as they approach 45 degrees.
* The wobble is just more obvious with straight lines, even though the same amount of wobble occurs with curves.
* Generally, wobble becomes more visible the slower the pen is traveling.
* Some tablets exhibit the wobble even when moving the pen fast. This is less common.

## Prevalence

* Diagonal wobble is present in all drawing tablets in varying amounts.
* There is no clear pattern by price, brand, or device type for when wobble appears.

## Causes

* The wobble is NOT due to the nib wobbling in the pen.
  * The nib can be perfectly fixed in the pen and you would still observe the wobble.
  * In any case, remember that the nib is not what the tablet senses to detect position, but rather the inductor coil deeper inside the pen.
* The wobble comes from the tablet and how it senses the pen position.
* The wobble is due to how the tablet senses and interpolates the pen's position.
* Wobble is present in multiple digital pen technologies.
  * It is present with EMR pens.
  * It is also present with non-EMR technologies such as MPP, AES, and the Apple Pencil.

## Pen velocity

If there is wobble, it tends to show up at **slow speeds**. This is a bit expected.

If the wobble shows up at **faster speeds**, that is unusual.

## Tilt

Tilt **could** affect the wobble.

Most often, I have not seen tilt affect wobble. But I have one tablet where an extreme tilt angle, one that would not be used for drawing, causes massive wobble. I have not tested all my tablets at extreme tilt, so I am not sure how common this is.

## How much does wobble matter?

All tablets have wobble.

But for most tablets, you would only notice wobble when trying to find it. In other words, it will not affect normal drawing.

The real problem starts when wobble creates stroke changes you did not intend.

It also depends on what you are doing. You might notice wobble more in line art, but not notice it at all with an airbrush.

## Mitigating diagonal wobble

**OPTION 1 : Turn on smoothing**

Applications have different brush smoothing options. Explore those to see if they eliminate or reduce the wobble.

**OPTION 2 : Zoom in**

Try zooming in on the canvas, for example by 2x, and drawing the same stroke. The wobble will still be there technically, but because it happens in physical pen movement, zooming in by 2x cuts its visible effect on the stroke in half.

**OPTION 3 : Draw faster**

Wobble often appears when you draw slowly. Try drawing the stroke faster. On most tablets, this eliminates the wobble.

If your strokes are small and drawing faster would reduce control, try zooming in more. This makes your physical stroke longer while keeping it the same size on the canvas.

**OPTION 4: Use vector tools and brushes**

Instead of drawing your stroke manually, if your application supports it, use vector strokes.

## Diagonal Wobble samples

These are my wobble samples across a number of tablets.

[https://1drv.ms/f/s!Aml8i4Jd6crChTjTXo89k5jO8mb8?e=t3ijPC](https://1drv.ms/f/s!Aml8i4Jd6crChTjTXo89k5jO8mb8?e=t3ijPC)

All were created using my standard testing process: [Measuring diagonal wobble](../process/measuring/measuring-diagonal-wobble.md).

## Brand-specific notes

### XP-Pen

Some recent XP-Pen models show excessive [Diagonal wobble](diagonal-wobble.md). This is something you should check when evaluating these models. Here are examples of line wobble in recent XP-Pen tablets:

* XP Pen Deco LW at 8:06 in this video: [https://youtu.be/0VaH-UTRL7A?t=486](https://youtu.be/0VaH-UTRL7A?t=486)
* XP Pen Artist 16 (GEN2) at 7:04 in this video: [https://youtu.be/0VaH-UTRL7A?t=424](https://youtu.be/0VaH-UTRL7A?t=424)
* XP Pen Artist 12 (GEN2) 5:45 in this video: [https://youtu.be/O6OzBT7BLsA?t=345](https://youtu.be/O6OzBT7BLsA?t=345)

## Discussions

* [Huion Kamvas Pro 13 diagonal wobble discussion](https://www.reddit.com/r/huion/comments/9x3qwg/huion_kamvas_pro_13_regarding_the_infamous_line/)
