# Windows PnP support for drawing tablets

## Introduction

Microsoft Windows includes built-in drivers for many devices. Mice are a great example. You plug them in, and they just work. This is why these drivers are called “plug-and-play” drivers.

Windows also has PnP drivers for drawing tablets. Sometimes, these PnP drivers are useful. However, they lack many essential features.

Windows PnP drivers are useful in some cases:

* You intend to use the drawing tablet as a mouse replacement. You are not drawing. You are only pointing, selecting, and clicking.
* You need to troubleshoot problems with the manufacturer's tablet drivers.
* You need to use them as a last resort if your manufacturer's tablet drivers aren't working.

The key things you should know:

* Not all tablets work with Windows PnP tablet drivers.
* The drivers are extremely limited in what they can do.
* In my opinion, they may work better with pen displays than screenless pen tablets. This is due to missing features.

## Feature support status

* **hover** - supported
* **pressure sensitivity** - supported
* **tilt sensitivity** - supported
* **pen button actions** - not supported. The buttons will have default, unchangeable behavior.
* **tablet button and dial actions** - not supported.
* **force proportions** - not supported. Mismatched aspect ratios can distort pen tablet input. For more information, see [Matching aspect ratios with Force Proportions](../../customizing/force-proportions.md).
* **map active area to specific display** - supported
* **map active area to full virtual desktop** - not supported
* **per-app settings** - not supported

## Forcing Windows to use PnP drivers

* Uninstall your manufacturer's tablet driver
* Restart your computer.

When your computer starts back up, it should be using the PnP drivers.

## Is your tablet using PnP drivers?

The easiest way to see if this is how Windows is interacting with your tablet is to look at the system pointer.

Normally your pointer will look like this when you are using the mouse or when you have a tablet driver installed.

<figure><img src="../../../.gitbook/assets/windows-pnp-support-1.jpg" alt=""><figcaption></figcaption></figure>

> **Note:** It is hard to capture this pointer on screen. This image uses a phone camera.

## When should you use PnP drivers?

If your manufacturer's tablet driver has problems, PnP drivers may be a last resort.

## Using PnP mode for testing and diagnosing problems

If you have tablet problems, PnP mode can help diagnose them. It can identify whether the manufacturer’s tablet driver causes the problem. More information: [DIAG: Testing with Windows PNP drawing tablet drivers](../../../troubleshoot/diag-windows-pnp-tablet-drivers.md)

## Interactions between tablet drivers and PnP mode

When you install a tablet driver, it takes over handling the tablet. Windows no longer uses PnP mode.

PnP mode no longer affects you.

Windows may occasionally use PnP mode even when a driver is installed. This typically happens when:

* Windows is starting up and the tablet driver has not started yet. You may see the PnP cursor for a few seconds. It may last up to 30 seconds. The tablet driver then starts, and the cursor returns to normal. This may happen once or twice a year.
* The tablet driver has problems working with Windows.

## Which tablets are compatible with Windows PnP?

See [Windows PNP driver compatibility testing](windows-pnp-compat-testing.md).

## Notes

Windows supports PnP for many devices, including mice and monitors. PnP is not limited to tablets.
