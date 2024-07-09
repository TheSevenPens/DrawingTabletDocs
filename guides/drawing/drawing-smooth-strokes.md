# Drawing smooth strokes

## Overview

When you draw a stroke with a drawing tablet, your stroke will not be perfectly smooth. There are many causes for it any many things you can do to address it.

## Causes

The tablet and driver are components that can contribute to strokes that aren't as smooth as you would like

* All tablets have a degree of [diagonal wobble](../core-features/diagonal-wobble.md) that can appear in your stroke.&#x20;
* Tablet sometimes exhibit a little bit of "noise" in their stroke. This noise is similar to wobble in that it deviates from a smooth line, but it does so in a more random way.
* The surface of a tablet may be too smooth and this can cause the pen to easily "slip" away from your intended path.

You are user and your drawing style can affect the smoothness of a stroke

* Your hand and arm and way of moving them over the tablet can cause imperfections in your stroke.
* Drawing slower is more prone to introducing errors into your strokes.

## How you hold the pen

Consider how you hold you pen. Different techniques of holding your pen can affect how smooth your strokes are.

* [**Aaron Rutten - How to Hold a Drawing Tablet Pen**](https://www.youtube.com/watch?v=AAm0DrOrDGQ) 2023/09/03&#x20;
* [**Brad Colbow - How Pros Hold a Pencil**](https://www.youtube.com/watch?v=pB9m4TxZ7oQ) 2024/05/28

## Increase the surface texture of your tablet

Using a digital; pen on a very smooth tablet surface can result in the pen feeling "slippery" as you draw. And so the pen often seems to "slide away" from the intended path of the stroke you are trying to make.  This is a common complain for iPads because an iPad's surface if very smooth glass.

Consider buying a protective sheet to increase the surface texture a bit. See: [**protective sheets**](../../accessories/surface-protectors/).

## Use a felt nib

Another way of increasing the surface texture and avoiding a slippery feeling is to use a felt nib. Many tablets now come with felt nibs, though they may not be installed in your pen by default.

## Draw with your shoulder instead of your wrist

Many people draw just by moving their wrist. Try instead drawing by moving your shoulders more.

## Rotate or mirror the canvas to make it easier to draw a smooth stroke.

Usually someone's hand can draw a smooth stroke easier at some angles than at others. For example, if you are right handed drawing a strong from bottom left to top right is easy but drawing from top left to bottom right is harder and the stroke less smooth. Rotate the application canvas so that you accommodate what your hand is better at doing.&#x20;

## Draw your stroke toward your instead of away from you

Some people find that drawing a stroke toward themselves is easier to keep smooth than drawing away from themselves.

## Draw a faster stroke

Generally speaking a faster stroke will result in a smoother stroke.

## Avoid mouse mode

Occasionally some people enable mouse mode in their tablet driver. Mouse mode uses relative positioning and usually makes it harder to make a consistent stroke. Instead try disabling mouse mode.

## Match aspect ratios (very important)

If you are using a pen tablet, mismatched aspect rations between your pen tablet and your monitor will distort your strokes and make it harder to draw smoothly. Make sure you check for this and correct it. More here: [Matching aspect ratios](../customizing-your-experience/matching-aspect-ratios.md).&#x20;

Please do check for this. Many people have been using their tablets for years with mismatched aspect ratios and when they make the ratios match it is a BIG DIFFERENCE in their ability to draw strokes correctly.

## Zoom in as much as possible for your stroke

Use zoom to your advantage. The stroke is affected several things which are physical in nature. For example, a diagonal wobble may introduce a 1mm wobble as your draw. If you are drawing with your canvas zoomed out then 1mm accounts for a lot of pixels. If you zoom in more then the 1mm accounts for fewer pixels of wobble. So you can really minimize some effects my zooming in as much as possible for your stroke. This minimizes the effect of those disturbances and also forces you to draw with a longer stroke which itself will minimize errors.

## Application brush smoothing

Use brush smoothing in your applications.

### Krita

Krita, under **Tool Options**, has 4 different brush smoothing options: **None**, **Basic**, **Weighted**, and **Stabilizer**.&#x20;

### Clip Studio Paint

Clip Studio Paint has several options

* A setting called **Stabilization** that goes from 0 to  100. Where 100 adds the most amount of smoothing possible.
* You can also separately use the **Adjust by speed** setting. It has two options: **Increase stabilization when drawing slowly** and **increase stabilization when drawing quickly**.



<div align="left">

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

## Application stroke post-correction smoothing

Some apps like Clip Studio Paint have the ability to "fix" strokes after they have been drawn.

The advantage to this technique is that it doesn't slow down your stroke as you draw.

The disadvantage to this technique is that you don't exactly know the path of your stroke until a moment after you draw the stroke. Also if you draw a sharp corner, post-correction techniques can somethings not recognize the corner and instead show it as a smooth corner.

<div align="left">

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

## Use vector drawing tools

Applications like Krita also support vector tools. If you are having problems with smooth strokes with you pen, the vector tools can produce perfectly smooth strokes.

## Use application auto-shape detection

Some applications, like ProCreate on the iPad, have a a shape detection feature. Roughly speaking after you draw a stroke and hold you pen still for a moment, it will recognize a line, or circle, or curve and create a perfect smooth version of your stroke.&#x20;
