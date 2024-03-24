# Testing with Windows PNP drawing tablet drivers

## Overview

Windows has built-in tablet drivers through its Plug-and-play framework. More here: [**Windows PNP support for drawing tablets** ](../guides/windows/windows-pnp-support-for-drawing-tablets.md)

## Using Windows PNP tablet drivers to investiagate problems

The Windows PNP tablet driver is extremely basic. However, you can use it to diagnose problems with a drawing tablet.&#x20;

* if a problem occurs with both the manufacturer tablet driver and the Windows PNP tablet driver, then the problem is likely not related to drivers.
* if a problem only occurs with the manufacturer driver, then it you know the problem is driver related.

## **Instructions**

* First uninstall your manufacturer's tablet driver
* Restart your computer.&#x20;
* The try to reproduce the problem.

## Notes

* You do NOT need to disconnect your tablet.
* Some tablets do not work with Windows PNP drivers. This is usually a deliberate choice of the tablet manufacturer. So if the tablet isn't working with the PNP drivers, don't worry.&#x20;

## The pointer

When Windows PNP drivers are being used and you are moving your pen, you'll see the pointer look like this&#x20;

<img src="../.gitbook/assets/image (397).png" alt="" data-size="original">

If you see it look like the normal mouse pointer when you use the pen, that usually means the manufacturer driver is being used.
