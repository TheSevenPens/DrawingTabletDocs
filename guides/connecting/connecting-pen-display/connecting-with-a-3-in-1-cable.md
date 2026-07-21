# Connecting with a 3-in-1 cable

A 3-in-1 cable is a special connection cable that pen displays use to connect to a computer.

{% embed url="https://youtu.be/iKl_3NYjlsY" %}

More here on the different ways a pen display can connect to a computer: [Connecting a pen display](./)

A 3-in-1 cable typically looks like this:

<figure><img src="../../../.gitbook/assets/connecting-with-a-3-in-1-cable-1.png" alt=""><figcaption></figcaption></figure>

Here's a typical picture of the three cables on the right.

<figure><img src="../../../.gitbook/assets/connecting-with-a-3-in-1-cable-2.jpg" alt=""><figcaption></figcaption></figure>

The power end can work in different ways, depending on which 3-in-1 cable you have.

<figure><img src="../../../.gitbook/assets/connecting-with-a-3-in-1-cable-3.png" alt=""><figcaption></figcaption></figure>

Older 3-in-1 cables may have a proprietary connection to the tablet instead of a regular USB-C connection.

<figure><img src="../../../.gitbook/assets/connecting-with-a-3-in-1-cable-4.png" alt=""><figcaption></figcaption></figure>

## Benefits of a 3-in-1 cable

* **Simplifies the physical design of the tablet**. It minimizes the number of physical ports on the tablet. Instead of having an HDMI port, power port, and USB-A data port, the tablet can just have 1 USB-C port.
* It also makes it **easier to keep track of cables**. You only need one 3-in-1 cable instead of three separate cables.
* Ideally, you would connect your tablet to the computer with a single USB-C cable. But this is not always possible.
  * USB-C ports on your computer may not supply enough power
  * USB-C ports on your computer may not support sending a display signal (aka DP alt mode)
  * Your computer may not have a USB-C port at all
  * So a 3-in-1 cable lets you use older ports that many computers do have, such as HDMI and USB-A, while still getting enough power to the tablet.

## Power for larger pen displays

Pen displays use a lot of power, and most of that power goes to the screen. The bigger the display, the more power it needs.

At some point a display gets big enough that your computer cannot supply enough power through its ports. In that case, you connect the power end of the 3-in-1 cable to a **separate power adapter** (a wall plug) instead of to the computer.

* This power adapter often comes with the tablet, but sometimes you have to buy it separately.
* Many tablets also include a **power extension cable**, which helps when the outlet or adapter is some distance from your computer.

## Which USB-C port on the tablet should you use?

Many modern pen displays have **two** USB-C ports. Which one the 3-in-1 cable goes into depends on the tablet:

* Some tablets want you to use the top port.
* Some want you to use the bottom port.
* Some let you use either one.

The most reliable way to know is to **read your tablet's user manual** - it will have a diagram showing exactly where the cable goes.

## 3-in-1 cable compatibility

3-in-1 cables are generally designed for specific tablets. Do NOT assume a cable is interchangeable:

* You can't mix and match 3-in-1 cables between brands (for example, Wacom vs. Huion vs. XP-Pen).
* You can't even assume a cable works across models from the _same_ brand. A 3-in-1 cable made for one Huion tablet may not work with a different Huion tablet.

So if you need to replace a broken cable, or your tablet didn't come with one, **verify compatibility with your specific tablet** before you buy. The compatibility information is usually listed on the brand's online store; if you can't find it, contact their customer support.

## Other cable variations

Not every tablet uses a true 3-in-1 cable. A couple of common variations:

* **2-in-1 cable + separate power.** One cable is dedicated to power, and a second "2-in-1" cable carries data and video from the computer.
* **3-in-2 cable.** This cable has two USB-C connectors on the tablet end instead of one.

## Using the 3-in-1 cable without the power end connected

You may encounter situations where the 3-in-1 cable is only partially connected:

* The HDMI cable is plugged into the computer
* The USB data cable is plugged into the computer
* But the power cable is not connected to anything

In some cases, even though only 2 of the 3 connections are accounted for, you may still successfully be able to use your pen display.

The reason for this is that the USB data cable MAY be able to get enough power from the USB-C port it is plugged into.

Some notes:

* If this works, it tends to be with 13-inch pen displays. At 16 inches or larger, they often need more power than many computer USB ports can provide.
* If this works, it may supply enough power for your pen display, but it might not be enough to use the display at full brightness.
* If there is not enough power from the USB data cable then you might see the pen display briefly turn on, then off, then on again repeatedly.
* I haven't seen anyone damage their tablet because of this configuration.

**My recommendation**

I strongly recommend that you always plug in all three parts of the 3-in-1 cable. It is better to know you have enough power than to guess.

## If the data cable is not connected

If you forget the **data** cable, your tablet driver will report that the tablet is not detected - even if you can see an image on the screen. That's because the video and data connections are separate: the screen can light up from the video cable while the driver still has no way to receive pen data. If the driver says your tablet isn't connected, check the data (USB-A) cable first. See [TSG: Tablet driver does not detect tablet](../../../troubleshoot/tsg-tablet-driver-does-not-detect-tablet.md).
