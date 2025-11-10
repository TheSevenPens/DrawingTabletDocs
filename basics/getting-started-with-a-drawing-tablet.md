# Getting started with a drawing tablet

## Overview

If you just acquired a drawing tablet and want to start using it, this guide will lead you through the basics.&#x20;

{% hint style="info" %}
* If you are new to drawing tablets, first read [**the beginner's guide**](beginners-guide.md)&#x20;
* If you don't have a drawing tablet: [**buying guide**](../buying-a-drawing-tablet/)&#x20;
{% endhint %}

## Find out the tablet's model number

* Make sure you know the model number of the tablet. This will help you in many ways later. More here: [**Finding the model number of a drawing tablet**](../guides/general/finding-the-model-number-of-a-drawing-tablet.md).&#x20;

## Identify how to contact support

* The vast majority of time everything "just works" but you may need help or a question answered by customer support. So, Make sure you know how to [**contact support**](contacting-support.md) for your tablet manufacturer&#x20;

## Read the user manual

* Most questions you have will be answered already in the user manual.&#x20;
* You will spare yourself a lot of frustration if you read it first.
* You don't need to even open the box. You can download the manual from the manufacturer website.
* The most important thing to understand in the user manual is how the tablet physically connects to your computer. This is especially important if you have a pen display (screen tablet).

## Don't drop the pen

* If drop the pen to the floor, usually it will be unharmed.
* When you are not using it make sure its stored in such a way it doesn't fall off your desk.
* HOWEVER, sometimes a pen seems to hit just right and the fall can damage the pen.&#x20;

## Keep the box safe

* You may need to return or transport the tablet, the original box is the best way of doing thus.

## Verify the box contains what it should

The box will usually list everything that is supposed to be inside it. If you can't see it there look for it in the user manual, or the manufacturer website.

Then verify that box contains everything that is expected.

99.9999% if of the time it will have everything is supposed to have. But every now and then you might encounter a box that is missing a cable.

&#x20;

## Prepare for replacing your pen

The pen has somewhat delicate parts inside and is the most likely thing you will break. If you lose or damage your pen, there are some things you need to know:

* First drawing tablets are generally only compatible with the pen they came with or a small number of pens. So note down the model number of the pen. You will need this to get a replacement. More here: [**Pen compatibility with drawing tablets**](../guides/pens/pen-compatibility-with-drawing-tablets.md)
* Pens are surprisingly expensive to replace.
  * Some pens cost half the cost of the tablet
  * Some pens (especially Wacom Pro pens) are more expensive than the tablets of other brands.

## Install the tablet driver

* You need the tablet driver installed for the tablet to work correctly.
* You can go to the manufacturer site and download the driver and install now before your tablet even arrives.&#x20;
* If the tablet driver is installed, when you connect the tablet with USB cable the driver will just detect the tablet and the pen will work as soon as it comes close to the tablet (about 10mm)
* The drivers install an app you can use to configure the driver. The apps have different names depending on your tablet brand
* More here: [**drivers**](../guides/drivers/)

## Connect the tablet

* Pen tablet - There will be a simple USB cord. These days the cords are all USB-C cords.
  * Some pen tablets ALSO support wireless connection. For now ignore wireless. It just adds more complication. Get it working with a cable first. Once everything is working, then try wireless.
* Pen display - There are several options. See [**connecting a pen display**](../guides/connections-and-cabling/connecting-a-pen-display.md)

## Finding the Driver UI

At some point you'll need to find the driver again after you have installed it. You MUST be familiar with how to do this. Here are the instructions: [**Finding the driver settings UI**](../guides/drivers/finding-the-driver-settings-ui.md).

## The NO SIGNAL problem with pen displays

If you encounter a "NO SIGNAL" message, follow these troubleshooting steps: [**Troubleshoot the NO SIGNAL problem**](../troubleshooting/tsg-no-signal.md)

## How the pen & tablet work with the computer

* Once the tablet driver is installed and the tablet is connected it will detect the pen. It will treat the pen just like a mouse. (except a mouse uses relative positioning and the pen uses absolute positioning. more here: [**Absolute versus relative positioning**](../core-features/absolute-versus-relative-positioning.md))
* If the pen is in range (about 10mm) of the tablet or touching the tablet , then moving the pen will move the mouse pointer.
  * If the pen is not touching the tablet, it will be like your are not pressing down any mouse buttons
  * if the pen is touching the tablet, it will be like you are holding down the left mouse button
* In drawing apps which are pen aware can take advantage of other features like pressure and tilt.
* If you are using a drawing program, You don't need to hold down any button for it to draw, just put touch the pen to the tablet.

## Learn what the active area is (aka "Working Area")

* The active area on the tablet is the region of the tablet that is sensitive to the pen.&#x20;
  * Wacom calls this the "Active Area" in their docs. In their driver, it is called "Mapping"&#x20;
  * Huion calls this the "Working Area"
  * I will always call it the "active area" because that is the oldest term for it.
* Go into the driver and and find the active area and get familiar with what it looks like. It's one of the most common things you'll need to adjust.
* More here: [**Active Area**](../core-features/active-area.md)

## Pen tablets: map the Active Area to a single display&#x20;

* This step is needed for pen tablets (the ones without a screen)
* The active area can be mapped to one of your displays or multiple displays.
* By default, they are often mapped to multiple displays.&#x20;
* For now, map the active area to a single display.
* If you want to use both displays, later on you can configure a "display toggle" feature that lets you switch between displays by pressing a button on the pen or the tablet.

## Pen displays: map the Active Area to your pen tablet if needed

* With a pen tablet, the active area should be mapped to the screen of your tablet.
* Sometimes however, drivers get confused and they initially map the active area to some other display that your have. When this happens you will move the pen on your tablet but you'll see the mouse pointer move on a different display.&#x20;
* This is VERY easy to solve:   [**Troubleshoot pen moving pointer on the wrong display** ](../troubleshooting/tsg-pen-moving-pointer-on-the-wrong-display.md)

## Pen tablets: Enable Force Proportions to match aspect ratios between the active area and your display

* <mark style="color:red;">**This step is very important for pen tablets**</mark> (the ones without a screen). You don't have to do this for pen displays.&#x20;
* If you don't do this there will be a distortion as you draw - in other words tracing out a perfect circle on the tablet will draw an oval on the screen.
* Explanation and instructions here: [**Matching aspect ratios with Force Proportions**](../guides/customizing-your-experience/match-aspect-ratios-with-force-proportions.md).&#x20;

## Adjust the pressure curve to give you more control

Drawing tablet pens are "over-sensitive" at low physical pressure. Near the initial activation force the pressure can swing wildly. If you are using pressure to control for example the width of your strokes, then the width can vary more than you expect. This is especially obvious as you are doing linework and you brushes start getting larger (>50px).

This over-sensitivity is common to pens, and not unusual. Some people may not even notice. But if you do, you can use pressure curves to reduce the over sensitivity.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

## Mapping buttons dials and sliders

If you tablet has additional inputs such as buttons, dials, etc. You can control what they do. Even assign them to do different things per application.

Here are some popular assignments: [Popular bindings for auxiliary inputs](../core-features/popular-bindings-for-auxiliary-inputs.md)

## Windows&#x20;

Perform this configuration: [**Disable the press-and-hold ring in Windows**](../guides/operating-systems/windows/disable-the-press-and-hold-ring-in-windows.md)&#x20;

## Apps

* **Krita -** I highly recommend you Install [**Krita**](../app-links/krita/). It is a FREE and good drawing app. Eve if you are not going to draw anything, it is useful for testing and troubleshooting.
* **Kleki -** [**Kleki**](../app-links/kleki.md) is a FREE web-based app that is very simple. It's ideal I think for something for kids to start with before they try something complicated like Krita.
* **Clip Studio Paint -** I draw a lot of illustrations so I pay for a subscription to [**Clip Studio Paint**](../app-links/clip-studio-paint/).
* **Photopea** ([https://www.photopea.com/](https://www.photopea.com/)) is a web-based Photoshop-like app. It is very good and also has a free tier.
* [**Procreate**](../app-links/procreate/) - this is THE drawing app to get if you are drawing on an iPad.
* [**Infinite Painter**](../app-links/infinite-painter.md) - this is the equivalent of Procreate, but for Android devices.
* **Other applications -** Look here to find a large number of applications to explore: [**applications**](../apps/)&#x20;

&#x20;





&#x20;&#x20;

&#x20;

## &#x20;

