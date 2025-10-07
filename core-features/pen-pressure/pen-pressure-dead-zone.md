# Pen pressure dead zone

## Overview

The pressure dead zone is an area of a pressure curve that is deliberately designed to ignore a bit of the lower end of the pressure range. The pressure dead zone effectively increases the IAF of the pen.

## Visualization

Visually the pressure dead zone can be seen whenever the lower left corner of the pressure curve is displaced to the right

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Uses

We often prize having extremely low initial activation force with our EMR pens because it makes them more sensitive to lighter strokes.

But that sensitivity comes at a cost. It can introduce several kinds of problems. And a pressure dead zone can address these problems

examples of problems that pressure dead zone could be applied to:

* drawing while hovering
* strokes having tails

## Default dead zones in tablet drivers

When you look at the default pressure curve and a tablet driver for most of the EMR pens you will encounter, you will notice that they almost always do not have a dead zone predefined.

There are a couple of notable exceptions (as of 2025/03/18).

* The default pressure curve for the Wacom pro pen 2 (KP-504E) has a pressure dead zone
* The default pressure curve for the Huion PW600 pens also has a small pressure dead zone.

## Testing results

I've tested 4 Wacom pro pen 2 units by using them without the default pressure dead zone. Of the four two did not have any drawing while hover problems. The other two did in fact draw while hovering. It appears that the Wacom pro pen 2 is a bit oversensitive and some units by default do draw on hover. So this explains why Wacom defaults to a small pressure dead zone for these pens. Note that the Wacom pro pen 3 does not have a default pressure dead zone.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

For the Huion PW600 series of pens, without the pressure dead zone I did not encounter any drawing while hovering problems.

## Recommendation

the pressure dead zone is intended to solve a problem. But not all pens have that problem. I would suggest that when you get a new tablet or a new pen you take a look at the tablet driver and verify whether a pressure dead zone is set by default.

If it is try using the pen without the pressure dead zone. And if you don't notice any problems then leave it that way. Because that will give you a more sensitive pen with a lower initial activation force.

## Links

* [Tablet\_P - Tablet Pressure Deadzones](https://www.youtube.com/watch?v=rvEuwuKcAWE) 2025/03/18&#x20;
