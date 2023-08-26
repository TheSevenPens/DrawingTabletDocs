# 7p notes: Wacom One Pen (Gen 2)

<mark style="color:red;">**PLEASE READ THIS INFORMATION ABOUT THE NEW GEN 2 PEN. I AM CURRENTLY INVESTIGATING AN ISSUE WITH IT. I RECOMMEND YOU DON'T GET THE NEW PEN UNTIL MY INVESTGATION HAS CONCLUDED.**</mark>

## Overview

### **The new Wacom One Pen: (**CP92303B2Z)

<figure><img src="../../.gitbook/assets/Screenshot 2023-08-10 133804.jpg" alt=""><figcaption></figcaption></figure>

This is the Wacom One Pen for the Wacom One (Gen 2) tablets. Wacom also shows this on their site as the "Wacom One Standard Pen".

I will refer to this pen as the "Wacom One Pen (Gen 2)"

### The Old Wacom One Pen (CP91300B2Z)

Notice that the model numbers can look very similar. Here are the highlighted differences in the model numbers.

* New pen: CP9<mark style="color:red;">**2303**</mark>B2Z
* Old pen: CP9<mark style="color:red;">**1300**</mark>B2Z

<figure><img src="../../.gitbook/assets/Screenshot 2023-08-20 204732.jpg" alt=""><figcaption></figcaption></figure>

### **Pen support**

* All the Wacom One (Gen 2) tablets are compatible with the new Wacom One Pen (Gen 2).&#x20;
* This is good. It eliminates a huge source of confusion around pen compatibility.

### **Pen evolution**

* One by Wacom (CTL-472, CTL-672) -> Wacom Pen 2K (LP-190K)
* Intuos (CTL-4100\*, CTL-6100\*) -> Wacom Pen 4K (LP-1100K)&#x20;
* Wacom One Pen (Gen 1) -> CP91300B2Z
* Wacom One Pen (Gen 2) -> CP92303B2Z

NOTE: If you own an existing Wacom One (Gen 1) pen display. It is unknown if the it;s pen (CP91300B2Z) will be compatible with the Wacom One (Gen 1) pen displays

### **Pressure levels**

* One by Wacom (CTL-472, CTL-672) -> 2048
* Intuos (CTL-4100\*, CTL-6100\*) -> 4096
* Wacom One (Gen 1) -> 4096
* Wacom One (Gen 2) -> 4096

So no improvements to pen pressure levels. As a reminder, all you really need are 2048 pressure levels and it is the pressure range that is more important.

## **Pressure range**

### <mark style="color:red;">Issue with pressure range</mark>

The problem manifests as: The new Wacom One Pen (Gen 2) has a MUCH higher Initial Activation Force than the Wacom One Pen (Gen 2) &#x20;

### I have confirmed this issue in these cases

* With these tablets:
  * DTC-121
  * CTC-6110WL
* On three 3 different machines
* Using
  * Wacom driver&#x20;
  * OpenTablet driver
* Wioth these applications
  * Krita
  * Clip Studio Paint&#x20;
* With these Wacom tablets
  * Wacom One 13 touch (DTH-134) a pen display
  * Wacom One M (CTC-6110WL) a pen tablet
* And I have have one other person (Kuuube) confirm the same behavior with the CTC-6110WL

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



I also tested both pens using the CTC-6110WL using OpenTabletDriver. Here are my observations:

* NOTE: Pressure in both pens is reported in two bytes. So there is a MSB and LSB
* With the OLD Wacom One pen - when there is pressure the MSB range starts from 01
* With the NEW Wacom One pen - when there is pressure the MSB range starts from 04 (occasionally I will see a 03)
* How to translate these numbers. &#x20;

### **Number of pen buttons**

* New pen (CP92303B2Z) -> 2 buttons
* Old pen (CP91300B2Z) -> 1 button

