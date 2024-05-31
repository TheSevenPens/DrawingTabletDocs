# Pen tilt

## Introduction

Almost all drawing tablets can detect the tilt of the pen. The support tilt for drawing tablets usually ranges from 0 degrees to 60 degrees.

<figure><img src="../../.gitbook/assets/Slide_20240506_184008 (1).png" alt="" width="563"><figcaption></figcaption></figure>



The tilt is measured in both the x and y directions

<div align="left">

<figure><img src="../../.gitbook/assets/image (72).png" alt="" width="188"><figcaption><p>pen not perfectly perpendicular to tablet as indicated by shadow. Diagram shows x&#x26;y components of tilt.</p></figcaption></figure>

</div>

## How tilt is used in drawing applications

Think about how you use a pencil - when you want a fine line you keep the pencil more penpendicular. However, when you want a wider line - maybe you are shading in an area - you tilt the pencil.

Many drawing applications have digital brushes that mimic that same behavior.

For example, here is a stroke I drew with Krita. I configured the brush to ignore pressure entirely, but to let the amount of tilt control the width of the brush.

As draw left to right I started with the pen very perpendicular and gradually started tilting the pen.&#x20;

<figure><img src="../../.gitbook/assets/tilt demo.png" alt=""><figcaption></figcaption></figure>

Mapping tilt to brush width is just the most common way of using tilt. However, depending on the application you could have tilt control other attributes of the stroke.

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

## Technical details

You don't need to know these details, but if you are curious how an EMR tablet actually detects the tilt of the pen go here: [**EMR tilt detection**](../digital-pen-tech/emr/emr-tilt-detection.md).

## **Tilt angle range**

* The standard range is +/- 60 degrees for both X and Y directions
* I don't know of any tablets that support a wider range

## Tilt support in applications

* Even if your tablet is sending tilt data to your computer, your application may or may not be using the data.
* Some applications don't use the tilt data at all. An example would be most note taking applications like OneNote. They tend to recognize pressure but not tilt.
* Other applications do recognize tilt but the use of the tilt data is only for specific brushes. So for example, typically a "pencil" brush would support tilt. But other kinds of  brushes may not. Even then, these brushes has settings that let you customize whether and how tilt is used for the brush.
* Here's a good example for a brush in Krita. You can seee that the Rotation of the brush is set to the Drawing Angle, but that it could also be set to the tilt.
* ![](<../../.gitbook/assets/image (88).png>)

## Tilt affect on pen tracking accuracy (tilt compensation)

To calculate the location of the pen, the tablet must take into account how much the pen is tilted. This process is called **tilt compensation**. Remember: no tablet has perfect tilt compensation and at extreme title angles you might see some deviation - This is normal.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Disabling tilt

You may not always want to have tilt affect your drawing. It is possible in some cases to disable it. More here: [**Disable pen tilt**](disable-pen-tilt.md)&#x20;

