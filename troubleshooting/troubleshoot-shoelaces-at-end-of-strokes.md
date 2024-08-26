# Troubleshoot shoelaces at end of strokes

## Overview

This is a common effect that is highly dependent on how you draw and the specific brush in your drawing app. It manifests as a longer "string" at the end of your stroke. These ends can be rendered as a constant width or a long very thin string.

NOTE: There is a related problem: [Troubleshoot hooks at start of strokes](troubleshoot-hooks-at-start-of-strokes.md)

## Examples

![](<../.gitbook/assets/image (113).png>)![](<../.gitbook/assets/image (71).png>)

## Avoid flicking

Are you "flicking" the pen away from the tablet at the end of your strokes? This can induce the effect. Try not taking the pen off the tablet surface and ending the line slowly.

## Smoothing

Smoothing (also called Stabilization) can cause this issue. Try using less smoothing.

## Pressure sensitivity

In my experience this can happen when pens have a low IAF (Initial Activation Force).

Even though a low IAF is a good thing. It can also mean that at the end of strokes it is still picking up the very last bit of low pressure.

Try adjusting your pressure curve as shown below to see if this helps reduce the problem.

<figure><img src="../.gitbook/assets/image (451).png" alt="" width="375"><figcaption></figcaption></figure>

## Your application

Different apps may be more prone to this problem - depending on the implementation in their brush engine.

Reach out to other users of your application to see how they addressed it.

## OpenTabletDriver & Slimy Scylla

If you are using OpenTabletDriver, the Slimy Scylla plug-in can remove shoelacing with its **Remove Tail Position Reports** option on any of the Slimy Scylla's pressure smoothing filters.

The default value for **Remove Tail Position Reports** is 1, and usually this is enough.

However, sometimes may need to increase it to 2 or higher.

In general, set the value to as low a number as it will go and still work correctly for you.

## Lazy Nezumi

The Lazy Nezumi tool ([https://lazynezumi.com/](https://lazynezumi.com/)) has several tools to help deal with these shoelace effect.

![](<../.gitbook/assets/image (183).png>)



## Reddit threads

* [https://www.reddit.com/r/huion/comments/11imlzd/kamvas\_16\_2021\_shoestringing/](https://www.reddit.com/r/huion/comments/11imlzd/kamvas\_16\_2021\_shoestringing/)&#x20;
* [https://community.adobe.com/t5/photoshop-ecosystem-bugs/p-shoelace-shaped-brush-stroke-with-wacom-and-smoothing-on-macos/idi-p/12558795](https://community.adobe.com/t5/photoshop-ecosystem-bugs/p-shoelace-shaped-brush-stroke-with-wacom-and-smoothing-on-macos/idi-p/12558795)&#x20;
* [https://www.reddit.com/r/wacom/comments/yr6hhb/sudden\_checkmarkshoelace\_effect\_at\_end\_of\_every/](https://www.reddit.com/r/wacom/comments/yr6hhb/sudden\_checkmarkshoelace\_effect\_at\_end\_of\_every/)





