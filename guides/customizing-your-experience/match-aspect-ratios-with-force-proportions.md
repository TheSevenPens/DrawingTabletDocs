# Match aspect ratios with Force Proportions

Introduction

If the aspect ratio of your pen tablet's active area does not match your monitor's aspect ratio. You will see distortion. For example, if you trace out a circle on the pen tablet, you will have traced out an oval on the screen. This distortion events every movement of your pen on the tablet. Drawing this way feels VERY WEIRD and messes with your mind.  **Don't worry!** You can **EASILY** correct this with FORCE PROPORTIONS.&#x20;

**Force Proportions** what Wacom calls it in their tablet driver, but other tablet brands use different names. I'll use Wacom's name for it in this document. And this document will show you how to fix it for many tablet brands.

<div align="left"><figure><img src="../../.gitbook/assets/Slide6 (1).JPG" alt="" width="375"><figcaption></figcaption></figure></div>

## **Should everyone use this setting?**

For users of pen tablets: YES. I highly recommend it for for everyone using a pen tablet.

For users of pen displays: NO. It is not needed.

## Pen tablets are prone to this problem

The issue with pen tablets is that the tablet and the display are separate devices. And each device has its own aspect ratio. The odds of the aspect rations matching by chance are very low. For example, as of 2025 most pen tablets do not have a 16x9 aspect ratio even though most displays do have a 16x9 aspect ratio.

<div align="left"><figure><img src="../../.gitbook/assets/Slide4.JPG" alt="" width="375"><figcaption></figcaption></figure></div>

If the aspect ratios match, then there is no distortion when you draw.

<div align="left"><figure><img src="../../.gitbook/assets/Slide5.JPG" alt="" width="375"><figcaption></figcaption></figure></div>

## The distortion can be significant without Force Proportions

Here are some examples of what happens some Wacom pen tablets because of the mismatched aspect ratios when using a 16:9 monitor. The black circle is what I draw on the tablet. The red circle is what actual got drawn on the monitor.

<div align="left"><figure><img src="../../.gitbook/assets/Slide10.JPG" alt="" width="375"><figcaption></figcaption></figure></div>

## How Force Proportions work

FP restricts the region of the active area that matches to that of your monitor - so the aspect ratios will match.

## Trading-off Active area versus accuracy

If you enable FP, you will not be able to take advantage of some of your tablet's full native active area, but BY FAR this is the better alternative than the distorted drawing.

## Active area is loss with Force Proportions

It varies depending on the specific aspect ratio of tablet and monitor. The more mismatched they are the bigger the loss. For the Wacom Intuos Pro 2017 series with FP on 16:9 monitors the loss can be between 10% to 20%.&#x20;

Note that if the active areas of the tablet and monitor are the same, then enabling FP does not incur any loss.



<figure><img src="../../.gitbook/assets/image (581).png" alt="" width="375"><figcaption></figcaption></figure>

## Instructions&#x20;

### Wacom > Wacom tablet properties

* Launch **Wacom Tablet Properties**
* Under the **Mapping** tab, enable **Force Proportions**&#x20;

### Wacom > Wacom Center&#x20;

* Launch **Wacom Center**
* Click **Mapping**
* Enable **Force Proportions**

### Huion

Huion calls it **Screen Ratio**.

* Launch the **HuionTablet App**
* Go to **Working Area**&#x20;
* On the bottom left there is a drop down.&#x20;
* Switch the dropdown to **Screen Ratio**.

### Gaomon

Gaomon calls **Screen Ratio**.

* Open the Gaomon driver app
* Go to **Workspace**
* Select **Screen Ratio**

### XP-Pen PenTablet app

XP-Pen calls it **Proportion**

* Open the XP-Pen driver app (called **PenTablet**)
* Go to **Work Area**
* Go to **Pen Tablet**
* Select **Proportion**

### Xencelabs app

Xencelabs calls it Screen Ratio

* Open the Xencelabs driver app
* Go to **Device Settings**
* Look in **Tablet to Screen Area Mapping**
* There's a drop down on the left side. It has three options: **Full Tablet Area**, **Define Portion**, and **Screen Ratio**
* Select **Screen Ratio** in the bottom&#x20;



### Companion Video

This video goes into great detail about this topic.&#x20;

{% embed url="https://youtu.be/9oAvsJk5ESU" %}
