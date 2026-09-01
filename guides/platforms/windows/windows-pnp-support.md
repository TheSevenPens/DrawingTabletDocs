# Windows PnP support for drawing tablets

## Introduction

Windows has built-in support for many types of devices, including mice, keyboards, and some drawing tablets.

This means Windows can provide basic pen functionality for some drawing tablets without installing the manufacturer's tablet driver.

Depending on the tablet, features such as pen position, hover, pressure, tilt, and pen buttons may work. However, Windows' built-in support does not provide many of the configuration features available in manufacturer tablet drivers.

## Why use PnP drivers

Windows PnP drivers are useful in some cases:

* You do not need the full artistic features that the manufacturer's tablet driver provides, such as tilt and pressure. For example, you might intend to use the drawing tablet as a mouse replacement—for basic pointing, selecting, and clicking.
* You need to troubleshoot problems with the manufacturer's tablet drivers.
* You need to use PnP drivers as a last resort because your manufacturer's tablet driver is not working.

## Limitations of PnP drivers

* Not all tablets work with Windows PnP tablet drivers. Notably, Wacom Intuos Pro tablets tend not to work with Windows PnP drivers.
* The drivers are extremely limited in what they can do in terms of configuring and customizing how the tablet behaves.

## Feature support status

### **Basic features**

* **hover** - supported
* **pressure sensitivity** - supported
* **tilt sensitivity** - supported (most tablets support tilt)
* **barrel rotation** - supported (very few tablets support barrel rotation)

### Mapping buttons to actions

* **pen button actions** - basic pen-button input can be supported. Windows recognizes standard HID pen functions, such as barrel buttons and erasers. However, Windows does not provide the extensive button remapping available in most manufacturer tablet drivers. You cannot map buttons to arbitrary keystrokes without third-party software. Windows provides basic native toggles, such as right-click or eraser, in the [Windows Pen & Windows Ink settings](windows-pen-and-windows-ink-settings.md).&#x20;
* **tablet button and dial actions** - not supported

### Active area mapping

Windows treats pen tablets (screenless tablets) and pen displays differently.

* **mapping across the entire virtual desktop** –
  * For pen tablets, this is the default behavior. The pointer spans all connected displays.
  * For pen displays, this is not supported.
* **mapping to a single specific display** –
  * For pen tablets, this is supported but requires manual configuration through [Windows Tablet PC Settings](windows-tablet-pc-settings.md).
  * For pen displays, this is supported. Windows automatically tries to map the tablet's active area to its embedded display.
* **force proportions** - not supported. Mismatched aspect ratios can distort pen tablet input. This results in distorted strokes. For example, tracing a circle on the tablet creates an oval on the display. For more information, see [Matching aspect ratios with Force Proportions](../../customizing/force-proportions.md).
* **pen position calibration for pen displays** - supported through `tabcal.exe`. I have not used this tool, so I cannot share specific experience with it.

### Other

* **per-app settings** - not supported

## Forcing Windows to use PnP drivers

* Uninstall your manufacturer's tablet driver.
* Restart your computer.

When your computer starts back up, it should use the PnP drivers.

## A clue that Windows is using PnP drivers

The easiest way to see if this is how Windows is interacting with your tablet is to look at the system pointer while you are looking at the desktop.

### Windows Ink hover cursor

On the desktop, your pointer normally looks like this when you use a mouse. It also looks like this when you install a tablet driver. However, when Windows uses the PnP driver, it appears as a small, fuzzy diamond. The official name for this cursor is the "Windows Ink hover cursor."

<figure><img src="../../../.gitbook/assets/windows-pnp-support-1.jpg" alt=""><figcaption></figcaption></figure>

> **Note:** It is hard to capture this pointer onscreen. This image uses a phone camera.

### The Windows Ink hover cursor may not appear, even with PnP drivers

In some apps, you might not see the Windows Ink hover cursor even when Windows uses the PnP driver. This might be because:

* _"Show cursor"_ or visual feedback is disabled in Windows Pen settings.
* Some applications hide or replace the Windows pen cursor.

## Using PnP drivers for testing and diagnosing problems

If you have tablet problems, PnP drivers can help diagnose them. They can identify whether the manufacturer's tablet driver causes the problem. For more information, see [DIAG: Testing with Windows PnP drawing tablet drivers](../../../troubleshoot/diag-windows-pnp-tablet-drivers.md).

## Interactions between tablet drivers and PnP drivers

When you install the manufacturer's tablet driver, the driver normally becomes responsible for translating the tablet's input and providing tablet-specific features. Exactly how this works varies by manufacturer and tablet.

Windows may occasionally use Windows PnP drivers even when a tablet driver is installed. This typically happens when:

* On some tablets, Windows' built-in pen handling may briefly become visible while the manufacturer's tablet software starts. You may see the PnP cursor for a few seconds. It may last up to 30 seconds. I experience this once or twice a year.
* The tablet driver has problems working with Windows.

## Which tablets are compatible with Windows PnP?

See [Windows PnP driver compatibility testing](windows-pnp-compat-testing.md).

## Links

* [Tablet Pro - Windows 11 Stylus Settings Every Digital Artist Should Know - The ULTIMATE guide](https://www.youtube.com/watch?v=dz9nvS5NXyA) 2025-08-14

## Technical notes

### Terminology

Although we may say "PnP driver," PnP handles device discovery and other low-level tasks. The built-in Windows USB HID driver stack supports tablets. In conversation, it is easier to call these "PnP drivers."

When you plug in a PnP-compatible tablet without installing the manufacturer's driver, Windows can use its built-in HID driver stack to interpret the tablet's HID reports. These reports include pen position, pressure, tilt, and button status.

### Why some tablets do not work with PnP drivers

A tablet should send a report descriptor to the computer when connected. A report descriptor describes how the tablet organizes its data. Many, but not all, consumer tablets expose these descriptors. Windows can interpret those reports using its built-in HID support.

Some tablets, particularly Wacom professional tablets such as the Intuos Pro (PTH-460, PTH-660, and PTH-860), do not send a standard report descriptor when connected. Instead, they send a vendor-specific report descriptor that Windows cannot handle. In this situation, only the manufacturer's driver can communicate with the device.
