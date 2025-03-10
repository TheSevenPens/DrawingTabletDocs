# Pen pressure stability

## Overview

Ideally when you're drawing with an EMR pen, smooth changes to physical pressure are translated to smooth changes in the pressure data the computer is getting from the tablet.

In reality at low pressure near the IAF, you can experience some instability where pressure readings might do certain strange things. And this will produce odd artifacts in your strokes.

Often this instability is present in your strokes but may not be noticeable at all especially if your brush size is small (for example 10px). But if you are using very large brush sizes like 100 pixels or 500 pixels that it may be much more obvious.

## Prevalence

All drawing tablet pens have some pressure instability near their initial activation force. The amount of this instability and the way it manifests itself does vary a bit between different pen models. However even the best drawing tablet pen on the market (Wacom Pro Pen 2) can be made to exhibit these issues.

## Examples

All of the example below were created with the Wacom Intuos Pro 2017 M (PTH-660) with the Wacom Pro Pen 2 (KP-504E).&#x20;

* Application: Krita
* Brush: Ink3 Gpen, null pressure curve, 500px brush

<figure><img src="../.gitbook/assets/image (572).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (573).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (574).png" alt=""><figcaption></figcaption></figure>



