# Windows on ARM

## Overview

We are now seeing Windows computers running on ARM processors. This holds gives us the possibility for cooler running, high-performance machines with great battery life.

## Drawing tablets compatibility with Windows on ARM

You cannot use older tablet drivers with Windows on ARM devices. These require special ARM compatible drivers. Different brands are at different stages of ARM support as described below:

As of 2024/10/03:

* **Xencelabs**: Has an beta ARM driver available [https://www.xencelabs.com/support/download-drivers](https://www.xencelabs.com/support/download-drivers)
* **Huion**: Actively working on an ARM driver. Not available for download yet.
* **Wacom**: Actively working on an ARM driver. Not available for download yet. See this link: [Does Wacom have a driver for PCs that run Windows 11 on ARM processors (e.g. Snapdragon X)? ](https://support.wacom.com/hc/en-us/articles/23838303808407-Does-Wacom-have-a-driver-for-PCs-that-run-Windows-11-on-ARM-processors-e-g-Snapdragon-X)
* **XP-Pen**: I asked them and they had no comment on whether they were working on an ARM driver or when one might be expected.

## A POSSIBLE alternative: Windows PNP tablet drivers

If you cannot use a tablet until, an ARM driver is available the only other option that may help you is the use of windows PNP tablet drivers.

The windows PNP drivers come with windows and are quite limited. Sometimes they are missing features that you need. I don't recommend using the Windows PNP drivers unless it's a last resort. And keep in mind that not all tablets support windows PNP drivers.

For example Wacom Intos Pro tablets do not support Windows PNP drivers.

More here:&#x20;

* [Windows PNP Drivers](windows-pnp-support-for-drawing-tablets.md)
* [Testing with Windows PNP drawing tablet drivers](../../troubleshooting/testing-with-windows-pnp-drawing-tablet-drivers.md)

### June 2024 update video

{% embed url="https://www.youtube.com/watch?v=3RGkj0vs-z0" %}

## Older Windows ARM devices

Microsoft previously released versions of the Surface Pro with using the SQ1 and SQ2 ARM processors.   Interestingly, the new Windows improvements for ARM processors seem to be improving performance on these old devices.

See this reddit thread: [https://www.reddit.com/r/Surface/comments/1czcxoc/windows\_11\_24h2\_update\_made\_my\_arm\_tablet\_faster/](https://www.reddit.com/r/Surface/comments/1czcxoc/windows\_11\_24h2\_update\_made\_my\_arm\_tablet\_faster/)

## Native ARM applications

Your best performance will be with those apps that are built for ARM.

Go to [https://armrepo.ver.lt/](https://armrepo.ver.lt/) for a list of apps that are available with native ARM support.

&#x20;
