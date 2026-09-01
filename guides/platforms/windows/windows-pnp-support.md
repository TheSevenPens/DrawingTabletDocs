# Windows PnP support for drawing tablets

## Introduction

Microsoft Windows includes built-in drivers for many devices. Mice are a great example. You plug them in, and they just work. This is why these drivers are called “plug-and-play” drivers. Windows also has PnP drivers for drawing tablets. Sometimes, these PnP drivers are useful. However, they lack many essential features.

## Why use PnP drivers

Windows PnP drivers are useful in some cases:

* You intend to use the drawing tablet as a mouse replacement. You are not drawing. You are only pointing, selecting, and clicking.
* You need to troubleshoot problems with the manufacturer's tablet drivers.
* You need to use PnP drivers as a last resort because your manufacturer's tablet drivers aren't working.

If your manufacturer's tablet driver has problems, PnP drivers may be a useful last resort.

## Considerations

The key things you should know:

* Not all tablets work with Windows PnP tablet drivers.
* The drivers are extremely limited in what they can do.
* In my opinion, they may work better with pen displays than screenless pen tablets. This is due to missing features.

## Feature support status

* **hover** - supported
* **pressure sensitivity** - supported
* **tilt sensitivity** - supported
* **barrel rotation** - supported
* **pen button actions** - limited support. You can't map the buttons to arbitrary keystrokes without third-party software. Windows provides basic native toggles, such as right-click or eraser, in the Windows Pen settings. Go to **Settings**, search for "Pen & Windows Ink," or open **Start** > **Run** > `ms-settings:pen`.
* **tablet button and dial actions** - not supported
* **force proportions** - not supported. Mismatched aspect ratios can distort pen tablet input. For more information, see [Matching aspect ratios with Force Proportions](../../customizing/force-proportions.md).
* **map active area to specific display** - supported
* **map active area to full virtual desktop** - not supported
* **mapping across the entire virtual desktop** –
  * for pen tablets (screenless tablets) - this is the default behavior. The pointer spans all connected displays.
  * for pen displays - this is not supported
* **mapping to a single specific display** –
  * for pen tablets - supported but needs manual configuration via Tablet PC Settings (`control.exe /name Microsoft.TabletPC`).
  * for pen displays - supported automatically
* **per-app settings** - not supported
* **pen position calibration for pen displays** - supported through `tabcal.exe`. I have not used this tool myself, so I cannot share specific experience with it.

## Forcing Windows to use PnP drivers

* Uninstall your manufacturer's tablet driver.
* Restart your computer.

When your computer starts back up, it should use the PnP drivers.

## Is your tablet using PnP drivers?

The easiest way to see if this is how Windows is interacting with your tablet is to look at the system pointer while you are looking at the desktop.

On the desktop, your pointer normally looks like this when you use a mouse. It also looks like this when you install a tablet driver. However, when Windows uses the PnP driver, it appears as a small, fuzzy diamond. The official name for this cursor is "Windows Ink hover cursor."

<figure><img src="../../../.gitbook/assets/windows-pnp-support-1.jpg" alt=""><figcaption></figcaption></figure>

> **Note:** It is hard to capture this pointer on screen. This image uses a phone camera.

#### Sometimes the diamond cursor does not show, even with PnP drivers

In some apps, you might not see the Windows Ink hover cursor even when Windows uses the PnP driver. This might be because:

* _"Show cursor"_ or visual feedback is disabled in the Windows Pen settings.
* The app bypasses Windows Ink for raw pointer capture.

## Using PnP drivers for testing and diagnosing problems

If you have tablet problems, PnP drivers can help diagnose them. They can identify whether the manufacturer's tablet driver causes the problem. For more information, see [DIAG: Testing with Windows PnP drawing tablet drivers](../../../troubleshoot/diag-windows-pnp-tablet-drivers.md).

## Interactions between tablet drivers and PnP drivers

When you install a tablet driver, it takes over handling the tablet. Windows no longer uses PnP drivers.

Windows may occasionally use Windows PnP drivers even when a tablet driver is installed. This typically happens when:

* Windows is starting up and the tablet driver has not started yet. You may see the PnP cursor for a few seconds. It may last up to 30 seconds. The tablet driver then starts, and the cursor returns to normal. This may happen once or twice a year.
* The tablet driver has problems working with Windows.

## Which tablets are compatible with Windows PnP?

See [Windows PnP driver compatibility testing](windows-pnp-compat-testing.md).

## Links

* [Tablet Pro - Windows 11 Stylus Settings Every Digital Artist Should Know - The ULTIMATE guide](https://www.youtube.com/watch?v=dz9nvS5NXyA) 2025-08-14

## Technical notes

### Terminology

Although we may say "PnP driver," PnP handles device discovery and other low-level tasks. The built-in Windows USB HID driver stack supports tablets. In conversation, it is easier to call these "PnP drivers."

When you plug in a tablet without installing the manufacturer's driver, Windows uses its built-in USB HID Digitizer class driver. It parses the device's raw data using the standardized USB-IF HID Digitizer specification. The data includes pen position, pressure, tilt, and button status.

### Why some tablets do not work with PnP drivers

A tablet should send a report descriptor to the computer when connected. A report descriptor identifies the tablet. It also describes how the tablet organizes its data. Many, but not all, consumer tablets expose these descriptors.

Some tablets, particularly Wacom professional tablets such as the Intuos Pro (PTH-460, PTH-660, and PTH-860), do not send a standard report descriptor when connected. Instead, they send a vendor-specific report descriptor that Windows cannot handle. In this situation, only the manufacturer's driver can communicate with the device.

### General device support

Windows supports PnP for many devices, including mice and monitors. PnP is not limited to tablets.
