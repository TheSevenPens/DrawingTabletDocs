# OpenTabletDriver vs manufacturer drivers

## Overview

OpenTabletDriver (OTD) can be very useful, but especially for those of you who are used to existing drivers from Wacom, Huion, XP-Pen, and how they work, OTD does work a little differently than you are used to. Here I will summarize the key differences that you need to be aware of and what your options are if you encounter any limitations.

This document is written from the perspective of a user who wants to DRAW/PAINT/etc. If you simply want to use OTD for playing osu, then many things here do not apply.

## Summary

In comparison to manufacturer drivers:

* Is more difficult to uninstall
* Is missing some features you might expect
* The UI is more complex
* OTD supports drivers from multiple brands
* OTD supports MANY tablet models 330+

## Basics

* OTD is a "user-mode" driver. Think of this more as a companion app that you run when you need to use your tablet. You have to launch it and minimize the app. If you exit the app, you won't be able to use the driver.
* OTD UI is more challenging to use
* OTD only supports one tablet plugged in at one time.
* You cannot mix and match OTD with manufacturer drivers. You must uninstall manufacturer drivers to use OTD.

## Installation

* OTD is more difficult to install.
* OTD binaries are not signed. This means macOS and Windows will warn you when you first try to run them, and you have to take a special action to run them.
* OTD on Windows requires the installation of a driver called VMulti (separate download and install) and a "Windows Ink plug-in" (integrated download and install in the OTD UI)
* OTD on Windows requires your drawing app to use Windows Ink. WinTab will not work.

## Missing features

* OTD is missing many convenience features out of the box. Some of these can be added with OTD plug-ins. But for some features, there is no equivalent OTD plugin
* OTD has no built-in smoothing, which means the pointer will respond faster to your pen, but it may be a little more jittery
* OTD does not yet support TOUCH on tablets
* OTD does not yet support DIALS and ROLLERS on tablets
* OTD does not support precision mode
* OTD does not support the display toggle feature.
* OTD uninstall is more difficult on Windows because you have to manually uninstall VMulti
* OTD on Windows does not yet let you configure the 2nd button to do something
