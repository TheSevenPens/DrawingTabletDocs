# Smoothing with OpenTabletDriver

## Overview

OpenTabletDriver lets you configure smoothing via plug-ins.

## Installing the Slimy Scylla plug-in

Instructions for installing Slimy Scylla are here: [**Slimy Scylla**](opentabletdriver-smoothing-1.md)&#x20;

## Position smoothing&#x20;

There are several filters that involve smoothing the position of the pen.

* Position Smoothing Moving Average
* Position Smoothing Pulled String
* Position Smoothing Exponential Moving Average &#x20;

The one I recommend using is **Position Smoothing Exponental Moving Average**

## Configuring Position Smoothing Exponential Moving Average

This is what the configuration looks like:&#x20;

<figure><img src="../../../.gitbook/assets/image (292).png" alt=""><figcaption></figcaption></figure>

If you want to enable the filter, click **Enable Smily Scylla ...** at the top and click **Apply**.

**Amount** = how much smoothing (range 0.0 to 1.0). Try 0.1 to start with

**Always Apply to Hover** = to leave this unchecked.&#x20;



## Slimy Scylla documentation

here: [https://github.com/Kuuuube/Slimy\_Scylla/tree/main/docs](https://github.com/Kuuuube/Slimy\_Scylla/tree/main/docs)



*
