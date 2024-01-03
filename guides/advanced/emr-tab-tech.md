# EMR technology in drawing tablets

## Companion video: How do EMR pens work?

{% embed url="https://youtu.be/Vv668I4LEdg" %}

## Pressure detection

In the video, a specific method to detect pressure is shown. This method involves moving the ferrite core which then alters the resonant frequency of the LC circuit. This design is from a very, very old EMR pen design.&#x20;

Modern designs use a separate pressure sensor which is more reliable for detecting pressure.

<figure><img src="../../.gitbook/assets/7P SLIDE EMR Old New Design (1).png" alt=""><figcaption></figcaption></figure>

The OLD EMR pen design can be seen in [**this teardown of the Huion PEN80 pen**](../pens/pen-teardown-huion-pen80.md).

## EMR design: Concepts vs Implementation

Think of the EMR design illustrated in the video as a baseline example that demonstrates the fundamental concepts, different manufacturers can tweak this design in their implementation.

## **Active EMR vs Passive EMR**

Active vs Passive refers to how the EMR pen gets its power.

* With Passive EMR, the pen gets its power from the tablet.
* With Active EMR, the pen gets its power from a battery inside the pen. That battery may be replaceable or rechargable.

Modern EMR pens are Passive EMR. DO NOT Buy as tablet that uses a Passive EMR pen.

Mixing and matching: You cannot use an Active EMR pen with a tablet that supports Passive EMR pens. And likewise you cannot use a Passive EMR pen with a tablet that supports an Active EMR pen.

## **Pen technologies**

Even though EMR is used in drawing tablets, there are many other pen technologies in the market, such as AES, Apple Pencil, etc. More here: [**Digital pen technologies**](digital-pen-technologies.md)&#x20;

## **General resources**

* [Sabins - Understanding Inductors](https://youtu.be/d73e3QiMdSU) &#x20;
* [Lesics - The beauty of LC Oscillations!](https://youtu.be/2\_y\_3\_3V-so)&#x20;
* [The Organic Chemistry Tutor - LC Oscillator Tank Circuit](https://youtu.be/nh4q7mIhLrY) &#x20;
* [Digital Art Tablet Guides - The Insides of Some Tablet Pens!](https://digitalarttabletguides.wordpress.com/2019/03/21/a-note-about-tablet-pens/)  &#x20;
* [rukozhop - This video shows the internals of a Huion PW100 pen](https://youtu.be/21LObZYVyLs) &#x20;
* [Satoshi Uchino, et al - A full integration of electromagnetic resonance sensor and capacitive touch sensor into LCD](https://sid.onlinelibrary.wiley.com/doi/abs/10.1002/jsid.777) &#x20;

## **Wacom resources**

* **Wacom: EMR Stylus (Electro-magnetic Resonance): How Wacom Pens work** https://community.wacom.com/us/emr-stylus-electro-magnetic-resonance-how-wacom-pens-work/ &#x20;
* **Wacom: EMR (Electro-Magnetic Resonance) Technology** https://archive.is/mhHkP
* **Wacom: How the Wacom cordless, batteryless pen work** https://quietpc.sk/instructions/wacom/tech\_bam\_en.pdf &#x20;
* **Wacom Patents** https://patents.google.com/patent/US4786765A/en https://patents.google.com/patent/US4878553B1/en
* **Wacom: Wacom feel EMR** https://wcm-cdn.wacom.com/-/media/graveyard/wacomdotcom/archived%20images/enterprise/technology-solutions/2015-12-21/f\_emr\_datasheet\_12192015.pdf?la=en\&rev=5973a6a064ce4f57b20a049410aed106\&hash=A479EA340EE48BD510113192CCC3D271 &#x20;

## **Scanlime resources**

* The Scanlime videos are the deepest examination on drawing tablet tech I have found.&#x20;
* **Scanlime: Your Wacom pen is an Electric Pendulum** ([https://youtu.be/oKVCwPn6OPI](https://youtu.be/oKVCwPn6OPI))
  * 1:10 a tuned LC circuit can act as an EMR pen &#x20;
* **Scanlime 013: Graphics Tablet Primer for Hackers** ([https://youtu.be/nPab7pbOhBY](https://youtu.be/nPab7pbOhBY))&#x20;
  * Accompanying write up: [https://scanlime.org/2016/08/scanlime013-wacom-teardown-and-schematic/](https://scanlime.org/2016/08/scanlime013-wacom-teardown-and-schematic/)&#x20;
  * This video shows an Huion H610PRO tablet and Huion PEN80 (rechargable) battery-powered pen.&#x20;
  * Key points at around 24:20
    * 24:22 buttons lower the frequency of the oscillation
    * 24:41 the nib is plastic and does not affect the inductance of the coil
    * 24:44 the nib moves a small ferrite core that changes the inductance of the coil.&#x20;
    * 24:50 Pressure decreases inductance which decreases energy stored in the magnetic field and slightly increases the oscillation
  * Other points
    * 25:35 Shielding freom electromagnetic interference
* **Scanlime: Wacom Teardown and Schematic** - ([https://youtu.be/j4AKwJERxOw](https://youtu.be/j4AKwJERxOw))
* **What’s Inside those Wacoms, And How Can You Use Them In Projects?**([https://makezine.com/article/maker-news/whats-inside-wacoms-can-use-projects/](https://makezine.com/article/maker-news/whats-inside-wacoms-can-use-projects/)) (archive: [https://archive.is/wip/wr9mn](https://archive.is/wip/wr9mn))
* Key points:
  * "At this point the Wacom and Huion designs diverge. Huion’s pen \[PEN80] is a single-transistor oscillator. Pressure on the nib changes the frequency from 255 to 266kHz by tuning the inductor, and the two buttons switch to 235 or 245kHz with additional capacitors. The simplest Wacom pen would be a resonant LC circuit tuned to 750kHz. To transmit button and pressure status, an additional digital circuit modulates the resonant damping to send out individual bits of sensor data on each carrier burst."

## Apple Pencil

The Apple Pencil does not use EMR. Apple uses a proprietary protocol for their pen.

If you are curious about what is inside an Apple pencil, see this video: [https://youtube.com/shorts/M9sArtVjRps?feature=share](https://youtube.com/shorts/M9sArtVjRps?feature=share) &#x20;

## Circuit simulations

The companion video contains several circuit simulations.&#x20;

<figure><img src="../../.gitbook/assets/Screenshot 2023-07-03 204827.png" alt=""><figcaption></figcaption></figure>

I used the **Falstad** tool https://www.falstad.com/circuit/ to create those simulations

##
