# Pointer lag

## Overview

* For a more general introduction to lag, see [**Lag**](lag.md).
* If you you are "painting", there is a separate kind of lag called [**brush lag**](lag-1.md). &#x20;

## EMR pointer lag Apple iPad pointer lag

With the Apple Pencil the iPad has lag but the overall perceivable lag is very low compared o an EMR drawing tablet. I **suspect** the lower lag is due to some of these factors:

* Very tight and optimized integration between the pen subsystem and the operating system. It makes sense Apple can do this because they own the entire tech stack.
* in a normal drawing tablet the EMR pens have a coil that is detected by the tablet and that coil is deeper inside the pen while the equivalent Apple Pencil component is close to the tip of the pen and thus to the tablet. This smaller distance should result in less electromagnetic interference. In turn this should require less position smoothing to remove the interference which then shows up as reduced lag.
* Relating to the previous point about distance. Just based on the visual parallax it seems like there is less physical distance between the tip of the Apple Pencil and the display panel compared to other EMR-based pen displays I have used. So, again this should reduce the amount electromagnetic interference and thus require less smoothing and result in less lag.
* From some things I've read, the iPads do some position prediction with the Apple Pencil so that results in an reduction in lag at the cost of reduced accuracy with abrupt changes in direction. I've even seen one video showing that iPads also can predict contact with the surface of the iPad so that they can start drawing just a moment before physical contact is made.

## Can pointer lag be reduced?

YES - in theory and to some degree. But it is not a trivial thing to do.

Pointer lag comes from two sources: The tablet **firmware** and the tablet **driver**&#x20;

* It's possible to get rid of the lag caused by the driver by using a third party driver - for example OpenTabletDriver.&#x20;
* I've tried this with both an Intuos Pro and a Cintiq Pro. My results here
  * **Intuos Pro** - Noticeable reduction in lag (at the cost of a little more imprecision in the tracking of the pen)
  * **Cintiq Pro** - slight reduction in lag. But mostly stays exactly the same. From that I think the Cintiq Pro lag is primarily caused by the tablet firmware - probably to deal with the electromagnetic noise caused by the embedded display panel.
* The pointer lag in the firmware cannot be removed because essentially it is impossible for a user to modify the tablet firmware.&#x20;

