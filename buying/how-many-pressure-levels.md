# How many pressure levels do you really need?

## Overview

You need about 2,000 levels of pressure — and could probably get by with far less.

These days, it's fashionable for drawing tablets to advertise 8,000 or 16,000 levels of pressure. In my analysis, the vast majority of users only need about 2,000 levels and could get by with far less.

<figure><img src="../.gitbook/assets/image-000658 (1).png" alt="" width="375"><figcaption></figcaption></figure>

## Reasoning

The short explanation is that the number of pressure levels has to be translated into visible aspects of your artwork, and there are natural limits to how many distinctions matter.

For example, if your pen supports 8,000 levels of pressure but your brush size is 100 pixels, there are only 100 different possible brush sizes. In other words, many of those 8,000 pressure levels map to the same brush size.

The same logic applies to transparency. Most people use 8-bit transparency, which gives 256 possible transparency values. So many of those 8,000 pressure levels map to the exact same transparency value.

There are some very specific conditions where someone might need more than 2,000 levels. Based on what I've observed, those cases are incredibly rare and highly specialized.

{% embed url="https://youtu.be/PRbI02Y0CAo" %}
