# EMR tilt detection

## Overview

EMR pens do NOT report the pens tilt to the tablet. For example it doesn't tell the tablet "I am tilted by 5 degrees"

Instead, an EMR digitizer can detect the tilt of the pen just by examining the strength and shape of the signal the digitizer coils receive from the pen.

## Details

When the pen is perpendicular, the digitizer detects a single perpendicular shape.

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

As the pen tilts, it produces two shapes. And the relationship between the two shapes indicates the tilt.

For example, in the diagram below, the pen is pointing to the lower left - meaning the top part of the pen is "falling" toward upper right of the tablet.

<figure><img src="../../.gitbook/assets/Slide_20240506_185502.png" alt=""><figcaption></figcaption></figure>

## **How tilt is reported to the computer**

The tablet measures the tilt in both the x and y directions

<div align="left">

<figure><img src="../../.gitbook/assets/image (72).png" alt="" width="375"><figcaption><p>pen not perfectly perpendicular to tablet as indicated by shadow. Diagram shows x &#x26; y components of tilt.</p></figcaption></figure>

</div>

Measuring as x tilt and y tilt is also equivalent to measuring as azimuth and altitude. Think of azimuth as an angle from the tablet measured from "north" and the altitude as how high the far end of the pen is from the tablet surface.

In the example below the orange lines indicator the azimuth. And the purple line indicates the altitude (also known as elevation).

<figure><img src="../../.gitbook/assets/image.png" alt="" width="375"><figcaption></figcaption></figure>





