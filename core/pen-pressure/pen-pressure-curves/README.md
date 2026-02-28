# Pen pressure curves

{% hint style="info" %}
Before you read this document, read: [Pen pressure response](../pen-pressure-response.md)
{% endhint %}

## Overview

Your pen senses pressure and encodes it as a number. You can think of the number as ranging from 0 to the maximum number of pressure levels of your pen. In many cases its easier to "normalize" this number so that it ranges from 0.0 to 1.0. This makes discussing the pressure easier to understand in many cases.

This number flows through a "Pipeline" of components: tablet firmware -> tablet driver -> OS pen subsystem-> pen-aware application -> brush engine

Some of these components can process the the pressure - that means they can alter the number - before it is sent to the next component.

The processing of the pressure number alters how the pen will feel to draw with.

There are different ways in which components can process the pressure number. These include:

* Pressure processing curves (also called just "pressure curves")
* Pressure smoothing

This document deals with pressure processing curves.

## Response curve vs processing curve

Thinking of it as numbers:

* The pressure response curve is how the pen hardware handles pressure. It maps physical pressure into a pressure number.
* The processing curve is a mathematical operation that takes a pressure number and can change it into a different number.

Thinking of it as a behavior ("how the pen feels")

* The pressure response curve is the "native" behavior of how the pen feels to draw with.
* The pressure processing curve is a way of modifying that behavior.

## What a pressure processing curve looks like

For example in the Wacom Tablet Properties app it looks like this:

![](../../../.gitbook/assets/image-000256.png)

* The X axis labelled as "Pen pressure" is the logical input pressure
* The Y axis labelled as "Output" is the output logical pressure
* This particular curve bends down a little. But many other shapes are possible. Each shape has their uses.

## Popular coverage of pressure curves is misleading

You might encounter YouTube videos where people describe the pressure curve as the pressure behavior of the pen. This is completely inaccurate. The pressure curve describes how the pressure behavior (the pressure response) is being modified. You cannot look at a pressure curve and understand the pressure behavior of your pen. The only way for you to understand the pressure behavior of pen is to physically measure it with the scale and start mapping physical pressure values to logical pressure values.

## Pressure curve shapes

There are a variety of pressure curve shapes - each of which can solve some problem or achieve some visual effect.

<figure><img src="../../../.gitbook/assets/image-000434.png" alt=""><figcaption></figcaption></figure>

To see which drivers and apps support which shapes see this: [Adjusting pressure curves in apps](app-pressure-curves.md)

## Things you can do with pressure curves

* [Null pressure curve](null-pressure-curve.md) - a curve that "does nothing"
* [Pressure curves that constrain output](constraining-pressure-curve-output.md)
* [Pressure curves that ignore input](constraining-pressure-curve-input.md)
* [Lowering the IAF](../../../guides/customizing/lowering-iaf.md)
* [Increasing IAF](../../../guides/customizing/increasing-iaf.md)
* [Lowering maximum physical pressure](../../../guides/customizing/lowering-max-physical-pressure.md)

## Driver UX for pressure curves

See [Adjusting pressure curve in tablet driver](driver-pressure-curves.md)
