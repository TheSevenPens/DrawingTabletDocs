# Troubleshoot the NO SIGNAL problem

## Overview

The "NO SIGNAL" message is a VERY COMMON experience for people who have a pen display. Most often this can be fixed. But it can be challenging to diagnose the cause because there are so many factors involved.

<figure><img src="../.gitbook/assets/PXL_20221202_033015550.MP smaller.jpg" alt="" width="375"><figcaption><p>A typical no signal message. In this case the message indicates that the USB-C port is where the pen display is looking for the signal.</p></figcaption></figure>

What it means:  The "NO SIGNAL" message tells you that the pen display is not receiving a display signal from the computer. Commonly when people encounter the NO SIGNAL problem, they will notice that their pen continues to work on the tablet, even though they can't see anything.

## About this guide

This guide lists every piece of information and tactic I am aware of that might help.&#x20;

However, it may be that even this guide is not enough to help. And ultimately you should be prepared to contact your tablet manufacturer's customer support team.

## What you can tell from the message

The fact that you are seeing a NO SIGNAL message already tells you a few things:

* **The pen display is getting enough power.** If it wasn't getting enough power, you wouldn't see this message.
* **The backlight inside the display panel is working.** If the backlight wasn't working, this message would not be visible or incredibly difficult to read.&#x20;
* **There is nothing wrong with the display panel itself.** The fact that it is showing you anything at all tells you the display panel is working.

### Why the message might say "POWER SAVING"

For some tablets, the NO SIGNAL message is accompanied bya POWER SAVING message.&#x20;

POWER SAVING is **NOT** indicating a problem with POWER.

POWER SAVING means "The pen display is not receiving a display signal from the computer. So rather than wasting energy by keeping the display powered up but not showing anything, the pen display is going to shut down."&#x20;

So, ultimately this message is telling you the tablet is trying to save you money not that there is a power problem.&#x20;

## How your computer interprets a pen display

Troubleshooting the the NO SIGNAL problem starts with understanding how your computer interprets an attached pen display. Pen displays are a single physical device that you connect to a computer. However, your computer thinks of the pen display as two separate devices:&#x20;

* a pen tablet (aka screenless tablet)&#x20;
* and a monitor/display

<figure><img src="../.gitbook/assets/image (453).png" alt=""><figcaption></figcaption></figure>

Your computer and operating system have no idea that these two devices are related in any way. Even if a single cable is used to connect your pen display to your computer, it will continue to believe two devices are part of the same pen display. On the other hand, your tablet driver will know that these two devices are related.

The reason it is important to understand this is that the NO SIGNAL issue is a display issue, not a pen tablet issue. &#x20;

Another consequence of this "two devices" behvaior, is that even though you may be experiencing a "no signal" error, you can still use your tablet as a pen tablet (a screenless tablet). In fact this is often feature of drawing tablets, some people occasionally want to use them as pen tablets without the screen.&#x20;

## Tablet drivers

So, In general, messing around the tablet drivers WILL NOT HELP. So, don't bother reinstalling, upgrading, changing tablet drivers. While I do recommend having the latest drivers generally, it is very unlikely to help the NO SIGNAL problem.

## Things to verify

### Verify that the computer see the attached display

Presumably, your computer already has one screen, so when you plug in your tablet it should at least recognize that there are two screens (one coming from the pen display).

In your operating system's **Display Settings**, you should see two displays. And one of them should be your tablet's display

| Windows 11                                                                 | MacOS (Ventura)                           |
| -------------------------------------------------------------------------- | ----------------------------------------- |
| <img src="../.gitbook/assets/image (455).png" alt="" data-size="original"> | ![](<../.gitbook/assets/image (334).png>) |

If your computer doesn't think there is a display attached, it certainly isn't going to send a signal to it. So if you don't see this detection, follow these troubleshooting steps: [**Troubleshoot display detection**](troubleshoot-display-detection.md)&#x20;

## Verify that you operating system is trying to use the display.

Sometimes you operating system knows the display is there, but it is deliberately not sending a display signal to it.

For example, in Windows for the display in your tablet, Windows might be configured to "show desktop only on Display \<X>" - change it to one of the other options that will use the tablet display.&#x20;

### Verify that the pen display can receive an HDMI signal

Try connecting your pen display to another source of HDMI input. This can be anything: another PC, a laptop, a XBOX, a camera, anything that sends a signal via an HDMI port.

### Verify that your computer can send an HDMI signal&#x20;

Try connecting a monitor the the same HDMI port you want to use with your pen display.&#x20;

### Verify cable connections

Verify that your cables are fully connected.&#x20;

* Sometimes cables can sit in a port without fully "locking" in.
* Check for lint or any other foreign objects in the port. They can prevent the connection from working

## Physically disconnect your pen display from power

* Turn off your pen display and **DISCONNECT ALL THE CABLES**, then plug it back in.&#x20;
* **DO NOT** just press the ON/OFF button while the pen display is connected. Actually DISCONNECT ALL THE CABLES
* Some variations to try
  * Some people recommend to disconnect, then hold the tablet power button down for long time (30 seconds), and then reconnect. &#x20;
  * Some people recommend that you try leaving the tablet disconnected for an extended period of time - like 30 minutes before you reconnect.&#x20;

## HDMI connect options

### Use a different HDMI ports

Your computer may have multiple HDMI ports, try different ones.

### Graphics card HDMI vs motherboard HDMI

* If the computer PC has graphics card, it have HDMI ports
* Always first try the HDMI port on your graphics card first - it's better to use them than HDMI ports on your motherboard
* Some people suggest that motherboard ports NEVER work. This is NOT true. It is highly dependent on the specific machine. I can confirm I have several computers where the motherboard does work.

<div align="left">

<figure><img src="../.gitbook/assets/7P SLIDE Motherboard vs GPU ports.jpg" alt="" width="375"><figcaption><p>Motherboard ports on the left. GPU ports on the right.</p></figcaption></figure>

</div>

## USB-C connection options

**IF** your computer has a USB-C port that supports a display signal there are a couple of options for you.

More here: [USB-C support for display signal](../guides/pen-displays/usb-c-displayport-alt-mode.md)&#x20;

### USB-C to USB-C

If your tablet has a USB-C port and your computer has a USB-C port that supports a display signal, then you might be able to use a USB-C to USB-C cable.

### USB-C to HDMI

You can try a USB-C to HDMI adapter. More here: [Using HDMI adapters with pen displays](../guides/pen-displays/using-hdmi-adapters-with-pen-displays.md).

## Converting other ports to HDMI

if your PC has a DisplayPort or DVI output, try an adapter. More here: [Using HDMI adapters with pen displays](../guides/pen-displays/using-hdmi-adapters-with-pen-displays.md). &#x20;

### Issues with HDMI Adapter

Sometimes adapters themselves can be the source of the NO SIGNAL problem.&#x20;

* Try a different HDMI adapter .&#x20;
* Try NOT using an HDMI adapter.

## HDMI Splitters

HDMI Splitters are are also sometimes a bit "flaky" and can cause a NO SIGNAL problem. more here: [**Using HDMI splitters with pen displays**](../guides/pen-displays/using-hdmi-splitters-with-pen-displays.md)

* Try connecting WIHOUT an HDMI splitter

## Try using your pen display as your only display

* If you have a computer, disconnect all other displays and then **only** connect your pen display. Sometimes computers get tripped up when multiple displays are being used, so by trying this procedure you help force it to use the pen display.&#x20;
* If that works, start reconnecting the other displays until they are all plugged back in and working.

## Check if there is any difference when using mirror vs extend for your desktop

* Typically you PC will already have one monitor attached to it. So the pen display will be the second screen.
* You have two options in your operating system:
  * Mirror the contents of your desktop across both screens. This means they will show the same thing.
  * Extend the contents of your desktop across both screens. This means that the screens will show different things.
* If you are getting no signal in extended mode, then try mirrored mode. And vice versa.

## Maximum number of display outputs on your graphics card

Graphics cards usually have multiple ports for sending a display signal. However, sometimes not all of them can be used at the same time.

Suppose your graphics card has 4 physical HDMI outputs. It's possible your card only supports using 3 of them at the same time. And so if you plug in the to the 4th port, you may get a no signal issue.

Read the documentation for your graphics card to verify how many it supports.&#x20;

## Display signal properties

### Display refresh rates

If your computer recognizes that a display is attached but you are still getting no signal, try changing the Refresh Rate the computer is using for the display.

Sometimes a misconfigured refresh rate causes the computer to not send a signal. For example, I have seen this happen with a  Windows Update, my pen display worked, but then after the update I saw the NO SIGNAL error. Somehow the refresh rate had been set to some unsupported value, once I changed it back to 60Hz it all worked again.

So always verify the refresh rate.

Start with a lower refresh rate, and build up to higher ones.

Typically pen displays only go up to 60Hz.&#x20;

### Display resolution

If your computer recognizes that a display is attached but you are still getting no signal, try changing the Resolution the computer is using for the display.

First try a very low resolution first and then build up to higher resolutions.

## Get the tablet to work with another computer then reattach to your computer

Some users report that if they are getting NO SIGNAL with their pen display, they have been able to connect the pen display to another computer where it does work. And then once it worked, they reattached it back to the first computer where it then began working.

See this reddit comment: [https://www.reddit.com/r/huion/comments/109wjgx/comment/j41ekyk/?utm\_source=share\&utm\_medium=web2x\&context=3](https://www.reddit.com/r/huion/comments/109wjgx/comment/j41ekyk/?utm\_source=share\&utm\_medium=web2x\&context=3)

The reason this process might work is not clear. It could be because depowering the pen display was the reason. It could be because the connection to the other computer altered something in the pen display. In any case, it is worth a try if you continue to have problems.

## Wacom One GEN1 cable orientation

The Wacom One 2019 gen-1 is very sensitive to the orientation of the how the 3-in-1 cable is plugged into its USB-C port. Usually the orientation that works, is when the cable sticks out to left side of the Wacom one.

## Tablet firmware updates

It sometimes happens that monitors require firmware updates to make getting a display signal work. For example: [This ASUS monitor required a firmware update](https://www.asus.com/lk/support/FAQ/1045839/) to get video to work over USB C.   &#x20;

IMPORTANT: Don't install firmware updates on the general hope they will improve things. Please consult your manufacturer and support team to verify whether they recommend a firmware update to solve the problem.

## Possible triggers&#x20;

This is one of the most surprising things about the NO SIGNAL problem is that it can occur to an existing working system. It's happened to me.

Here's what can trigger it

* A GPU driver update
* An Operating System update

## Other resources

### Reddit threads

* [https://www.reddit.com/r/XPpen/comments/z2h51j/tips\_when\_there\_is\_no\_signal\_andor\_tablet\_is/ ](https://www.reddit.com/r/XPpen/comments/z2h51j/tips\_when\_there\_is\_no\_signal\_andor\_tablet\_is/)

### Misc

* [https://www.windowscentral.com/how-fix-your-second-monitor-not-being-detected-windows-10](https://www.windowscentral.com/how-fix-your-second-monitor-not-being-detected-windows-10)
* [https://support.microsoft.com/en-us/windows/troubleshoot-external-monitor-connections-in-windows-10-5b46f4a4-9634-06bb-7622-f960facdfd49](https://support.microsoft.com/en-us/windows/troubleshoot-external-monitor-connections-in-windows-10-5b46f4a4-9634-06bb-7622-f960facdfd49)&#x20;
* [TheHowToGuy123 - How To Enable Motherboard HDMI Port for Multiple Monitors - Use Graphics Card & Integrated Graphics](https://youtu.be/\_Ftk8jQhsqE) Jul 3, 2020

### Manufacturer guidance

#### Huion&#x20;

* General: [https://support.huion.com/en/support/solutions/articles/44001154156-what-to-do-if-your-huion-pen-display-shows-a-black-screen-or-no-signal](https://support.huion.com/en/support/solutions/articles/44001154156-what-to-do-if-your-huion-pen-display-shows-a-black-screen-or-no-signal)
* Huion support for Kamvas 13: [https://support.huion.com/en/support/solutions/articles/44001949665-how-to-fix-my-kamvas-13-no-signal-black-screen-problem-](https://support.huion.com/en/support/solutions/articles/44001949665-how-to-fix-my-kamvas-13-no-signal-black-screen-problem-)







