---
description: Using drawing tablets with Linux
---

# Using a drawing tablet on Linux

## Summary

Drawing tablets work well on Linux for core drawing: pressure, tilt, mapping the tablet to a display, and keeping the aspect ratio. Wacom tablets, and many Huion and XP-Pen tablets, work without installing anything. However, you get fewer settings than the Windows and macOS drivers offer, and how you configure the tablet depends on your desktop environment (GNOME, KDE Plasma, Cinnamon, and so on) rather than on the tablet brand.

I recommend Linux for tablet users who are already comfortable with Linux. If you have a very new tablet, expect to need a recent distribution.

{% hint style="warning" %}
**TODO (Seven):** Add a sentence or two on your overall impression from your recent testing.
{% endhint %}

## Drivers

### Built-in support versus manufacturer drivers

On Windows, the built-in tablet support is primitive and you should always install the manufacturer's driver. On Linux it's the opposite: **for most people, the built-in support is the best place to start.**

* **Wacom** - the Linux kernel includes Wacom drivers, and many distros come with everything pre-installed. See [Wacom - Are Wacom devices supported under Linux?](https://support.wacom.com/hc/en-us/articles/4418603622295-Are-Wacom-devices-supported-under-Linux) and the [list of Wacom devices supported on Linux](https://github.com/linuxwacom/input-wacom/wiki/Device-IDs).
* **Huion, XP-Pen, Gaomon, and other UC-Logic based tablets** - many models are supported by the kernel's `hid-uclogic` driver. The work of the DIGImend project is now part of this driver, so you no longer need to install DIGImend separately on a recent kernel.

Manufacturer drivers are the fallback for models or features the built-in support doesn't cover:

* **Xencelabs** ships a Linux driver. See [Does my pen tablet work with Linux?](https://solutions.xencelabs.com/en/support/solutions/articles/67000412792-does-my-pen-tablet-work-with-linux-). Note that their list of [tested Linux distributions](https://solutions.xencelabs.com/en/support/solutions/articles/67000635098-tested-and-compatible-linux-operating-systems) has not been updated for recent releases.
* **XP-Pen** ships a Linux driver. See [How to install XPPen Linux driver on Ubuntu (64 bits)](https://www.xp-pen.com/faq/how-to-install-xppen-linux-driver-on-ubuntu-64-bits.html).
* **Huion** has drivers for some models. See [Does Huion Have a Tablet Driver That Supports Linux?](https://support.huion.com/en/support/solutions/articles/44001769972-does-huion-have-a-tablet-driver-that-supports-linux-) and [Huion driver for Linux (Wayland) FAQ](https://support.huion.com/en/support/solutions/articles/44002812104-huion-driver-for-linux-wayland-frequently-asked-questions).

{% hint style="warning" %}
**TODO (Seven):** Did you try any Huion, XP-Pen, or Xencelabs tablets? If so, with the built-in support, the manufacturer driver, or OpenTabletDriver, and how did it go?
{% endhint %}

### What to expect from Huion and XP-Pen without a manufacturer driver

With only the built-in support, the pen usually works out of the box, including pressure. But:

* The buttons on the tablet and on the pen may be fixed to default actions and can't be remapped.
* On many models, the second pen button acts as an eraser. This is how the kernel handles pens that identify themselves like a Microsoft Surface pen.
* Dials and some tablet buttons may not work at all until support for that model is added.

The usual fix for these is [udev-hid-bpf](https://gitlab.freedesktop.org/libevdev/udev-hid-bpf), which adds per-model fixes without rebuilding the kernel. For a detailed walkthrough, see David Revoy's [Huion Inspiroy H610X review on GNU/Linux](https://www.davidrevoy.com/article1072/huion-inspiroy-h610x-review-on-gnulinux) and [Huion Kamvas Pro 19 review on GNU/Linux](https://davidrevoy.com/article1054/huion-kamvas-pro-19-review-on-gnulinux).

### Newer tablets need a newer distribution

Support for a new tablet arrives in several separate pieces: the kernel, libwacom (a database that tells the desktop what buttons and features the tablet has), libinput, and the desktop environment itself. Each one reaches your distribution on its own schedule.

This means that a tablet that was released recently may not be recognized, or may be only partly supported, on a distribution with older packages. For example, the XP-Pen Artist 22R Pro needed Linux 6.17 and KDE Plasma 6.4 and 6.5 before its buttons and dials worked ([source](https://planet.kde.org/redstrate-2025-07-30-the-xp-pen-artist-22r-pro-works-on-linux-now)).

If you have a tablet that is less than a year or two old, use a distribution that updates quickly, such as Fedora or Arch, rather than one with long-term-support packages such as Debian, Ubuntu LTS, or Linux Mint.

Also see [Why is my tablet unknown?](https://help.gnome.org/gnome-help/wacom-tablet-unknown.html) in the GNOME help.

### Only install one tablet driver

I don't recommend installing two different tablet drivers. On Linux this includes the built-in support: OpenTabletDriver and the manufacturer drivers work by taking the tablet away from the kernel driver, and two of them will fight over the same tablet. For example, do not install a Huion driver AND OpenTabletDriver. For more details, see [Using multiple tablet drivers on the same computer](../../drivers/multiple-tablet-drivers.md).

### OpenTabletDriver

[OpenTabletDriver](https://docs.sevenpens.com/opentabletdriver) (OTD) is a popular alternative on Linux, especially in the osu! community. Consider it when your tablet isn't supported by the built-in drivers, when you want more control over the mapping, or when you want lower latency for gaming.

Things to know about OTD on Linux:

* OTD disables the `wacom`, `hid_uclogic`, and `hid_digimend_uclogic` kernel modules and installs udev rules so it can access the tablet. This means the built-in support stops working while OTD is installed. See [Required Permissions](https://opentabletdriver.net/Wiki/Documentation/RequiredPermissions).
* OTD runs as a user service. To start it automatically: `systemctl --user enable opentabletdriver.service --now`.
* To get pen pressure, switch the output mode to **Artist Mode**.
* With multiple monitors, set the display area to **Virtual Display** in OTD, and map the tablet to all screens in your desktop's tablet settings.

For troubleshooting, see the [OpenTabletDriver Linux FAQ](https://opentabletdriver.net/Wiki/FAQ/Linux).

## X11 versus Wayland

Linux desktops run on one of two display systems: the older X11, or the newer Wayland. This matters for tablets because **many older guides and videos use the `xsetwacom` command, which only works on X11.**

* Fedora (GNOME) and recent Ubuntu use Wayland. KDE Plasma uses Wayland by default.
* Linux Mint Cinnamon uses X11 by default.

On Wayland, configure your tablet through your desktop's settings app instead. On GNOME, [gsetwacom](https://who-t.blogspot.com/2024/06) is a command-line replacement for `xsetwacom`.

## Configuring the tablet

Tablet settings are part of the desktop environment, not a separate driver app.

### GNOME (Fedora, Ubuntu, Debian)

Open **Settings** > **Wacom Tablet** (called **Graphics Tablets** starting with GNOME 48). Even though the old name says "Wacom", this panel works for other brands too.

<div><figure><img src="../../../.gitbook/assets/fedora-drawtab-ui (1).png" alt="GNOME Settings tablet panel on Fedora 43"><figcaption><p>GNOME Settings on Fedora 43</p></figcaption></figure> <figure><img src="../../../.gitbook/assets/fedora-drawtab-ui (2).png" alt="GNOME Settings tablet panel on Fedora 43"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/fedora-drawtab-ui (3).png" alt="GNOME Settings tablet panel on Fedora 43"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/fedora-drawtab-ui (4).png" alt="GNOME Settings tablet panel on Fedora 43"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/fedora-drawtab-ui (5).png" alt="GNOME Settings tablet panel on Fedora 43"><figcaption></figcaption></figure></div>

Features:

* Absolute vs relative positioning (mouse mode)
* Mapping tablet button actions
* Mapping the tablet's active area to a display
* Force proportions - called **Keep aspect ratio**
* Pressure feel for the pen tip and eraser

{% hint style="warning" %}
**TODO (Seven):** Check the caption, alt text, and feature list against the five screenshots.
{% endhint %}

### KDE Plasma

Open **System Settings** > **Drawing Tablet**. KDE has added tablet features steadily during Plasma 6:

* Plasma 6.2 - pen calibration
* Plasma 6.3 - a pressure curve editor, a pressure range setting, mapping part of the tablet to the whole screen, and a pen tester that shows pressure and tilt ([source](https://blogs.kde.org/2025/01/04/this-week-in-plasma-artistry-and-accessibility/))
* Plasma 6.4 and 6.5 - support for dials

### Cinnamon (Linux Mint)

{% hint style="warning" %}
**TODO (Seven):** Describe the Cinnamon tablet settings you used on Mint 22.2.
{% endhint %}

For step-by-step instructions to keep the aspect ratio on GNOME and KDE, see [Force proportions](../../customizing/force-proportions.md).

## My experience

{% hint style="warning" %}
**TODO (Seven):** Which desktop(s) did you use: Mint Cinnamon only, plus GNOME on Fedora 43? Any KDE? Were you on X11 or Wayland when you noticed the lower pointer lag?
{% endhint %}

I tested several Wacom devices with the built-in support of Linux Mint 22.2 Cinnamon:

* One by Wacom CTL-672 - worked
* Wacom Intuos Pro Medium 2017 (PTH-660) - worked
* Wacom Movink 13 - was not recognized
* Wacom Intuos Pro Medium 2025 (PTK-670) - was not recognized

Linux Mint 22.2 is based on Ubuntu 24.04, so the two newest tablets are probably not recognized because its packages are older than these tablets (see [Newer tablets need a newer distribution](#newer-tablets-need-a-newer-distribution)).

{% hint style="warning" %}
**TODO (Seven):** Did the Movink 13 and PTK-670 work on Fedora 43? If so, say so here; it confirms the explanation above.
{% endhint %}

Pointer lag: I noticed less pointer lag than on a Windows or macOS system using the Wacom driver.

## What you give up compared to Windows and macOS drivers

Basic features are available, but many features you might be used to in the manufacturer drivers are not:

* No per-application settings.
* Pressure curve settings depend on the desktop: GNOME has a simple pressure feel slider, and KDE Plasma 6.3 and later has a pressure curve editor. Neither offers the per-app curves of the Wacom driver.
* No multiple profiles that you can switch between.
* Support for touch rings, dials, and other extra controls varies by tablet and desktop.

## Apps

Krita, GIMP, Inkscape, and MyPaint run natively on Linux and support pen pressure.

{% hint style="warning" %}
**TODO (Seven):** Which apps did you draw in, and did pressure and tilt work?
{% endhint %}

### Windows apps through WINE

Some Windows-only apps can run through WINE, or Bottles (which manages WINE for you).

* A note from [Tablet kitten](../../../resources/community/tablet-kitten.md) - WINE builds with wow64 have a broken wintab32.
* Clip Studio Paint - [Clip Studio Paint on Linux](https://kw0.gitbook.io/tablet-resources/linux/clip-studio-paint) uses Bottles, and reports that pressure works through WinTab.
* Paint Tool SAI 2 - [https://github.com/TibixDev/sai2-guide](https://github.com/TibixDev/sai2-guide)

## Troubleshooting

### Checking whether Linux sees your pen

These command-line tools show whether Linux receives input from the pen, including pressure and buttons:

* `libinput debug-tablet` - shows the pen's position, pressure, and tilt as libinput sees them.
* `sudo evtest` - lists input devices and shows their raw events.
* `hid-recorder` - shows the raw reports from the tablet. See [Tablet reports](../../advanced/tablet-reports.md).

### Known issues

* **Ubuntu 26.04: Krita ignores the pen** (May 2026) - the pen works in other apps but not in Krita. Users traced it to Xwayland 24.1.10, and downgrading to 24.1.9 fixed it. See the [Krita Artists thread](https://krita-artists.org/t/krita-5-3-on-ubuntu-26-04-wacom-not-working/183761).
* **Huion driver on Wayland** - a second cursor can appear in mouse mode, and some features may stop working after a reboot until you restart the driver. See [Huion driver for Linux (Wayland) FAQ](https://support.huion.com/en/support/solutions/articles/44002812104-huion-driver-for-linux-wayland-frequently-asked-questions).

## Uninstalling and cleaning up drivers

When switching between a manufacturer driver and OpenTabletDriver, uninstall the old one first. Manufacturer drivers for Linux usually come with an uninstall script, or can be removed with your package manager. After uninstalling OTD, make sure its kernel module blacklist and udev rules are gone too, so the built-in support works again.

For brand-specific steps, see [Uninstalling tablet drivers](../../drivers/uninstalling-tablet-drivers.md).

## Further reading

### Guides

* [GNOME Help - Why is my tablet unknown?](https://help.gnome.org/gnome-help/wacom-tablet-unknown.html)
* [KDE UserBase - KDE Wayland for artists](https://userbase.kde.org/Kde_wayland_for_artists)
* [ArchWiki - Graphics tablet](https://wiki.archlinux.org/title/Graphics_tablet)
* [NixOS Wiki - Drawing Tablet](https://wiki.nixos.org/wiki/Drawing_Tablet)
* [David Revoy - Interim Install Guide: KDE Neon User Edition for a professional digital painter workstation](https://www.davidrevoy.com/article1145/interim-install-guide-kde-neon-user-edition-for-a-professional-digital-painter-workstation) - 2026-05-22
* [David Revoy - Why Drawing Tablet Brands Won't Collaborate on Linux FLOSS Drivers](https://davidrevoy.com/article1154/why-drawing-tablet-brands-wont-collaborate-on-linux-floss-drivers) - 2026-06-22

### Videos

* [MossCharmly - HUION Tablets (Kamvas 16 (2.5k) on LINUX (POP\_os)](https://www.youtube.com/watch?v=ibuH-hGkmdI) - 2023-05-13
* [MossCharmly - Demystifying Linux for Artists](https://www.youtube.com/watch?v=hQ2VpPchETk) - 2024-03-02
* [MossCharmly - Linux PC Build for Digital Artists](https://www.youtube.com/watch?v=eiLnEUS3r5k) - 2024-03-17
* [Mindful Technology - Huion Inspiroy H1161 drawing tablet on Debian Linux: install driver & declutter HOME](https://www.youtube.com/watch?v=kbzlKn3zhrk) - 2023-10-24
* [Linuxedo - Wacom Intuos S Wireless | Unboxing and Setting up on Linux Mint](https://www.youtube.com/watch?v=-TBT_l6qwj0) - 2021-01-17
* [Tony Tascioglu - How to Map a Wacom Tablet to a Single Monitor on Linux](https://www.youtube.com/watch?v=DEdUa5lHZbU) - 2021-01-19
* [Brodie Robertson - Easily Setup Your Wacom Tablet Under Linux](https://www.youtube.com/watch?v=dzplf-0RJDE) - 2021-09-12
* [Switched to Linux - Wacom Tablets on Linux Mint](https://www.youtube.com/watch?v=stDM3T4Fu5A) - 2018-02-27

Note: the older videos may use `xsetwacom`, which only works on X11 (see [X11 versus Wayland](#x11-versus-wayland)).

### Do you use Arch, btw?

* [ALCC - Part 6: Creating Art on Arch Linux](https://www.youtube.com/watch?v=7jcb4p-FmUU) - 2026-02-10
* CSP + Arch - [eninabox - Easily Install CLIP STUDIO PAINT on Linux (CachyOS/Arch)](https://www.youtube.com/watch?v=5CPzvDQ1Nm4) - 2025-12-31
