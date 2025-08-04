# Active Area Mapping for pen tablets and widescreen monitors

Using a pen tablet with a widescreen monitor presents some challenges and some new opportunities with a pen tablet due to the extreme differences in aspect ratio.

## Background: a common situation for typical monitors

Most pen tablets have  an aspect ratio of around 16:10&#x20;

Many monitors have an aspect ratio of 16:9.

The mismatch in aspect ratios, causes strokes to be slightly distorted. For example, a circle drawn on the the pen tablet will appear as an oval on the monitor.

How can we avoid distortion?

With a widescreen monitor there are some interesting options.

## Option 1: Use Force Proportions. Map a proportional part of the tablet's active area to the entire monitor.

The solution is the use the Force Proportions feature which changes the tablets active area to match that of the monitor. This solves the distortion problem at the cost of the loss of some of the tablet's active area.&#x20;

<figure><img src="../../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

## Option #2: Entire tablet active area mapped to a portion of the widescreen monitor

This is like the opposite of Option #1.

You could map the active area of the tablet to a region of the monitor with the same aspect ratio.

<figure><img src="../../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

The region is shown in the center of the monitor, but it could be left or right aligned.

You get to use the full area of your tablet, but then you have to carefully possition yoru drawing application into a region that the tablet is mapped to.

## Option #3 Split the widescreen into two monitors

Some widescreen monitors support being treated as two separate monitors. FOr example they will require TWO separate HDMI cables leading to your computer. Your computer will think there are two monitors even though they half of the same monitor.

Then:

* Enable Force Proportions
* And use Display Toggle

This option:

* Avoids distortion
* Maximizes use of tablet active area
* Maximizes use of monitor screen



<figure><img src="../../.gitbook/assets/image (476).png" alt=""><figcaption></figcaption></figure>

### Note: How to split a widescreen monitor into two separate monitors.

* Some widescreen monitors have a built-in feature allowing this. They may call it "Picture-by-Picture" or "PBP".
* On Windows, another option to explore is a tool called DisplayFusion.
