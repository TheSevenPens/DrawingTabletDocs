# How many pressure levels do you really need?

## Overview

You need about 2000 levels of pressure could probably get by with a lot less.

These days it's very fashionable for drawing tablets to advertise that they have 8000 levels of pressure or 16,000 levels of pressure. In my analysis the vast majority of users only need about 2000 levels of pressure and could get by with far less.

<figure><img src="../.gitbook/assets/Slide_20250107_220448 (1).png" alt="" width="375"><figcaption></figcaption></figure>

## Reasoning

The quick summary is that the number of pressure levels has to be quantized or reduced into certain visible aspects of your artwork.

So for example if your pen supports 8000 levels of pressure but your brush size is 100 pixels - then there are only 100 different possible Brush sizes. In other words many of those 8000 levels of pressure map to the same brush size. By extension the same logic applies to transparency. Most people are using 8 bit transparency which results in 256 possible transparency values. So many of those 8000 pressure levels mapped to the same exact transparency value.

There are some very specific conditions where someone might need more than 2000. But based on what I've observed those cases are incredibly rare and very specialized.

{% embed url="https://youtu.be/PRbI02Y0CAo" %}

