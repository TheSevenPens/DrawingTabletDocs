# Testing with Windows PNP drawing tablet drivers

## Overview

Windows has built-in tablet drivers through it's Plug-and-play framework.

This tablet driver is extremely basic, but is  useful for diagnosing problems with a tablet. Suppose you have a problem with your tablet. The problem might be with the manufacturer's tablet driver. So by trying your tablet with the Windows PNP drivers, and seeing what happens we might be able to see if the problem is in the driver or not.

More here: [**Windows PNP support for drawing tablets** ](../guides/windows/windows-pnp-support-for-drawing-tablets.md)

## **Instructions**

* First uninstall your manufacturer's tablet driver
* Restart your computer
* NOTES:
  * You do NOT need to disconnect your tablet
* The try to reproduce the problem that occured.

## The pointer

When WIndows PNP drivers are being used and you are moving your pen, you'll see the pointer look like this&#x20;

\\![](<../.gitbook/assets/image (371).png>)

If you see it look like the normal mouse pointer when you use the pen, that usually means the manufacturer driver is being used.





