# Smoothing with OpenTabletDriver

## Overview

By default, OTD performs no smoothing on the pen data. This is desirable because:

* It gives you a very responsive drawing experience.
* It gives you complete control over smoothing.

There are two ways to introduce smoothing:

* **Application-level smoothing** - To add smoothing back to your drawing, the first and easiest option is to use the smoothing features in your drawing application. Learn more here: [Configure smoothing in applications](../../drawing/configure-smoothing-in-apps.md)
* **Driver-level smoothing in OTD** - This is a little more complex. Since OTD does not have built in smoothing, you have to install plug-ins to achieve driver-level smoothing. The specific plug-in I recommend is Slimy Scylla.&#x20;

## Installing the Slimy Scylla plug-in

Instructions for installing Slimy Scylla are here: [Slimy Scylla](otd-plugin-slimyscylla.md)

## Position smoothing

There are several filters that involve smoothing the position of the pen.

* Position Smoothing Moving Average
* Position Smoothing Pulled String
* Position Smoothing Exponential Moving Average

The one I recommend is **Position Smoothing Exponential Moving Average**.

## Configuring Position Smoothing Exponential Moving Average

This is what the configuration looks like:

<figure><img src="../../../.gitbook/assets/image-000369.png" alt=""><figcaption></figcaption></figure>

If you want to enable the filter, click **Enable Slimy Scylla ...** at the top, then click **Apply**.

**Amount** = how much smoothing to apply. The range is 0.0 to 1.0. Try `0.1` to start.

**Always Apply to Hover** = leave this unchecked.

## Slimy Scylla documentation

See: [https://github.com/Kuuuube/Slimy\_Scylla/tree/main/docs](https://github.com/Kuuuube/Slimy_Scylla/tree/main/docs)
