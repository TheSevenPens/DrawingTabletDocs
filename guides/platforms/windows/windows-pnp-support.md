# Windows PNP support for drawing tablets

## Introduction

Microsoft Windows includes built-in drivers for many devices. A great example is mice. You plug them in and they just work. This is why these drivers are called “plug-and-play” or P\&P drivers.

And Windows has PNP drivers for drawing tablets. Sometimes these PNP drivers are very useful. But you should keep in mind that these PNP drivers are missing a lot of features that you really need to have.

Windows PNP drivers are useful in some cases:

* You intend to use the drawing tablet as a mouse replacement. So you're not drawing. You're just pointing, selecting, and clicking.
* You need to troubleshoot problems with the manufacturer's tablet drivers.
* You need to use them as a last resort if your manufacturer's tablet drivers aren't working.

The key things you should know:

* Not all tablets work with Windows PNP tablet drivers
* The drivers are extremely limited in what they can do.
* In my opinion they may work better with pen displays than pen tablets that don't have a screen. This is due to some missing features.

## Feature support status

* **hover** - supported
* **pressure sensitivity** - supported
* **tilt sensitivity** - supported
* **pen button actions** - not supported. The buttons will simply have some default unchangable behavior.
* **tablet buttons & dials actions** - not supported.&#x20;
* **force proportions** - not supported. This means that mismatched aspect ratios for pen tablets will result in distortion when drawing. More here explaining what this means: [Matching aspect ratios with Force Proportions](../../customizing/force-proportions.md)
* **map active area to specific display** - supported
* **map active area to full virtual desktop** - not supported
* **per-app settings** - not supported

## Forcing Windows to use PNP drivers

* Uninstall your manufacturer's tablet driver
* Restart your computer.

When your computer starts back up, it should be using the PNP drivers.

## Is your tablet using PNP drivers?

The easiest way to see if this is how Windows is interacting with your tablet is to look at the system pointer.

Normally your pointer will look like this when you are using the mouse or when you have a tablet driver installed.

<figure><img src="../../../.gitbook/assets/windows-pnp-support-1.jpg" alt=""><figcaption></figcaption></figure>

(NOTE: It's hard to do a screen capture of this pointer, so I had to rely on a phone camera)

## When should you use PNP drivers?

If your manufacturer tablet driver is having problems, the PNP drivers may be a "last resort".

## Using PNP mode for testing and diagnosing problems

If you are having problems with your tablet, trying PNP mode can be a good diagnostic test to help identify if the problem is related to the manufacturer tablet driver or not. More here: [DIAG: Testing with Windows PNP drawing tablet drivers](../../../troubleshoot/diag-windows-pnp-tablet-drivers.md)

## Interactions between tablet drivers and PNP mode

When you install a tablet driver, the tablet driver basically takes over handling the tablet, and Windows no longer uses its PNP mode.

And so the PNP mode will not affect you anymore.

Every now and then, I have Windows use PNP mode even though a driver is installed. Typically, this seems to happen when:

* Windows is starting up and the tablet driver hasn't been started yet. For a little bit of time, maybe a few seconds or maybe 30 seconds, you might see the PNP mode cursor. But then the tablet driver will start, and it will go back to normal. I might see this happen once or twice a year on my Windows machines.
* Sometimes, when the tablet driver is having problems working with Windows, you might see PNP mode being used.

## Which tablets are compatible with Windows PNP?

See this: [Windows PNP driver compatibility testing](windows-pnp-compat-testing.md).

## Notes

Windows supports PNP for lots of devices. For example mice or monitors. PNP is not limited to just tablets.
