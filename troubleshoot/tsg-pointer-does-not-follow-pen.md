# TSG: Pointer moves in a different or opposite direction from the pen

## Symptoms

Sometimes when you move the pen, the pointer may move in the opposite direction.

* Example: You move the pen right, but the pointer goes left.
* Example: You move the pen up, but the pointer goes down.

Or the pointer goes in a different direction.

* Example: You move the pen up, but the pointer goes right.

## Explanation

* Usually this means nothing is wrong with the pen or the tablet itself.
* It usually means that the driver is misconfigured.
  * Sometimes drivers misconfigure themselves
  * Sometimes you accidentally misconfigure them without realizing it.
* The specific misconfiguration is that the tablet driver's relation to the screen is not accurate. The driver thinks the tablet physically rotated.

## Solution

You need to examine your tablet driver settings, find where the rotation is done, and then change the setting so that it works for you.

See: [Rotating a drawing tablet](../guides/ergonomics/rotating-drawtab.md)

If you are still having problems, contact customer support.

<br>
