# Pen pressure curves

{% hint style="info" %}
Before you read this document, read: [Pen pressure response curves.](../pen-pressure-response.md)&#x20;
{% endhint %}

## Overview

Your pen senses pressure and encodes it as a number.

You can think of the number as ranging from 0 to the maximum number of pressure levels of your pen. In many cases its easier to "normalize" this number so that it ranges from 0.0 to 1.0. This makes discussing the pressure easier to understand in many cases.

This number flows through a "Pipeline" of components: tablet firmware -> tablet driver -> OS pen subsystem-> pen-aware application -> brush engine

Some of these components can process the the pressure - that means they can alter the number - before it is sent to the next component.

The processing of the pressure number alters how the pen will feel to draw with.





A pressure curve is essentially a little bit of math that transforms a pressure response to another pressure response. In more everyday terms a pressure curve creates a new pressure behavior for the pen.&#x20;

<figure><img src="../../../.gitbook/assets/image (10) (1).png" alt=""><figcaption></figcaption></figure>

Most often, we see the results of this transformation shown to us visually in driver or application UI.

For example in the Wacom Tablet Properties app it looks like this:

&#x20;![](<../../../.gitbook/assets/image (11) (1).png>)

The X axis labelled as "Pen pressure" is the logical input pressure

The Y axis labelled as "Output" is the output logical pressure

This particular curve bends down a little. But many other shapes are possible. Each shape has their uses.

## Pressure curve vs pressure response

It is important to distinguish the pressure curve from the pressure response because they describe different things completely.&#x20;

A pressure response describes the pressure behavior of a pen - and this is a description of physically happens in the world. It relates physical pen pressure to logical pen pressure.

A pressure curve is an abstract mathematical entity that transforms logical pressure values. A pressure curve is completely arbitrary and does not describe a relationship in the physical world. It is a purely logical construct.

## Popular coverage of pressure curves is highly misleading

So often in documents and YouTube videos you might encounter people describe the pressure curve as the pressure behavior of the pen. This is completely inaccurate. The pressure curve describes how the pressure behavior (the pressure response) is being modified. You cannot look at a pressure curve and understand the pressure behavior of your pen. The only way for you to understand the pressure behavior of pen is to physically measure it with the scale and start mapping physical pressure values to logical pressure values.

## Pressure curve shapes

There are a variety of pressure curve shapes - each of which can solve some problem or achieve some visual effect.

<figure><img src="../../../.gitbook/assets/image (522).png" alt=""><figcaption></figcaption></figure>

To see which drivers and apps support witch shapes see this: [Curve support in applications](app-pressure-curves.md)

Details on specific shapes and what you can do with them

* [Null pressure curve](null-pressure-curve.md)
* [Pressure curves that constrain the output logical pressure range](constraining-pressure-curve-output.md)
* [Pressure curves that ignore input](constraining-pressure-curve-input.md)
* [Lowering IAF](../../../guides/customizing/lowering-the-iaf.md)
* [Increasing IAF](../../../guides/customizing/increasing-iaf.md)
* [Lowering maximum physical pressure](../../../guides/customizing/lowering-maximum-physical-pressure.md)

## Driver UX for pressure curves

See [Adjusting pressure curve in tablet driver](driver-pressure-curves.md)

