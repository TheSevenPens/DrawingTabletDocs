# Connecting with HDMI

## Overview

{% hint style="info" %}
Read this first: [Connecting a pen display](./)
{% endhint %}

There are two common ways to get a video signal to a pen display: an **HDMI** cable or a **USB-C** cable. This page covers the **HDMI** approach - how to connect to an HDMI port, and what to do if you don't have one. For the other approach, see [Connecting a pen display with USB-C](connecting-pen-display-usbc.md).

## Video

[https://youtu.be/iKl\_3NYjlsY](https://youtu.be/iKl_3NYjlsY)

{% embed url="https://youtu.be/iKl_3NYjlsY" %}

## Understand the basics

PLEASE read [Connecting a Pen Display](./). One you understand the basics, this document will be easier understand.

## Cabling when HDMI is used

**HDMI** carries only the video signal, so power and data are handled by separate cables. Typically, this will be two cables (one for power and one for data) or a 3-in-1 cable (see [Connecting with a 3-in-1 cable](connecting-with-a-3-in-1-cable.md)). When a 3-in-1 cable is used, there will be two USB-C ports on the tablet.

<figure><img src="../../../.gitbook/assets/image (7).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (8).png" alt="" width="563"><figcaption></figcaption></figure>

## Getting power

The power cable will typically be marked with a red connector or tag that is red or has a power symbol.

<figure><img src="../../../.gitbook/assets/Slide_20260715_224955.jpg" alt="" width="563"><figcaption></figcaption></figure>

A power adapter will come with the tablet. Use it.

<figure><img src="../../../.gitbook/assets/image (9).png" alt="" width="563"><figcaption></figcaption></figure>

Some tablets also have a power extension cable to be used with the 3-in-1 cable.

<figure><img src="../../../.gitbook/assets/image (11).png" alt="" width="563"><figcaption></figcaption></figure>

## Important reminder

ALL THREE CABLES/CONNECTIONS MUST BE USED.

<figure><img src="../../../.gitbook/assets/image (12).png" alt="" width="563"><figcaption></figcaption></figure>

**If the DATA cable is not connected,** the screen will show something, but the driver will not detect the tablet and the pen will not work.

**If the POWER cable is not connected,** your tablet MIGHT get enough power from the DATA cable. But even if it does, I highly recommend connecting the power cable to the supplied power adapter.

<figure><img src="../../../.gitbook/assets/image (13).png" alt="" width="563"><figcaption></figcaption></figure>

If the power cable is not connected, you might see a variety of problems:

* The pen display will not turn on (the screen is black).
* The pen display screen turns on briefly, then goes dark for a few seconds. This may repeat.
* The pen display's screen shows something but cannot reach maximum brightness.

**If the HDMI cable is not connected,** the screen will turn on, but you will see a NO SIGNAL message (possibly followed by a POWER SAVING message). You might also see the screen cycle between RED, GREEN, and BLUE. The NO SIGNAL problem can occur for other reasons and can be confusing. For a detailed troubleshooting guide, see [TSG: Pen display shows NO SIGNAL message](../../../troubleshoot/tsg-no-signal.md).

<figure><img src="../../../.gitbook/assets/image (14).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Slide_20260715_230117.jpg" alt="" width="563"><figcaption></figcaption></figure>

## Which USB-C port on the tablet to use?

Pen displays usually have 3 USB-C ports. The 3-in-1 cable needs to be plugged into one of them. Which one to use, or whether both can be used, depends on the specific tablet. Consult the user manual.

* Sometimes the top USB-C port is intended for the 3-in-1 cable.
* Sometimes the bottom USB-C port is intended for the 3-in-1 cable.
* Read the user manual or contact customer support if you are not sure.

<figure><img src="../../../.gitbook/assets/image (15).png" alt="" width="563"><figcaption></figcaption></figure>

## Unusual cabling

There are some variations on the 3-in-1 cable pattern. Not many tablets use these alternative connection patterns, but you should be prepared for them. Everything in this document will also apply to these cases.

<figure><img src="../../../.gitbook/assets/image (16).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (17).png" alt="" width="563"><figcaption></figcaption></figure>

## Picking an HDMI port

If your computer has multiple HDMI ports, you need to pick one.

**Laptops.** It shouldn't matter. Any HDMI port should work.

**Small form factor / mini PCs.** Also shouldn't matter. Any HDMI port should work.

**Desktop PCs with a separate graphics card.** This is where it gets complicated. You might have HDMI ports in two different locations:

* You could have HDMI ports on the graphics card (GPU).
* You could have HDMI ports on the motherboard I/O panel.

As a general rule, always use the HDMI ports on the graphics card. Only use the motherboard HDMI ports as a last resort. More here: [Motherboard HDMI vs GPU HDMI ports](motherboard-vs-gpu-hdmi.md).

## Covered HDMI ports

Sometimes a port you are looking for is there, but it is covered by a small plastic cap.

You may see these caps referred to as:

* port dust covers
* port dust plugs
* port protectors
* port caps

These caps are often black and easy to miss. They pull off with almost no effort, and they do **not** mean the port is unusable - they only protect the port from dust and damage. I mention this because people often conclude they "don't have a port" when it is simply capped and they do not realize what they are looking at.

## Not enough HDMI ports?

A very common situation: your computer has one HDMI port, but it is already being used by a monitor.

Before you buy anything, know that **most modern GPUs have only one HDMI port but several DisplayPort ports**. So you often have more video outputs than you think - they just aren't HDMI. Here are your options, roughly best to worst:

* **Move your monitor to a DisplayPort connection.** Many monitors accept DisplayPort. If you connect the monitor with DisplayPort, that frees up the HDMI port for your pen display.
* **Use an adapter** to convert another video output (DisplayPort, USB-C, DVI, VGA) to HDMI. See [Using HDMI adapters with pen displays](../../pen-displays/hdmi-adapters/).
* **Add or upgrade a graphics card** so you have more - and better - video outputs.
* **Avoid HDMI splitters.** They can be flaky, they can only mirror the same image to both displays, and your computer sees them as a single display. More here: [Using HDMI splitters with pen displays](../../pen-displays/hdmi-splitters.md).

## No HDMI ports at all?

If you need an HDMI connection but have no HDMI ports, you can convert other ports to HDMI with an adapter. See [Using HDMI adapters with pen displays](../../pen-displays/hdmi-adapters/).

In theory, if you have a GPU, you could buy a different one with multiple HDMI ports. The challenge is that there are vanishingly few such GPUs.
