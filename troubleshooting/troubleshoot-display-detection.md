# Troubleshoot computer does not detect display

## Overview

* To use your pen display, your computer must be able to detect the display panel inside it.
* Most of the time, when you plug in your tablet to your computer this will work automatically.
* Unfortunately, sometimes your computer can sometimes have difficulty.

For example if you a computer with one monitor and a pen display attached, you should see TWO displays in your operating systems Display Settings. If you only see one, then the computer does not thing a second display is attached.

| Windows 11                                                                                                                                                                                                                                                                                                                                                     | MacOS (Ventura)                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](https://docs.thesevenpens.com/\~gitbook/image?url=https%3A%2F%2F1457921496-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FNde0PQIvNcFZNVxuTO0G%252Fuploads%252FBd9wPLauCDUqwHZlnIaJ%252Fimage.png%3Falt%3Dmedia%26token%3D075706fd-5c49-400d-bb0c-8904bf9f4bd5\&width=300\&dpr=4\&quality=100\&sign=471983f1\&sv=1) | ![](https://docs.thesevenpens.com/\~gitbook/image?url=https%3A%2F%2F1457921496-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FNde0PQIvNcFZNVxuTO0G%252Fuploads%252Fo8LCtp1VFfxFG0UwbmAk%252Fimage.png%3Falt%3Dmedia%26token%3D48c9dffa-e80a-43b6-b6c2-c9e5a0774a86\&width=300\&dpr=4\&quality=100\&sign=55ebce81\&sv=1) |

## Basic things to try or investigate

* Restart the computer - sometimes that can trigger the detection.
* Check the ports to make sure the cables are plugged in all the way. This is a very common mistake.

## Ensure the ports are clear of obstruction

Check the ports to ensure that there isn't some lint or other material preventing a secure connection.

## Windows > built-in display detection

&#x20;In Display Settings, there is an option to detect a display. Try it.

<div align="left">

<figure><img src="../.gitbook/assets/image (399).png" alt="" width="375"><figcaption></figcaption></figure>

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



![](<../.gitbook/assets/image (319).png>)



![](<../.gitbook/assets/image (32).png>)

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

Contact support

