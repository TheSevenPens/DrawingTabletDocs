# Using barrel rotation with your brush

## Overview

If you are using a pen that supports barrel rotation and a tablet that supports barrel rotation, the tablet will always send barrel rotation information to the tablet.

## Getting started

However, your apps brushes may not be configured to use the barrel rotation data.

So, make sure your brush is correctly configured to map barrel rotation to have some effect on your brush. Typically this means having barrel rotation control the rotation of the brush shape.

Make sure your brush shape is something that would show barrel rotation clearly.

A shape like this would work

<figure><img src="../../.gitbook/assets/image-000240 (1).png" alt=""><figcaption></figcaption></figure>

whereas a shape like this would not demonstrate barrel rotation because it is symetric about its center.

<figure><img src="../../.gitbook/assets/image-000298.png" alt=""><figcaption></figcaption></figure>

## Krita: enabling barrel rotation

* Launch Krita and open the brush editor
* Under **Flow** , enable **Rotation**
* Check **Enable Pen Settings**
* Uncheck all the options under **Enable Pen Settings**, but check **Rotation**.
* Then go to the canvas of your document and try rotating the pen around its long axis

<figure><img src="../../.gitbook/assets/image-000340.png" alt="" width="563"><figcaption></figcaption></figure>

## Photoshop 2026

* Open the **Brush Settings** window
* Navigate to **Shape Dynamics**
* Under **Angle Jitter**, set **Control** to **Rotation**

<figure><img src="../../.gitbook/assets/image.png" alt="" width="563"><figcaption></figcaption></figure>
