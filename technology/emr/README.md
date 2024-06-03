# EMR

## Overview

EMR technology was introduced to drawing tablets by Wacom. And they held all the core key patents to EMR. Those core patents have expired and now other manufacturers can build increasingly sophisticated EMR designs which are begin to rival Wacom products.

## EMR key features

* Power
  * Passive EMR: The pen gets power from proximity to the tablet
  * Active EMR: The pen gets power from a battery inside&#x20;
* Hover (i.e. proximity detection)
* Position detection
* Pressure detection
* Tilt detection
* Barrel rotation detection - very rare
* Communication of button information.&#x20;

## Explanation of how EMR works

{% embed url="https://youtu.be/Vv668I4LEdg" %}

## Position detection

The basics of how the tablet detects position are described here: [**EMR position detection**](emr-position-detection.md).

## Pressure detection

See this document for details on [**EMR pressure detection**](emr-pressure-detection.md). It also contains a clarification of pressure detection in the video which depicts a very old way of doing pressure detection.

## Tilt detection

more here: [**EMR tilt detection**](emr-tilt-detection.md) &#x20;

## Concepts vs Implementation

Think of the EMR design illustrated in the video as a baseline example that demonstrates the fundamental concepts, different manufacturers can tweak this design in their implementation.

## **Active EMR vs Passive EMR**

{% hint style="info" %}
Modern EMR pens are **Passive EMR**. <mark style="color:red;">**DO NOT Buy a tablet that uses Active EMR**</mark>.
{% endhint %}

**Active** vs **Passive** indicates how an EMR gets power.

* Passive EMR - The tablet wirelessly powers the pen
* Active EMR - A battery inside the pen powers the pen

**Active EMR battery type** - The battery may be replaceable or rechargeable.

**Mixing and matching?** -  It doesn't work.

* You cannot use an Active EMR pen with a Passive EMR tablet
* You cannot use a Passive EMR pen with Active EMR tablet.

## **Resonant frequency**

The exact resonant frequency used by the pen will vary.

In the case of the Wacom Bamboo Fun tablet (CTH-661) the frequency is around 750KHz. Source: the last 10 seconds of this scanlime video: [https://www.youtube.com/watch?v=oKVCwPn6OPI](https://www.youtube.com/watch?v=oKVCwPn6OPI)&#x20;

## **How fast does the tablet switch between sensing the pen and sending it power?**

We don't know.

We suspect this is MUCH faster than a typical pen report rate of 200Hz.

## **Other pen technologies**

Even though EMR is used in drawing tablets, there are many other pen technologies in the market, such as AES, Apple Pencil, etc. More here: [**Digital pen tech**](../digital-pen-tech.md)&#x20;

## Apple Pencil

The Apple Pencil does not use EMR. Apple uses a proprietary protocol for their pen. If you are curious about what is inside an Apple pencil, see this video: [https://youtube.com/shorts/M9sArtVjRps?feature=share](https://youtube.com/shorts/M9sArtVjRps?feature=share) &#x20;

## EMR Technical resources

More here: [EMR technical resources](./#emr-technical-resources)&#x20;

## Circuit simulations

The companion video contains several circuit simulations.&#x20;

<figure><img src="../../.gitbook/assets/Screenshot 2023-07-03 204827.png" alt=""><figcaption></figcaption></figure>

I used the **Falstad** tool https://www.falstad.com/circuit/ to create those simulations

