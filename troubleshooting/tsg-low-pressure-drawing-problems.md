# TSG: Low pressure drawing problems

## Overview

When drawing at low pressure you can experience some instability in the pressure and this can cause your strokes to look bad. To learn more about the problem itself: [**Pen pressure stability**](../core-features/pen-pressure/instability-at-low-physical-pressure.md)

## Examples

<figure><img src="../.gitbook/assets/image (575).png" alt=""><figcaption></figcaption></figure>

## Techniques to address the problems

### Draw with higher pressure

Fundamentally these problems are because you're drawing at low pressure. Maybe this is because you want very thin strokes. Consider just drawing at higher pressure and reducing your brush size.

### Tilt the pen more

Drawing tablet pens are more sensitive to pressure when the pens are held more vertically. And this vertical orientation can exacerbate pressure stability issues. When tilted some of the physical pressure applied to the nib is not transferred to the pressure sensor but to the shell of the pen itself. While this does reduce pressure sensitivity it also has the effect of stabilizing the pressure readings a bit.

And many pens that exhibit even severe pressure stability problems when they're held vertically will not show those problems if you're holding them at a more normal angle as you draw.

<div align="left"><figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure></div>

### Point the nib away from the direction the pen is moving

There is an interaction the direction the pen is moving and the direction the nib is pointing.

If you point the nib TOWARD the direction the pen is moving that means the pen may pick up more of the surface texture which can translate into pressure readings that are bouncing around a lot.

Instead try pointing the nib AWAY from the direction of travel. In general I found that this produces less weird pressure artifacts.

<div align="left"><figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure></div>

### Use a Pressure curve

Pressure curves can mitigate low pressure problems. There are two techniques you can apply here.

The first is to decrease the sensitivity at the lower end of physical pressure. And this will reduce some of the wild swings you might see.

Another technique is simply to ignore the lower end of physical pressure near the initial activation force. This essentially increases the IAF of the pen.&#x20;

<div align="left"><figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure></div>

### Use pressure smoothing

Some applications offer pressure smoothing. Pressure smoothing can also diminish the effects of any sudden changes in pressure readings that might be occurring at low pressure.



