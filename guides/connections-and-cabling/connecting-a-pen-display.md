# Connecting a pen display to a computer

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

* You could have HDMI ports on the graphics card
* You could have HDMI ports on the motherboard of the computer

As a general rule, always use the HDMI ports on the graphics card

Only use the HDMI ports on the motherboard as a last resort.

## Motherboard HDMI ports

Sometimes you'll read a statement like "HDMI doesn't work on the motherboard". That's kind of an exaggeration but its a well intentioned one. But it is true that sometimes HDMI ports don't work on the motherboard. Let's go through the reasons.

First, to get an motherboard HDMI port working you need several things to be true

* First the HDMI port must exist
* Second, the computer has to have a component that sends a display signal to the port. This is called integrated graphics. It's called "integrated" because the graphics component is on the CPU.&#x20;
* Third, the use of the HDMI port must be enabled.

What often happens is, not all these conditions are met with motherboard HDMI ports on all PCs.

The HDMI port might exist, but there is no "integrated graphics" - so that port won't work

You might have the port and integrated graphics is available, but also the BIOS might be set to disable the use of that port. So you'll have to enable it in the BIOS.

Finally, some computers have an interesting behavior where, if a graphics card is installed, then they automatically disable the motherboard HDMI. In other words, you can either use the motherboard HDMI or the graphics card, but not both.

You aren't going to hurt your computer by trying to use motherboard HDMI, but you should know why it might not work.

## HDMI ports on graphics cards

These will work, but there is one thing you should be aware of. Sometimes graphics cards have N ports, but only N-1 can be used simultaneously. I have a card like this.

## Motherboard HDMI vs graphics card HDMI

If you have two ports that work - one on the motherboard and one on the graphics card, then which should you pick? The answer is **ALWAYS try the graphics card HDMI first and only use the motherboard HDMI as a last resort**.

First, Motherboard HDMI support just isn't as powerful as what you will typically find on a graphics card from the same era. The motherboard HDMI may not support 4K or may not support a high enough refresh rate. So it might, work but your experience might be degraded.

Second, both motherboard HDMI and the graphics card need to use memory to do their work. A graphics card comes with its own memory that is dedicated to dealing with graphics. Motherboard HDMI as far as I know - does not use any dedicated memory - but instead uses the same memory as the CPU. This means that you CPU is "losing" some memory so that the motherboard HDMI can use it instead.

## What if you don't have any HDMI ports?

If you need to make an HDMI connection but have no HDMI ports you can convert other ports to HDMI using an adapter. See [**Using HDMI adapters with pen displays**](../pen-displays/using-hdmi-adapters-with-pen-displays/)&#x20;

## Dealing with NO SIGNAL

When you've connected your display you might see it show a message saying NO SIGNAL. Here is a [**troubleshooting guide to work through the NO SIGNAL problem**](../../troubleshooting/troubleshoot-no-signal.md).

## What about connecting a pen display mobile devices?

Go here: [**Connecting a pen display to a mobile device**](connecting-a-pen-display-to-a-mobile-device.md)&#x20;

## What about wireless connectivity?

No pen displays connect wirelessly. They all require at least one cable to connect to your computer.&#x20;



