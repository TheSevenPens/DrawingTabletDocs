---
description: Using drawing tablets with Linux
---

# Linux

## Introduction

I don't have any experience with drawing tablets and Linux. However, here are some resources I found that you may find useful.

## Wacom support for Linux

Many distros come with Wacom drivers pre-installed. More details here: [Wacom - Are Wacom devices supported under Linux?](https://support.wacom.com/hc/en-us/articles/4418603622295-Are-Wacom-devices-supported-under-Linux)

The list of Wacom devices supported on Linux: [https://github.com/linuxwacom/input-wacom/wiki/Device-IDs](https://github.com/linuxwacom/input-wacom/wiki/Device-IDs)

### Notes on my experience

* I tested several Wacom devices with the built in support of Linux Mint 22.2 Cinnamon.
* I tested several Wacom devices with the built-in support of Linux Mint 22.2 Cinnamon.
  * One by Wacom CTL-672 - worked
  * Wacom Intuos Pro Medium 2017 (PTH-66) - worked
  * Wacom Movink 13 - was not recognized
  * Wacom Intuos Pro Medium 2025 (PTK-670) - was not recognized
* Pointer lag
  * I noticed less pointer lag than on a Windows or macOS system using the Wacom driver
* Feature set
  * Basic features are available, but lots of typical features you might be used to in the Wacom driver are not
    * No per-application settings
    * No visualization of the pressure curve

## Xencelabs support for Linux

Xencelabs ships Linux drivers

## XP-Pen support for Linux

XP-Pen has Linux drivers from

[XP-Pen - How to install XPPen Linux driver on Ubuntu (64 bits)](https://www.xp-pen.com/faq/how-to-install-xppen-linux-driver-on-ubuntu-64-bits.html)

## Huion support for Linux

Huion has drivers for some models.

[Huion - Does Huion Have a Tablet Driver That Supports Linux?](https://support.huion.com/en/support/solutions/articles/44001769972-does-huion-have-a-tablet-driver-that-supports-linux-)

## OpenTabletDriver

Often, people prefer to use OpenTabletDriver for tablets on Linux. This is especially popular in the osu community.

## WINE notes

* A note from [Tablet kitten](../../resources/community/tablet-kitten.md) - WINE builds with wow64 have a broken wintab32

## Fedora 43 drawing tablet UX

<div><figure><img src="../../.gitbook/assets/fedora-drawtab-ui (1).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/fedora-drawtab-ui (2).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/fedora-drawtab-ui (3).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/fedora-drawtab-ui (4).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/fedora-drawtab-ui (5).png" alt=""><figcaption></figcaption></figure></div>

Features

* Absolute vs relative positioning (mouse mode).
* Mapping tablet button actions
* Mapping tablet active area to displays
* Force proportions - called "Keep aspect ratio"

## Links

### General

* [MossCharmly - HUION Tablets (Kamvas 16 (2.5k) on LINUX (POP\_os)](https://www.youtube.com/watch?v=ibuH-hGkmdI) - 2023-05-13
* [MossCharmly - Demystifying Linux for Artists](https://www.youtube.com/watch?v=hQ2VpPchETk) - 2024-03-02
* [MossCharmly - Linux PC Build for Digital Artists](https://www.youtube.com/watch?v=eiLnEUS3r5k) - 2024-03-17
* [Mindful Technology - Huion Inspiroy H1161 drawing tablet on Debian Linux: install driver & declutter HOME](https://www.youtube.com/watch?v=kbzlKn3zhrk) - 2023-10-24
* [Linuxedo - Wacom Intuos S Wireless | Unboxing and Setting up on Linux Mint](https://www.youtube.com/watch?v=-TBT_l6qwj0) - 2021-01-17
* [Tony Tascioglu - How to Map a Wacom Tablet to a Single Monitor on Linux](https://www.youtube.com/watch?v=DEdUa5lHZbU) - 2021-01-19
* [Brodie Robertson - Easily Setup Your Wacom Tablet Under Linux](https://www.youtube.com/watch?v=dzplf-0RJDE) - 2021-09-12
* [Switched to Linux - Wacom Tablets on Linux Mint](https://www.youtube.com/watch?v=stDM3T4Fu5A) 2018-02-27

### Do you use Arch, btw?

* [ALCC - Part 6: Creating Art on Arch Linux](https://www.youtube.com/watch?v=7jcb4p-FmUU) - 2026-02-10
* CSP + Arch - [eninabox - Easily Install CLIP STUDIO PAINT on Linux (CachyOS/Arch)](https://www.youtube.com/watch?v=5CPzvDQ1Nm4) - 2025-12-31

### Guides for specific apps

* Getting Paint Tool SAI 2 setup on Linux - [https://github.com/TibixDev/sai2-guide](https://github.com/TibixDev/sai2-guide)
