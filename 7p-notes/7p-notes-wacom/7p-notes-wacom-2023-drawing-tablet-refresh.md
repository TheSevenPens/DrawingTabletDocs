# 7P notes: Wacom 2023 drawing tablet refresh

Last updated: 10/8/2023 8:10PM PST

On Aug 10 2023, Wacom started rolling out new consumer drawing tablets. These are my notes on what I am learning about the tablets. My goal is to make it easier to understand how these new products relate to what is in market today.

I'll keep updating as a learn more.

Send feedback to @thesevenpens on twitter.

## 4 new consumer drawing tablets announced

* Wacom One 13 touch (DTH-134) a pen display
* Wacom One 12 (DTC-121) a pen display
* Wacom One S (CTC-4110WL) a pen tablet
* Wacom One M (CTC-6110WL) a pen tablet

On Wacom's website you may see some other things that look like model numbers

* DTCW2AB -> seems to be a series identifier referring to the new pen displays (DTH-134, DTC-121)
* CTCW1AB -> seems to be a series identifier referring to the new pen tablets (CTC-4110WL, CTC-6110WL)

## Understanding product evolution

This diagram is my summary how their consumer line of tablets is evolving

<div align="left">

<figure><img src="../../.gitbook/assets/image (346).png" alt=""><figcaption></figcaption></figure>

</div>

## Branding

* "Wacom One" now includes both pen displays and pen tablets
* The successors to the Wacom Intuos pen tablets (CTL-4100\*, CTL-6100\*) are: the Wacom One (Gen2) pen tablets (CTC-4110WL, CTC-6110WL).
* **My speculation:** Wacom looks to stop using the "Wacom Intuos" brand starting now.

## Disambiguating models

To disambiguate the discussion the tablets:

* I will refer to this new series launched in 2023 as "Wacom One (Gen 2)" even though Wacom is just calling it "Wacom One"
* I will refer the the old series as "Wacom One (Gen 1)" because this is what Wacom is calling it. Though sometimes it is referred to as "Wacom One 2019 (Gen 1)"

## Fate of the One by Wacom series

* The One by Wacom series ...
  * Existing models: CTL-472, CTL-672
* Wacom announced nothing about this series. They have communicated nothing about its status.
* We do not know if are going to be any updates to this series

## Purchase advice

* **Purchase advice:** Because there are many similarly named tables: <mark style="color:red;">**ALWAYS LOOKING AT THE MODEL NUMBERS**</mark> if you are going to make a purchase

## Intuos Pro

* No mention made of the Intuos Pro series.&#x20;

## **Wireless support for pen tablets**&#x20;

The Wacom One (Gen 2) pen tablets all support wireless as indicated by their model numbers that include the "WL" code.&#x20;

## **Pen**

### **The new Wacom One Pen: (**CP92303B2Z)

<figure><img src="../../.gitbook/assets/Screenshot 2023-08-10 133804.jpg" alt=""><figcaption></figcaption></figure>

This is the Wacom One Pen for the Wacom One (Gen 2) tablets. Wacom also shows this on their site as the "Wacom One Standard Pen".

I will refer to this pen as the "Wacom One Pen (Gen 2)"

### The Old Wacom One Pen (CP91300B2Z)

Notice that the model numbers can look very similar. Here are the highlited differences in the model numbers.

* New pen: CP9<mark style="color:red;">**2303**</mark>B2Z
* Old pen: CP9<mark style="color:red;">**1300**</mark>B2Z

<figure><img src="../../.gitbook/assets/Screenshot 2023-08-20 204732.jpg" alt=""><figcaption></figcaption></figure>

### **Pen support**

* All the Wacom One (Gen 2) tablets are compatible with the new pen.&#x20;
* This is good. It eliminates a huge source of confusion around pen compatibility.

### **Pen evolution**

* One by Wacom (CTL-472, CTL-672) -> Wacom Pen 2K (LP-190K)
* Intuos (CTL-4100\*, CTL-6100\*) -> Wacom Pen 4K (LP-1100K)&#x20;
* Wacom One (Gen 1) -> CP91300B2Z
* Wacom One (Gen 2) -> CP92303B2Z

NOTE: If you own an existing Wacom One (Gen 1) pen display. It is unknown if the it;s pen (CP91300B2Z) will be compatible with the Wacom One (Gen 1) pen displays

### **Pressure levels**

* One by Wacom (CTL-472, CTL-672) -> 2048
* Intuos (CTL-4100\*, CTL-6100\*) -> 4096
* Wacom One (Gen 1) -> 4096
* Wacom One (Gen 2) -> 4096

So no improvements to pen pressure levels. As a reminder, all you really need are 2048 pressure levels and it is the pressure range that is more important.

### **Pressure range**

No information available on IAF or max pressure.

### <mark style="color:red;">Issue with pressure range</mark>

I have discovered an issue with the lower end of pressure range with the new pen.

The new pen seems to have a very high IAF.&#x20;

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

I also tested both pens using the CTC-6110WL using OpenTabletDriver. Here are my observations:

* NOTE: Pressure in both pens is reported in two bytes. So there is a MSB and LSB
* With the OLD Wacom One pen - when there is pressure the MSB range starts from 01
* With the NEW Wacom One pen - when there is pressure the MSB range starts from 04 (occasionally I will see a 03)
* How to translate these numbers. &#x20;

### **Number of pen buttons**

* New pen (CP92303B2Z) -> 2 buttons
* Old pen (CP91300B2Z) -> 1 button

## **Pen display connectivity**

The Wacom (Gen 1) can only be connected with a 3-in-1 cable.&#x20;

The Wacom One (Gen 2) pen displays can be connected three ways

* With a 3-in-1 cable
* With a single USB-C cable
* With two USB-C cables. One for display. One for power. Not all computers supply enough power over a USB-C connection to power a display. So this makes sense to provide the option. Most other pen displays work this way.

## **Pen display > parallax**

Wacom estore says there is "no parallax"

![](<../../.gitbook/assets/image (341).png>)

This is a physical impossibility in a pen display that has a piece of glass over the display panel. I demonstrated this clearly in my video on pen display accuracy: [https://youtu.be/M4rEk\_RNBrM](https://youtu.be/M4rEk\_RNBrM)&#x20;

That being said the Wacom One (Gen 1) did not have much parallax. You can see photos of it here: [parallax](../../guides/pen-displays/parallax.md)&#x20;

So, I expect the low parallax story will continue for the Wacom One (Gen 2).

## **Tablet Buttons**



Curious the Wacom One (Gen 2) pen tablets no longer have buttons on the tablets. Even though their predecessors - CTL-4100 and CTL6100 - did have buttons.&#x20;

This is a disappointment. I am concerned that tablet buttons are going to be limited to their Intuos Pro line going forward.

## Pen display > OSD

<div align="left">

<figure><img src="../../.gitbook/assets/Screenshot 2023-08-10 184306.jpg" alt="" width="358"><figcaption></figcaption></figure>

</div>

Picture above from this video: ([https://youtu.be/-vwMZf1nbVU](https://youtu.be/-vwMZf1nbVU))&#x20;

## Pen displays > display panel

* Native resolution: HD (2K): 1920x1080
* Refresh rate: 60Hz&#x20;
* The new display panels have a wider color gamut. They are clearly better than the old Wacom One Gen 1 tablet.&#x20;

## Pen tablets > USB port

* The predecessor Intuos pen tablets used a micro USB slot
* The Wacom One (Gen 2) pen tablets now use a more common USB-C port

## Legs

The new Wacom One (Gen 2) pen displays do not have any legs. They lay flat on the desk.

The old Wacom One (Gen 1) pen display has legs on the back. You can lay the display flat on the desk or you can pull out the legs and draw at and angle.

## User manuals

* Wacom One 13 touch - [https://101.wacom.com/userhelp/en/toc/dth134.html](https://101.wacom.com/userhelp/en/toc/dth134.html) &#x20;
* Wacom One 12 - [https://101.wacom.com/userhelp/en/toc/dtc121.html](https://101.wacom.com/userhelp/en/toc/dtc121.html)&#x20;
* Wacom One S - [https://101.wacom.com/userhelp/en/toc/ctc4110wl.html](https://101.wacom.com/userhelp/en/toc/ctc4110wl.html)&#x20;
* Wacom One M - [https://101.wacom.com/userhelp/en/toc/ctc6110wl.html](https://101.wacom.com/userhelp/en/toc/ctc6110wl.html)

## Wacom videos Wacom One (Gen 2)

There are many videos on Wacom's youtube channel ([https://www.youtube.com/@wacom](https://www.youtube.com/@wacom)) showing various aspects of the Wacom One (Gen 2) series. Here are few select ones:&#x20;

* Wacom One product trailer ([https://youtu.be/3iyeURJRRNs](https://youtu.be/3iyeURJRRNs)) Aug 8 2023
* Wacom Center for Android ([https://youtu.be/sf8r\_zxLl7o](https://youtu.be/sf8r\_zxLl7o)) Aug 8 2023
* Multi-touch on Wacom One 13 touch ([https://youtu.be/u4kK5M\_SxyM](https://youtu.be/u4kK5M\_SxyM)) Aug 9 2023
* On-Screen Display Button (OSD) ([https://youtu.be/-vwMZf1nbVU](https://youtu.be/-vwMZf1nbVU)) Aug 10, 2023

## Legs

The old Wacom One (Gen 1) pen display had foldable legs.

The new model does not.

Instead you must a separate stand.

Wacom is offering a very unique design for their stand.

<figure><img src="../../.gitbook/assets/Screenshot 2023-08-10 201447.jpg" alt=""><figcaption></figcaption></figure>

## VESA mounting

Neither the Wacom One (Gen 1) or the Wacom One (Gen 2) pen displays are vesa mountable.

## Reviews

* Tom's Guide - Wacom One 13 touch hands-on review - [https://www.tomsguide.com/reviews/wacom-one-13-touch](https://www.tomsguide.com/reviews/wacom-one-13-touch)&#x20;

