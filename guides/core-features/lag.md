# Lag

## Introduction

Unlike a pen and paper system, where there is essentially an instantaneous feeling to drawing, a drawing tablet being a digital system where many components are processing and communicating data is always subject to some form of lag.

In the context of drawing tablets, I use the word log to describe how things are "following" the physical pen.&#x20;

## Overview

<figure><img src="../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

## Companion videos

The details on lag are described in this video series:

* Drawing tablet lag - Episode 1: Basics ([https://youtu.be/CRwzPJPA\_5A](https://youtu.be/CRwzPJPA\_5A)) Apr 28, 2023
* Drawing tablet lag - Episode 2: Pointer lag ([https://youtu.be/tNj6vxx0FWM](https://youtu.be/tNj6vxx0FWM))  Aug 7, 2023
* Drawing tablet lag - Episode 3: Position smoothing in the tablet firmware and tablet driver ([https://youtu.be/sWvluY9w-Bk](https://youtu.be/sWvluY9w-Bk))  Aug 7, 2023

## EMR pointer lag Apple iPad pointer lag

With the Apple Pencil the iPad has lag but the overall perceivable lag is very low compared o an EMR drawing tablet. I **suspect** the lower lag is due to some of these factors:

* Very tight and optimized integration between the pen subsystem and the operating system. It makes sense Apple can do this because they own the entire tech stack.
* in a normal drawing tablet the EMR pens have a coil that is detected by the tablet and that coil is deeper inside the pen while the equivalent Apple Pencil component is close to the tip of the pen and thus to the tablet. This smaller distance should result in less electromagnetic interference. In turn this should require less position smoothing to remove the interference which then shows up as reduced lag.
* Relating to the previous point about distance. Just based on the visual parallax it seems like there is less physical distance between the tip of the Apple Pencil and the display panel compared to other EMR-based pen displays I have used. So, again this should reduce the amount electromagnetic interference and thus require less smoothing and result in less lag.
* From some things I've read, the iPads do some position prediction with the Apple Pencil so that results in an reduction in lag at the cost of reduced accuracy with abrupt changes in direction. I've even seen one video showing that iPads also can predict contact with the surface of the iPad so that they can start drawing just a moment before physical contact is made.

## Notes on brush lag

Aaron Rutten did a nice video to explaining how to minimize brush lag

{% embed url="https://www.youtube.com/watch?v=e9KA16TaDbg" %}

