# Install OpenTabletDriver on MacOS

## Introduction

This document will walk you through the installation of OpenTabletDriver (OTD) on MacOS.

If you want the windows instructions, go here: [Install OpenTabletDriver on Windows](otd-windows-install.md).

The official OTD installation guide for MacOS is here: [https://opentabletdriver.net/Wiki/Install/MacOS](https://opentabletdriver.net/Wiki/Install/MacOS) This document is s more detailed walkthrough for those who are not familiar with OTD.

<mark style="color:red;">**This document is IN PROGRESS and going through some significant edits. You might encounter incomplete sections.**</mark>

### MacOS

These instructions are shown for MacOS Tahoe. They should be similar to the steps needed on earlier versions of MacOS such as Sequoia but I have not confirmed this.

### CPU architecture

OTD runs on both Intel x86 and Apple Silicon macs.

### OTD versions

* This document shows the steps for OTD version 0.66
* I recommend you use at least version OTD version 0.6.5 or higher. Before version 0.6.5 - OTD does not support pressure and tilt on MacOS

## STEP 1: make sure your tablet is supported.

Check if your tablet is on this list: [https://opentabletdriver.net/Tablets](https://opentabletdriver.net/Tablets)

## STEP 2: Uninstall any currently installed tablet drivers

* If you have a Wacom, Huion, XP-Pen, etc driver. Uninstall it now.
* Once you are finished uninstalling, I recommend restarting your MacOS computer.

## STEP 3: Download OTD

* Click in this link to download [latest release](https://github.com/OpenTabletDriver/OpenTabletDriver/releases/latest/download/OpenTabletDriver-0.6.6.2_osx-x64.tar.gz)
* This downloads a file called `OpenTabletDriver-0.6.6.2_osx-x64.tar.gz` to your Downloads folder.
* Double-click on the tar.gz file that was downloaded.
* You'll see a brief progress bar indicating it is being extracted into a folder
* When the extraction is done in your Downloads folder you will see

<figure><img src="../../../.gitbook/assets/otd-macos-install-1.png" alt=""><figcaption></figcaption></figure>

* Extract it and drag `OpenTabletDriver` into your **Applications** folder

<figure><img src="../../../.gitbook/assets/otd-macos-install-2.png" alt=""><figcaption></figcaption></figure>

## STEP 4 Installing

* Run the OpenTabletDriver app.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-3.png" alt="" width="260"><figcaption></figcaption></figure></div>

* If you see this - this is normal. MacOS is trying to protect you. Click **Done**, do NOT click **Move to Trash**
* To fix the "Apple could not verify is free of malware" warning on macOS, go to **System Settings > Privacy & Security**, scroll down, and click **"Open Anyway"** under the security section.

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-4.png" alt="" width="563"><figcaption></figcaption></figure></div>

* Once you click Open Anyway, this dialog will appear. Click **Open Anyway**.
*

```
<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-5.png" alt="" width="260"><figcaption></figcaption></figure></div>
```

* If you click Open Anyway, it's going to require you to enter your password
* Then you will see

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-6.png" alt="" width="375"><figcaption></figcaption></figure></div>

* Click Open Input Monitoring Preference

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-7.png" alt="" width="375"><figcaption></figcaption></figure></div>

* FOr this dialog click Open System Settings

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-8.png" alt="" width="375"><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-9.png" alt="" width="375"><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-10.png" alt="" width="375"><figcaption></figcaption></figure></div>

## STEP 5 Launching OTD

Launch OTD from Applications

If no tablet is connected, you'll see this

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-11.png" alt="" width="563"><figcaption></figcaption></figure></div>

Once a tablet is plugged in the UI will change

<div align="left"><figure><img src="../../../.gitbook/assets/otd-macos-install-12.png" alt="" width="375"><figcaption></figcaption></figure></div>

At the bottom left you'll see

the Outout mode set to Absolute Mode

The Tablet identified (the screenshot shows Wacom PTH-660 which is the Wacom Intuos Pro 2017 Medium)

The very vetical looking shape on top is a the "virtual desktop" that contains two monitors stacked on top of each other.

Right click on one of the monitors and select which one the tablet should be mapped to.

<figure><img src="../../../.gitbook/assets/otd-macos-install-13.png" alt=""><figcaption></figcaption></figure>

Now it will look like this

<figure><img src="../../../.gitbook/assets/otd-macos-install-14.png" alt=""><figcaption></figcaption></figure>

Now right click on the bottom are and select **Lock Aspect Ratio**

<figure><img src="../../../.gitbook/assets/otd-macos-install-15.png" alt=""><figcaption></figcaption></figure>

Once you do you'll see a slight change in the bottom area

<figure><img src="../../../.gitbook/assets/otd-macos-install-16.png" alt=""><figcaption></figcaption></figure>

This setting is important because it will stop distortion of strokes

## STEP 6 Configure the Pen

Under Pen Settings, you'll see this as ghe default settings.

Leave it alone for now.

<figure><img src="../../../.gitbook/assets/otd-macos-install-17.png" alt=""><figcaption></figcaption></figure>
