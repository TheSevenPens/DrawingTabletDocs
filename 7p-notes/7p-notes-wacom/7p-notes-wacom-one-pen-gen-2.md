# 7P notes: Wacom One Pen (Gen 2) (CP92303B2Z)

<mark style="color:red;">**PLEASE READ THIS INFORMATION ABOUT THE NEW GEN 2 PEN. I AM CURRENTLY INVESTIGATING AN ISSUE WITH IT. I RECOMMEND YOU DON'T GET THE NEW PEN UNTIL MY INVESTGATION HAS CONCLUDED.**</mark>

## Overview

### \*\*The new Wacom One Pen: (\*\*CP92303B2Z)

<figure><img src="../../.gitbook/assets/Screenshot 2023-08-10 133804.jpg" alt=""><figcaption></figcaption></figure>

This is the Wacom One Pen for the Wacom One (Gen 2) tablets. Wacom also shows this on their site as the "Wacom One Standard Pen".

I will refer to this pen as the "Wacom One Pen (Gen 2)"

### The Old Wacom One Pen (CP91300B2Z)

Notice that the model numbers can look very similar. Here are the highlighted differences in the model numbers.

* New pen: CP9<mark style="color:red;">**2303**</mark>B2Z
* Old pen: CP9<mark style="color:red;">**1300**</mark>B2Z

<figure><img src="../../.gitbook/assets/Screenshot 2023-08-20 204732.jpg" alt=""><figcaption></figcaption></figure>

### **Pen support**

* All the Wacom One (Gen 2) tablets are compatible with the new Wacom One Pen (Gen 2).
* This is good. It eliminates a huge source of confusion around pen compatibility.

### **Pen evolution**

* One by Wacom (CTL-472, CTL-672) -> Wacom Pen 2K (LP-190K)
* Intuos (CTL-4100\*, CTL-6100\*) -> Wacom Pen 4K (LP-1100K)
* Wacom One Pen (Gen 1) -> CP91300B2Z
* Wacom One Pen (Gen 2) -> CP92303B2Z

### **Pressure levels**

* One by Wacom (CTL-472, CTL-672) -> 2048
* Intuos (CTL-4100\*, CTL-6100\*) -> 4096
* Wacom One (Gen 1) -> 4096
* Wacom One (Gen 2) -> 4096

So no improvements to pen pressure levels. As a reminder, all you really need are 2048 pressure levels and it is the pressure range that is more important.

### **Number of pen buttons**

* New pen (CP92303B2Z) -> 2 buttons
* Old pen (CP91300B2Z) -> 1 button

### **Tilt**

* New pen (CP92303B2Z) -> supports tilt
* Old pen (CP91300B2Z) -> does not support tilt

## Compatibility

### Backwards compatibility

* New pen (CP92303B2Z) -> **Does not work** with Wacom One (Gen 1) (DTC-133) tablet

### Forwards compatibility

* Old pen (CP91300B2Z) -> Does work with new new Wacom One (Gen 2) tablets

### Samsung Galaxy S compatibility

* I confirmed both pens work with the Samsung Galaxy S8 Ultra.
* I confirmed that the Samsung S Pen works with both the Wacom One (Gen 1) tablet and the Wacom One (Gen 2) tablets

## <mark style="color:red;">**Pressure range \[UNDER INVESTIGATION]**</mark>

### <mark style="color:red;">Problem with pressure range</mark>

The problem:

* The new Wacom One Pen (Gen 2) has a MUCH higher Initial Activation Force than the Wacom One Pen (Gen 2)
* As a result the new Gen 2 pen has a noticeably smaller effective pressure range than the Gen 1 pen

### Effect of the pressure problem

Summary: Even the lightest physical pressure you put on the pen will cause a higher pressure to be reported to the computer. This will interfere with your drawing.

Look at the effects in the Wacom Center's pressure test area below.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Location of the problem

The issue is the pen hardware.

* It does not have to do with the tablet driver
* It does not have to do with the tablet hardware

## Explanation of the problem

EMR pens sense pressure and report that pressure to the tablet which then passes it on to the computer.

To make it easy to explain let's simplify the problem. Pretend there are only 10 pressure levels that go from 0 to 9. 0 means no pressure. 9 means max pressure.

Keep two things in mind:

* (a) What the pen is physically capable of detecting.
* (b) What the pen reports to the tablet.

Essentially the new pen simply does not report the lower pressure values to the tablet.

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

This can be observed in the pressure test region of the Wacom Center app. The blue bar at the bottom of the test area shows the current pressure. With the old pen I can keep the blue bar very small by applying light pressure. With the new pen no matter how little pressure I apply the blue bar won't get any smaller.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

### Testing scenarios

I have confirmed this issue in these cases

* With these tablets:
  * DTC-121
  * CTC-6110WL
* On three 3 different machines
* Using
  * Wacom driver
  * OpenTablet driver
* With these applications
  * Krita
  * Clip Studio Paint
* With these Wacom tablets
  * Wacom One 13 touch (DTH-134) a pen display
  * Wacom One M (CTC-6110WL) a pen tablet
* And I have had one other person (Kuuube) confirm the same behavior with the Wacom One S (CTC-4110WL)

## Workarounds

While you cannot change how the pen works. You
