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

As of Jan 2025, the highest report rates stated for a tablet are 300Hz. And for Wacom specifically only 220Hz. This can be surprising for those of us who are familiar with mice that have a report rate of one 1000Hz.

As far as I know there is no clear hardware or system limitation to why tablets. don't have higher report rates.

I believe the reason we don't see higher report rates is that for a drawing scenario an artist would not notice a high report rate. And so the current report rates are "good enough . and table brands don't seem interested in improving them

