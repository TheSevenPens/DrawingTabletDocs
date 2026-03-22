# Notes on OpenTabletDriver

## Overview

As I've gotten a chance to use open tablet driver here are some notes I've collected that I think will be useful for you if you ever want to explore using it for yourself.

## Links

* [OpenTabletDriver](./)
* [Install OpenTabletDriver on Windows](otd-windows-install.md)
* [Install OpenTabletDriver on MacOS](otd-macos-install.md)

## Use the OTD discord to get help

* Join the OTD Discord server: [https://discord.gg/9bcMaPkVAR](https://discord.gg/9bcMaPkVAR)
* **DO** ask questions in the `#support-windows` channel.
* **DO NOT** ask for support via DMs.

## Your tablet manufacturer will not help with OTD

<mark style="color:red;">**Your tablet manufacturer WILL NOT help or support you in any way when you are using OpenTabletDriver instead of their own drivers.**</mark>

## Limitations of OpenTabletDriver

* Features that a typical driver has, but OTD does not.
  * OTD does NOT support touch input.
  * OTD does NOT support tablet rotary dials.
  * OTD does NOT support pen barrel rotation.
  * OTD does NOT support wireless or Bluetooth connections.
  * OTD does NOT support per-application configuration. All OTD settings are system-wide.
* Features that a typical driver has, and OTD does not have built-in, but for which you can use OTD plug-ins to achieve the same result.
  * OTD does not have a built in pressure curve, for that you should use an OTD plug-in like Slimy Scylla. [Pressure curves in OpenTabletDriver](pressure-curves-in-otd.md)

## **OpenTabletDriver on Windows**

### **Running OTD as admin**

* <mark style="color:red;">**DO NOT run OTD as administrator**</mark>.
* OTD will not work correctly if you do.

### **Windows Ink & WinTab**

* There are two Pen APIs in the Windows ecosystem: **WinTab** which is older, and **Windows Ink** which is newer.
* OTD only supports **Windows Ink** so any apps you want to use it with must also support Windows Ink.
* Most creative apps support Windows Ink - Clip Studio Paint, Krita, Photoshop.
* If you want pressure sensitivity, tilt, etc. - you must **you MUST configure OTD to use Windows Ink** and configure your apps to also use Windows Ink.

### Application data directory

* OTD stores information in its application data directory
* More here: [OpenTabletDriver application data directory](otd-app-data-directory.md)
* If you are doing more advanced things with OTD you should be familiar with this folder.

## Pen hover height

By default, OTD **has no restriction on the hover height of your pen**. Most drivers impose an artificial limit of about 10mm for a pen. But you'll often find with OTD that the hover height is increased substantially.

The maximum hover height is dependent on the specific model of tablet involved. For example with a Wacom Intuos Pro (PTH-860) my hover height goes from 10mm with the Wacom Driver to 20mm with Open Tablet driver.

You can install a plug-in to control the hover height and have whatever limit you want.
