# TSG: Touch input goes to a different display on Windows

## Overview

On Windows, if you have a pen display that supports touch, you may find that if you touch the pen display, it will act as if you are touching a different display.

This is a common thing people run into with displays that support touch on Windows. It's not the fault of the pen display and it can be easily fixed.

## Background

When you attach a device that supports touch input, by default Windows will map its touch input to the "main display".  And most often this will NOT be your pen display.

## OPTION #1: Set your pen display to be the main display

* Open Display Settings
* Click on the display that corresponds to your pen display
* Enable "Make this my main display"

## Option #2: Configure Windows to send touch input to the a different display

* Open **Control Panel**
* Find and open **Tablet PC Settings**
* Under the **Display** > **Configure** tab click **Setup**
* Select **Touch input**
* In the screen you'll be asked to follow some instructions to identify which display touch should go it. Follow those instructions

## Links

* [https://support.huion.com/en/support/solutions/articles/44002416035-how-to-make-finger-gestures-control-kamvas-studio-16-kamvas-pro-19-kamvas-pro-27-instead-of-the-exter](https://support.huion.com/en/support/solutions/articles/44002416035-how-to-make-finger-gestures-control-kamvas-studio-16-kamvas-pro-19-kamvas-pro-27-instead-of-the-exter)















* By default, touch on the tablet will normally map to whichever display is your "main monitor".&#x20;
* You can map touch back to the tablet when it is not the main monitor. See this document from Huion: [How to make finger gestures control Kamvas Studio 16/Kamvas Pro 19/Kamvas Pro 27 instead of the external monitor](https://support.huion.com/en/support/solutions/articles/44002416035-how-to-make-finger-gestures-control-kamvas-studio-16-kamvas-pro-19-kamvas-pro-27-instead-of-the-exter). When I first tried this, it fixed the touch problem, but it had an odd interaction with the pen - when I used the pen on the tablet, the pointer always stayed near the top border. After I uninstalled the driver, restarted the computer, and reinstalled the driver, the problem went away and the pen worked normally.

