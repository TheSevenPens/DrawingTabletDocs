# Customize pen buttons with OpenTabletDriver

## Overview

This document explains how to change what the pen's buttons do when you use OTD on **Windows** or **macOS**.

## MacOS and Windows behave differently

Remember that the OTD instructions are for an artistic setup to enable Pressure and Tilt. This means on Windows, the setup requires the Windows Ink plugin. he Windows Ink plugin limits what you can do with the pen buttons.s Ink plugin is not needed, and there are more options for configuration.

{% hint style="info" %}
For general information about pen buttons, such as how many a pen has and what people usually assign to them, see [Pen buttons](../../pens/pen-buttons.md).

For the buttons on the tablet itself, see [Configure tablet buttons with OpenTabletDriver](otd-tablet-buttons.md).
{% endhint %}

## Notes

* This document is based on OTD `v0.6.7` and, on Windows, the Windows Ink plugin `v0.5.2`.
* The Windows parts apply to **Windows Ink Absolute Mode** from the Windows install instructions.
* The macOS parts describe how OTD's macOS output works - but I have not carefully checked them on a Mac.

## Settings

### Adaptive Binding (the default)

#### Adaptive binding on Windows

What the button does is up to the app and Windows. Many apps treat it as a right-click or a context menu. Some let you change it in their own settings. For Windows' own pen settings, see [Windows Pen & Windows Ink settings](../../platforms/windows/windows-pen-and-windows-ink-settings.md).

Every button set to Adaptive Binding will perform the same action set to adaptive binding will perform the same action on Windows.

#### Adaptive binding on MacOS

By default, every pen button is set to `Adaptive Binding`. On macOS, that sends a mouse click:

* **Button 1** is a right-click.
* **Button 2** is a middle-click.
* **Button 3** does nothing.

The pen tip and the eraser end each send a left-click.

### Keyboard shortcut (Key Binding, Multi-Key Binding)

* **Windows (Windows Ink):** Works.
* **macOS:** Works. Needs the Accessibility permission from the install steps. When you type key names in the **Advanced Binding Editor**, OTD calls the Command key `Application`, the Option key `Alt`, and the Control key `Control`. Shift is `Shift`.

### Mouse Button Binding & Mouse Scroll Binding

* **Windows (Windows Ink):** Does not work.
* **macOS:** Works.

`Mouse Button Binding` and `Mouse Scroll Binding` are available on macOS. Use the **Advanced Binding Editor** to choose one. If you assign a mouse action and notice unstable input, as the [macOS install guide](otd-macos-install.md) warns can happen, set the button back to `Adaptive Binding` or to a keyboard shortcut.

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

## Notes assigning buttons to hotkeys

* The keys are pressed when you press the pen button, and released when you release it.
* That makes a key that an app uses while it is held work the way you would expect. For example, a button set to `Space` pans the canvas in many apps while you hold the button and drag.

See [Pen buttons](../../pens/pen-buttons.md) for common choices for assigning hotkeys.

## Related topics

* [Install OpenTabletDriver on Windows](otd-windows-install.md)
* [Install OpenTabletDriver on macOS](otd-macos-install.md)
* [Pen buttons](../../pens/pen-buttons.md)
* [Configure tablet buttons with OpenTabletDriver](otd-tablet-buttons.md)
* [Notes on OpenTabletDriver](otd-notes.md)
* [Windows Pen & Windows Ink settings](../../platforms/windows/windows-pen-and-windows-ink-settings.md)
