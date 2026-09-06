# Pen compatibility

## Overview

<mark style="color:red;">**Drawing tablets are very specific about which pens they work with. Never buy a pen without verifying compatibility first. The best way to confirm compatibility is to contact support.**</mark>

## **Key points**

* Usually a drawing tablet is only compatible with the exact pen model it came with
* A pen from Manufacturer A will most likely not work with a tablet from manufacturer B.
* A pen from Manufacturer A may not work with all tablets made by manufacturer A
* Using the same technology such as "EMR" does not mean two pens are interchangeable.
* Apple Pencils are only compatible with Apple iPads.
* Wacom has so many tablets and pens that compatibility can get confusing: [Wacom pen compatibility](../../catalog/pens/wacom-pens/wacom-pen-compatibility.md)

If you need to replace a pen, find out the model number that is compatible with your tablet. Then order that exact model. If you don't know the model you need, contact support for your drawing tablet.

## Can I use a cheap third-party pen?

The answer is usually no. Almost always, off-brand, generic and "universal" styluses don't work with drawing tablets.

## UD EMR pens have some cross-compatibility

There is one real exception worth knowing about. Some tablets support **UD EMR**, a Wacom pen technology that a number of devices share, and those do accept several different pens: [Tablets that support UD EMR 2nd gen](../../tech/wacom-ud-emr/ud-emr-tablets.md).

Outside that, buy the pen model your tablet is documented to take.

## Looking up which pen your tablet takes

The **DrawTab Data Explorer** records the included pen and the compatible pens for hundreds of tablets, including models that have no page in this catalog: [https://thesevenpens.github.io/DrawTabDataExplorer/](https://thesevenpens.github.io/DrawTabDataExplorer/)

Two cautions when you use it:

* Compatibility is recorded thinly for older hardware. If a tablet lists one pen, that is what I know of - it is not proof that nothing else fits.
* Confirm with customer support before buying either way.

## Video: Buying compatible pens for your drawing tablet [https://youtu.be/cKBSpIVeZJk](https://youtu.be/cKBSpIVeZJk)

{% embed url="https://youtu.be/cKBSpIVeZJk" %}

## What causes pen incompatibility?

### Tech differences

* Different pens use different resonant frequencies for their EMR signal. So pens that don't use the same frequency as the tablets expect will not be compatible
* Different pens use different techniques for transmitting some kinds of information back to the tablet, and these techniques have to also be supported by the tablet to work.
* This is sometimes why, for example, you can try using a Brand X pen with a Brand Y tablet, and the tablet might sense the position of the pen, but not the button presses or pressure.

### Non-tech causes

**Driver selectively excludes pens** - I know of at least one case with Wacom where the pen and tablet would actually work, but the Wacom driver prevents it. The way around this is to use [OpenTabletDriver](../drivers/opentabletdriver/), which does not have that restriction.

## Resources

* Huion's guide to finding compatible pens: ([https://support.huion.com/en/support/solutions/articles/44002337828-how-do-i-choose-correct-pen-for-my-huion-tablet-](https://support.huion.com/en/support/solutions/articles/44002337828-how-do-i-choose-correct-pen-for-my-huion-tablet-))
* [Wacom pen compatibility](../../catalog/pens/wacom-pens/wacom-pen-compatibility.md)
