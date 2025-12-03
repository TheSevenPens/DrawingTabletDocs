# Disabling pen pressure

## Overview

Pen pressure information is always sent from the tablet to the tablet driver and from there to the operating system and then to pen-aware applications. This pressure information is used to draw strokes by varying the width or opacity and also this pressure information is used to tell the operating system that a "click" or "drag" is happening.

There are several options you can pursue depending on which tablet you have and what you want to accomplish.

## The need for turning of pressure

However, sometimes when drawing it can be useful to turn off pressure. For example:

* Some people want to draw ONLY when they press a button on the pen. This may be because this find it difficult to keep hovering the pen until they are ready to draw.
* Some people use the pen as a mouse replacement and find tapping with the pen difficult to produce a click. They also just want to rely on a pen button to indicate clicks.

## **OPTION 1** Turn off pressure in the tablet driver

**SOME** tablet drivers let you simply turn off pressure so that it isn't reported to your operating system or applications.

### XP-Pen

XP-Pen drivers have this feature.

* Launch the XP Pen driver (called **Pen Tablet**)
* Click on the gear icon
* Then check the **Disable pressure** checkbox.

<div align="left"><figure><img src="../../.gitbook/assets/image (496).png" alt="" width="563"><figcaption></figcaption></figure></div>

### Huion

* Launch the **HuionTablet** app
* Navigate to **Digital Pen > Pressure Sensitivity Adjustment**
* Change the tip setting from **Valid** to **Invalid**
* This should prevent it from clicking and from registering pressure.

### **OPTION 2 Use Brush settings to disable using pressure**

Drawing apps that use brushes may let you control how pressure affects the brush. So, you can configure specific brushes to ignore pressure. Examples of applications that support this are Clip Studio Paint and Krita.

## OPTION 3 Use a flat pressure curve

In some applications you can completely flatten the pressure curve. This allows you to have the pressure report. This means the pressure is constant and will not result in the brush changing due to pressure.

![](<../../.gitbook/assets/image (523).png>)

This will still let you draw, but the pen is not changing pressure.
