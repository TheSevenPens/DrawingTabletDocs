# Calibrating color

## Overview

For other calibration types, see [Calibrating a drawing tablet](calibrating.md).

There are two broad categories of methods used to calibrate color for a display:

**Profile-based color calibration** uses specialized calibration hardware and software to measure your display's color output and then modify how it displays those colors to help the display more closely match industry color standards. This technique requires expertise and familiarity with advanced color concepts.

**Ad hoc color adjustment** uses basic color, brightness, and contrast adjustments. It helps your display match your preferences or another nearby display. This method requires no specialized calibration hardware or software. It is available on most displays.

## Matching colors on two different displays

People often get a new pen display and find its colors differ. The colors may not match their monitor, laptop screen, or phone. Users will of course want them to look exactly the same.

Let me set expectations before you get frustrated. In most cases, two displays cannot look exactly the same in color and brightness. In most cases they will be obviously different. Too many factors in the hardware exist to make an exact match impossible. Aim to make your pen display close enough for your work.&#x20;

Why don't displays look the same?

* They use different display technologies and/or emit color in differently.
* They use different surface treatments (anti-glare treatments, etched glass, etc) that affect black levels and color intensity. Many phone and mobile screens do not use such treatments and giving them glossier screens more intense colors.
* Display panels may shift a bit depending on viewing angles. You might be viewing a pen display from a broader set of angles than your much smaller phone. &#x20;

In limited cases, two displays can look very similar. Both must support the same color standard, such as Display P3. You must also use profile-based color calibration.&#x20;

## Profile-based color calibration

This guide does not cover profile-based calibration in detail. Use these resources to learn more.

* [Keith Cooper - Monitor calibration: how do you know it's right? Can you match monitors? Are cheaper calibrators OK?](https://www.youtube.com/watch?v=v2mwdvxI3iw) 2024-11-01
* [Wacom — Cintiq Pro 27 Color Calibration](https://www.youtube.com/watch?v=b1hfF0U6UtM) — 2024-08-14
* [Snazzy Labs — How Does Color Calibration Work?](https://www.youtube.com/watch?v=i0oQKsYc-tU) — 2021-05-07
* [Hardware Unboxed — How to Calibrate Your Monitor: The Comprehensive Beginner's Guide](https://www.youtube.com/watch?v=f2nVNxx1IHo) — 2020-07-06

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
