# Tablet reports

## Overview

Somewhere between 100 to 300 times a second, your tablet sends a "package" of data to your computer. This package is called a "tablet report" or just "report". The tablet driver, operating, and application may modify that data. And of course a drawing application uses that data to draw a stroke.

## Report rate

You can see this often in the specifications for a tablet as "report rate". Here is an example.

<figure><img src="../../.gitbook/assets/image (59).png" alt="" width="375"><figcaption></figcaption></figure>

"RPS" means "Reports per second"

Because this is a value per second in some literature you might see the unit Hz being used. So for example instead of "200 RPS" you might see "200hz".

## Report contents

The exact format of the data varies depending on the tablet. But conceptually the report will include data like this:

* The x,y **position** of the pen
* The **pressure** reading. 0 = no pressure or some positive integer if there is pressure
* The **tilt** - composed of two values. Either given as a x tilt and y tilt or as altitude angle and azimuth angle.
* The **button** press status

The report contains other interesting things, but these are the critical ones for drawing strokes.

## Higher report rates

### The current state of the art

As of Jan 2025, the highest report rates stated for a tablet are 300Hz. Even the leading brand, Wacom, only supports a maximum of 220Hz. Numbers in the 200Hz to 300Hz are surprising when we see mice that have report rate of 1000Hz.

### Is there a hardware limitation?

No. As far as I know there is no clear hardware or system limitation.

### Why don't we see higher report rates

I believe the reason is simple: The typical customer for a drawing tablet would experience no benefit while the tablet manufacturer would have to implement a more expensive design. In other words: Nobody benefits. The current state of affairs is "good enough".

See: I think tablet brands are aware of this desire from gamers but they haven't done anything to make the tablets work better for these scenarios.

[Wacom - Does a higher, or faster, report rate mean better performance?](https://support.wacom.com/hc/en-us/articles/1500006331322-Does-a-higher-or-faster-report-rate-mean-better-performance) ([archive](https://archive.is/s6gOg))

## Finding report rates

Different tools can be used: [Measuring report rate](../../process/measuring-report-rate.md)
