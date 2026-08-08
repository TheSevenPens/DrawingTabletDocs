# Pen tilt

## Introduction

Almost all drawing tablets can detect the tilt of the pen. Tilt support for drawing tablets usually ranges from 0 degrees to 60 degrees.

Tilt is described by two angles: tilt elevation and tilt azimuth.

* elevation = "how much the pen leans over"
* azimuth = "the direction of the lean — like north, west, or northwest"

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

This video demonstrates tilt. I highly recommend that you watch it.

{% embed url="https://www.youtube.com/watch?v=O9cMFehZnsI" %}

## How tilt is used in drawing applications

Think about how you use a pencil. When you want a fine line, you keep the pencil more perpendicular. When you want a wider line — perhaps while shading an area — you tilt the pencil.

Many drawing applications have digital brushes that mimic that same behavior.

For example, here is a stroke I drew with Krita. I configured the brush to ignore pressure entirely, but to let the amount of tilt control the width of the brush.

As I drew from left to right, I started with the pen very perpendicular and gradually started tilting the pen.

<figure><img src="../../.gitbook/assets/pen-tilt-3.png" alt=""><figcaption></figcaption></figure>

Mapping tilt to brush width is the most common use of tilt. However, depending on the application, you could use tilt to control other stroke attributes.

## Which tablets support tilt

The vast majority of modern drawing tablets support tilt.

It's easier to list the modern tablets that do not support tilt:

* Wacom One by Wacom Small (CTL-472)
* Wacom One by Wacom Medium (CTL-672)
* Wacom Intuos Medium (CTL-6100 & CTL-6100WL)
* Wacom Intuos Small (CTL-4100 & CTL-4100WL)
* Huion Frego S (L310)

## Do you need tilt support?

The vast majority of drawing tablets have tilt support, but a few entry-level Wacom ones do not.

For some people tilt is critical and for others, it is not useful at all. It strongly depends on what they are doing.

| Scenario                                    | Is tilt useful? | Notes                                                    |
| ------------------------------------------- | --------------- | -------------------------------------------------------- |
| Whiteboarding                               | Not useful      | It's rare for whiteboarding apps to even support tilt.   |
| Taking notes                                | Not useful      | It's rare for note-taking apps to even support tilt.     |
| Educational videos                          | Not useful      |                                                          |
| Digital painting with natural media brushes | Can be useful   | Some artists require it.                                 |
| Line art                                    | Can be useful   | Many people create line art without using tilt features. |

## Technical details

You don't need to know these details. If you are curious about how an EMR tablet detects pen tilt, see [EMR tilt detection](../../tech/emr/emr-tilt-detection.md).

## Tilt angle range

* The standard range is ±60 degrees in both the X and Y directions.
* I don't know of any tablets that support a wider range.

## Tilt support in applications

* Even if your tablet is sending tilt data to your computer, your application may or may not be using the data.
* Some applications don't use tilt data at all. Most note-taking applications, such as OneNote, recognize pressure but not tilt.
* Other applications recognize tilt only for specific brushes. For example, a "pencil" brush typically supports tilt. Other brush types may not. These brushes may also have settings for customizing whether and how they use tilt.
* Here is an example of a brush in Krita. Its Rotation setting uses the Drawing Angle, but it could use tilt instead.
* ![](../../.gitbook/assets/pen-tilt-1.png)

## Tilt effect on pen tracking accuracy (tilt compensation)

To calculate the pen location, the tablet must account for its tilt. This process is called **tilt compensation**. Remember: no tablet has perfect tilt compensation. You might see some deviation at extreme tilt angles. This is normal.

See [tilt compensation](tilt-compensation.md)

## Disabling tilt

You may not always want to have tilt affect your drawing. It is possible in some cases to disable it. More here: [Disabling pen tilt](disable-tilt.md)
