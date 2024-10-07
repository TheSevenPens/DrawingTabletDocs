# Troubleshoot computer does not detect display

## Overview

* To use your pen display, your computer must be able to detect the display panel inside it.
* Most of the time, when you plug in your tablet to your computer this will work automatically.
* Unfortunately, sometimes your computer can sometimes have difficulty.

When you plug in your pen display your computer should detect it as an additional display/monitor in display setttings. If you don't see another monitor in Display Settings, then for whatever reason it does not think the display part of your pen display is attached.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (2).png" alt="" width="563"><figcaption></figcaption></figure>

## Don't bother reinstalling the tablet drivers

Your computer thinks of your pen display as two devices:

* a pen tablet (aka a screenless tablet) without a display
* a monitor

The tablet driver is talking to the pen tablet. So reinstalling the driver is likely not going to do anything about this problem.

Your computer's operating system is taking to the display. You need to focus your efforts on why the operating system doesn't think the display in the tablet exists.

Also reinstalling tablet drivers can't hurt, reinstalling them multiple times is not going to change anything.

## Restart the computer

Sometimes this can trigger the detection

## Check that the cables are plugged in all the ay

This is a very common mistake.

## Ensure the ports are clear of obstruction

Check the ports to ensure that there isn't some lint or other material preventing a secure connection. Material like lint in the port can prevent the cable from working.

## Windows > built-in display detection

&#x20;In Display Settings, there is an option to detect a display. Try it.

<div align="left">

<figure><img src="../.gitbook/assets/image (472).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

## MacOS

See: [https://support.apple.com/en-tm/guide/mac-help/mchla25b377d/mac](https://support.apple.com/en-tm/guide/mac-help/mchla25b377d/mac)

## Using NVIDIA Rigorous Display Detection

If your computer is not even detecting the existence of the display, and it has an NVIDIA GPU, the NVIDIA Control Panel have a feature called **Rigorous Display Detection** which help.

* Open the **NVIDIA Control Panel**
* Navigate to **Display > Set up multiple displays >  Select the displays you want to use**&#x20;
* Click on **My display is not shown**&#x20;
* This will launch the **Detect Missing Display** dialog
* Click **Rigorous Display Detection**



![](<../.gitbook/assets/image (392).png>)



![](<../.gitbook/assets/image (105).png>)

## Use Intel Graphics Command Center to detect your display

If your computer is a laptop or similar device that has an embedded Intel GPU, on Windows you can use the Intel Graphics Commend Center app to potentially detect additional displays.

You can download the Intel Graphics Comment Center from the Microsoft Store.

## Use a another port of the same type

Suppose you are using an HDMI port, there may be multiple HDMI ports on your computer. Try the other ones.

## Use a another port of a different type

For example, if you are using HDMI, try DisplayPort instead.

## Check if the pen display can get a signal from another device

See if the display can be detected by another computer or even any device that can send a display signal such as a DVD player or an XBOX.&#x20;

If this works it tells you the pen display and cables work correctly and the problem has something to do with your computer.

## Depowering the device

Some people suggest doing this:

* UNPLUG the pen display from POWER
* hold the power button down&#x20;
* while continuing to hold the power button down, attach the pen display to power, and continue holding down the power for a few seconds.

## Firmware updates

Check with your manufacturer if there are any firmware updates.

## If all else fails

Contact support!



