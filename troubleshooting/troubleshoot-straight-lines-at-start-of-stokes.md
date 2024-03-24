# Troubleshoot straight lines at start of stokes

## Overview

This problem happens on Windows due to some interaction between the Windows Ink system and an application that uses the pen.&#x20;

It manifests during the start of a stroke where as you begin the stroke nothing will happen at first - you pen tip will move but the stroke does not. And then suddenly the stroke will move to where the pen is. This will produce a small straight line. &#x20;

It will also manifest as a small delay when first moving a slider. As you move the pointer with the pen, the slider will not move for several millimeters and then suddenly snap to the location of the pen.

## Examples

## ![](<../.gitbook/assets/image (331).png>)

## Things to try

* Try [**disabling windows ink in the app**](../guides/windows/windows-ink/configure-windows-ink-for-apps.md) and [**disabling windows ink in the driver**](../guides/windows/windows-ink/configure-windows-ink-in-the-tablet-driver.md).
* Try [**disabling the press-and-hold ring in Windows**](../guides/windows/disable-the-press-and-hold-ring-in-windows.md).

## Links

* ([https://www.reddit.com/r/wacom/comments/sa6wjd/is\_this\_kind\_of\_thing\_supposed\_to\_happen\_when\_im/](https://www.reddit.com/r/wacom/comments/sa6wjd/is\_this\_kind\_of\_thing\_supposed\_to\_happen\_when\_im/))
* ([https://www.reddit.com/r/Windowsink/comments/ao0kvs/is\_this\_just\_a\_non\_issue\_for\_microsoft\_windows\_ink/](https://www.reddit.com/r/Windowsink/comments/ao0kvs/is\_this\_just\_a\_non\_issue\_for\_microsoft\_windows\_ink/))
* ([https://www.zbrushcentral.com/t/windows-ink-api-support/214256](https://www.zbrushcentral.com/t/windows-ink-api-support/214256))
* ([https://forums.getpaint.net/topic/113173-the-first-5mm-of-a-freehand-line-are-straight-when-using-a-tablet/](https://forums.getpaint.net/topic/113173-the-first-5mm-of-a-freehand-line-are-straight-when-using-a-tablet/))
