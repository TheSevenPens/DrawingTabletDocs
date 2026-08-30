# Calibrating color

## Overview

For other calibration types, see [Calibrating a drawing tablet](calibrating.md).

There are two broad categories of methods used to calibrate color for a display:

**Profile-based color calibration** uses specialized calibration hardware and software to measure your display's color output and then modify how it displays those colors to help the display more closely match industry color standards. This technique requires expertise and familiarity with advanced color concepts.

**Ad hoc color adjustment** uses basic color, brightness, and contrast adjustments. It helps your display match your preferences or another nearby display. This method requires no specialized calibration hardware or software. It is available on most displays.

{% hint style="info" %}
If you are looking to make your pen display match the color of some other display/screen, then go also here: [Matching colors across displays](matching-colors-across-displays.md)
{% endhint %}

##

## Profile-based color calibration

This guide does not cover profile-based calibration in detail. Use these resources to learn more.

* [Keith Cooper - Monitor calibration: how do you know it's right? Can you match monitors? Are cheaper calibrators OK?](https://www.youtube.com/watch?v=v2mwdvxI3iw) 2024-11-01
* [Wacom — Cintiq Pro 27 Color Calibration](https://www.youtube.com/watch?v=b1hfF0U6UtM) — 2024-08-14
* [Snazzy Labs — How Does Color Calibration Work?](https://www.youtube.com/watch?v=i0oQKsYc-tU) — 2021-05-07
* [Hardware Unboxed — How to Calibrate Your Monitor: The Comprehensive Beginner's Guide](https://www.youtube.com/watch?v=f2nVNxx1IHo) — 2020-07-06
* [PhotographyLife - The Basics of Monitor Calibration](https://photographylife.com/the-basics-of-monitor-calibration)

## Ad-hoc color calibration

Ad hoc calibration uses available controls to adjust your display's colors.

### Display panel color controls

Many pen displays let you control how colors appear. You can often access these controls through the on-screen display (OSD) menu. Some controls may also be available in the tablet driver. Some pen displays offer no color controls or only limited controls.

Here are some adjustments you can typically make with these controls:

* Change the intensity of individual red, green, and blue components.
* Adjust brightness, contrast, and color temperature.
* Change the color mode, such as sRGB or Display P3.

There is no single formula for configuring display color. Experiment to find settings that work for you.

### Accessing the OSD menu

There are different methods to access a Pen display's OSD menu.&#x20;

* For many Pen displays, you may need to hold down the power button for a few seconds.
* For others, the OSD will appear when you press a capacitive touch sensor.&#x20;
* Some let you bring up the OSD by clicking on a button in the tablet driver user interface
* Some displays simply do not have an OSD.

NOTE: Some pen displays have an OSD with color settings but those color settings may be disabled.

### Color gamut clamping

Some displays have a very wide color gamut. For example, a pen display may report 140% sRGB volume. Highly saturated colors can then look uncomfortably intense. Standard saturation controls may not reduce this effect enough. Consider clamping the wide gamut to a smaller gamut. See [Clamping wide-gamut displays to sRGB](clamping-to-srgb.md).
