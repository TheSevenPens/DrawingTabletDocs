# WinTab vs Windows Ink

## Overview

On Windows, there are two ways a drawing tablet communicates with your computer and the tablet driver: WinTab and Windows Ink.

## For normal users

By default, **I recommend you use Windows Ink** unless something forces you to use WinTab.&#x20;

If you use WinTab I suggest you only use it for a specific application.

To learn how to configure Windows Ink. [**Windows Ink**](../guides/operating-systems/windows/winink/)&#x20;

## For developers

Wacom published a page with frequently asked questions about WinTab:

[https://developer-support.wacom.com/hc/en-us/articles/12844524637975-Wintab](https://developer-support.wacom.com/hc/en-us/articles/12844524637975-Wintab) ([archive](https://archive.is/htSEG))

Here's a small snippet of the relevant section of the doc

<div align="left"><figure><img src="../.gitbook/assets/image (38).png" alt="" width="375"><figcaption></figcaption></figure></div>

Please read the document for the full details.

### My developer perspective

But here are a few things that stand out to me:

* It is a well understood and stable API
* There are wrappers or many languages (C#, Rust, Python) that let you talk to the APIs. &#x20;
  * I had a relatively simple time incorporating it into my test drawing app called [WinTabPainter](https://github.com/TheSevenPens/WinTabPainter).
* You can find many projects that use WinTab
* It has been difficult for me to find clear examples of how to use the Windows Ink API. Most of the code is heavily focused on the inking features - which is great but not on what I need which is a way to get the pen position, pressure, tilt data, etc.

So at the moment, I intend to continue to use WinTab until I find an easy way to consume the Windows Ink APIs.
