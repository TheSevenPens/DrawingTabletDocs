# Getting started with a drawing tablet

## Overview

If you just acquired a drawing tablet and want to start using it, this guide will lead you through the basics.

{% hint style="info" %}
* If you are new to drawing tablets, first read [Beginner's guide to drawing tablets](beginners-guide.md).
* If you do not have a drawing tablet yet, read the [Drawing tablet buying guide](../buying/).
{% endhint %}

## Find the tablet's model number

* Make sure you know the tablet's model number. This will help in many ways later. More here: [Finding the model number of your drawing tablet](../guides/general/finding-tablet-model-number.md).

## Identify how to contact support

* Most of the time, everything just works. But you may still need help from customer support. Make sure you know how to contact support for your tablet manufacturer. More here: [Contacting support](support.md).

## Read the user manual

* Most questions you have are already answered in the user manual.
* You will spare yourself a lot of frustration if you read it first.
* You do not even need to open the box. You can download the manual from the manufacturer's website.
* The most important thing to understand in the user manual is how the tablet physically connects to your computer. This is especially important if you have a pen display (screen tablet).

## Don't drop the pen

* If you drop the pen on the floor, it will usually be unharmed.
* When you are not using it, make sure it is stored so it cannot fall off your desk.
* However, sometimes a pen lands just wrong and the fall damages it.

## Keep the box safe

* You may need to return or transport the tablet. The original box is the best way to do that.

## Verify the box contains what it should

The box usually lists everything that is supposed to be inside it. If you cannot find that list there, check the user manual or the manufacturer's website.

Then verify that the box contains everything expected.

99.9999% of the time, it will contain everything it should. But every now and then, you may get a box with a missing cable.

## Prepare for replacing your pen

The pen has somewhat delicate parts inside and is the most likely thing you will break. If you lose or damage your pen, there are some things you need to know:

* First, drawing tablets are generally compatible only with the pen they came with, or with a small number of pens. Note the pen model number. You will need it to get a replacement. More here: [Pen compatibility](../guides/pens/pen-compatibility.md)
* Pens are surprisingly expensive to replace.
  * Some pens cost half as much as the tablet.
  * Some pens (especially Wacom Pro pens) are more expensive than the tablets of other brands.

## Install the tablet driver

* You need the tablet driver installed for the tablet to work correctly.
* You can go to the manufacturer's website, download the driver, and install it before your tablet arrives.
* If the driver is installed, then when you connect the tablet with a USB cable, the driver will detect it and the pen will work as soon as it comes close to the tablet, at about 10 mm.
* The driver also installs an app you can use to configure the tablet. That app has a different name depending on the brand.
* Why you need to install tablet drivers: [https://www.youtube.com/watch?v=qUsZUcH6SWk](https://www.youtube.com/watch?v=qUsZUcH6SWk)
* More here: [Drivers](../guides/drivers/)

## Connect the tablet

* Pen tablet - There will be a simple USB cable. These days, these cables are usually USB-C.
  * Some pen tablets ALSO support wireless connection. For now, ignore wireless. It adds more complexity. Get it working with a cable first. Once everything is working, try wireless.
* Pen display - There are several options. See [Connecting a pen display](../guides/connecting/connecting-pen-display/)

## Find the driver UI

At some point, you will need to find the driver UI again after installing it. You should know how to do this. Here are the instructions: [Finding the driver settings UI](../guides/drivers/finding-the-driver-settings-ui.md).

## The NO SIGNAL problem with pen displays

If you encounter a "NO SIGNAL" message, follow these troubleshooting steps: [TSG: Pen display shows NO SIGNAL message](../troubleshoot/tsg-no-signal.md)

## How the pen & tablet work with the computer

* Once the tablet driver is installed and the tablet is connected, it will detect the pen. It treats the pen much like a mouse, except a mouse uses relative positioning and the pen uses absolute positioning. More here: [Absolute versus relative positioning](../core/active-area/absolute-versus-relative-positioning.md)
* If the pen is in range, about 10 mm from the tablet, or touching the tablet, moving the pen will move the mouse pointer.
  * If the pen is not touching the tablet, it is like you are not pressing any mouse buttons.
  * If the pen is touching the tablet, it is like you are holding down the left mouse button.
* Pen-aware drawing apps can also use features like pressure and tilt.
* If you are using a drawing program, you do not need to hold down any button to draw. Just touch the pen to the tablet.

## Learn what the active area is, also called the "Working Area"

* The active area is the region of the tablet that responds to the pen.
  * Wacom calls this the "Active Area" in their docs. In their driver, it is called "Mapping."
  * Huion calls this the "Working Area."
  * I will always call it the "active area" because that is the oldest term for it.
* Go into the driver, find the active area setting, and get familiar with it. It is one of the most common things you will need to adjust.
* More here: [Active area](../core/active-area/)

## Pen tablets: map the active area to a single display

* This step is needed for pen tablets, the ones without a screen.
* The active area is mapped to one of your displays or multiple displays.
* By default, they are often mapped to multiple displays.
* My recommendation is:
  * Map the active area to a single display.
  * If you want to use multiple displays with your pen tablet, use the tablet driver's **display toggle** feature. It lets you switch the active area mapping between displays by pressing a button on the pen or tablet. See: [Display toggle](../core/active-area/display-toggle.md)

## Pen tablets: Enable Force Proportions

* <mark style="color:red;">**This step is very important for pen tablets**</mark> (the ones without a screen). You don't have to do this for pen displays.
* If you do not do this, your drawing will be distorted. In other words, tracing a perfect circle on the tablet will produce an oval on the screen.
* Explanation and instructions here: [Matching aspect ratios with Force Proportions](../guides/customizing/force-proportions.md).

## Pen displays: map the active area to your pen display if needed

* With a pen display, the active area should be mapped to its own display.
* However, sometimes tablet drivers get confused. They might initially map the active area to another display you have. When this happens, you move the pen on your tablet but see the pointer move on a different display. This is easy to solve: [TSG: Pointer on wrong display](../troubleshoot/tsg-pointer-on-wrong-display.md)

## Adjust the pressure curve to give you more control

Drawing tablet pens are often over-sensitive at low physical pressure. Near the initial activation force, pressure can swing wildly. If you use pressure to control the width of your strokes, the width may vary more than you expect. This is especially obvious when you are doing linework and your brushes start getting larger, such as above 50 px.

This over-sensitivity is common. Some people may not even notice it. But if you do, you can use pressure curves to reduce it.

<figure><img src="../.gitbook/assets/image-000239.png" alt="" width="375"><figcaption></figcaption></figure>

## Mapping buttons, dials, and sliders

If your tablet has additional inputs such as buttons or dials, you can control what they do. You can even assign different actions per application.

Here are some popular assignments: [Popular bindings for auxiliary inputs](../core/expresskeys/popular-bindings.md)

## Windows

Perform this configuration: [Disable the press-and-hold ring in Windows](../guides/platforms/windows/disable-press-hold-ring.md)

## Apps

* **Krita -** I highly recommend [Krita](../catalog/apps/krita.md). It is a free, good drawing app. Even if you are not going to draw anything yet, it is useful for testing and troubleshooting.
* **Kleki -** [Kleki](../catalog/apps/kleki.md) is a free web-based app that is very simple. It is a good starting point for kids before they try something more complex like Krita.
* **Clip Studio Paint -** I draw a lot of illustrations, so I pay for a subscription to [Clip Studio Paint](../catalog/apps/clip-studio-paint.md).
* **Photopea** ([https://www.photopea.com/](https://www.photopea.com/)) is a web-based Photoshop-like app. It is very good and also has a free tier.
* [Procreate](../catalog/apps/procreate.md) - This is the drawing app to get if you are drawing on an iPad.
* [Infinite Painter](../catalog/apps/infinite-painter.md) - This is the closest equivalent to Procreate on Android devices.
* **Other applications -** Look here for many more apps to explore: [Apps](../apps/)
