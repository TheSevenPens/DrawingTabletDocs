# TSG: Delay and straight lines or gaps at start of stokes

## Overview

This problem happens on Windows due to some interaction between the Windows Ink system and an application that uses the pen.&#x20;

## Symptoms

When drawing a stroke (for example simple curve). You may notice that the there is a slightly delay before something is drawn. The resulting stroke will either:

* (a) skip over the beginning part of the stroke&#x20;
* or (b) have a straight line drawn from where you put the pen down to a little latter in stroke.

<figure><img src="../.gitbook/assets/image (591).png" alt=""><figcaption></figcaption></figure>

## Other manifestations

The same delay at the beginning of dragging the pen, can manifest in other user experiences. For example, you might see it as small delay when first moving a slider. As you move the pointer with the pen, the slider will not move for several millimeters and then suddenly snap to the location of the pen.

## Examples

## ![](<../.gitbook/assets/image (404).png>)

## Diagnostic questions to answer

* Does it happen in a specific app or all apps?
* Does it happen in this online app? [**7P online tablet tester**](../developers/7p-online-tablet-tester.md)&#x20;
* Does it happen in the driver pressure test region?&#x20;

## Potential solutions

* Restart the computer
* Try [**disabling the press-and-hold ring in Windows**](../guides/operating-systems/windows/disable-the-press-and-hold-ring-in-windows.md)
* Try [**disabling windows ink in the app**](../guides/operating-systems/windows/windows-ink/configure-windows-ink-for-apps.md) then restart the app
  * and if that doesn't solve it, then also try [**disabling windows ink in the driver**](../guides/operating-systems/windows/windows-ink/configure-windows-ink-in-the-tablet-driver.md) and then restart the app.

## Links

* ([https://www.reddit.com/r/wacom/comments/sa6wjd/is\_this\_kind\_of\_thing\_supposed\_to\_happen\_when\_im/](https://www.reddit.com/r/wacom/comments/sa6wjd/is_this_kind_of_thing_supposed_to_happen_when_im/))
* ([https://www.reddit.com/r/Windowsink/comments/ao0kvs/is\_this\_just\_a\_non\_issue\_for\_microsoft\_windows\_ink/](https://www.reddit.com/r/Windowsink/comments/ao0kvs/is_this_just_a_non_issue_for_microsoft_windows_ink/))
* ([https://www.zbrushcentral.com/t/windows-ink-api-support/214256](https://www.zbrushcentral.com/t/windows-ink-api-support/214256))
* ([https://forums.getpaint.net/topic/113173-the-first-5mm-of-a-freehand-line-are-straight-when-using-a-tablet/](https://forums.getpaint.net/topic/113173-the-first-5mm-of-a-freehand-line-are-straight-when-using-a-tablet/))
