# Using a drawing tablet without installing drivers

## Overview

In some cases it is possible to use a drawing tablet - to various degrees - without installing a driver.

Note that this is highly dependent on:

* The operating system - Some operating systems MAY come with built-in drivers for tablets (though these are limited in features)
* The specific tablet model - Some tablets REQUIRE a driver to be installed

## Scenario

The most common reason I see where people are interested in using a tablet without installing a driver is simply that they are **not allowed** to install a driver in their situation.

This is very common in an educational environment. Where their IT has "locked down" their computers, preventing anyone (even the instructors) from installing software. And getting IT to change their policy is incredibly difficult.

## Windows without installing a driver

Assume you have a Windows computer with no driver installed, and then you attach a tablet. One of two things will happen:

* The tablet will work - due to Windows PNP (Plug and Play) support for devices. Keep in mind that Windows PNP support is absolutely not as full featured as using the driver. See: [Windows PNP support for drawing tablets](../windows/windows-pnp-support-for-drawing-tablets.md).&#x20;
* The tablet will literally do nothing. This is because some tablets are designed to deliberately NOT work without drivers. A great example is the Wacom Intuos Pro Large (PTH-860). Plugging it into a Windows computer, doesn't enable you to use&#x20;

## Windows using OpenTabletDriver

[OpenTabletDriver](opentabletdriver/) is a special kind of driver. It's called a "user mode" driver.

A normal tablet driver has to be installed - the driver components have to be placed in a specific location and affect how the operating system works. But OpenTabletDriver isn't "installed" at all. It's just a program you run. You can copy the OTD binaries to a machine and while it is running, a connected tablet will work to **some degree**.

You will get the ability to move the pointer and click. But you will NOT get pressure and tilt by default.

If you want those additional capabilities you have to install an additional component called VMulti - and this component unfortunately actually has to be installed in a more traditional sense. And your IT setup may prevent it from being installed.

If you are interested in using OTD as your tablet driver on Windows and want to use features like pressure and tilt, I wrote a detailed step-by-step guide to help you: [Install OpenTabletDriver on Windows](opentabletdriver/opentabletdriver-windows.md)&#x20;

## MacOS without installing driver

I haven't tested a Mac for this yet.



##

