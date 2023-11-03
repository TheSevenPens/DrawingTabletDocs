# Using older drawing tablets

## Overview

Most often people use tablets that have been very recently manufactured - in just the past few years. However, sometimes people ask about using tablets that are older. In summary, the primary issue that determines whether you can use an older tablet comes down to tablet drivers.

## My experience

As of 2023 I have used tablets that were manufactured 25 years ago on my windows 11 system. So it is certainly possible to use an older tablet with a modern computer for creative purposes and was able to use pressure and tilt.

Models I have specifically used with Windows 11:

* Wacom Intuos 4 XL (PTK-1240) - using Wacom drivers and OpenTabletDriver. This tablet was released in 2009.
* Wacom Intuos 3 12x12 (PTZ-1230) - using OpenTabletDriver. This tablet was released in 2004.
* Wacom Intuos 2 12x18 (XD-1218-U) - Using OpenTabletDriver. This tablet was released in 2001.

## Common reasons why people want to use an older tablet

* They bought the tablet a long time ago but I haven't used it recently.
* It was a tablet that was gifted to them
* They bought the tablet used - for example from eBay (more here: [**buying used drawing tablets**](../../buying-a-drawing-tablet/buying-used-drawing-tablets.md))

## Drivers overview

Drivers are allow a tablet to be used with a computer. They are really important when you want to use the special features of a drawing tablet and the pen such as pressure sensitivity and tilt. Without the drivers a drawing tablet may not function at all or may work just essentially as a mouse with no pressure sensitivity and no tilt. More here: [**drivers**](../drivers/)

## Driver compatibility with multiple tablets&#x20;

A specific version of a tablet driver tends to be compatible with a range of tablets from a specific manufacturer.&#x20;

For example Wacom's windows are compatible with wide range of their tablets.

Here is the [compatibility list](https://cdn.wacom.com/u/productsupport/drivers/win/professional/releasenotes/Windows\_6.4.4-3.html) for version 6.4.4-3 of the Wacom drivers.

![](<../../.gitbook/assets/image (366).png>)&#x20;

## Driver updates

Drivers have to be updated over time because there are new tablets that they need to support and also changes to the underlying operating system may require the drivers to be updated.

## Driver compatibility issues

Every time a driver is updated it may be the case that a manufacturer drops support for one of the tablets that the driver used to support.

For example today, if you install the latest Wacom tablet drivers and then proceed to plug in a Wacom Intuos 3 tablet, the driver will simply tell you it does not work with this tablet.

Here's what the message looks like from the Wacom driver when I plug in an older tablet the very latest drivers from Wacom.

## Driver options for older tablets

if the latest drivers do not work with the tablet that you have, then you have two options:

* Use an older version of the tablet driver
* Use OpenTabletDriver

## Finding older drivers

Manufacturers usually keep all the old versions of their tablet drivers on their website. If you can't find the driver you need you can always contact customer support and they should be able to help you find it for you.

## Challenges in using older drivers

You may run into problems using an older version of a tablet driver.

A common issue is that the operating system has changed since the driver was first created and applications have also changed in that time. So if you have an older driver you may have difficulty using some features. For example a very new version of Photoshop combined with an older version of the Wacom driver can create a situation where buttons on the pen do not work. The issues you will run into are highly dependent on the specific version of the operating system and the specific version of the application.

## Using OpenTabletdriver

OpenTabletDriver is compatible with many older tablets. The key issues when using OTD are:

* OTD is more challenging to set up especially if you want to use features like pressure sensitivity and tilt
* OTD does not support features like pressure sensitivity and tilt are on MacOS, but they are supported on Windows

If you are interested in using open tablet driver I have created a detailed guide to explain how to set it up on windows: [**Install OpenTabletDriver on Windows**](../drivers/opentabletdriver/opentabletdriver-windows.md)&#x20;

