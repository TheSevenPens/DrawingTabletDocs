# Motherboard HDMI vs GPU HDMI ports

## Overview

On some computers there may be HDMI ports in two different locations:

* The motherboard
* The GPU (aka the graphics card)

You should always prefer to use the HDMI ports on the GPU first and only use the motherboard HDMI ports as a last resort.

## Location

There are two general locations on the back of a computer.

* There motherboard IO panel
* The GPU (aka the graphics card)

<figure><img src="../../../.gitbook/assets/image-000660.jpg" alt=""><figcaption></figcaption></figure>

## Motherboard HDMI vs GPU HDMI

If you have two ports that work - one on the motherboard and one on the graphics card, then which should you pick? The answer is **ALWAYS try the graphics card HDMI first and only use the motherboard HDMI as a last resort**.

First, Motherboard HDMI support just isn't as powerful as what you will typically find on a graphics card from the same era. The motherboard HDMI may not support 4K or may not support a high enough refresh rate. So it might, work but your experience might be degraded.

Second, both motherboard HDMI and the graphics card need to use memory to do their work. A graphics card comes with its own memory that is dedicated to dealing with graphics. Motherboard HDMI as far as I know - does not use any dedicated memory - but instead uses the same memory as the CPU. This means that you CPU is "losing" some memory so that the motherboard HDMI can use it instead.

## Other issues with motherboard HDMI&#x20;

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

##



