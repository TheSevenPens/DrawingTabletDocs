# Troubleshoot tablet driver does not detect tablet

## Overview

The "tablet not connected/detected" problem is fundamentally that your driver cannot "see" , "find", or "communicate" with the drawing tablet even though it is plugged in via USB cable. The driver will often claim that the tablet "is not connected" or "is not detected".

If this happens with a **pen tablet (a screenless tablet)**, then essentially the tablet isn't functional at all.

If this happens with a **pen display (a screen tablet)**, usually the display part of the tablet works fine but you won't be able to use the pen with the tablet. In other words, now the pen display works only like a monitor.



{% hint style="info" %}
I want to be candid with you. If this problem isn't due to some simple cabling problems, usually it is very difficult to diagnose and solve. I have never discovered a consistent solution or even a real root cause to this problem.
{% endhint %}

## Driver versus operating system

What makes this issue confusing is that sometimes your computer's operating system may know that a device is connected even if the tablet driver does not. For example, your operating system may "beep" when you plug the tablet in. And even may list it as a device, even though the driver insists nothing is connected"

## What is not being detected

Your tablet is a plastic shell that contains at least one component - the tablet digitizer. This digitizer is the fundamental component of a tablet that deals with the pen.&#x20;

When a driver is saying your tablet is not connected, it is talking about this digitizer

The digitizer is the primary component of a pen tablet (screenless tablet) though some pen tablets have other components. You may for example see your tablet detected as a keyboard because it has some keyboard like buttons.

For a pen display (screen tablet) there is of course another component - the screen. Your computer detects the screen completely separately from the tablet digitizer. This explains why the display part still works.

## NO SIGNAL for pen displays

Another kind of connection problem is the "NO SIGNAL" problem. It has nothing to do with the digitizer and is a completely unrelated topic. It means a pen display cannot detect a video signal from the computer. If you are experiencing the NO SIGNAL problem, then go here: [**Troubleshoot No Signal**](troubleshoot-no-signal.md).&#x20;

## Basic troubleshooting&#x20;

* Restart the computer. This sometimes resolves the problem.
* Uninstall and reinstall the driver. Then restart the computer.
* Check if there is a more recent version of the driver. Install it. Then restart the computer.
* If you are using a pen display, verify it is getting enough power.

## USB-connection options

* Try unplugging other USB devices leaving only the tablet then plug devices back in.&#x20;
* If you have a USB hub, try not using it.&#x20;
* Look at the USB ports and ends of the USB cables and verify they are clean. Remove any lint, etc. that you find.
* Try a different USB cable - make sure the USB cable supports data and not just power.
* Try a different USB port.
* Unplug and re-plug the USB cable
* Check your tablet documentation. Some tablets have a "reset" option.&#x20;

## Try the tablet with another computer

The issue may be specific with your computer, so try with another computer.

* If it doesn't work there, then that suggest the tablet itself is having problems.
* If it does work there, then retry with your own computer.&#x20;

## Reset the tablet

* This is an option for SOME tablets. More here: [**Reset a drawing tablet**](reset-wacom-intuos-pro-tablets.md)

## Windows > Check if Windows PNP drivers work

Windows has some limited built-in support for tablets. Not all tablets work with Windows PNP, but many do.

How to test with the Windows PNP drivers: [**Testing with Windows PNP drawing tablet drivers**](testing-with-windows-pnp-drawing-tablet-drivers.md)

If it does work correctly, it points to a problem with the manufacturer tablet driver instead of the tablet hardware.

## Windows > power options for the tablet

Some people say this has helped them. I'm not sure.&#x20;

* In **device manager**, select **View > By container**
* Find your tablet
* Under it will be a list of devices
* For each device under the tablet, right-click and select **Properties**

Uncheck **Power Management > Allow the computer to turn off this device to save power** if that option exists for the device.

## Manufacturer support pages

* **Wacom**: What does the error message “A supported tablet is not found on the system” or "No Wacom device connected to your computer" mean and how do I fix it? ([**link**](https://support.wacom.com/hc/en-us/articles/1500006339862))
* **Huion**: What To Do When Huion Driver Shows Device Disconnected?  ([**link**](https://support.huion.com/en/support/solutions/articles/44001163422-what-to-do-when-huion-driver-shows-device-disconnected-))

## Time

Sometimes just waiting out the problem is all you can do. Some people report that they leave their tablet disconnected from their computer for a few days, and then afterwards it just starts working again.&#x20;

Both the times I've personally encountered this problem it seems like nothing I did worked, but I just waited and it eventually resolved itself.

## Still not solved?

If none of these suggestions are helping, then [**contact support**](../guides/general/contacting-support.md).

## Notes

* When you plug in the tablet or unplug the tablet, check if the computer makes a "beep". This at least indicates that the computer is aware that there is some device there.
* Sometimes this problem is sporadic. I've had it personally occur with a tablet and after about 30 minutes of restarts, things just started working again.
* Some vendors like Huion recommend disabling antivirus when reinstalling the drivers. I do not recommend this, but some people say it has helped.

## Reference: Driver disconnected messages

Here are several examples of how the driver indicates the tablet is not connected.

#### Huion

#### ![](<../.gitbook/assets/Huion device disconnected.png>)

#### XP-Pen

driver version: 3.4.12(104e65f)&#x20;

<div align="left">

<figure><img src="../.gitbook/assets/image (7) (1).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

**Wacom / Wacom Center**

Date: 2023/12/23

<div align="left">

<figure><img src="../.gitbook/assets/Screenshot 2023-12-23 at 10.03.09 PM.png" alt="" width="563"><figcaption></figcaption></figure>

</div>

