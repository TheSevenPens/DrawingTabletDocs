# Mirroring or extending

## Overview

In terms of what you see on it, your pen display is just another monitor/display to your computer. So, you can control how the computer shows its desktop to the pen display.

You have two options:

* **Extend the desktop** - this means you can see different things on the pen display from your monitor. This is what I recommend you use.
* **Duplicate the desktop (aka "Mirror the desktop")** - This means your pen display and monitor will try to show the same exact thing.

## About duplication/mirror

### Considerations

Duplicating is very useful and intuitive, but generally I think Extend is a better choice for most people and situations.

Things that may happen with duplication:

* Black bars on one of the screens. This happens if they don't have the same aspect ratio
* If the two screens have different resolutions, the duplication may use the lower resolution.
* If the two screens have different max refresh rates, duplication will use the lower refresh rate for both.

### Alternative methods that effectively duplicate your canvas

If you just want to see your canvas on both displays, explore this option instead: [Showing canvas on another display](../../apps/tips/canvas-on-another-display.md)

## Steps to control extend vs duplicate

{% tabs %}
{% tab title="Windows 11" %}
* Open **Display Settings**
* The displays your computer is connected to will be shown and each one is numbered. The one in blue is the display currently selected.
  * If a display has two numbers, that means the desktop is being duplicated across those displays
* NOTE: If you only see one display, then these settings do not apply.
* Select the display that corresponds to your tablet
* Toward the bottom right, to the right of the **Identify** button, you will see a dropdown that controls how the desktop is applied to this display. Depending on how the display is already configured, the dropdown will say either:
  * **Extend desktop to this display**
  * **Duplicate desktop on X and Y**
    * X and Y will be the numbers referring to the displays
* Switch the dropdown between the **Extend** or **Duplicate** option as needed.
{% endtab %}

{% tab title="MacOS" %}
* Go to **Displays > Display Settings**
* Select your monitor, then set **Use As** to **Primary Display**
* Then select your drawing tablet's display and set **Use As** to **Mirror**.
{% endtab %}
{% endtabs %}
