# Customize pen buttons with OpenTabletDriver

## Overview

This document explains how to change what the pen's buttons do when you use OpenTabletDriver (OTD) on **Windows** or **macOS**.

What you can assign depends on the platform:

* On **Windows**, you use OTD with the Windows Ink plugin, as described in [Install OpenTabletDriver on Windows](otd-windows-install.md). Only some kinds of button settings work well with Windows Ink. Others can interrupt your strokes or do nothing.
* On **macOS**, OTD does not use Windows Ink, so most settings are available. See [Install OpenTabletDriver on macOS](otd-macos-install.md).

{% hint style="info" %}
For general information about pen buttons, such as how many a pen has and what people usually assign to them, see [Pen buttons](../../pens/pen-buttons.md).

For the buttons on the tablet itself, see [Configure tablet buttons with OpenTabletDriver](otd-tablet-buttons.md).
{% endhint %}

### Version information

* This document is based on OTD `v0.6.7` and, on Windows, the Windows Ink plugin `v0.5.2`.
* The Windows parts apply to **Windows Ink Absolute Mode** from the Windows install instructions.
* The macOS parts describe how OTD's macOS output works. They have not been checked on a Mac.
* Linux is not covered.

## What is supported on each platform

| Setting | Windows (Windows Ink) | macOS |
| --- | --- | --- |
| **Adaptive Binding** (the default) | Works. Passes the pen's own button to Windows. Every button sends the same signal. | Works. Sends a mouse click: Button 1 is a right-click, Button 2 is a middle-click, Button 3 does nothing. |
| **Keyboard shortcut** (Key Binding, Multi-Key Binding) | Works. | Works. Needs the Accessibility permission from the install steps. |
| **Mouse Button Binding** | Avoid. Can interrupt your stroke. | Works. |
| **Mouse Scroll Binding** | Does not work. | Works. |
| **Windows Ink binding** (eraser on a button) | Available. | Not available. It is part of the Windows Ink plugin. |
| **Clear** (button does nothing) | Works. | Works. |
| **Tip and eraser** | Leave on Adaptive Binding. | Leave on Adaptive Binding. |

## Where the settings are

These steps are the same on both platforms.

1. In the OTD app, open the **Pen Settings** tab.
2. Under **Pen Buttons**, find the list of buttons: **Pen Binding 1**, **Pen Binding 2**, and so on. Your pen determines how many appear.
3. Each one shows what it is set to. Out of the box, **Pen Binding 1** shows `Adaptive Binding: (Binding: Button 1)`, **Pen Binding 2** shows `Adaptive Binding: (Binding: Button 2)`, and so on.
4. Click that text to change it in the **Binding Editor**.
5. Click the **...** button beside it to open the **Advanced Binding Editor**, which has a **Type** dropdown that lists every kind of setting OTD offers.

After any change, click **Apply**, then click **Save**. The install guides explain what those two buttons do.

## Assign a keyboard shortcut to a button

This works on both platforms.

1. On the **Pen Settings** tab, under **Pen Buttons**, click the button you want to change.
2. The **Binding Editor** opens with the message *Press a key, combination of keys, or a mouse button.*
3. **Press the shortcut on your keyboard.** For example, press the modifier key and `Z` together.
4. The box shows what OTD recorded. A single key shows as `Key Binding: (Key: Space)`, for example. A combination shows as `Multi-Key Binding: (Keys: Control+Z)`. Check that it shows the keys you meant.
5. Click **Apply** in the **Binding Editor**.
6. Click **Apply**, then **Save**, in the main OTD window.

{% hint style="danger" %}
Do **not** click inside the box while the **Binding Editor** is open. A mouse click there sets the button to a **mouse button** setting. On Windows that is the kind to avoid. On macOS it works, but it is probably not what you wanted.
{% endhint %}

### How a shortcut behaves

* The keys are pressed when you press the pen button, and released when you release it.
* That makes a key that an app uses while it is held work the way you would expect. For example, a button set to `Space` pans the canvas in many apps while you hold the button and drag.

See [Pen buttons](../../pens/pen-buttons.md) for common choices.

## Make a button do nothing

This works on both platforms.

1. Click the button's setting to open the **Binding Editor**.
2. Click **Clear**.
3. Click **Apply**, then **Save**, in the main OTD window.

This is useful if you keep pressing a button by accident.

## Leave the tip and the eraser alone

On both platforms, the **Tip Binding** and **Eraser Binding** are what make the pen draw and erase. They are set to `Adaptive Binding` by default. Replacing them can stop the pen from drawing, so leave them as they are.

If you want to turn pressure or tilt off, use the **Disable Pressure** and **Disable Tilt** settings on the same tab, not the tip binding.

## On Windows

### What the default does

By default, every pen button is set to `Adaptive Binding`. In Windows Ink mode, this passes the button to Windows as a real pen button. Apps see it the way they would see the barrel button on a pen that Windows Ink supports natively.

What it does is up to the app and Windows. Many apps treat it as a right-click or a context menu. Some let you change it in their own settings. For Windows' own pen settings, see [Windows Pen & Windows Ink settings](../../platforms/windows/windows-pen-and-windows-ink-settings.md).

{% hint style="warning" %}
With Windows Ink, all of the pen's buttons send the **same** signal. Two buttons that are both set to `Adaptive Binding` do the same thing, even though OTD labels them Button 1 and Button 2.

If you want two different actions, set one button to `Adaptive Binding` and give the other a keyboard shortcut.
{% endhint %}

### Do not use mouse settings with Windows Ink

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

### Optional: an eraser on a button

The Windows Ink plugin adds its own kind of setting called `Windows Ink`. Its **Button** option includes:

* **Eraser (Hold)** - the pen acts as an eraser while you hold the button.
* **Eraser (Toggle)** - each press switches the pen between pen and eraser.

Switching between pen and eraser briefly takes the pen out of range, so use it between strokes, not during one. The names of these options can differ between versions of the plugin.

### Windows cautions

* **A shortcut that works everywhere except one app.** Windows does not let a normal program send key presses to an app that is running as administrator. If a shortcut fails in only one app, check whether that app is running as administrator, and start it normally.

## On macOS

OTD on macOS does not use Windows Ink. It sends the pen to macOS directly, with pressure, tilt, and the eraser end handled by OTD. Mouse actions are sent as ordinary mouse events, so the Windows Ink limitations do not apply.

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

## Things to know

* **A shortcut can get stuck.** A keyboard shortcut is held down while you hold the pen button. If you switch presets, or the tablet disconnects, at that moment, the key can stay down. Press that key once on your keyboard to release it.
* **Changes do nothing until you click Apply.** Click **Save** as well, or the change is lost when you close OTD.

## Related topics

* [Install OpenTabletDriver on Windows](otd-windows-install.md)
* [Install OpenTabletDriver on macOS](otd-macos-install.md)
* [Pen buttons](../../pens/pen-buttons.md)
* [Configure tablet buttons with OpenTabletDriver](otd-tablet-buttons.md)
* [Notes on OpenTabletDriver](otd-notes.md)
* [Windows Pen & Windows Ink settings](../../platforms/windows/windows-pen-and-windows-ink-settings.md)
