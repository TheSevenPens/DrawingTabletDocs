# Drawing tablets vs mice

## Overview

Almost certainly you've used a mouse with a computer, and this this document will help you understand how using a drawing tablet with its pen differs from using a mouse.

## Positioning strategy

Mice and drawing tablets have very different positioning strategies. Mice use **relative positioning**. Drawing tablets use **absolute positioning**. Learn more here: [**Absolute versus relative positioning**](../core-features/absolute-versus-relative-positioning.md). Drawing tablets can simulate relative positioning if needed with [**mouse mode**](../core-features/mouse-mode.md). However, I don't recommend using mouse mode.

## **Stroke smoothness in drawing apps**

With a drawing applications you'll notice that the strokes drawn with a mouse have a rougher stair-step effect and in general are not as smooth.&#x20;

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

There are many techniques and features to help you draw smooth strokes. Some will work for both mouse and tablet, and some are specific to drawing tablets. More here: [**Drawing smooth strokes**](../guides/drawing/drawing-smooth-strokes.md).

Position smoothing (aka "stabilization") is one of these techniques. However, Some apps may allow position smoothing with drawing tablets but not with mice. &#x20;

Here's what Krita currently does:

* Basic smoothing: applies ONLY to drawing tablets
* Weighted smoothing: applies BOTH to drawing tablets and mice

Here's what Clip Studio Paint does:

* Stabilization: applies ONLY to drawing tablets &#x20;

## **Clicking and moving the pointer**&#x20;

With a mouse, you move the pointer and clicks only happen when you take a very conscious effort to click a mouse button.&#x20;

A drawing tablet feels very different. To move the pointer and avoid clicking you hover the pen over the drawing tablet (up to about 10mm) and this will move the pointer without clicking. If you touch the pen to the tablet however, this will count as a click.

So with a drawing tablet you have to get used to hovering and only pressing down when you want to click.&#x20;

## **Keep the pointer on a single pixel (without clicking)**

With a mouse it's usually pretty easy to put the pointer on a single pixel and keep it there. You can just move the mouse and once the pointer is where you want it, it's easy to hold the mouse in that position. Or you can even let go of the mouse and the pointer will stay there.&#x20;

Drawing tablets feel very different in this regard. First, you can't touch the tablet with the pen you have to hover the pen over that spot. While it is very easy to hover in a general location (a couple of pixels wide) its much harder to keep the pen over a specific pixel while hovering because you hand will move around a bit. Also most drawing tablet pens are sensitive to the tilt of the pen, and so if you tilt the pen it may cause some movement in the mouse pointer.

## **Keep the pointer on a single pixel (while clicking)**

Mice are really good at this. Once the pointer is where you want it, you can click the buttons and this can be done without changing the pointer location.

This is much harder with a pen. First there is the general difficulty of keeping the pointer on a specific pixel. And then, if you press the buttons on the pen, this will almost always change the position of the pen and thus the pointer.

## Application considerations

if you are drawing strokes  or painting in an app like Clip Studio Paint or Krita, then a drawing tablet will feel MUCH more natural.

If you are layout out shapes and creating vector shapes in applications like Illustrator, a mouse might actually be better because they are easier to keep in a specific pixel location. For example, I normally just use a mouse when I use illustrator.

## Ergonomics > Wrist Pain

Using a mouse can place strain on your wrist. Drawing tablets are generally less stressful on your wrist. However, they also can place strain.&#x20;

## Power

Mice get their power from either a cable or they use batteries.

Modern drawing tablets all support wired connection through USB. Some tablets also support wireless connection through bluetooth.

The pens for a modern drawing tablet neither use a cable nor do they have batteries. Instead they get power simply from being near the drawing tablet.

## ProTip: Match aspect ratios when using a pen tablet

Make sure you match aspect ratios when you are using a pen tablet so that drawing feels natural and your strokes are not distorted. More here: [Matching aspect ratios](../guides/customizing-your-experience/matching-aspect-ratios.md)  &#x20;

