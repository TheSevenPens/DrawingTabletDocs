# EMR tilt detection

## Overview

EMR pens do NOT report the pen's tilt to the tablet. For example, it doesn't tell the tablet, "I am tilted by 5 degrees."

Instead, an EMR digitizer can detect the tilt of the pen just by examining the strength and shape of the signal the digitizer coils receive from the pen.

## Details

When the pen is perpendicular, the digitizer detects a signal from the pen that has one peak.

<figure><img src="../../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

As the pen tilts, it produces a signal with two peaks.

<figure><img src="../../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

The work for the EMR sensor and tablet firmware is to detect that there are two signal peaks and then disambiguate them.

Once two peaks are established and their relative strengths and positions are known, then the direction of tilt and amount of tilt can be established and then reported to the computer.

The specific algorithm to do this has, to my knowledge, never been exactly revealed. But those knowledgeable in how signals like this are processed will probably have a clearer idea of how this tilt detection is done.

## **How tilt is reported to the computer**

The two ways - two sets of angles. Azimuth/Altitude or X/Y.

We'll begin with Azimuth and Altitude because despite the names they are easy to understand. If we think of a tilted pen as "leaning" then:

* Azimuth = Lean direction
* Altitude = Lean amount

<figure><img src="../../.gitbook/assets/image (58).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

Now that you understand Azimuth and Altitude, X/Y tilt is just another equivalent way of describing it where tilt is describes as how much lean it has on the A and Y axes of the tablet.&#x20;

<figure><img src="../../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>



