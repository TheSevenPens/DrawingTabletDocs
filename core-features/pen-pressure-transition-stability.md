# Pen pressure transition stability

## Overview

Smooth changes to physical pressure should produce smooth changes to the pressure readings from a a tablet. When this is done well I use the term "pressure transition stability".

An unstable transition would mean that smooth changes in physical pressure would produce exaggerated or wild swings in the pressure readings. I call this "pressure transition instability"

No pen is perfect, but most are pretty good. However, it is not uncommon to discover a pen that has problems with these pressure transitions. Usually it happens in the lower range of pressure.

## Detection

These unstable readings may not be visible if pressure used to alter the size of small brushes - for example 5px or 10px. So to see the behavior we need to scale up the effect by using larger brush sizes - for example 300px.

NOTE: Your hand itself will introduce imperfections in a stroke. So it takes some practice to learn how to distinguish the effects you are causing, versus what is happening with the tablet.

## Visual examples

Compare the three cases below. The example on the far right has noticeable "pulsing" effect which is a common way this instability shows up.

<figure><img src="../.gitbook/assets/image (492).png" alt=""><figcaption></figcaption></figure>

##

