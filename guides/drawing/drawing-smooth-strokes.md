# Drawing smooth strokes

## Overview

When you draw a stroke with a drawing tablet, your stroke will not be perfectly smooth. There are many causes for it any many things you can do to adress it.

## Causes

* Tablet hardware and driver
  * All tablets have a degree of [diagonal wobble](../core-features/diagonal-wobble.md) that can appear in your stroke.&#x20;
  * Tablet sometimes exhibit a little bit of noise in their stroke - it's similar to wobble in that it deviates from a smooth line, but it does so in a more random way.
* You and how you draw
  * Your hand and arm and way of moving them over the tablet can cause imperfections in your stroke.
  * Drawing slower is more prone to introducing errors into your strokes.

## Option: Drawing style

Use more of your arm to draw instead of your wrist

## Option: Application zoom

Use zoom to your advantage. The stroke is affected several things which are physical in nature. Fo example, a diagonal wobble may introduce a 1mm wobble as your draw. If you are drawing with your canvas zoomed out then 1mm accounts for a lot of pixels. If you zoom in more then the 1mm accounts for fewer pixels of wobble. So you can really minimize some effects my zooming in as much as possible for your stroke. This minimizes the effect of those disturbances and also forces you to draw with a longer stroke which itself will minimize errors.

## Option: Application brush smoothing

Use brush smoothing in your applications.

### Krita

Krita, under **Tool Options**, has 4 different brush smoothing options: **None**, **Basic**, **Weighted**, and **Stabilizer**.&#x20;

### Clip Studio Paint

Clip Studio Paint has several options

* A setting called **Stabilization** that goes from 0 to  100. Where 100 adds the most amount of smoothing possible.
* You can also separately use the **Adjust by speed** setting. It has two options: **Increase stabilization when drawing slowly** and **increase stabilization when drawing quickly**.



<div align="left">

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

## Option: Post-correction

Some apps like Clip Studio Paint have the ability to "fix" strokes after they have been drawn.

The advantage to this technique is that it doesn't slow down your stroke as you draw.

The disadvantage to this technique is that you don't exactly know the path of your stroke until a moment after you draw the stroke. Also if you draw a sharp corner, post-correction techniques can somethings not recognize the corner and instead show it as a smooth corner.

<div align="left">

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

## Option: Use vector drawing tools

Applications like Krita also support vector tools. If you are having problems with smooth strokes with you pen, the vector tools can produce perfectly smooth strokes.



## &#x20;





