# Pen tilt

## Introduction

Tilt is easy to understand. Imagine you hold the then pen completely perpendicular to the tablet and that the sun is showing directly down on the tablet.

If the tablet is completely perpendicular, the shadow is a perfect circle that centered where the tip of the pen touches the tablet.dd

<div align="left">

<figure><img src="../../.gitbook/assets/image (321).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

Now keep left the top of the pen "fall" a bit. The shadow looks quite different. It begins at the tip and ends at the other side of the pen. it clearly is not a circle. What you are seeing is the tilt of the pen. Notice that the tilt has two components:

* a tilt in the y direction&#x20;
* a tilt in the x direction.

<div align="left">

<figure><img src="../../.gitbook/assets/image (46).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

## How tilt is measured

* The tilt of the pen is measured by the tablet, NOT the pen.
* The pen does not "report" its tilt to the tablet.
* The EMR pen generates an electromagnetic signal across multiple coils in the EMR sensor
* By evaluating the shape of the signal on the coils the tablet can determine the tilt of the pen.

## **How tilt is reported to the computer**

* The tablet reported tilt as as an X tilt and a Y tilt number
* Below is what it looks like in the Diagnostics UI of the Wacom Driver for the Wacom Intuos Pro Large PTH-860
* ![](<../../.gitbook/assets/Screenshot 2022-11-25 193023-annotated.png>)
* The X tilt reported by Wacom ranges from -64 to 63
  * a negative X value means that the pen is "falling" to the left of the tablet
  * a positive X value means the pen is "falling" to the right of the tablet
* The Y tilt reported by Wacom ranges from -64 to 63
  * a negative Y value means that the pen is "falling" to the top of the tablet
  * a positive Y value means the pen is "falling" to the bottom of the tablet
* If the X & Y are both zero, then the pen is perfectly perpendicular to the tablet

## **Tilt angle range**

* The standard range is +/- 60 degrees for both X and Y
* I don't know of any tablets that support a wider range

## **Tilt support in tablets**

* For many years now tilt has been a common feature on drawing tablets.&#x20;
* Wacom seems to only include tilt on its professional models.&#x20;
* Other manufacturers include it on all models.

## Tilt support in applications

* Even if your tablet is sending tilt data to your computer, your application may or may not be using the data.
* Some applications don't use the tilt data at all. An example would be most note taking applications like OneNote. They tend to recognize pressure but not tilt.
* Other applications do recognize tilt but the use of the tilt data is only for specific brushes. So for example, typically a "pencil" brush would support tilt. But other kinds of  brushes may not. Even then, these brushes has settings that let you customize whether and how tilt is used for the brush.
* Here's a good example for a brush in Krita. You can seee that the Rotation of the brush is set to the Drawing Angle, but that it could also be set to the tilt.
* ![](<../../.gitbook/assets/image (62).png>)



## Disabling tilt

Pen tilt information is always sent from the tablet to the tablet driver and from there to the operating system and then to pen-aware applications.

Sometimes when drawing it can be useful to turn off tilt. There are options

**OPTION 1 Use Brush settings** - Drawing apps that use brushes may let you control how tilt affects the brush. So, you can configure specific brushes to ignore tilt. Examples of applications that support this are Clip Studio Paint and Krita.

**OPTION 2** Turn off tilt in the driver - SOME tablet drivers let you simply turn off tilt so that it isn't reported to your operating system or applications.

XP-Pen drivers have this feature.

<div align="left">

<figure><img src="../../.gitbook/assets/image (333).png" alt="" width="563"><figcaption></figcaption></figure>

</div>







&#x20;&#x20;

