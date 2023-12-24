# Troubleshoot tablet driver does not detect tablet

## Overview

The "tablet not connected/detected" problem is fundamentally that your computer cannot "see" the device even though it is plugged in via USB cable.

**IMPORTANT**: If you have a pen display and see a "NO SIGNAL" message, that is a different kind oof problem. Go here: [**Troubleshoot No Signal**](troubleshoot-no-signal.md).&#x20;

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

Try uninstalling your manufacturer tablet driver. The restart your computer. Then see if the tablet works correctly.

If it does work correctly, it points to a problem with the manufacturer tablet driver.

## Windows > power options for the tablet

Some people say this has helped them. I'm not sure.&#x20;

In **device manager**, select **View > By container**

Find your tablet

Under will be a list of devices

for each device under the tablet, right-click and select **Properties**

Uncheck **Power Management > Allow the computer to turn off this device to save power** if that option exists for the device.

## Manufacturer support pages

* **Wacom**: What does the error message “A supported tablet is not found on the system” or "No Wacom device connected to your computer" mean and how do I fix it? ([link](https://support.wacom.com/hc/en-us/articles/1500006339862))
* **Huion**: What To Do When Huion Driver Shows Device Disconnected?  ([link](https://support.huion.com/en/support/solutions/articles/44001163422-what-to-do-when-huion-driver-shows-device-disconnected-))

## Still not solved?

If none of these suggestions are helping, then [**contact support**](../guides/general/contacting-support.md).

## Notes

* When you plug in the tablet or unplug the tablet, check if the computer makes a "beep". This at least indicates that the computer is aware that there is some device there.
* Sometimes this problem is sporadic. I've had it personally occur with a tablet and after about 30 minutes of restarts, things just started working again.
* Some vendors like Huion recommend disabling antivirus when reinstalling the drivers. I do not recommend this, but some people say it has helped.

## Reference: Driver UX

#### Huion

#### ![](<../.gitbook/assets/Huion device disconnected.png>)

#### XP-Pen

driver version: 3.4.12(104e65f)&#x20;

<div align="left">

<figure><img src="../.gitbook/assets/image (2) (1).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

**Wacom / Wacom Center**

Date: 2023/12/23

<div align="left">

<figure><img src="../.gitbook/assets/Screenshot 2023-12-23 at 10.03.09 PM.png" alt="" width="563"><figcaption></figcaption></figure>

</div>

