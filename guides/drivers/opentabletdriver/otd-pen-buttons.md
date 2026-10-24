# Customize pen buttons with OpenTabletDriver

## Overview

This document explains how to change what the pen's buttons do when you use OpenTabletDriver (OTD) on Windows in **Windows Ink Absolute Mode**. That is the setup from [Install OpenTabletDriver on Windows](otd-windows-install.md).

The short version: only some kinds of button settings work well with Windows Ink. Others can interrupt your strokes or do nothing. This document tells you which is which.

{% hint style="info" %}
For general information about pen buttons, such as how many a pen has and what people usually assign to them, see [Pen buttons](../../pens/pen-buttons.md).

For the buttons on the tablet itself, see [Configure tablet buttons with OpenTabletDriver](otd-tablet-buttons.md).
{% endhint %}

### Version information

* This document is based on OTD `v0.6.7` and the Windows Ink plugin `v0.5.2`.
* It applies to Windows with the **Windows Ink Absolute Mode** from the install instructions.
* If you use plain **Absolute Mode** instead of Windows Ink, mouse button settings are fine. The cautions below are specific to Windows Ink.

## The short version

* **Leave one button on its default**, `Adaptive Binding`. It acts as the pen's own button. Many apps treat that as a right-click or a context menu, but your app and your Windows pen settings decide.
* **For any other action, use a keyboard shortcut.** Keyboard settings work normally with Windows Ink.
* **Do not use mouse settings** such as left-click, right-click, or scroll. With Windows Ink they can interrupt your stroke, or do nothing.
* **Leave the tip and the eraser alone.**

## Where the settings are

1. In the OTD app, open the **Pen Settings** tab.
2. Under **Pen Buttons**, find the list of buttons: **Pen Binding 1**, **Pen Binding 2**, and so on. Your pen determines how many appear.
3. Each one shows what it is set to. Out of the box, **Pen Binding 1** shows `Adaptive Binding: (Binding: Button 1)`, **Pen Binding 2** shows `Adaptive Binding: (Binding: Button 2)`, and so on.
4. Click that text to change it in the **Binding Editor**.
5. Click the **...** button beside it to open the **Advanced Binding Editor**, which has a **Type** dropdown that lists every kind of setting OTD offers.

After any change, click **Apply**, then click **Save**. See [Install OpenTabletDriver on Windows](otd-windows-install.md) for what those two buttons do.

## What the default does

By default, every pen button is set to `Adaptive Binding`. In Windows Ink mode, this passes the button to Windows as a real pen button. Apps see it the way they would see the barrel button on a pen that Windows Ink supports natively.

What it does is up to the app and Windows. Many apps treat it as a right-click or a context menu. Some let you change it in their own settings. For Windows' own pen settings, see [Windows Pen & Windows Ink settings](../../platforms/windows/windows-pen-and-windows-ink-settings.md).

{% hint style="warning" %}
With Windows Ink, all of the pen's buttons send the **same** signal. Two buttons that are both set to `Adaptive Binding` do the same thing, even though OTD labels them Button 1 and Button 2.

If you want two different actions, set one button to `Adaptive Binding` and give the other a keyboard shortcut.
{% endhint %}

## Assign a keyboard shortcut to a button

1. On the **Pen Settings** tab, under **Pen Buttons**, click the button you want to change.
2. The **Binding Editor** opens with the message *Press a key, combination of keys, or a mouse button.*
3. **Press the shortcut on your keyboard.** For example, press `Ctrl` and `Z` together.
4. The box shows what OTD recorded. A single key shows as `Key Binding: (Key: Space)`, for example. A combination shows as `Multi-Key Binding: (Keys: Control+Z)`.
5. Click **Apply** in the **Binding Editor**.
6. Click **Apply**, then **Save**, in the main OTD window.

{% hint style="danger" %}
Do **not** click inside the box while the **Binding Editor** is open. A mouse click there sets the button to a **mouse button** setting, which is the kind to avoid with Windows Ink.
{% endhint %}

### How a shortcut behaves

* The keys are pressed when you press the pen button, and released when you release it.
* That makes a key that an app uses while it is held work the way you would expect. For example, a button set to `Space` pans the canvas in many apps while you hold the button and drag.

See [Pen buttons](../../pens/pen-buttons.md) for common choices.

## Do not use mouse settings with Windows Ink

These settings appear in the **Type** dropdown of the **Advanced Binding Editor**, and a click in the **Binding Editor** creates one:

* `Mouse Button Binding`, with Left, Right, Middle, Back, or Forward
* `Mouse Scroll Binding`

Windows Ink sends the pen to Windows as a pen. A mouse click is a different kind of input. To send one, the Windows Ink plugin has to take the pen out of range, move the Windows mouse pointer to the pen's position, and send a mouse click. This is the same limitation noted in [Install OpenTabletDriver on Windows](otd-windows-install.md).

What that means in practice:

* **Left, Right, Middle:** the click can interrupt a stroke in progress. If it works at all, the pen briefly stops acting as a pen.
* **Back and Forward:** no click is sent, but the pen still leaves range.
* **Scroll:** does nothing in Windows Ink mode.

If you want a right-click, leave the button on `Adaptive Binding`. If you need another action, use a keyboard shortcut.

{% hint style="info" %}
If you find a button already set to a mouse setting, for example from an earlier configuration, change it to `Adaptive Binding` or a keyboard shortcut.

To set a button back to the default, open the **Advanced Binding Editor** with the **...** button, set **Type** to `Adaptive Binding`, and choose the button number that matches it.
{% endhint %}

## Make a button do nothing

1. Click the button's setting to open the **Binding Editor**.
2. Click **Clear**.
3. Click **Apply**, then **Save**, in the main OTD window.

This is useful if you keep pressing a button by accident.

## Leave the tip and the eraser alone

The **Tip Binding** and **Eraser Binding** are what make the pen draw and erase. They are set to `Adaptive Binding` by default. Replacing them can stop the pen from drawing, so leave them as they are.

If you want to turn pressure or tilt off, use the **Disable Pressure** and **Disable Tilt** settings on the same tab, not the tip binding.

## Optional: an eraser on a button

The Windows Ink plugin adds its own kind of setting called `Windows Ink`. Its **Button** option includes:

* **Eraser (Hold)** - the pen acts as an eraser while you hold the button.
* **Eraser (Toggle)** - each press switches the pen between pen and eraser.

Switching between pen and eraser briefly takes the pen out of range, so use it between strokes, not during one. The names of these options can differ between versions of the plugin.

## Things to know

* **A shortcut can get stuck.** A keyboard shortcut is held down while you hold the pen button. If you switch presets, or the tablet disconnects, at that moment, the key can stay down. Press that key once on your keyboard to release it.
* **A shortcut that works everywhere except one app.** Windows does not let a normal program send key presses to an app that is running as administrator. If a shortcut fails in only one app, check whether that app is running as administrator, and start it normally.
* **Changes do nothing until you click Apply.** Click **Save** as well, or the change is lost when you close OTD.

## Related topics

* [Install OpenTabletDriver on Windows](otd-windows-install.md)
* [Pen buttons](../../pens/pen-buttons.md)
* [Configure tablet buttons with OpenTabletDriver](otd-tablet-buttons.md)
* [Notes on OpenTabletDriver](otd-notes.md)
* [Windows Pen & Windows Ink settings](../../platforms/windows/windows-pen-and-windows-ink-settings.md)
