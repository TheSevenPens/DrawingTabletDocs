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
* OTD uninstall is more difficult on Windows because you have to manually uninstall VMulti
* OTD is simple to install on MacOS - but will require some additional Mac security configuration just as a manufacturer driver does

## Tablet mapping to displays

* OTD does not support precision mode
* OTD does not support the display toggle - there is no hotkey or pen button that can switch between displays

## Pen tracking

* OTD has no built-in position smoothing, which means the pointer will respond faster to your pen, but it may be a little more jittery. To smooth it out you can use a plug-in like Slimy Scylla

## Pen buttons

* OTD supports buttons for many tablets, but not all.
* OTD on Windows does not yet let you configure the 2nd button to do something

## Configuration

* OTD does not have per-application settings.
* OTD does have per-tablet model settings
* OTD does not come with support for pressure curves. You have to install a plug-in like Slimy Scylla to get pressure curves. To edit the pressure curve, you don't use UI, you enter numbers.

## Wheels

* OTD does support WHEELS, DIALS on tablets. This is a relatively new feature in OTD that launched with OTD v0.6.7 on April 25, 2026.

## Touch

* OTD does not yet support TOUCH on tablets

