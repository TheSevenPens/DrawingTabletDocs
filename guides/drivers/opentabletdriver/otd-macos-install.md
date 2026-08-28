# Install OpenTabletDriver on macOS

## Introduction

This document walks you through installing OpenTabletDriver (OTD) on macOS.

For Windows instructions, see [Install OpenTabletDriver on Windows](otd-windows-install.md).

The official OTD installation guide for macOS is [available here](https://opentabletdriver.net/Wiki/Install/MacOS). This document provides a more detailed walkthrough for users unfamiliar with OTD.

<mark style="color:red;">**This document is IN PROGRESS and going through some significant edits. You might encounter incomplete sections.**</mark>

Before you start:

* If you do not know what OTD is or why you might want it, read [OpenTabletDriver](./).
* Familiarize yourself with [Notes on OpenTabletDriver](otd-notes.md), which covers what OTD can and cannot do.

### Some expertise is required

Using OTD for artwork is an advanced setup. Try this only if you are confident in your technical skills or can get someone to help you.

### macOS

These instructions apply to macOS Tahoe. Earlier versions, such as Sequoia, should require similar steps. This has not been confirmed.

### CPU architecture

OTD runs on both Intel and Apple Silicon Macs, but there is only one macOS build and it is Intel-only (`osx-x64`). OTD does not ship a native Apple Silicon build.

* On an **Intel** Mac, the build runs natively.
* On an **Apple Silicon** Mac (M1 and later), the build runs through **Rosetta 2**. If Rosetta 2 is not already installed, macOS prompts you to install it the first time you launch OTD. Accept the prompt.

### OTD versions

* This document shows steps for OTD version 0.6.6.2.
* Use OTD version 0.6.5 or later. Earlier versions do not support pressure or tilt on macOS.

### Prerequisites

There are none. The macOS download is self-contained.

If you have read the Windows instructions, note two differences:

* You do **not** need to install the .NET Runtime. The macOS build bundles it. This is why the macOS download is much larger than the Windows one.
* There is no VMulti driver to install, and no Windows Ink plugin. On macOS, pressure and tilt work through the driver itself once OTD is running.

## STEP 1: Make sure your tablet is supported

Check whether your tablet appears on this [supported tablet list](https://opentabletdriver.net/Tablets).

## STEP 2: Uninstall any currently installed tablet drivers

* If you have a Wacom, Huion, XP-Pen, or other tablet driver, uninstall it now.
* After uninstalling it, restart your Mac.

## STEP 3: Download OTD

* Click this link to download [OpenTabletDriver 0.6.6.2 for macOS](https://github.com/OpenTabletDriver/OpenTabletDriver/releases/download/v0.6.6.2/OpenTabletDriver-0.6.6.2_osx-x64.tar.gz).
* This downloads a file called `OpenTabletDriver-0.6.6.2_osx-x64.tar.gz` to your Downloads folder.
* Double-click on the tar.gz file that was downloaded.
* A brief progress bar shows the archive extracting into a folder.
* When extraction finishes, your **Downloads** folder shows the following:

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-1.png" alt="" width="563"><figcaption></figcaption></figure></div>

* Open the extracted folder and drag `OpenTabletDriver` into **Applications**.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-2.png" alt="" width="375"><figcaption></figcaption></figure></div>

## STEP 4: Install OTD

* Run the OpenTabletDriver app.
* You will see a warning about verifying OTD.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-3.png" alt="" width="260"><figcaption></figcaption></figure></div>

* This warning is normal. macOS is protecting your device. You will still be able to install OTD.
* Click **Done**.
* To dismiss the “Apple is not able to verify that it is free from malware” warning, go to **System Settings → Privacy & Security**. Scroll down and click **Open Anyway**.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-4.png" alt="" width="375"><figcaption></figcaption></figure></div>

* After you click **Open Anyway**, macOS asks you to confirm.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-5.png" alt="" width="375"><figcaption></figcaption></figure></div>

* Click **Open Anyway**.
* macOS then prompts you for your password.
* OTD then explains that it needs the **Input Monitoring** permission. You must grant this for OTD to work correctly.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-6.png" alt="" width="375"><figcaption></figcaption></figure></div>

* Click **Open Input Monitoring Preference**.
* The **Input Monitoring** panel of **System Settings** opens. Make sure **OpenTabletDriver** is listed and its toggle is turned on.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-7.png" alt="" width="375"><figcaption></figcaption></figure></div>

* macOS also shows a **Keystroke Receiving** prompt. Click **Open System Settings**.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-8.png" alt="" width="375"><figcaption></figcaption></figure></div>

* OTD needs a second permission, **Accessibility**, which is separate from Input Monitoring. When the **Accessibility Access** prompt appears, click **Open System Settings**.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-9.png" alt="" width="375"><figcaption></figcaption></figure></div>

* In the **Accessibility** panel, turn on the toggle for **OpenTabletDriver**. You may also see a separate **OpenTabletDriver.UX.MacOS** entry, as shown below.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-10.png" alt="" width="375"><figcaption></figcaption></figure></div>

## STEP 5: Launch OTD

Launch OTD from **Applications**.

### OTD must stay running

For OTD to work, the OpenTabletDriver app must be running at all times. The app contains the driver daemon that talks to your tablet. If you quit the app, your tablet stops working with OTD.

You do not have to keep the window in front of you. You can hide it and leave the app running.

<mark style="color:red;">**Quitting OpenTabletDriver stops your tablet from working. Closing or hiding the window is fine.**</mark>

### Connect your tablet

If no tablet is connected, you see the following:

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-11.png" alt="" width="375"><figcaption></figcaption></figure></div>

When you connect a tablet, the UI changes:

NOTE: The top blue rectangle in the example picture below is actually TWO monitors stacked on top of each other.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-12.png" alt="" width="375"><figcaption></figcaption></figure></div>

At the bottom left, you see:

* The output mode set to **Absolute Mode**.
* The identified tablet. This example shows a Wacom PTH-660, or Wacom Intuos Pro 2017 Medium.
* A vertical virtual desktop shape. It represents two vertically stacked monitors.

### Checkpoint

At this point, moving the pen on the tablet should move the mouse pointer.

Do not worry about which monitor the pointer lands on. That is the next step.

### Map the tablet to a display

Right-click a monitor and select the tablet mapping target.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-13.png" alt="" width="375"><figcaption></figcaption></figure></div>

The display now looks like this:

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-14.png" alt="" width="375"><figcaption></figcaption></figure></div>

Right-click the bottom area and select **Lock Aspect Ratio**.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-15.png" alt="" width="375"><figcaption></figcaption></figure></div>

The bottom area changes slightly:

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-16.png" alt="" width="375"><figcaption></figcaption></figure></div>

This setting prevents stroke distortion.

Click **Apply**, then click **Save**.

## STEP 6: Understanding Apply and Save

The previous step asked you to click **Apply** and **Save**. Here is what they do.

You will find both buttons in the bottom-right corner of the OTD window. They stay in the same place no matter which tab you are on.

**Apply**

* **Apply** activates the settings currently shown in the user interface.
* Until you click **Apply**, changes you make in the UI do not take effect.

**Save**

* **Save** stores the current settings, even if you have not clicked **Apply**.
* Those settings load the next time you open OTD.
* You can test this by clicking **Save** without clicking **Apply**, then restarting the OTD app.

To keep things simple for now, always click **Apply** and then **Save** whenever you change something in the OTD app.

<mark style="color:red;">**If you close OTD without clicking Save, you lose your changes.**</mark>

## STEP 7: Configure the pen

Under **Pen Settings**, you see the default settings.

Leave it alone for now. You should see that everything is set to "Adaptive Binding". This is a good default.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-17.png" alt="" width="563"><figcaption></figcaption></figure></div>

Click **Apply**, then click **Save**.

**Note:** Assigning pen buttons to mouse actions, such as left-click, right-click, or middle-click, may cause unstable input.

## STEP 8: Configure your drawing application

Unlike Windows, macOS has no separate pen API to enable. There is no Windows Ink equivalent to turn on, and no plugin to install. Once OTD is running and your tablet is detected, pressure and tilt are available to any app that supports a pressure-sensitive tablet.

If pressure does not work in a particular app, check that app's own tablet or pressure settings first.

## STEP 9: Checkpoint

At this point, you should be able to draw effectively with OTD, and pressure and tilt should work.

Try some basic drawing in your app of choice and confirm that:

* The pointer stays on the display you mapped the tablet to.
* A circle drawn on the tablet produces a circle on screen, not a stretched oval.
* Pressing harder produces a heavier stroke.

## Optional customization

**Pressure curves** - By default, OTD does not use a pressure curve to modify how the pressure data is interpreted. You can edit the pressure curve by following these instructions: [Pressure curves in OpenTabletDriver](pressure-curves-in-otd.md)

**Smoothing** - [Smoothing with OpenTabletDriver](otd-smoothing.md)

**Tablet buttons** - [Configure tablet buttons with OpenTabletDriver](otd-tablet-buttons.md)

### Start OpenTabletDriver when you log in

Because OTD must stay running, you may want it to start automatically.

* Open **System Settings**.
* Go to **General** > **Login Items & Extensions**.
* Under **Open at Login**, click the **+** button.
* Select **OpenTabletDriver** from **Applications**, then click **Open**.

OTD now starts each time you log in.

## Uninstalling OpenTabletDriver

There is no uninstaller. To remove OTD:

* Quit the OpenTabletDriver app.
* Drag `OpenTabletDriver` from **Applications** to the Trash.
* Remove its settings folder at `~/Library/Application Support/OpenTabletDriver`.
* Remove its cache folder at `~/Library/Caches/OpenTabletDriver`.
* In **System Settings** > **Privacy & Security**, remove the OpenTabletDriver entries from **Input Monitoring** and **Accessibility**.

If you want your manufacturer driver back, install it after removing OTD, then restart your Mac.

## Related topics

* [OpenTabletDriver](./)
* [Notes on OpenTabletDriver](otd-notes.md)
* [Install OpenTabletDriver on Windows](otd-windows-install.md)
* [Pressure curves in OpenTabletDriver](pressure-curves-in-otd.md)
* [Smoothing with OpenTabletDriver](otd-smoothing.md)
* [Configure tablet buttons with OpenTabletDriver](otd-tablet-buttons.md)

