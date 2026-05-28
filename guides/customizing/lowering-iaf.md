# Decreasing IAF

## Overview

The initial activation force is the smallest amount of physical pressure that the pen can detect.

Strictly speaking, the IAF is a characteristic of the pen hardware, and it cannot be lowered or increased.

However, there are some techniques that may effectively give you a lower IAF, even though they do not change the pen hardware in any way.

## Option #1: perpendicular pen orientation

Typically, people hold the pen at about a 45° angle relative to the tablet surface.

However pens are more sensitive to pressure when you hold them perpendicular to the tablet surface.

So try holding the pen more perpendicular to the tablet surface. You should see that it is more sensitive.

## Option #2: eliminate any dead zones in your pressure curves

Pressure curves are a form of post-processing of pressure information. So even though your pen's hardware does not change, the post-processing of pressure can effectively change pressure behavior.

Check the pressure curve used in the driver and in your application brushes.

They might have a pressure dead zone. Such a dead zone has the net effect of increasing the IAF. More here: [Pressure curve dead zones](../../core/pressure/pen-pressure-curves/pressure-curve-deadzone.md)

Reduce or get rid of the dead zone to reduce the effective IAF.

Keep in mind that you will never be able to reduce the IAF below what the pen's hardware can natively support.
