# Connecting with HDMI

## Overview

{% hint style="info" %}
Read this first: [Connecting a pen display](./)
{% endhint %}

There are two common ways to get a video signal to a pen display: an **HDMI** cable or a **USB-C** cable. This page covers the **HDMI** approach — how to connect to an HDMI port, and what to do if you don't have one. For the other approach, see [Connecting a pen display with USB-C](connecting-pen-display-usbc.md).

Remember that a pen display has three requirements to work: **power**, **data**, and a **video signal**. HDMI carries only the video signal, so power and data are handled by separate cables (see [Connecting with a 3-in-1 cable](connecting-with-a-3-in-1-cable.md)).

## Video

[https://youtu.be/iKl\_3NYjlsY](https://youtu.be/iKl_3NYjlsY)

{% embed url="https://youtu.be/iKl_3NYjlsY" %}

## Considerations

Key things to keep in mind:

* HDMI is the most widely supported way to connect a pen display — most computers can use it directly or through an adapter.
* HDMI carries **only** video. You still need separate power and data connections, usually via a 3-in-1 cable.
* The main things to sort out are which HDMI port to use, and what to do if you have too few or no HDMI ports.

Compared to USB-C, HDMI is usually the more forgiving option — the rest of this page covers the few details worth getting right.

## 3-in-1 cables

This is a special kind of cable. One end has a single USB-C connection. The other end has several different connectors, usually HDMI, USB-A, and power. More here: [Connecting with a 3-in-1 cable](connecting-with-a-3-in-1-cable.md)

## Which HDMI port on the computer should you use?

If your computer has multiple HDMI ports you need to pick one.

**Laptops.** It shouldn't matter. Any HDMI port should work.

**Small form factor / mini PCs.** Also shouldn't matter. Any HDMI port should work.

**Desktop PCs with a separate graphics card.** This is where it gets complicated. You might have HDMI ports in two different locations:

* You could have HDMI ports on the graphics card (GPU)
* You could have HDMI ports on the motherboard I/O panel

As a general rule, always use the HDMI ports on the graphics card. Only use the motherboard HDMI ports as a last resort.

More here: [Motherboard HDMI vs GPU HDMI ports](motherboard-vs-gpu-hdmi.md).

### Watch out for hidden ports

Sometimes a port you are looking for is there, but it is covered by a small plastic cap. These caps are often black and easy to miss. They pull off with almost no effort, and they do **not** mean the port is unusable — they are only there to protect the port from dust and damage. I mention this because I've seen a lot of people conclude they "don't have a port" when it was simply capped.

## What if you don't have enough HDMI ports?

A very common situation: your computer has one HDMI port, but it is already being used by a monitor.

Before you buy anything, know that **most modern GPUs have only one HDMI port but several DisplayPort ports**. So you often have more video outputs than you think — they just aren't HDMI. Here are your options, roughly best to worst:

* **Move your monitor to a DisplayPort connection.** Many monitors accept DisplayPort. If you connect the monitor with DisplayPort, that frees up the HDMI port for your pen display.
* **Use an adapter** to convert another video output (DisplayPort, USB-C, DVI, VGA) to HDMI. See [Using HDMI adapters with pen displays](../../pen-displays/hdmi-adapters/).
* **Add or upgrade a graphics card** so you have more — and better — video outputs.
* **Avoid HDMI splitters.** They can be flaky, they can only mirror the same image to both displays, and your computer sees them as a single display. More here: [Using HDMI splitters with pen displays](../../pen-displays/hdmi-splitters.md).

### What if you don't have any HDMI ports at all?

If you need an HDMI connection but have no HDMI ports, you can convert other ports to HDMI with an adapter. See [Using HDMI adapters with pen displays](../../pen-displays/hdmi-adapters/).
