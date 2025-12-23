# SevenPens Tablet Tester

## Overview

With my Tablet Tester browser-based tool you can test out the basic features of your tablet. This is useful for troubleshooting.&#x20;

## Try out the tool now

Go here to launch the tool: [**SevenPens Tablet Tester**](https://thesevenpens.github.io/HtmlTabletTester/)**.** Then start drawing in the blue box.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

## Safety and privacy

This tool:

* Does **not** collect any data about you, your computer, etc.
* Does **not** uses no cookies.
* Does **not** track your behavior.
* Does **not** record what you draw.

## Features

* Inputs
  * Draw with pen
  * Draw with mouse
* Formatting
  * Control stroke size by pressure or tilt or use a fixed size
  * Control stroke color by pressure or tilt or use a fixed color
  * Control the minimum size of a stroke - useful when drawing with very light pressyre
* Live Pointer information
  * Position, Tilt, Pressure, Barrel Rotation
  * Calculated information: Velocty & Direction
  * Button status
* Utilities
  * Erase canvas when starting a new stroke
  * &#x20;Show stroke stats such as pointer events/sec
* Processing
  * Position smoothing
  * Pressure smoothing
  * Tilt smoothing
  * Pressure quantization
  * Pressure curve
* Multiple ways to erase the canvas:
  * Press **Clear** button
  * Press **BACKSPACE** key
  * Press **DELETE** key
* Press **Save** button to download canvas as PNG file&#x20;

## OS & Browser compatibility

**Windows**

* Pen API:
  * Needs Windows Ink to be enabled in the tablet driver.&#x20;
  * If you tablet driver is using only WinTab, no pressure is supported.
* Chrome - WORKS
* Firefox - WORKS

**MacOS**

* Safari - yet to be tested
* Chrome -  WORKS

**Linux**

* Chrome - WORKS
* Firefox
  * Wayland - WORKS
  * X11 -&#x20;
    * use `env MOZ_USE_XINPUT2=1 firefox` to make it work
    * more info on what's going on with the X11 issue:&#x20;
      * [https://stackoverflow.com/questions/78073830/pen-pointer-events-in-linux-chrome-and-firefox-not-working-as-intended/78764151#78764151](https://stackoverflow.com/questions/78073830/pen-pointer-events-in-linux-chrome-and-firefox-not-working-as-intended/78764151#78764151)
      * [https://bugzilla.mozilla.org/show\_bug.cgi?id=1207700](https://bugzilla.mozilla.org/show_bug.cgi?id=1207700)&#x20;

**iPadOS**

* Safari - WORKS

**Android**

* Chrome - WORKS

## Open source

The entire source code is on the github repo ([https://github.com/TheSevenPens/HtmlTabletTester](https://github.com/TheSevenPens/HtmlTabletTester)). I encourage you to look through it and fork and modify it for your needs.
