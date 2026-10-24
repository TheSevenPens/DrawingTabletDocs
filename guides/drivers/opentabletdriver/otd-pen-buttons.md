# Customize pen buttons with OpenTabletDriver

## Overview

This document explains how to change what the pen's buttons do when you use OpenTabletDriver (OTD) on **Windows** or **macOS**.

## Which OS you use is important

Rememeber that my OTD instructions are for an artistic setup.

* On **Windows**, this artistic setup requires the Windows Ink plugin. And the WIndows Ink plugin restricts how the pen buttons can be configured.
* On **MacOS**, there the Windows Ink plugin is not needed, and there are more options for configuration.

{% hint style="info" %}
For general information about pen buttons, such as how many a pen has and what people usually assign to them, see [Pen buttons](../../pens/pen-buttons.md).

For the buttons on the tablet itself, see [Configure tablet buttons with OpenTabletDriver](otd-tablet-buttons.md).
{% endhint %}

### Version information

* This document is based on OTD `v0.6.7` and, on Windows, the Windows Ink plugin `v0.5.2`.
* The Windows parts apply to **Windows Ink Absolute Mode** from the Windows install instructions.
* The macOS parts describe how OTD's macOS output works - but I have not carefully checked them on a Mac.

## What is supported on each platform

### Adaptive Binding (the default)

* **Windows (Windows Ink):** Works. But there is a big limitation on Windows: it performs a "default" button action, and every button on the pen that is set to Adaptive Binding does that same action.
* **macOS:** Works. Button 1 is a right-click, Button 2 is a middle-click, and Button 3 does nothing.

### Keyboard shortcut (Key Binding, Multi-Key Binding)

* **Windows (Windows Ink):** Works.
* **macOS:** Works. Needs the Accessibility permission from the install steps.

### Mouse Button Binding

* **Windows (Windows Ink):** Does not work.
* **macOS:** Works.

### Mouse Scroll Binding

* **Windows (Windows Ink):** Does not work.
* **macOS:** Works.

### Windows Ink binding (eraser on a button)

* **Windows (Windows Ink):** Available.
* **macOS:** Not applicable.

### Clear (button does nothing)

* **Windows (Windows Ink):** Works.
* **macOS:** Works.

### Tip and eraser

* **Windows (Windows Ink):** Leave on Adaptive Binding.
* **macOS:** Leave on Adaptive Binding.

## Settings location

1. In the OTD app, open the **Pen Settings** tab.
2. Under **Pen Buttons**, find the list of buttons: **Pen Binding 1**, **Pen Binding 2**, and so on. Your pen determines how many appear.
3. Each one shows what it is set to. Out of the box, **Pen Binding 1** shows `Adaptive Binding: (Binding: Button 1)`, **Pen Binding 2** shows `Adaptive Binding: (Binding: Button 2)`, and so on.
4. Click that text to change it in the **Binding Editor**.
5. Click the **...** button beside it to open the **Advanced Binding Editor**, which has a **Type** dropdown that lists every kind of setting OTD offers.

After any change, click **Apply**, then click **Save**. The install guides explain what those two buttons do.

## Assign a keyboard shortcut to a button

1. On the **Pen Settings** tab, under **Pen Buttons**, click the button you want to change.
2. The **Binding Editor** opens with the message _Press a key, combination of keys, or a mouse button._
3. **Press the shortcut on your keyboard.** For example, press the modifier key and `Z` together.
4. The box shows what OTD recorded. A single key shows as `Key Binding: (Key: Space)`, for example. A combination shows as `Multi-Key Binding: (Keys: Control+Z)`. Check that it shows the keys you meant.
5. Click **Apply** in the **Binding Editor**.
6. Click **Apply**, then **Save**, in the main OTD window.

{% hint style="danger" %}
Do **not** click inside the box while the **Binding Editor** is open. A mouse click there sets the button to a **mouse button** setting. On Windows that is the kind to avoid. On macOS it works, but it is probably not what you wanted.
{% endhint %}

### How pressing a pen button works with hotkeys

* The keys are pressed when you press the pen button, and released when you release it.
* That makes a key that an app uses while it is held work the way you would expect. For example, a button set to `Space` pans the canvas in many apps while you hold the button and drag.

See [Pen buttons](../../pens/pen-buttons.md) for common choices for assigning hotkeys.

## Leave the tip and the eraser alone

On both platforms, the **Tip Binding** and **Eraser Binding** are what make the pen draw and erase. They are set to `Adaptive Binding` by default. Replacing them can stop the pen from drawing, so I recommend that leave them as they are.

If you want to turn pressure or tilt off, use the **Disable Pressure** and **Disable Tilt** settings on the same tab, not the tip binding.

## On Windows

### What the default does

By default, every pen button is set to `Adaptive Binding`. In Windows Ink mode, this passes the button to Windows as a real pen button. Apps see it the way they would see the barrel button on a pen that Windows Ink supports natively.

What it does is up to the app and Windows. Many apps treat it as a right-click or a context menu. Some let you change it in their own settings. For Windows' own pen settings, see [Windows Pen & Windows Ink settings](../../platforms/windows/windows-pen-and-windows-ink-settings.md).

{% hint style="warning" %}
With Windows Ink, all of the pen's buttons send the **same** signal. Two buttons that are both set to `Adaptive Binding` do the same thing, even though OTD labels them Button 1 and Button 2.

If you want two different actions, set one button to `Adaptive Binding` and give the other a keyboard shortcut.
{% endhint %}

## On macOS

### What the default does

By default, every pen button is set to `Adaptive Binding`. On macOS, that sends a mouse click:

* **Button 1** is a right-click.
* **Button 2** is a middle-click.
* **Button 3** does nothing.

The pen tip and the eraser end each send a left-click.

### Mouse and scroll settings

`Mouse Button Binding` and `Mouse Scroll Binding` are available on macOS. Use the **Advanced Binding Editor** to choose one. If you assign a mouse action and notice unstable input, as the [macOS install guide](otd-macos-install.md) warns can happen, set the button back to `Adaptive Binding` or to a keyboard shortcut.

### Keyboard shortcuts

* Keyboard shortcuts need the **Accessibility** permission that the macOS install guide has you grant. If a shortcut does nothing while the pen still moves the pointer, check that permission first.
* When you type key names in the **Advanced Binding Editor**, OTD calls the Command key `Application`, the Option key `Alt`, and the Control key `Control`. Shift is `Shift`.

### What is not available

* There is no `Windows Ink` setting, so there is no eraser-on-a-button option.
* The administrator caution for Windows does not apply.

## Related topics

* [Install OpenTabletDriver on Windows](otd-windows-install.md)
* [Install OpenTabletDriver on macOS](otd-macos-install.md)
* [Pen buttons](../../pens/pen-buttons.md)
* [Configure tablet buttons with OpenTabletDriver](otd-tablet-buttons.md)
* [Notes on OpenTabletDriver](otd-notes.md)
* [Windows Pen & Windows Ink settings](../../platforms/windows/windows-pen-and-windows-ink-settings.md)
