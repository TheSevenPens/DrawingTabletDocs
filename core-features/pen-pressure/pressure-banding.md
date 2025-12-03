# Pressure banding

## Overview

Pressure banding t features sudden dips or harsh transitions transitions to pressure in very regular horizontal and vertical bands especially when drawing at lower pressure.

## Prevalence

This is a very rarely seen.

I have only encountered it in two tablets:

* Wacom One M (CTC-6110WL)&#x20;
* Wacom One S (CTC-4110WL)&#x20;

I do not recommend buying those two tablets for this reason.

## Cause

* The pen is NOT the problem
* I suspect it is a problem with the firmware in combination with the digitizer.

## Examples

All the examples below are from the Wacom One M (CTC-6110WL) pen tablet that was released in 2023. With the original firmware (v 1.5.0.0) of the tablet significant pressure banding occured. Later firmware updates significantly reduced the effect, but did not eliminate it.

## Pressure to stroke width

Here are 7 strokes drawn in Krita on the CTC-6110WL

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

Even now you yours may detect some regular pattern to the width of the strokes

Looking carefully you'll see that the strokes appear pinched in regular horizontal bands.

<figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>



## Pressure to stroke opacity

The effect is more clearly shown when having pressure control opacity - and employing a little bit of image processing.

You might be able to make out some banding in the original image.

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

Performance some contrast enhancement makes it much more obvious

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

## What normal strokes should look like.

These examples were created with a Wacom Intuos Pro Medium (2017) tablet

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

## Testing

Here is how i test for banding: [Measuring pressure banding](../../process/measuring-pressure-banding.md)
