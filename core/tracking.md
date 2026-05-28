# Tracking

## Introduction

**Pen tracking** is the tablet's interpretation of the physical position of the pen.

**Pen tracking accuracy** is how close the operating system cursor, or mouse pointer, is to the physical tip of the pen.

* This accuracy must be measured without taking parallax into account.
* It must also be measured when the pen is **not** moving, because pointer lag causes a kind of dynamic inaccuracy.

### Real-world accuracy

Perfectly accurate pen tracking means the tablet thinks the pen is exactly where the physical tip is. Any deviation from that is an inaccuracy. **All tablets are slightly inaccurate**.

### Accuracy in pen tablets vs pen displays

Pen tracking accuracy is a concept that applies to both pen tablets and pen displays. However, in practice it is only really an issue with pen displays. This is because with pen displays you can see the inaccuracy - which shows up as the operating system pointer being offset from the tip of the pen.

## Pen tracking calibration

If your pen position does not match the pointer in a major way, especially across most of the tablet, then [Calibrate pen position](../guides/customizing/calibrate-pen-position.md) may help.

## Video: Accuracy in pen displays

{% embed url="https://youtu.be/M4rEk_RNBrM" %}

## Edge and corner accuracy in pen displays

The pointer is generally a bit more offset from the pen tip near the edges, and especially the corners, than in the main part of the screen.

This offset in the edges and corners is totally normal. Some tablets have more and some have less.

Tablet manufacturers, except Wacom, often publish official corner accuracy numbers. Here are some typical values I have seen.

* ±3mm
* ±1.5mm
* ±1mm

If you have a pen display and the inaccuracy seems worse than the manufacturer's spec, and it bothers you, contact support.

For me, even ±3 mm is usually not a real problem because I am not drawing in those areas. But it does look weird, and I would always prefer ±1 mm.
