# Decreasing IAF

## Overview

The initial activation force is the smallest amount of physical pressure that the pen can detect

Strictly speaking, the IAF is a characteristic of the pen hardware and it cannot be lowered or increased.

However there are some techniques you can apply that might be able to effectively give you a lower IAF even though you're not changing the pen hardware in any way.

## Option #1: perpendicular pen orientation

Typically when people draw they're holding the pen at something like a 45° angle relative to the tablet surface.

However pens are more sensitive to pressure when you hold them perpendicular to the tablet surface.

So try holding the pen more perpendicular to the tablet surface and you should see that it's more sensitive.

## Option #2: eliminate any dead zones in your pressure curves

Pressure curves are a form of post processing of pressure information. So even though your pen's hardware doesn't change the post processing of the pressure can effectively change things related to pressure.

check the pressure curve that's being used in the driver and in your application brushes.

They might have a pressure dead zone. Such a dead zone will have the net effect of increasing the IAF. more here: [Pressure curve dead zones](../../core/pressure/pen-pressure-curves/pressure-curve-deadzone.md)

Reduce or get rid of the dead zone to reduce the effective IAF.

Keep in mind you'll never be able to reduce the IAF to less than what the pens hardware can natively support.
