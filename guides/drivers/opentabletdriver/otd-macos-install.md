# Install OpenTabletDriver on macOS

## Introduction

This document walks you through installing OpenTabletDriver (OTD) on macOS.

For Windows instructions, see [Install OpenTabletDriver on Windows](otd-windows-install.md).

The official OTD installation guide for macOS is [available here](https://opentabletdriver.net/Wiki/Install/MacOS). This document provides a more detailed walkthrough for users unfamiliar with OTD.

<mark style="color:red;">**This document is IN PROGRESS and going through some significant edits. You might encounter incomplete sections.**</mark>

### macOS

These instructions apply to macOS Tahoe. Earlier versions, such as Sequoia, should require similar steps. This has not been confirmed.

### CPU architecture

OTD runs on Intel x86 and Apple Silicon Macs.

### OTD versions

* This document shows steps for OTD version 0.6.6.
* Use OTD version 0.6.5 or later. Earlier versions do not support pressure or tilt on macOS.

## STEP 1: Make sure your tablet is supported

Check whether your tablet appears on this [supported tablet list](https://opentabletdriver.net/Tablets).

## STEP 2: Uninstall any currently installed tablet drivers

* If you have a Wacom, Huion, XP-Pen, or other tablet driver, uninstall it now.
* After uninstalling it, restart your Mac.

## STEP 3: Download OTD

* Click this link to download the [latest release](https://github.com/OpenTabletDriver/OpenTabletDriver/releases/latest/download/OpenTabletDriver-0.6.6.2_osx-x64.tar.gz).
* This downloads a file called `OpenTabletDriver-0.6.6.2_osx-x64.tar.gz` to your Downloads folder.
* Double-click on the tar.gz file that was downloaded.
* A brief progress bar shows the archive extracting into a folder.
* When extraction finishes, your **Downloads** folder shows the following:

<figure><img src="../../../.gitbook/assets/otd-macos-install-1.png" alt=""><figcaption></figcaption></figure>

* Open the extracted folder and drag `OpenTabletDriver` into **Applications**.

<figure><img src="../../../.gitbook/assets/otd-macos-install-2.png" alt=""><figcaption></figcaption></figure>

## STEP 4: Install OTD

* Run the OpenTabletDriver app.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-3.png" alt="" width="260"><figcaption></figcaption></figure></div>

* This warning is normal. macOS is protecting your device. Click **Done**. Do **not** click **Move to Trash**.
* To dismiss the “Apple could not verify is free of malware” warning, go to **System Settings → Privacy & Security**. Scroll down and click **Open Anyway**.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-4.png" alt="" width="563"><figcaption></figcaption></figure></div>

* After you click **Open Anyway**, this dialog appears. Click **Open Anyway**.
* macOS then prompts you for your password.
* You then see the following:

<div align="left"><figure><img src="../../../.gitbook/assets/unused/image (9).png" alt="" width="375"><figcaption></figcaption></figure></div>

* Click **Open Input Monitoring Preferences**.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-7.png" alt="" width="375"><figcaption></figcaption></figure></div>

* In this dialog, click **Open System Settings**.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-8.png" alt="" width="375"><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-9.png" alt="" width="375"><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-10.png" alt="" width="375"><figcaption></figcaption></figure></div>

## STEP 5: Launch OTD

Launch OTD from **Applications**.

If no tablet is connected, you see the following:

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-11.png" alt="" width="563"><figcaption></figcaption></figure></div>

When you connect a tablet, the UI changes:

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-12.png" alt="" width="375"><figcaption></figcaption></figure></div>

At the bottom left, you see:

* The output mode set to **Absolute Mode**.
* The identified tablet. This example shows a Wacom PTH-660, or Wacom Intuos Pro 2017 Medium.
* A vertical virtual desktop shape. It represents two vertically stacked monitors.

Right-click a monitor and select the tablet mapping target.

<figure><img src="../../../.gitbook/assets/otd-macos-install-13.png" alt=""><figcaption></figcaption></figure>

The display now looks like this:

<figure><img src="../../../.gitbook/assets/otd-macos-install-14.png" alt=""><figcaption></figcaption></figure>

Right-click the bottom area and select **Lock Aspect Ratio**.

<figure><img src="../../../.gitbook/assets/unused/image (25).png" alt=""><figcaption></figcaption></figure>

The bottom area changes slightly:

<figure><img src="../../../.gitbook/assets/otd-macos-install-16.png" alt=""><figcaption></figcaption></figure>

This setting prevents stroke distortion.

## STEP 6: Configure the pen

Under **Pen Settings**, you see the default settings.

Leave it alone for now.

<figure><img src="../../../.gitbook/assets/otd-macos-install-17.png" alt=""><figcaption></figcaption></figure>
