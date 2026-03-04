# TSG: Tablet driver using too much memory

## Summary

Occasionally you might see a tablet driver consume a VAST amount of RAM - perhaps gigabytes - when you are looking at memory usage through Task Manager on Windows or Activity Monitor on MacOS. This is NOT normal.

## Typical memory usage

Here are more typical values for Wacom for example

* MacOS: WacomDriver in Activity Monitor -> 47.5 MB
* Windows: TabletService for professional driver -> 5MB

## Abnormal memory usage

Any values in the hundreds of MBs or GBs are very unusual.

## Which brand of drivers are affected?

I have seen this happen with all brands of tablet drivers: Wacom, Huion, XP-Pen, etc.

## What to do

Overall, there is nothing you can do to fix the problem directly. It is an issue in the driver code itself.

* First try restarting your computer and see if the problem comes back. The problem might be temporary.
* Your driver user interface may give you an option to restart the driver. This will reset the memory usage and is less of a headache than restarting the computer
* If the problem keeps happening though, then you need to contact customer support for your tablet.

## Examples of high memory usage

<figure><img src="../.gitbook/assets/wacom-macos-high-memory-1 (Large).jpeg" alt="" width="375"><figcaption><p>MacOS / Wacom Center / 166.5GB</p></figcaption></figure>

Reddit threads:

* [https://www.reddit.com/r/wacom/comments/1rj272t/wacom\_tablet\_is\_using\_too\_much\_memory/](https://www.reddit.com/r/wacom/comments/1rj272t/wacom_tablet_is_using_too_much_memory/)
*
