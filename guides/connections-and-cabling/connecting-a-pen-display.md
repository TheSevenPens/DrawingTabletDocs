# Connecting a pen display to a computer

## Video

{% embed url="https://youtu.be/iKl_3NYjlsY" %}

## Inputs & outputs

Remember that essentially a pen display is a plastic box that contains two separate devices: (1) a pen tablet and (2) a display.

We need to account for 4 things to use a pen display.

| Input or Output  | Needed by         | Notes                                                                                                                           |
| ---------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Power to tablet  | tablet component  | very little power is needed                                                                                                     |
| Data             | tablet component  | for example, pen position data is sent to the computer. Also the computer can send data to the tablet such as a firmware update |
| Power to display | display component | much more power needed than the tablet component                                                                                |
| Display signal   | display component | What is shown by the tablet                                                                                                     |

## Display connector types

This document is going to talk about connectors a lot. So you need to know what they look like first. Read this guide on [**different display connector types**](../pen-displays/display-connector-types.md) before you continue.

## Cabling options

Those four components are distributed over cabling differently, depending on the the cabling option involved.&#x20;

### Option A: one USB-C cable

Some pen displays can run on a single USB-C cable. This used to be uncommon. But Increasingly many pen displays support this option. More here: [**Connecting a pen display with one USB-C cable**](connecting-a-pen-display-with-one-usb-c-cable.md)&#x20;

### Option B: 3 cables&#x20;

* One USB cable for pen tablet (power, data)
* One power cable for the display power
* One display cable to carry the display signal - This will almost always be an HDMI cable. Though some tablets support alternate connector types for the display signal

### Option C: 2 cables

* one cable provides power for the display component
* one USB-C cable handles everything the other 4 components

The 2 cable setup is how I use my Wacom Cintiq Pro 27.&#x20;

### Option D: 3-in-one cable

This is a special kind of cable. One end will have a single USB-C connection. The other end it will have the different connections. Typically these will be: HDMI, USB-A, and some kind of power. More here: [**3-in-1 cables**](connecting-a-pen-display-with-a-3-in-1-cable.md)

## Connecting via HDMI

HDMI connectors are extensively used. So let's start by addressing HDMI which shows up in option B and option D.

In principle this is easy: Take the HDMI from the pen display and find an HDMI port and plug it in.

For the vast majority of you this will "just work".&#x20;

But now let us explore all the complications

## Which HDMI port on the computer should you use?

If your computer has multiple HDMI ports you need to pick one.&#x20;

If it's a laptop - it shouldn't matter. Any HDMI port should work.

If it's a small form factor PC - then also it shouldn't matter. Any HDMI port should work.

If it's a PC that has a separate graphics card you might have an HDMI port in multiple very different locations

* You could have HDMI ports on the graphics card (GPU)
* You could have HDMI ports on the motherboard of the computer

As a general rule, always use the HDMI ports on the graphics card (GPU) . Only use the HDMI ports on the motherboard as a last resort.

more here: [**Motherboard HDMI ports vs GPU HDMI ports**](motherboard-hdmi-vs-gpu-hdmi-ports.md).

## What if you don't have any HDMI ports?

If you need to make an HDMI connection but have no HDMI ports you can convert other ports to HDMI using an adapter. See [**Using HDMI adapters with pen displays**](../pen-displays/using-hdmi-adapters-with-pen-displays/)&#x20;

## Dealing with NO SIGNAL

When you've connected your display you might see it show a message saying NO SIGNAL. Here is a [**troubleshooting guide to work through the NO SIGNAL problem**](../../troubleshooting/tsg-no-signal.md).

## What about connecting a pen display mobile devices?

Go here: [**Connecting a pen display to a mobile device**](connecting-a-pen-display-to-a-mobile-device.md)&#x20;

## What about wireless connectivity?

No pen displays connect wirelessly. They all require at least one cable to connect to your computer.&#x20;



