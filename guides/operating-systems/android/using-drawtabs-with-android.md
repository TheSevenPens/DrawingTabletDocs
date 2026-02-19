# Using drawing tablets with Android devices

## Overview

TLDR: **ONLY SPECIFIC COMBINATIONS** of drawing tablets and Android devices work well enough together.

A given drawing tablet connected to an Android device might result in one of several outcomes:

* The the tablet does not work at all
* The tablet works - but in an incomplete or dissatisfying way
* The core tablet features work in a good way - this is rare

## Feature availability: Android versus desktop computer

Connecting your tablet to your PC with the tablet drivers installed, gives you ALL the capabilities of your tablet.

Connecting your tablet to an Android device - even if everything works well - will only give you SOME of the capabilities of your tablet. This is because tablet drivers DO NOT EXIST for Android devices. Though occasionally some tablets feature "helper apps".

| Feature                                    | Status on desktop OS with driver installed | Status on Android                                                 |
| ------------------------------------------ | ------------------------------------------ | ----------------------------------------------------------------- |
| Pressure curves in driver                  | AVAILABLE                                  | NOT SUPPORTED. Need to rely on application pressure curve support |
| Display Toggle for multi-monitor scenarios | AVAILABLE                                  | NOT SUPPORTED                                                     |
| Configuring Tablet Buttons                 | AVAILABLE                                  | NOT SUPPORTED                                                     |
| Configuring Pen Buttons                    | AVAILABLE                                  | Limited configuring might be available in applications            |
| On screen shortcut menus                   | AVAILABLE                                  | NOT SUPPORTED                                                     |
| Force Proportions                          | AVAILABLE                                  | May or May not be implemented                                     |



## Compatibility

DO NOT assume a drawing tablet **fully** works with your android device. Check with the tablet manufacturer before trying this.&#x20;

Key points

* BOTH the android and the tablet have to support this working.
* There are some specific features that must be supported for this scenario to work, and not combinations of  drawing tablet and android device support these features correctly.&#x20;
* In general, I found that Android 14 and Android 15 worked better with drawing tablets (if the drawing tablet supports being used with Android devices)
* In some specific cases, I have been informed that older Android versions work with some drawing tablets designed to work with those versions.

## My compatibility testing results

More here: [Testing Drawing Tablet Compatibility with Android devices](testing-drawing-tablet-compatibility-with-android-devices.md)

## **Feature support**&#x20;

### Overview

A drawing tablet and its driver provide many features. When used with Android not all features are supported or are supported equally well.&#x20;

### **Active area mapping with automatic "Force Proportions" for pen tablets**

Without this feature, if you draw shape on the on drawing tablet it will show up as distorted on the android tablet. The most common sign this is NOT happening is that if you draw a circle on the tablet it will show up as an oval on the android device.

With a normal desktop computer, you can enable "Force Proportions" in the tablet driver to fix this problem. But you cannot install any tablet drivers for android devices. So, you must rely on this happening automatically. Unfortunately not all combinations of drawing tablets and android devices can do this.&#x20;

More here: [Matching aspect ratios with Force Proportions](../../customizing/force-proportions.md)

### Active area mapping for landscape and portrait modes

Android device can be held in either landscape or portrait orientation. Ideally, the active area of the tablet is mapped such that it maximizes the drawing space of the active area for the current orientation.

A pen tablet may not be able to map the active area as you would intuitively expect to your android device. With some tablets only a portion of the tablet's active area will be usable for drawing when connected to an android device.

This is another case where on a normal computer, the tablet drivers can address this problem. But tablet drivers are not available for android devices.

### Buttons and dials on tablet

Because there is no manufacturer driver on an android device, there is no way to control what the buttons or dials on the tablet do. They are inactive when using an android tablet.

As a WORKAROUND, some people have used the KeyMapper app on the  to map the buttons and dials: see [r/huion - How to set up buttons and pen with phone](https://www.reddit.com/r/huion/comments/1mzhx0c/how_to_set_up_buttons_and_pen_with_phone/?utm_source=share\&utm_medium=web3x\&utm_name=web3xcss\&utm_term=1\&utm_content=share_button). I have not personally tested this, but it is worth exploring.

ChromeOS does have some limited support for configuring buttons on the tablet, so in the future I hope we see this feature brought into Android.\\

### Buttons on the pen

Like buttons on the tablet, currently android devices do not let you configure what the buttons on the pen do.&#x20;

### Pressure curve in the tablet driver

Because there is no manufacturer driver, there is no way to control what the pressure curve within the driver. You will have to rely on the pressure curve control in your applications - if it has them.

## Manufacturer tablet drivers

With a PC, to use your tablet you normally install drivers provided by the manufacturers.

But for Android devices, you don't install any drivers (and manufacturers don't provide any Android drivers). Instead, you will rely on the built-in support in your android device.

While this seems like a good thing, it also means you cannot configure the tablet or take advantage of some specific features.



## Applications

For a list of applications that work on Android go here: [Apps](../../../apps/).

## Considerations for a pen tablet

Bluetooth. I don't know if this will work. I haven't ever tried.

## Cabling issues

Some drawing tablets require a separately-purchased OTG ("on-the-go") USB adapter to work with your Android device.&#x20;

## Connecting a pen display

* Your android device must have a USB-C port that supports DP alt mode. Not all Android device support have such USB-C ports.
* The USB-C cable you use to connect the tablet to the android device must be capable of transmitting a display signal.
*

## **Power**

With a pen tablet, your android device will be able to provide enough power for the tablet.

With a pen display, your android device may NOT be able to provide enough power. You may need to get additional power from an adapter. Even if the android device can provide more power, be aware that the pen display reduce your battery life.

## Links

General

* [XP-Pen - Drawing tablets compatible with Android ](https://www.xp-pen.com/drawing-tablets-for-android.html)
* [Wacom - What Android applications can I use for painting or drawing?](https://support.wacom.com/hc/en-us/articles/1500006338802-What-Android-applications-can-I-use-for-painting-or-drawing)&#x20;

Pen tablets

* [Wacom - Connect your Wacom One pen tablet and turn it on (Android)](https://www.youtube.com/watch?v=22-ASsVGsuM) 2023-08-10
* [Wacom - Wacom Center for Android](https://www.youtube.com/watch?v=sf8r_zxLl7o) app 2023-08-10
* [Wacom - How to Setup your Wacom Intuos for Android - English](https://www.youtube.com/watch?v=JFTjUCiEy1s) 2019-11-07
* [Aaron Rutten - Wacom Intuos on ANDROID - Review](https://www.youtube.com/watch?v=tMWwTuNO_7A) 2019-11-21
* [ibisPaint -  I connected a Wacom pen tablet to my smartphone](https://www.youtube.com/watch?v=f1WudQ4MbnI) \[Wacom Intuos] 2019-10-04&#x20;

Pen displays

* [Brad Colbow - The Wacom One's New Android Drawing Features Explained](https://youtu.be/qF6cyT0bq8g) 2020-01-20
* [XPPEN - Artist 12 (2nd Gen) Connection with Smartphone(Android)](https://www.youtube.com/watch?v=Q11XAvbirtQ) 2021-12-27
* [Teoh on Tech Android and Pen Display Workflow for Artist (featuring Huion Kamvas)](https://www.youtube.com/watch?v=VCalf9rbQ9U) 2021-07-21
* [Huion How to connect Kamvas Pro 13&16 (2.5K) to Android phone](https://www.youtube.com/watch?v=8y-Dfp3AApc) 2022-01-11

