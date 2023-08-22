# Troubleshoot the NO SIGNAL problem

## Overview

The NO SIGNAL message is what your pen display tells you when it isn't receiving a display or video signal from another device. This error is one of the most challenging to diagnose and fix because so many factors can go into it.

The error often simply presents as literally a message that says "NO SIGNAL".

On some displays the message is "NO SIGNAL. POWER SAVING".&#x20;

In this guide, I'll provide every tactic I know about to help. But I also, want you to be prepared that it may be unresolvable and you may need to contact your tablet manufacturer.

## What you computer thinks of pen displays

Troubleshooting the the "no signal" problem starts with understanding how your computer interprets an attached pen display.

Pen displays are a single physical device that you connect to a computer.

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

However, your computer thinks of the pen display as two separate devices:

* a pen tablet (aka screenless tablet)
* a monitor/display

<figure><img src="../.gitbook/assets/image (270).png" alt=""><figcaption></figcaption></figure>

In fact, your computer and operating system has no idea that these devices are related in any way.

Even if a single cable is used to connect your pen display to your computer, it will continue to believe two devices are part of the same pen display.

On the other hand, your tablet driver will of course know that these two devices are related.

## Tablet drivers

**Tablet drivers usually DO NOT have control over the display signal being sent to the tablet**.&#x20;

So, don't bother reinstalling, upgrading, changing tablet drivers. While I do recommend having the latest drivers generally, it is very unlikely to help the NO SIGNAL problem.

## Does the computer think you attached a display?

It is important to understand if the computer itself thinks there is an additional monitor plugged into the computer.

Presumably, your computer already has one screen, so when you plug in your tablet it should at least recognize that there are two screens (one coming from the pen display).

In Windows, the **Display Settings** app should show two displays:

![](<../.gitbook/assets/image (276).png>)&#x20;

In macOS (Ventura) two displays looks like this:

![](<../.gitbook/assets/image (235).png>)

If your computer doesn't think there is a display attached, it certainly isn't going to send a signal to it.

## Things to verify

### Verify that the pen display can receive an HDMI signal

Try connecting your pen display to another source of HDMI input. This can be anything: another PC, a laptop, a XBOX, a camera, anything that sends a signal via an HDMI port.

### Verify that your computer can send an HDMI signal&#x20;

Try connecting a monitor the the same HDMI port you want to use with your pen display.

### Verify cable connections

Verify that your cables are fully connected. Sometimes they can sit in a port without fully "locking" in.

### Verify power

Lack of enough power for the pen display can also cause the NO SIGNAL problem.

If you are getting power from your computer or a hub, instead try to get power to the pen display directly from the wall.

## Physically disconnect your pen display from power

* Turn off your pen display and DISCONNECT ALL THE CABLES, then plug it back in.&#x20;
  * Some sourced recommend that while disconnected to hold the power button down for long time (30 seconds) before you reconnect.&#x20;
  * Other sources also recommend that you try leaving it disconnected for an extended period of time - like 30 minutes before you reconnect.&#x20;
* **Do not** rely on just pressing the ON/OFF button while the pen display is connected.

## Try different HDMI ports

Your computer may have multiple HDMI ports, try different ones.

## Try graphics card HDMI ports before motherboard HDMI ports

* If you have a PC with a graphics card, you may have HDMI ports on the graphics card and on your motherboard.
* Always try the HDMI port on your graphics card first.

## Try DisplayPort ports

* if you PC has a DisplayPort output, try an HDMI to DisplayPort adapter.

## Display adapter capabilities

* Make sure the adapter is capable of handling the resolution and framerate that your pen display supports. For example: you pen display may support 4K at 60Hz. But your adapter might only support up to 4K at 30Hz. &#x20;
* Sometimes adapters themselves can be the source of the NO SIGNAL problem. Sometimes a different adapter might work. In some cases, an you have to NOT use an adapter. &#x20;

## Try USB-C

* If your pen display supports USB-C for a display signal and if you have a USB-C port on your PC. That USB-C port **may** support sending a display signal over that port.&#x20;
  * NOTE: To find out if your USB-C port supports a display signal, you will likely have to read the documentation from your manufacturer. It's not possible to simply look at a port and determine if it supports a display signal.&#x20;
  * One easy sign that a USB-C port supports a display signal is if it has a lightning symbol above it. This means it is a Thunderbolt 3 or Thunderbolt 4 port.
* Get a USB-C cable that supports a display signal. Remember that not all USB C cables to support a display signal. The USB-C cables that do for sure carry a display signal are Thunderbolt 3 and Thunderbolt 4 cables. With every other cable you are going to have to check with the manufacturer or documentation.
* If needed consider a USB-C to HDMI adapter.

## Try using your pen display as your only display

* If you have a computer, disconnect all other displays and then **only** connect your pen display. Sometimes computer do get tripped up when multiple displays are being used, so by trying this procedure you help force it to use the pen display.&#x20;
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

## Refresh Rates

If your computer recognizes that a display is attached but you are still getting no signal, try changing the Refresh Rate the computer is using for the display.

Sometimes a misconfigured refresh rate causes the computer to not send a signal. For example, I have seen this happen with a  Windows Update, my pen display worked, but then after the update I saw the NO SIGNAL error. Somehow the refresh rate had been set to some unsupported value, once I changed it back to 60Hz it all worked again.

So always verify the rate.

Start with a lower refresh rate, and build up to higher ones.

## Display resolution

If your computer recognizes that a display is attached but you are still getting no signal, try changing the Resolution the computer is using for the display.

First try a very low resolution first and then build up to higher resolutions.

## Get it to work with another computer then reattach to your computer

Some users report that if they are getting NO SIGNAL with their pen display, they have been able to connect the pen display to another computer where it does work. And then once it worked, they reattached it back to the first computer where it then began working.

See this reddit comment: [https://www.reddit.com/r/huion/comments/109wjgx/comment/j41ekyk/?utm\_source=share\&utm\_medium=web2x\&context=3](https://www.reddit.com/r/huion/comments/109wjgx/comment/j41ekyk/?utm\_source=share\&utm\_medium=web2x\&context=3)

The reason this process might work is not clear. It could be because depowering the pen display was the reason. It could be because the connection to the other computer altered something in the pen display. In any case, it is worth a try if you continue to have problems.

## Using NVIDIA Rigorous Display Detection

If your computer is not even detecting the existence of the display, and it has an NVIDIA GPU, the NVIDIA Control Panel have a feature called **Rigorous Display Detection** which help.

* Open the **NVIDIA Control Panel**
* Navigate to **Display > Set up multiple displays >  Select the displays you want to use**&#x20;
* Click on **My display is not shown**&#x20;
* This will launch the **Detect Missing Display** dialog
* Click **Rigorous Display Detection**



![](<../.gitbook/assets/image (293).png>)



![](<../.gitbook/assets/image (6).png>)

## Use Intel Graphics Command Center to detect your display

If your computer is a laptop or similar device that has an embedded Intel GPU, on Windows you can use the Intel Graphics Commend Center app to potentially detect additional displays.

You can download the Intel Graphics Comment Center from the Microsoft Store.

## Wacom One

The Wacom One is very sensitive to the orientation of the how the 3-in-1 cable is plugged into its USB-C port. Usually the orientation that works, is when the cable sticks out to left side of the Wacom one.

## Firmware updates

It sometimes happens that monitors require firmware updates to make getting a display signal work. For example: [This ASUS monitor required a firmware update](https://www.asus.com/lk/support/FAQ/1045839/) to get video to work over USB C.   &#x20;

IMPORTANT: Don't install firmware updates on the general hope they will improve things. Please consult your manufacturer and support team to verify whether they recommend a firmware update to solve the problem.

## It worked before

This is one of the most surprising things about the NO SIGNAL problem is that it can occur to an existing working system. It's happened to me.

Here's what can trigger it

* A GPU driver update
* an Operating System update

## Other resources

### Reddit threads

* [https://www.reddit.com/r/XPpen/comments/z2h51j/tips\_when\_there\_is\_no\_signal\_andor\_tablet\_is/ ](https://www.reddit.com/r/XPpen/comments/z2h51j/tips\_when\_there\_is\_no\_signal\_andor\_tablet\_is/)

### Misc

* [https://www.windowscentral.com/how-fix-your-second-monitor-not-being-detected-windows-10](https://www.windowscentral.com/how-fix-your-second-monitor-not-being-detected-windows-10)
* [https://support.microsoft.com/en-us/windows/troubleshoot-external-monitor-connections-in-windows-10-5b46f4a4-9634-06bb-7622-f960facdfd49](https://support.microsoft.com/en-us/windows/troubleshoot-external-monitor-connections-in-windows-10-5b46f4a4-9634-06bb-7622-f960facdfd49)&#x20;
* TheHowToGuy123 - How To Enable Motherboard HDMI Port for Multiple Monitors - Use Graphics Card & Integrated Graphics ([https://youtu.be/\_Ftk8jQhsqE](https://youtu.be/\_Ftk8jQhsqE))

### Manufacturer guidance

#### Huion&#x20;

* General: [https://support.huion.com/en/support/solutions/articles/44001154156-what-to-do-if-your-huion-pen-display-shows-a-black-screen-or-no-signal](https://support.huion.com/en/support/solutions/articles/44001154156-what-to-do-if-your-huion-pen-display-shows-a-black-screen-or-no-signal)
* Huion support for Kamvas 13: [https://support.huion.com/en/support/solutions/articles/44001949665-how-to-fix-my-kamvas-13-no-signal-black-screen-problem-](https://support.huion.com/en/support/solutions/articles/44001949665-how-to-fix-my-kamvas-13-no-signal-black-screen-problem-)







