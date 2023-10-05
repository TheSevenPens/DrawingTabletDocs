# Using a drawing tablet without installing drivers

## Overview

In some cases, you can use a drawing tablet without installing a driver.

This is highly dependent on:

* The operating system - Some operating systems MAY come with built-in drivers for tablets (though these are limited in features)
* The specific tablet model - Some tablets REQUIRE a driver to be installed

Also, in this case it may be that not all tablet features are available.

## Scenario

A common reason why people are interested in using a tablet without installing a driver is simply that they are **not allowed to install a driver** in their situation.&#x20;

This is very common in educational environments. IT departments often "lock down" their computers. This prevents a normal users such as instructors and students from installing ANY software. Unfortunately, convincing IT to change their software installation policy is incredibly difficult. Also, often the IT department is even unwilling to pre-install the drivers on those machines.&#x20;

## Windows without installing a driver

If you have a Windows computer with no driver installed, and then you attach a tablet. One of two things will happen:

* **The tablet will work**. In Windows this is due to Windows PNP (Plug and Play) support for tablets. Keep in mind that Windows PNP support for tablets does NOT have all the features that a typical tablet driver would provide. See: [Windows PNP support for drawing tablets](../windows/windows-pnp-support-for-drawing-tablets.md).&#x20;
* **The tablet will not work at all**. Some tablets are designed to deliberately NOT work without drivers installed. A great example is the Wacom Intuos Pro Large (PTH-860). Plugging it into a Windows computer achieves nothing. doesn't enable you to use&#x20;

## Windows using OpenTabletDriver

If you can't install a driver, another option is [OpenTabletDriver](opentabletdriver/).&#x20;

Is a special kind of driver. It's called a "user mode" driver. A normal tablet driver has to be installed. The driver components have to be placed in a specific location and affect how the operating system works. But OTD isn't "installed" at all. It's just a program you run. You can copy the OTD executable files to your machine and start it. While OTD is running, a connected tablet will work.

What OTD provides by default:

* Moving the pen moves the pointer
* Clicking and drawing

What does work by default:

* pressure
* tilt&#x20;

If you want those pressure and tilt, you have to install an additional component called VMulti that OTD can work with.  Unfortunately, VMulti actually has to be installed in the traditional sense - it is not a "user mode" component. And your IT setup may prevent you from installing it.

If you are interested in using OTD as your tablet driver on Windows and want to use features like pressure and tilt, I wrote a detailed step-by-step guide to help you: [Install OpenTabletDriver on Windows](opentabletdriver/opentabletdriver-windows.md)&#x20;

## MacOS without installing driver

I haven't tested a Mac for this yet.

