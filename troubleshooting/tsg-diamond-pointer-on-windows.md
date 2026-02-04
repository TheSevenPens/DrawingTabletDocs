# TSG: Diamond pointer on Windows

## Overview

You may occasionally encounter a situation when using your drawing tablet on a Windows computer, that the pointer shows as a small diamond shape instead of what you would expect.

<figure><img src="../.gitbook/assets/image (630).png" alt=""><figcaption></figcaption></figure>

## Cause

This is fundamentally a tablet driver issue.

When you see the small diamond pointer, it means that Windows is not using your tablet driver. Instead Windows is using it's built in PNP driver support. More here:  [Windows PNP support](../guides/operating-systems/windows/windows-pnp-support.md)

This could be because

* Your have not installed your tablet driver
* Your tablet driver is taking longer than expected to load
* Your tablet driver is has crashed

## Steps to fix

* Make sure you have the tablet driver installed
* Uninstall it and reinstall if necessary

Notes

* This is NOT a failure of the tablet hardware or pen hardware
* MacOS does not have this problem

If you can't solve this problem, contact customer support.

