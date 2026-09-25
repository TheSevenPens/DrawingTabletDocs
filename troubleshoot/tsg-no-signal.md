# TSG: Pen display shows NO SIGNAL message

## Overview

The "No Signal" message is very common when using a Pen display. It can be challenging to diagnose and fix, but it is often fixable. This practical, step-by-step guide contains every technique I know that can help identify and fix the problem.

## Be prepared to contact customer support

However, even this guide may not be enough. <mark style="color:red;">**Ultimately, you should be prepared to contact your tablet manufacturer's customer support team.**</mark>

## The NO SIGNAL message

The "No Signal" message takes a variety of forms with a Pen display. Most often, you'll see it when you turn on your Pen display, and a message will appear in a box that literally has the words "no signal." This message might also indicate which port on the Pen display is not getting the signal. In the example below, it is the USB-C port.

One confusing aspect of the "no signal" message is that it does not specify the signal type. The message refers to a video signal.

<figure><img src="../.gitbook/assets/tsg-no-signal-2.jpg" alt="" width="375"><figcaption><p>A typical no signal message. In this case, the message indicates that the USB-C port is where the pen display is looking for the signal.</p></figcaption></figure>

## Flashing colors as a NO SIGNAL message

Most of the time, when a Pen display does not receive a video signal, it shows a "no signal" message. However, some Pen displays flash colors instead of showing a distinct message. The screen cycles continuously through red, green, and blue. There may be no other message. These flashing colors indicate that the Pen display is not receiving a video signal.

## The POWER SAVING message

Sometimes you will see a single message. Other times, you will also see "power saving" in the same box or a separate message. The Pen display usually shuts down a few seconds later.

The power-saving message can be confusing. It has nothing to do with the power reaching the tablet. It indicates that the Pen display is not receiving a video signal. The display shuts down to avoid wasting power.

If you see the power-saving message, do not investigate the display's power supply. The display is receiving enough power. Do not spend time solving power problems that do not exist.

## The fundamentals of connecting a pen display

To troubleshoot a no signal problem, understand how to connect a Pen display correctly. This knowledge helps you identify, test, and solve connection problems.

There are three fundamental requirements for a Pen display to work correctly when connected to your computer.

* First, the Pen display must be getting enough power.
* Second, the Pen display must be able to send data to the computer. The data in this case is the position, pressure, and tilt of the pen. If it's unable to send this data, then the pen won't work.
* Third, the Pen display must receive a video signal from the computer. If it isn't getting a video signal for whatever reason, you will encounter the "no signal" message.

To stress this point: if you're seeing a "no signal" message, it only relates to the video signal. It does not relate to data or power.

Next, understand how cabling works. Some Pen displays require three separate cables. Others require two cables or a three-in-one cable. Some displays support several options. Consult your Pen display's documentation or customer support to determine the correct option.

## <mark style="color:$danger;">WATCH THESE VIDEOS!!!</mark>

Now that you know the fundamentals, watch these videos. They will lead you through the process of how Pen displays actually connect to computers with different types of cables. You should not proceed with this guide unless you have watched these videos. In fact, from watching these videos, you might even be able to solve your problem directly.

{% embed url="https://youtu.be/iKl_3NYjlsY" %}

{% embed url="https://youtu.be/eyHkd3kcOZk" %}

## What you can tell from the NO SIGNAL message

The "no signal" message indicates a problem with the video signal. Because you can see the message, it also rules out several other problems.

* **The pen display is getting enough power.** If the tablet were not getting enough power, you would not see a NO SIGNAL message.
* **The backlight inside the display panel is working.** If the tablet's backlight were not working, this message would not be visible, or it would be incredibly difficult to read.
* **There is nothing wrong with the display panel itself.** If the tablet is showing anything at all, the display panel is working. The display panel is capable of showing you pixels, and that means it's working. Yes, there may be problems internally with the tablet, but they're not directly related to the display panel.

## The pen still works

People are often surprised when the pen still works with a "no signal" message. The Pen display can still function as a screenless tablet. It can send data to the computer but cannot receive a video signal.

## Reinstalling tablet drivers is not going to be helpful

Drawing tablet drivers have nothing to do with the video signal. So, while it's often recommended that you update or reinstall drivers when there are problems with a drawing tablet, it will not help you solve the "no signal" problem. Some people report that the problem went away after they installed the tablet driver, but that often seems to be indirectly related. After installing the driver, people tend to reboot their computer, and the reboot is what actually fixes the problem.

Don't waste your time reinstalling your tablet driver multiple times. You weren't doing anything that would help.

## A map of the problem space

To help guide your investigation, it's good to have a sense of the overall problem space so you know where you might have to direct your attention. This will also help you understand further topics introduced in this guide.

Here's a list of all the problem areas, roughly speaking, in order from the computer to your tablet.

* First is the GPU, or graphics card. It may have a problem sending a video signal. The issue may involve specific GPU ports or the GPU driver.
* Next are the GPU ports. They may be obstructed or contain dust.
* Next is the cable from the GPU port to the drawing tablet. Consider only the cable that carries the video signal.
* Next are the drawing tablet's port and internal components, including the display panel and backlight.
* Finally, consider the operating system and its configuration.

All of these components are potential places where the problem might exist. So, as you troubleshoot the "no signal" problem, you will essentially have to take a journey through these components to find the root cause.

## Restart your computer

One of the simplest things you can do to diagnose or resolve a "no signal" problem is to simply restart your computer. Sometimes this seems to force the computer to redetect displays, and suddenly your Pen display might start showing the video signal. It may not always work, but it's usually worth an attempt. If it doesn't work after one or two restarts, though, there's usually no point in repeating it over and over.

## Verify that the computer detects the tablet's display

Let's suppose you're using a computer that has a single display attached, which is your monitor. That means your computer has detected one display and is using that display. If you plug in a Pen display, the computer should also detect that Pen display as another display or monitor.

In your operating system's **Display Settings**, you should see two displays. And one of them should be your tablet's display.

| Windows 11                                                                     | macOS (Ventura)                             |
| ------------------------------------------------------------------------------ | ------------------------------------------- |
| <img src="../.gitbook/assets/tsg-no-signal-3.png" alt="" data-size="original"> | ![](../.gitbook/assets/tsg-no-signal-1.png) |

If your computer does not see the display from the tablet, it will not send a video signal to it. Follow these troubleshooting steps: [TSG: Computer does not detect the display](tsg-display-detection.md)

## Verify that the operating system is trying to use the display

Even if your computer detects the display of your drawing tablet, your operating system might not be configured to use that display. So the operating system will not even bother sending a video signal to it since it's been configured to ignore that display.

For example, in Windows, the display in your tablet might be configured to "show desktop only on Display \<X>". Change it to one of the other options that uses the tablet display.

## Verify that your computer can send an HDMI signal

If your Pen display uses HDMI, disconnect it and connect another monitor to the same HDMI port. Check whether the port sends a video signal.

## Verify that the pen display can receive an HDMI signal from another device

Try connecting your pen display to another HDMI source. This can be another PC, a laptop, an Xbox, a camera, or anything else that sends a signal through HDMI.

## Verify cable connections

Verify that your cables are fully connected.

* Sometimes cables can sit in a port without fully "locking" in.
* Check for dust, lint, or any other foreign objects in the port. They can prevent the connection from working.

## Depower your pen display

* Follow all these steps in order. Do not skip any.
  * Turn off the tablet using the **power button**
  * Disconnect all cables from the tablet. Do not disconnect only the power cable.
  * Wait 30 seconds to several minutes.
  * Reattach all the cables
  * Turn on the tablet.
* Variations to try
  * Some people recommend disconnecting power, then holding the tablet power button down for a long time, such as 30 seconds, before reconnecting.
  * Some people recommend leaving the tablet disconnected for an extended period, such as 30 minutes, before reconnecting.

## Explore HDMI connection options

### The HDMI cable goes to your computer

I've seen many newcomers to drawing tablets connect the HDMI cable from their Pen display to their monitor. This will absolutely never work because both the Pen display and the monitor are waiting to receive a video signal.

The HDMI cable from your tablet goes to your computer. Do not connect the HDMI cable to your monitor. Monitors do not send HDMI signals; they only receive them. Connecting your pen display to your monitor will not work.

### Use a different HDMI port on your computer

Your computer may have multiple HDMI ports. Try different ones.

### GPU HDMI vs motherboard HDMI

In general, connect via the GPU HDMI ports instead of motherboard HDMI ports.

More here: [Motherboard HDMI vs GPU HDMI ports](../guides/connecting/connecting-pen-display/motherboard-vs-gpu-hdmi.md).

### Try not using an HDMI adapter

If your PC has a DisplayPort or DVI output, or a USB-C port that supports DisplayPort Alt Mode, try an adapter. More here: [Using HDMI adapters with pen displays](../guides/pen-displays/hdmi-adapters/).

### Avoid HDMI splitters

HDMI splitters can also be a bit "flaky" and can cause a NO SIGNAL problem. More here: [Using HDMI splitters with pen displays](../guides/pen-displays/hdmi-splitters.md)

* Try connecting without an HDMI splitter.

### Swap HDMI ports

If you've already got an external monitor plugged into your computer and it's working, but you're getting the "No Signal" message with your Pen display, one technique you can use is to switch how they're connected. For example, if your monitor is using the HDMI port and it's working, then switch to using the Pen display with that HDMI port. Sometimes, just by switching the order of which ports you use, you can find that the problem goes away.

## USB-C connection options

**If** your computer has a USB-C port that supports a display signal, there are a couple of options for you. More here: [USB-C DisplayPort Alt Mode](../guides/pen-displays/usbc-dp-alt-mode.md)

### General thoughts about USB-C

If you've already got an external monitor plugged into your computer and it's working, but you're getting the "No Signal" message with your Pen display, one technique you can use is to switch how they're connected. For example, if your monitor is using the HDMI port and it's working, then switch to using the Pen display with that HDMI port. Sometimes, just by switching the order of which ports you use, you can find that the problem goes away.

### USB-C to USB-C

If your tablet has a USB-C port and your computer has a USB-C port that supports DisplayPort Alt Mode, power, and data, then you might be able to use a USB-C to USB-C cable.

### USB-C cable orientation

For the vast majority of USB-C cables that plug into a USB-C port, you can take the cable out, flip it around, and plug it in upside down, and it will still work. This is an intentional feature of the USB spec, and the vast majority of cables and ports work this way. However, occasionally, you might run into a cable or port that seems hypersensitive to the orientation of the cable. So it's at least worth flipping the cable upside down to see if it works that way.

#### Wacom One 2019 (DTC-133) cable orientation

The Wacom One 2019 (DTC-133) is very sensitive to the orientation of the 3-in-1 cable in its USB-C port. The orientation that works is the one where the cable sticks out to the left side of the Wacom One. As far as I know, this is the only Pen display that exists that has a deliberate preference for the orientation of the USB-C cable.

## Manufacturer versus third-party cables

In theory, any USB-C cable that carries a video signal will work. However, start by testing the USB-C cable provided by the manufacturer.

## Other connection options

### HDMI adapters

If your PC has a DisplayPort or DVI output, or a USB-C port that supports DisplayPort Alt Mode, try an adapter. More here: [Using HDMI adapters with pen displays](../guides/pen-displays/hdmi-adapters/).

## Test with your pen display as your only display

* If your computer has other displays connected, disconnect them and then **only** connect your pen display. Sometimes computers get tripped up when multiple displays are in use, so this can help force the system to use the pen display.
* If that works, start reconnecting the other displays until they are all plugged back in and working.

## Maximum number of display outputs on your graphics card

GPUs usually have multiple ports for sending a display signal. However, sometimes not all of them can be used at the same time.

Suppose your graphics card has four physical HDMI outputs. It is possible that the card supports only three of them at the same time. If you plug into the fourth port, you may get a no signal issue.

Read the documentation for your graphics card to verify how many active outputs it supports.

## Check display settings

### Test mirror vs extend for your desktop

* Typically your PC will already have one monitor attached to it. So the pen display will be the second screen.
* You have two options in your operating system:
  * Mirror the contents of your desktop across both screens. This means they will show the same thing.
  * Extend the contents of your desktop across both screens. This means that the screens will show different things.
* If you are getting no signal in extended mode, try mirrored mode, and vice versa.

### Test video refresh rates

If your computer recognizes that a display is attached, but you are still getting no signal, try changing the refresh rate the computer is using for that display.

Sometimes a misconfigured refresh rate causes the computer to stop sending a signal. For example, a Windows update can reset the refresh rate to an unsupported value. Changing it back to 60 Hz can make the display work again.

So always verify the refresh rate.

Start with a lower refresh rate, then work up to higher ones.

Typically, pen displays go only up to 60 Hz.

### Test video resolution

If your computer recognizes that a display is attached, but you are still getting no signal, try changing the resolution the computer is using for that display.

Start with a very low resolution, then work up to higher resolutions.

## Get the tablet to work with another computer, then reattach it to your computer

Some users report that if they get NO SIGNAL with their pen display, they can connect it to another computer where it does work. Then, after it works there, they reconnect it to the first computer and it starts working there too.

See this Reddit comment: [**r/huion - No signal - imac**](https://www.reddit.com/r/huion/comments/109wjgx/comment/j41ekyk/?utm_source=share\&utm_medium=web2x\&context=3) (2023-01-12).

The reason this process might work is not clear. It could be because fully depowering the pen display helps. It could also be because the connection to the other computer changes something inside the pen display. In any case, it is worth a try if you continue to have problems.

## Tablet firmware updates

It sometimes happens that monitors require firmware updates before they can receive a display signal correctly. For example: [This ASUS monitor required a firmware update](https://www.asus.com/lk/support/FAQ/1045839/) to get video to work over USB-C.

IMPORTANT: Do not install firmware updates on the general hope that they will improve things. Please consult your manufacturer or support team to verify whether they recommend a firmware update to solve the problem.

## Possible triggers

One of the most surprising things about the NO SIGNAL problem is that it can occur on an existing working system. It's happened to me.

Here is what can trigger it:

* A GPU driver update
* An operating system update

## Other resources

### Reddit threads

* [**r/XPpen - Tips when there is "No Signal" and/or tablet is recognized as a keyboard and not as a display monitor for PC + additional stuff**](https://www.reddit.com/r/XPpen/comments/z2h51j/tips_when_there_is_no_signal_andor_tablet_is/) 2022-11-22

### Misc

* [https://www.windowscentral.com/how-fix-your-second-monitor-not-being-detected-windows-10](https://www.windowscentral.com/how-fix-your-second-monitor-not-being-detected-windows-10)
* [https://support.microsoft.com/en-us/windows/troubleshoot-external-monitor-connections-in-windows-10-5b46f4a4-9634-06bb-7622-f960facdfd49](https://support.microsoft.com/en-us/windows/troubleshoot-external-monitor-connections-in-windows-10-5b46f4a4-9634-06bb-7622-f960facdfd49)
* [TheHowToGuy123 - How To Enable Motherboard HDMI Port for Multiple Monitors - Use Graphics Card & Integrated Graphics](https://youtu.be/_Ftk8jQhsqE) Jul 3, 2020

### Manufacturer guidance

#### Huion

* General: [https://support.huion.com/en/support/solutions/articles/44001154156-what-to-do-if-your-huion-pen-display-shows-a-black-screen-or-no-signal](https://support.huion.com/en/support/solutions/articles/44001154156-what-to-do-if-your-huion-pen-display-shows-a-black-screen-or-no-signal)
* Huion support for Kamvas 13: [https://support.huion.com/en/support/solutions/articles/44001949665-how-to-fix-my-kamvas-13-no-signal-black-screen-problem-](https://support.huion.com/en/support/solutions/articles/44001949665-how-to-fix-my-kamvas-13-no-signal-black-screen-problem-)
