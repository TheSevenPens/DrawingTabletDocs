# Connecting a pen display with a single USB-C cable

## Overview

It is POSSIBLE for SOME pen displays to be powered by a single USB-C cable.

## Key requirements

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## **DP alt mode support**

To find out if you ports and cables support DP alt mode, read this**:** [USB-C DisplayPort alt mode](usb-c-displayport-alt-mode.md)&#x20;

## Power support

* Cables
  * Thunderbolt USB-C cables do support carrying enough power
* Ports
  * Even if the cable supports power, your computers USB-C port may not supply enough power.
* Power needed
* The size of the pen display affects how much power is needed.&#x20;
  * It's very likely that if your USB-C port can deliver enough power a 13" pen display
  * At 16", some pen displays require additional power usually from a power adapter that is plugged into a wall.&#x20;
  * Above 16" most often in my experience a single USB-C cable is not enough and these pen displays require additional power.&#x20;

## Manufacturer cables vs third-party cables

I recommend you get the USB-C cables the manufacturer provides for use with a single USB-C cable configuration - primarily because these are known to work with the device and will fit into the well that contains the port.

I sometimes use thunderbolt 3 cables, but sometimes have to shave off a bit of plastic from the end to make them fit into the pen display.&#x20;

## Testing setup&#x20;

**Computer tested**

* Surface Pro 8
* Computer port: I connected to the USB-C ports on the side of the Surface Pro 8 which support Thunderbolt 4.
* The computer is plugged into a Surface dock to provide power.

**Cables tested**

* CableMatters \[Intel Certified] 20Gps Thunderbolt 3 cable (6.6 ft) supporting 100W charging. ([amazon link](https://www.amazon.com/dp/B01AS8U9KE))

**Cable end thickness**

* For the CableMatters Usb-C cable, the **cable ends are a little too thick** to be plugged into some ports.
* I had to remove some plastic from one of the ends to fit it into the tablets using a knife.&#x20;
* ![](<../../.gitbook/assets/Whittled USBC (1).jpg>)![](<../../.gitbook/assets/Whittled USBC (3) (2).jpg>)
* This plastic was tough to cut. I didn't do a very clean job but it **just barely** fits into the port - the fit is very snug and I should probably remove just a little more.

## Testing results

<table><thead><tr><th>Tablet</th><th width="98">Port</th><th>Cable</th><th>Results</th></tr></thead><tbody><tr><td><p><strong>Huion Kamvas 13</strong></p><p><strong>(GS1331)</strong></p></td><td>lower</td><td>CableMatters Thunderbolt 3 cable</td><td>VERIFIED TO WORK</td></tr><tr><td><p><strong>Huion Kamvas Pro 13 2.5K</strong></p><p><strong>(GT1302)</strong></p></td><td>upper</td><td>CableMatters Thunderbolt 3 cable</td><td>VERIFIED TO WORK</td></tr><tr><td><strong>Huion Kamvas Pro 16 Plus 4k (GT1562)</strong></td><td>lower</td><td>CableMatters Thunderbolt 3 cable</td><td>VERIFIED TO WORK</td></tr><tr><td><p><strong>XP-Pen Artist 12 GEN2</strong></p><p><strong>(CD120FH)</strong></p></td><td>upper</td><td>CableMatters Thunderbolt 3 cable</td><td>VERIFIED TO WORK</td></tr><tr><td><p> <strong>XP-Pen Artist 13 GEN2</strong></p><p><strong>(CD130FH)</strong></p></td><td>upper</td><td>CableMatters Thunderbolt 3 cable</td><td>VERIFIED TO WORK</td></tr><tr><td><strong>XP-Pen Artist Pro 16 GEN2 (MD160QH)</strong></td><td>left</td><td>CableMatters Thunderbolt 3 cable</td><td>VERIFIED TO WORK</td></tr><tr><td><strong>Wacom One 13 touch GEN2 (DTH-134)</strong></td><td>left</td><td>CableMatters Thunderbolt 3 cable</td><td>VERIFIED TO WORK</td></tr><tr><td><p><strong>Wacom One 12 GEN2</strong></p><p><strong>(DTC-121)</strong></p></td><td>left</td><td>CableMatters Thunderbolt 3 cable</td><td>VERIFIED TO WORK</td></tr><tr><td><p><strong>Wacom One GEN1</strong></p><p><strong>(DTC-133)</strong></p></td><td>only 1 port</td><td>CableMatters Thunderbolt 3 cable</td><td><p>This pen display does not support using a single USB-C connection. I tested it anyway and </p><p>VERIFIED that it did <mark style="color:red;"><strong>NOT WORK</strong></mark></p></td></tr></tbody></table>

## Resources

* Here is a list from Huion about devices that can use a single USB-C cable: [https://support.huion.com/en/support/solutions/articles/44002011098-list-of-compatible-devices-support-usb-c-to-usb-c-connection-with-huion-displays](https://support.huion.com/en/support/solutions/articles/44002011098-list-of-compatible-devices-support-usb-c-to-usb-c-connection-with-huion-displays)&#x20;
* Brad Colbow connecting the Huion Kamvas 13 with a single USB-C cable: See 6:00 in this video: [https://youtu.be/ku8x1q\_nhFQ](https://youtu.be/ku8x1q\_nhFQ)
* Teoh on Tech connecting the XP-Pen Artist 13 (2nd gen) using a single USB-C cable. See 4:30 in the video:  [https://youtu.be/Exj2PZu4MHM](https://youtu.be/Exj2PZu4MHM)
