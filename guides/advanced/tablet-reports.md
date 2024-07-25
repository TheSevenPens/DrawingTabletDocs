# Tablet reports

## Overview

Somewhere between 100 to 250 times a second, your tablet sends a "package" of data to your computer. This package is called a "tablet report" or just "report". The tablet driver, operating, and application may modify that data. And of course a drawing application uses that data to draw a stroke.

## Report rate

You can see this often in the specifications for a tablet as "report rate". Here is an example.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

"RPS" means "Reports per second"

Because this is a value per second in some literature you might see the unit Hz being used. So for example instead of "200 RPS" you might see "200hz".

## Report contents

The exact format of the data varies dpeending on the tablet. But conceptually the report will include data like this:

* The x,y **position** of the pen
* The **pressure** reading. 0 = no pressure or some positive integer if there is pressure
* The **tilt** - composed of two values: x tilt and y tilt
* The **button** press status

The report contains other interesting things, but these are the critical ones for drawing strokes.

