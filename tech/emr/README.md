# EMR

## Overview

Wacom introduced EMR technology to drawing tablets. They held the core EMR patents. Those patents have expired, and other manufacturers can now build increasingly sophisticated EMR designs that rival Wacom products.

## EMR key features

* Powering the pen - With **Passive EMR**, the pen gets power from proximity to the tablet. With **Active EMR**, the pen gets power from an internal battery. More here: [Active EMR vs Passive EMR](active-emr-vs-passive-emr.md)
* Position detection - The basics of how the tablet detects position are described here: [EMR position detection](emr-position-detection.md).
* Hover - Also called proximity detection.
* Pressure detection - See [EMR pressure detection](emr-pressure-detection.md) for details. It also clarifies the pressure detection shown in the video below, which depicts a much older method.
* Tilt detection - More here: [EMR tilt detection](emr-tilt-detection.md)
* Barrel rotation detection - Very rare in EMR pens.
* Communication of button press information.

## Explanation of how EMR works

NOTE: This video's explanation of pressure describes a very early EMR pen design. It involves physically moving the ferrite core inside the inductor coil, which changes the resonant frequency of the pen's signal. Modern EMR pens use a design in which the ferrite rod remains stationary relative to the inductor coil, and pressure is digitally encoded in the signal coming from the pen.

{% embed url="https://youtu.be/Vv668I4LEdg" %}

## Deeper EMR Technical resources

If you want to go deeper into how EMR works, go here: [EMR](./#emr-technical-resources)

## Notes on EMR

### EMR Concepts vs Implementation

Think of the EMR design illustrated in the video as a baseline example that demonstrates the fundamental concepts. Different manufacturers can tweak this design in their implementations.

### **Resonant frequency**

The exact resonant frequency used by the pen varies. In the case of the Wacom Bamboo Fun tablet (CTH-661), the frequency is around 750 kHz. Source: the last 10 seconds of this scanlime video: [https://www.youtube.com/watch?v=oKVCwPn6OPI](https://www.youtube.com/watch?v=oKVCwPn6OPI)

### **How fast does the tablet switch between sensing the pen and sending it power?**

We don't know. We suspect it is much faster than a typical pen report rate of 200 Hz.

## **Other digital pen technologies**

Even though EMR is used in drawing tablets, many other pen technologies are also on the market, such as AES and Apple Pencil tech. More here: [Digital pen tech](../digital-pen-tech.md)

### Apple Pencil

The Apple Pencil does not use EMR. Apple uses a proprietary protocol for its pen. If you are curious about what is inside an Apple Pencil, see this video: [https://youtube.com/shorts/M9sArtVjRps?feature=share](https://youtube.com/shorts/M9sArtVjRps?feature=share)
