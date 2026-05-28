# The realities of building your own EMR pen

## Overview

I often get asked if it is possible to build an EMR pen. The short answer is YES, but it may be challenging.

If you watched my "How do EMR pens work?" video, you'd probably know enough, if you were electronically inclined, to acquire the basic components and put them together in a way that would work if you were sufficiently motivated.

## Key challenges

* **Understanding how the pen and tablet talk.** You’ll need an oscilloscope and need to learn how to use it correctly. See the Scanline YouTube channel, which has a couple of videos that explore EMR tablets. You should learn a lot from there.
* **Components.**
  * Most components are things you can buy: ferrite core, copper coil, spring, piezoelectric sensor.
  * Some components you may need to 3D print: the pen shell, nibs, and assorted bits of plastic that hold everything together inside.
  * The PCB will require you to make something small enough to fit in the case. And it has to use very little power and know how to communicate certain kinds of data to the tablet.
* **Powering the pen.** You need to construct the inductor and PCB to get energy from the tablet and briefly power the pen so it can transmit a signal back.
* **Position and tilt** are done by the tablet simply by sensing the analog signal produced by the pen.
* **Pressure and button presses** require extra work. After studying the tablet and a pen, you will need to transmit button presses in the same way with components on the PCB. Some pens transmit these in an analog way - by modifying the resonant frequency of the signal from the pen. Some pens transmit these in a digital way by encoding the information digitally in the signal.
