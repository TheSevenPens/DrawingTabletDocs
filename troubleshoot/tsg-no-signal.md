# TSG: Pen display shows NO SIGNAL message

## Overview

The "No Signal" message is common when using a pen display. It can be challenging to diagnose and fix, but it is often resolvable. This practical, step-by-step guide contains techniques that can help identify and fix the problem.

## Be prepared to contact customer support

Even this guide may not be enough. <mark style="color:red;">**Be prepared to contact your tablet manufacturer's customer support team.**</mark>

## The NO SIGNAL message

The "No Signal" message takes several forms on a pen display. Most often, you see it when you turn on the pen display. A box appears with the words "no signal." This message might also indicate which port is not receiving a signal. In the example below, it is the USB-C port.

One confusing aspect of the "no signal" message is that it does not specify the signal type. The message refers to a video signal.

<figure><img src="../.gitbook/assets/tsg-no-signal-2.jpg" alt="" width="375"><figcaption><p>A typical no signal message. In this case, the message indicates that the USB-C port is where the pen display is looking for the signal.</p></figcaption></figure>

## Flashing colors as a NO SIGNAL message

Most of the time, when a pen display does not receive a video signal, it shows a "no signal" message. However, some pen displays flash colors instead. The screen cycles continuously through red, green, and blue. There may be no other message. These flashing colors indicate that the pen display is not receiving a video signal.

## The POWER SAVING message

Sometimes you will see a single message. Other times, you will also see "power saving" in the same box or in a separate message. The pen display usually shuts down a few seconds later.

The power-saving message can be confusing. It has nothing to do with power reaching the tablet. It indicates that the pen display is not receiving a video signal. The display shuts down to avoid wasting power.

If you see the power-saving message, do not investigate the display's power supply. The display is receiving enough power. Do not spend time solving power problems that do not exist.

## A note about getting enough power

A NO SIGNAL message requires that the pen display receives some power. However, your pen display might not receive enough power. In that case, the pen display may keep turning on and off, or the screen may be too dim. Insufficient power does not cause a NO SIGNAL problem.

## The fundamentals of connecting a pen display

To troubleshoot a no-signal problem, understand how to connect a pen display correctly. This knowledge helps you identify, test, and solve connection problems.

There are three fundamental requirements for a pen display to work correctly when connected to your computer.

* First, the pen display must receive enough power.
* Second, the pen display must be able to send data to the computer. This data includes the pen's position, pressure, and tilt. If it cannot send this data, the pen will not work.
* Third, the pen display must receive a video signal from the computer. If it does not receive a video signal, you will see the "no signal" message.

To stress this point: if you see a "no signal" message, it relates only to the video signal. It does not relate to data or power.

Next, understand how cabling works. Some pen displays require three separate cables. Others require two cables or a three-in-one cable. Some displays support several options. Consult your pen display's documentation or customer support to determine the correct option.

## <mark style="color:$danger;">WATCH THESE VIDEOS!!!</mark>

Now that you know the fundamentals, watch these videos. They show how pen displays connect to computers with different cable types. Watch them before continuing with this guide. They may solve your problem directly.

{% embed url="https://youtu.be/iKl_3NYjlsY" %}

{% embed url="https://youtu.be/eyHkd3kcOZk" %}

## What you can tell from the NO SIGNAL message

The "no signal" message indicates a problem with the video signal. Because you can see the message, it also rules out several other problems.

* **The pen display is receiving enough power.** If the tablet were not receiving enough power, you would not see a NO SIGNAL message.
* **The backlight inside the display panel is working.** If the tablet's backlight were not working, this message would not be visible, or it would be incredibly difficult to read.
* **The display panel itself is working.** If the tablet is showing anything, the display panel can render pixels. Other components inside the tablet may still have problems, including the USB ports, HDMI circuitry, or internal cabling. These components can cause the NO SIGNAL problem.

## The pen still works

People are often surprised when the pen still works with a "no signal" message. The pen display can still function as a screenless tablet. It can send data to the computer but cannot receive a video signal.

## A map of the problem space

To guide your investigation, understand the overall problem space and where to direct your attention. This will also help you understand the topics introduced later in this guide.

Here is a list of problem areas, roughly in order from the computer to your tablet.

* First is the GPU, or graphics card. It may have a problem sending a video signal. The issue may involve specific GPU ports or the GPU driver.
* Next are the GPU ports. They may be obstructed or contain dust.
* Next is the cable from the GPU port to the drawing tablet. Consider only the cable that carries the video signal.
* Next are the drawing tablet's ports and internal components, including the display panel and backlight.
* Finally, consider the operating system and its configuration.

The problem might exist in any of these components. Troubleshoot each component to find the root cause.

## Restart your computer

One of the simplest ways to diagnose or resolve a "no signal" problem is to restart your computer. This can force the computer to redetect displays, and your pen display might start showing a video signal. It may not always work, but it is worth trying. If it does not work after one or two restarts, do not repeat it.

## Verify that the operating system detects the tablet's display

If you plug in a pen display, the computer should detect it as another monitor. In your operating system's **Display Settings**, you should see two displays. One should be your tablet's display.

| Windows 11                                                                     | macOS (Ventura)                             |
| ------------------------------------------------------------------------------ | ------------------------------------------- |
| <img src="../.gitbook/assets/tsg-no-signal-3.png" alt="" data-size="original"> | ![](../.gitbook/assets/tsg-no-signal-1.png) |

If your computer does not see the display from the tablet, it will not send a video signal to it. Follow these troubleshooting steps: [TSG: Computer does not detect the display](tsg-display-detection.md)

## Verify cable connections

* The user manual for your tablet includes connection diagrams that show which cable goes where. Make sure your connections are set up as shown in the manual.
* Key things to check:
  * Based on the connection diagram, are all the required cables used?
  * Are the cables seated properly in ports? Some might not be in all the way.
  * Check for dust, lint, or any other foreign objects in the port. They can prevent the connection from working.

## Verify that the operating system is trying to use the display

Even if your computer detects the display on your drawing tablet, your operating system might not be configured to use it. The operating system will not send a video signal to a display it is configured to ignore.

For example, in Windows, the display in your tablet might be configured to "show desktop only on Display \<X>". Change it to one of the other options that uses the tablet display.

## Verify that your computer can send an HDMI signal

If your pen display uses HDMI, disconnect it and connect another monitor to the same HDMI port. Check whether the port sends a video signal.

## Verify that the pen display can receive an HDMI signal from another device

Try connecting your pen display to another HDMI source. This can be another PC, a laptop, an Xbox, a camera, or anything else that sends a signal through HDMI.

## Depower your pen display

* Follow these steps in order. Do not skip any.
  * Turn off the tablet using the **power button**
  * Disconnect all cables from the tablet. Do not disconnect only the power cable.
  * Wait 30 seconds to several minutes.
  * Reattach all cables.
  * Turn on the tablet.
* Variations to try
  * Some people recommend disconnecting power, then holding the tablet power button down for a long time, such as 30 seconds, before reconnecting.
  * Some people recommend leaving the tablet disconnected for an extended period, such as 30 minutes, before reconnecting.

## Explore HDMI connection options

### The HDMI cable goes to your computer

Many people new to drawing tablets connect the HDMI cable from their pen display to their monitor. This never works because both the pen display and monitor wait to receive a video signal.

The HDMI cable from your tablet connects to your computer. Do not connect it to your monitor. Monitors do not send HDMI signals; they only receive them. Connecting your pen display to your monitor will not work.

### Use a different HDMI port on your computer

Your computer may have multiple HDMI ports. Try different ones.

### GPU HDMI vs motherboard HDMI

In general, use GPU HDMI ports instead of motherboard HDMI ports.

More here: [Motherboard HDMI vs GPU HDMI ports](../guides/connecting/connecting-pen-display/motherboard-vs-gpu-hdmi.md).

### Try not using an HDMI adapter

If your PC has a DisplayPort or DVI output, or a USB-C port that supports DisplayPort Alt Mode, you may need an adapter. More here: [Using HDMI adapters with pen displays](../guides/pen-displays/hdmi-adapters/).

### Avoid HDMI splitters

HDMI splitters can also be a bit "flaky" and can cause a NO SIGNAL problem. More here: [Using HDMI splitters with pen displays](../guides/pen-displays/hdmi-splitters.md)

* Try connecting without an HDMI splitter.

### Swap HDMI ports

If you already have a working external monitor, try swapping its connection with your pen display. For example, if the monitor works through an HDMI port, connect the pen display to that port. Changing which ports you use can resolve the problem.

## USB-C connection options

### General thoughts about USB-C

If you already have a working external monitor, try swapping its connection with your pen display. For example, if the monitor works through an HDMI port, connect the pen display to that port. Changing which ports you use can resolve the problem.

### Verify you are using a USB-C cable that can carry a video signal

USB-C describes a connector shape. Most of the time, you cannot tell by looking at a USB-C cable whether it can carry a video signal. More here: [USB-C DisplayPort Alt Mode](../guides/pen-displays/usbc-dp-alt-mode.md).

Do not use arbitrary USB-C cables. For example, charging cables carry only power. Other USB-C cables carry only data. A data-only USB-C cable lets your pen work, but does not resolve the NO SIGNAL problem. Use a cable that carries a video signal.

USB-C cables are not always marked, but look for these signs:

* Is it a USB-C Thunderbolt cable? It should have a Thunderbolt logo.
* USB-C cables described as "full-featured" carry a video signal.
* The cable documentation may explicitly say that it carries a video signal or supports DisplayPort Alt Mode, often abbreviated as DP Alt Mode.

### Verify you are using the correct USB-C cable that came with the tablet

**Note:** Some pen displays come with multiple USB-C cables. Usually, one carries the video signal, and the other supplies power. These cables may look exactly alike or be difficult to tell apart.

### Try a different USB-C cable orientation

Most USB-C cables work in either orientation. This is an intentional feature of the USB specification. However, some cables or ports appear sensitive to cable orientation. Flip the cable and test the other orientation.

The **Wacom One 2019 (DTC-133) is very sensitive to the orientation** of the 3-in-1 cable in its USB-C port. The working orientation has the cable extend from the left side of the Wacom One. As far as I know, this is the only pen display with a deliberate preference for USB-C cable orientation.

### Try other USB-C ports on your computer

USB-C ports on your computer may or may not support a video signal.

You might see indicators next to a port that it can carry a display signal. These include a Thunderbolt symbol or labels such as "VIDEO," "DP ALT MODE," "DP," or "USB4."

If your computer has multiple USB-C ports, not all may support a video signal. It could be all, some, or none of them. Read your computer's documentation to be sure. Many USB-C ports support only power and data.

### USB-C ports on computer's motherboard

If you have a desktop PC and use a USB-C port on the motherboard I/O panel, the port may support video. To enable it, you may need to:

* Connect a DisplayPort cable from your GPU to a DP IN port on the motherboard I/O panel.
* Restart the computer.

### USB-C ports on a GPU

These are rare. If you have a GPU with a USB-C port, it can almost always send a video signal. However, it usually sends only a video signal. USB-C ports on a GPU typically do not support data or power.

### Manufacturer versus third-party cables

In theory, any USB-C cable that carries a video signal will work. However, start by testing the USB-C cable provided by the manufacturer.

## Other connection options

### HDMI adapters

If your PC has a DisplayPort or DVI output, or a USB-C port that supports DisplayPort Alt Mode, you may need an adapter. More here: [Using HDMI adapters with pen displays](../guides/pen-displays/hdmi-adapters/).

### Test with your pen display as your only display

* If your computer has other displays connected, disconnect them. Then connect **only** your pen display. Sometimes computers have problems when multiple displays are in use, so this can force the system to use the pen display.
* If that works, start reconnecting the other displays until they are all plugged back in and working.

### Maximum number of display outputs on your graphics card

GPUs usually have multiple ports for sending a display signal. However, sometimes not all of them can be used at the same time.

Suppose your graphics card has four physical HDMI outputs. The card may support only three at the same time. If you use the fourth port, you may encounter a no-signal issue.

Read the documentation for your graphics card to verify how many active outputs it supports.

### Test mirror vs extend for your desktop

* Your PC will typically already have one monitor attached. The pen display will be the second screen.
* You have two options in your operating system:
  * Mirror the contents of your desktop across both screens. This means they will show the same thing.
  * Extend the contents of your desktop across both screens. This means that the screens will show different things.
* If you get no signal in extended mode, try mirrored mode, and vice versa.

### Test video refresh rates

If your computer recognizes an attached display but you still get no signal, try changing the refresh rate for that display.

Sometimes a misconfigured refresh rate causes the computer to stop sending a signal. For example, a Windows update can reset the refresh rate to an unsupported value. Changing it back to 60 Hz can make the display work again.

Always verify the refresh rate.

Start with a lower refresh rate, then work up to higher ones.

Typically, pen displays go only up to 60 Hz.

### Test video resolution

If your computer recognizes an attached display but you still get no signal, try changing the resolution for that display.

Start with a very low resolution, then work up to higher resolutions.

### Get the tablet to work with another computer, then reattach it to your computer

Some users report that, after seeing NO SIGNAL on their pen display, they connect it to another computer where it works. They then reconnect it to the first computer, where it also starts working.

See this Reddit comment: [**r/huion - No signal - imac**](https://www.reddit.com/r/huion/comments/109wjgx/comment/j41ekyk/?utm_source=share\&utm_medium=web2x\&context=3) (2023-01-12).

The reason this process might work is unclear. Fully depowering the pen display may help. The connection to another computer may also change something inside the pen display. Try this if the problem continues.

## Drivers and firmware

### Tablet firmware updates

Some monitors require firmware updates before they can correctly receive a display signal. For example, [this ASUS monitor required a firmware update](https://www.asus.com/lk/support/FAQ/1045839/) to receive video over USB-C.

**Important:** Do not install firmware updates in the general hope that they will improve things. Consult your manufacturer or support team to verify whether they recommend a firmware update.

### Reinstalling drawing tablet drivers is not going to be helpful

Drawing tablet drivers do not affect the video signal. Updating or reinstalling them will not solve a "no signal" problem. Some people report that the problem disappeared after they installed a tablet driver, but this is often indirect. Installing the driver usually requires a reboot, which may fix the problem.

Do not reinstall your tablet driver repeatedly. It will not help.

### Reinstalling or updating GPU drivers might help

Sometimes your computer randomly fails to detect a display or stops sending it a video signal. This can result from a GPU driver issue, so reinstalling or updating the driver might help. Some sources also recommend testing an older GPU driver version.

## Possible triggers

One surprising aspect of the NO SIGNAL problem is that it can occur on a previously working system.

These events can trigger it:

* A GPU driver update
* An operating system update
* Your computer was sleeping or hibernating

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
