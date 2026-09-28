# Stroke quantization

## Overview

Stroke quantization is when strokes come out looking tightly stair-stepped, as if the pen position were snapping to a coarse grid.

It is easy to confuse with diagonal wobble. They look similar to an untrained eye, but they have different causes and different fixes. The comparison at the bottom of this page shows how to tell them apart.

If you have this problem now, go here: [TSG: Strokes look stair-stepped (quantization)](../troubleshoot/tsg-strokes-stair-stepped.md)

## Appearance

* Strokes look angular and stair-stepped instead of smooth
* The stairs are small and sudden - not smooth and spread out
* It can happen at any angle - though it is more obvious when pens are moving diagonally
* It tends to be more visible as you draw slower. Drawing faster tends to mask the effect visually even though it is still actually happening

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

Notice that it looks different from diagonal wobble - which is smoother, more wave-like, and more spread out over the length of the stroke

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>



## Platform

This is a Windows problem. I do not recall seeing it on macOS.

## Cause

On Windows there are multiple ways for an app to talk to a tablet. For example, there are two different primary API "languages": Windows Ink and WinTab. More here: [Windows Ink](../guides/platforms/windows/winink/)

In each API, an app can get back different resolutions of coordinates for the pen:

* One is called "screen coordinates" - literally mapping to the pixels of the screen
* One is called "digitizer coordinates" - which is MUCH higher resolution than screen coordinates

Examples:

* Screen coordinates might be 150 to 250 points per inch
* Digitizer coordinates are typically 5080 points per inch

When screen coordinates are used - that's when you get the quantized look. Switching APIs often fixes it because the other API is getting digitizer coordinates.

## Quantization vs diagonal wobble

|            | Quantization                                        | Diagonal wobble                                           |
| ---------- | --------------------------------------------------- | --------------------------------------------------------- |
| Shape      | Angular, tight stair-steps, like snapping to a grid | Smooth, regular oscillation                               |
| Worst at   | Any angle, most visible on diagonals                | 45 degrees; none at 0 or 90 degrees                       |
| Platform   | Windows                                             | Any                                                       |
| Cause      | The pen API path in software                        | How the tablet senses and interpolates the pen's position |
| Fix        | Restart, switch pen API, reinstall the driver       | Cannot be fixed, only mitigated                           |
| Present on | Some setups                                         | Every tablet, in varying amounts                          |

Both are more visible when you draw slowly and on diagonals, so those don't tell them apart. What does:

* **The shape** - quantization is tight, sudden steps; wobble is a smooth wave.
* **Whether it goes away** - if a restart or switching the pen API makes it go away, it was quantization. Wobble survives all of that.

Getting this backwards is costly either way. Treating wobble as a driver problem means reinstalling drivers to fix something every tablet has. Treating quantization as wobble means living with something that a restart or a setting would have fixed.

More here: [Diagonal wobble](diagonal-wobble.md)
