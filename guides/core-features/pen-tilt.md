# Pen tilt

## Introduction

Tilt is easy to understand. Imagine you hold the then pen completely perpendicular to the tablet and that the sun is showing directly down on the tablet.

If the tablet is completely perpendicular, the shadow is a perfect circle that centered where the tip of the pen touches the tablet.

<div align="left">

<figure><img src="../../.gitbook/assets/image (347).png" alt="" width="188"><figcaption><p>A pen perfectly perpendicular to the tablet - no tilt.</p></figcaption></figure>

</div>

<div align="left">

<figure><img src="../../.gitbook/assets/image (72).png" alt="" width="188"><figcaption><p>pen not perfectly perpendicular to tablet as indicated by shadow. Diagram shows x&#x26;y components of tilt.</p></figcaption></figure>

</div>

Now keep left the top of the pen "fall" a bit. The shadow looks quite different. It begins at the tip and ends at the other side of the pen. it clearly is not a circle. What you are seeing is the tilt of the pen. Notice that the tilt has two components:

* a tilt in the y direction&#x20;
* a tilt in the x direction.

## Which tablets support tilt

For many years now tilt has been a common feature on drawing tablets. And today the vast majority of tablets support tilt.

However, Wacom seems has traditionally included tilt only on its professional models. In particular tilt is NOT supported in these entry-level Wacom tablets:&#x20;

* One by Wacom Small (CTL-472)
* One by Wacom Medium (CTL-672)
* Wacom Intuos Medium (CTL-6100 & CTL-6100WL)
* Wacom Intuos Small (CTL-4100 &  CTL-6100WL)

## Do need tilt support in your drawing tablet?

The vast majority of drawing tablets have tilt support, but a few entry-level Wacom ones do not.

For some people tilt is critical and for others, it is not useful at all. It strongly depends on what they are doing.

* whiteboarding -> tilt not  useful
* taking notes -> tilt not useful
* educational videos -> tilt not useful
* digital painting with natural media brushes -> can be very useful if you would like your brushes to respond to it.&#x20;
* line art -> can be useful but many people do line art without using any tilt features

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

##

## Tilt support in applications

* Even if your tablet is sending tilt data to your computer, your application may or may not be using the data.
* Some applications don't use the tilt data at all. An example would be most note taking applications like OneNote. They tend to recognize pressure but not tilt.
* Other applications do recognize tilt but the use of the tilt data is only for specific brushes. So for example, typically a "pencil" brush would support tilt. But other kinds of  brushes may not. Even then, these brushes has settings that let you customize whether and how tilt is used for the brush.
* Here's a good example for a brush in Krita. You can seee that the Rotation of the brush is set to the Drawing Angle, but that it could also be set to the tilt.
* ![](<../../.gitbook/assets/image (88).png>)

## Tilt affect on pen tracking accuracy (tilt compensation)

To calculate the location of the pen, the tablet must take into account how much the pen is tilted. This process is called **tilt compensation**. Remember: no tablet has perfect tilt compensation and at extreme title angles you might see some deviation - This is normal.

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

## Disabling tilt

You may not always want to have tilt affect your drawing. It is possible in some cases to disable it. More here: [**Disable pen tilt**](disable-pen-tilt.md)&#x20;

