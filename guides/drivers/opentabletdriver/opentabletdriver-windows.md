# Install OpenTabletDriver on Windows

## **Overview**

This document is for creative users are interested in using OpenTabletDriver on Windows and want to use pen features such as pressure sensitivity, tilt, etc. If you don't know much about OpenTabletDriver, read this introduction first: [**OpenTabletDriver**](./). You should also familiarize yourself with these [**usage notes for OpenTabletDriver**](opentabletdriver-usage-notes.md).

What follows are the detailed steps I use to install OTD on Windows. This document **does not** replace the official OTD documentation ([https://opentabletdriver.net/Wiki](https://opentabletdriver.net/Wiki)).&#x20;

### Skills required

Using OTD for doing artwork is an advanced scenario. You should try only if you are confident in your technical skills or can get someone to help you.

### **Supported tablets**

Although OTD supports many (200+) tablets but not all of them. Consult the complete list here: [https://opentabletdriver.net/Tablets](https://opentabletdriver.net/Tablets)

In that list, your tablet may be marked as needing "Zadig WinUSB". If so, you will also have to install that component. I do not have any drawing tablets that require Zadig WinUSB so using Zadig WinUSB is NOT covered in this document.

### Important notes

* The instructions cover this specific version of OTD: v0.6.3.0
* These instructions are for x64 operating systems only. OTD does not support 32-bit versions of Windows.
* I tested these instructions on Windows 11 64-bit (version 10.0.22621)

## **Prepare your computer**

* Uninstall any existing tablet drivers (Wacom, XP-Pen, Huion, etc.).&#x20;
* To be absolutely sure you have completely removed the drivers follow this guide: [Uninstalling manufacturer tablet drivers](../uninstalling-manufacturer-tablet-drivers.md)
* Uninstalling may require a restart of your system. So get this out of the way before you proceed with the next steps.
* Create a folder somewhere on your computer called "OpenTabletDriver". I will use "C:\OpenTabletDriver" for the examples in this doc.&#x20;

## Install the VMulti driver

<mark style="color:red;">You MUST install</mark> <mark style="color:red;"></mark><mark style="color:red;">**VMulti driver**</mark> <mark style="color:red;"></mark><mark style="color:red;">if you want pressure sensitivity & tilt to work with your tablet on Windows.</mark>

* Download **VMulti.Driver.zip** from: [https://github.com/X9VoiD/vmulti-bin/releases/download/v1.0/VMulti.Driver.zip](https://github.com/X9VoiD/vmulti-bin/releases/download/v1.0/VMulti.Driver.zip)
* Right click the zip and select **Extract All**.
* This will create folder called **VMulti.Driver**.&#x20;
* Copy the VMulti.Driver folder to the C:\OpenTabletDriver.
* Right click on **install\_hiddriver.bat** and select **Run as Administrator**
  * NOTE: This bat file may restart your computer without warning. So, close any applications and save any docs before you run it.

## Install the .NET Runtime&#x20;

* OTD requires a specific version of the .NET Runtime
* You can directly download and installed the version of .NET Runtime needed by downloading it from this link: [https://opentabletdriver.net/framework](https://opentabletdriver.net/framework)&#x20;

## Download and extract OpenTabletDriver

* Download [**OpenTabletDriver.win-x64.zip**](https://github.com/OpenTabletDriver/OpenTabletDriver/releases/latest/download/OpenTabletDriver.win-x64.zip) and put it in your **Documents** folder&#x20;
* Right-click on **OpenTabletDriver.win-x64.zip**, then select **Extract All**
* This will create a folder called **OpenTabletDriver.win-x64**
* Copy the **OpenTabletDriver.win-x64** folder to **c:\OpenTabletDriver**&#x20;

## Launch the OpenTabletDriver app for the first time

* In the **OpenTabletDriver.win-x64** folder, launch **OpenTabletDriver.UX.Wpf.exe**
* That launches the OTD app
* If you see a message that .NET 6 Desktop Runtime X64 is not installed, then follow its instructions to install that runtime. Then launch OpenTabletDriver.UX.Wpf.exe. This message does not always come up, so I recommend that you install the .NET Runtime before you use OTD.
* The **OpenTabletDriver Guide** may automatically start&#x20;
  * Click the X in the upper right hand corner to close the guide.
  * You can get back to this guide at any time in OTD by navigating to **Help** > **Show guide**.
* When the OTD app is running, this icon will appear in your taskbar

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="188"><figcaption></figcaption></figure>

## **Detect your tablet**

* OTD will automatically try to detect your tablet
* The tablet will be shown in the Window title at the top
* To force detection click **Tablets** > **Detect tablet**

## Install the Windows Ink plugin

* In the OTD app, navigate to **Plugins** > **Open Plugin Manager**
* Click on the **Windows Ink** plugin , then click **Install**&#x20;
* The Windows Ink plugin will appear at the top of the plugin list
* Close the **Plugin Manager** window

## Configure tablet to display mapping

* In the OTD App, go to **Output** > **Tablet** Section
* In **Output** > **Display**, right-click anywhere and pick **Set to Display** \<displayname> where \<displayname> is specific display you want to use with the tablet.
* In **Output > Tablet**, right click anywhere, and then select **Lock Aspect Ratio**.
* ![](<../../../.gitbook/assets/image (35).png>)

## Configure Windows Ink

* In the OTD app, on the bottom change to mode dropdown from **Absolute Mode** to **Windows Ink Absolute Mode**
* NOTE: You will only see **Windows Ink Absolute Mode** listed if you previously enabled the Windows Ink plugin.

![](<../../../.gitbook/assets/image (111).png>)

## Configure the pen

### Overview

* In the OTD app, navigate to the **Pen Settings** tab
* To summarize, you'll want your Pen Settings to look like this:

<div align="left">

<figure><img src="../../../.gitbook/assets/image (322).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

| Setting                               | Value                                                                                                                      |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Tip Settings** >**Tip Binding**     | <p><strong>Type</strong> -> <strong>Windows Ink</strong></p><p><strong>Button</strong> -> <strong>Pen Tip</strong></p>     |
| **Pen Buttons** > **Pen Binding 1**   | <p><strong>Type</strong> -> <strong>Windows Ink,</strong></p><p><strong>Button</strong> -> <strong>Pen Button</strong></p> |
| **Pen Buttons** > **Pen Binding 2**   | <p><strong>Type</strong> -> <strong>Windows Ink</strong></p><p><strong>Button</strong> -> <strong>Pen Button</strong></p>  |
| **Eraser Settings > Eraser Bindings** | <p><strong>Type</strong> -> <strong>Windows Ink</strong></p><p><strong>Button</strong> -> <strong>Pen Tip</strong></p>     |

At the bottom of the OTD app, click **Apply**.

## Tablet buttons

* In the **Auxiliary Settings** tab, each button shows up as an **Auxiliary Binding**.
* ![](<../../../.gitbook/assets/image (328).png>)
* In the screenshot above, one of the buttons has been set to match the "e" key.

## Save OpenTabletDriver configuration

* Click **Save** at the bottom
* Click **Apply** at the bottom

## Minimize the OpenTabletDriver app

* You don't have to keep the OTD app visible all the time, you can minimize the app at any time
* If you need to open OTD app again, you can find it in the taskbar

![](<../../../.gitbook/assets/image (207).png>)

## Configure your drawing application to use Windows Ink

* The specific instructions vary per app.&#x20;
* Instructions for specific apps: [Configure Windows Ink for apps](../../windows/windows-ink/configure-windows-ink-for-apps.md)

## Automatically start OpenTabletDriver when Windows starts

* Right-click on OpenTabletDriver.UX.Wpf.exe
* Select **Create Shortcut**
* Right click on the shortcut, then select **Properties**
* Under **Run**, select **Minimized**
* Click **OK**
* Press WINDOWS+R to bring up the **Run** window
* In **Open**, type `shell:startup`
* This will open a new Explorer window pointing to a folder called **Startup**
* Move the shortcut to the **Startup** folder in that explorer window

## Customizing your experience

### Pressure curve

By default OTD does not use a pressure curve to modify how the pressure data is interpreted. However, you can edit the pressure curve by following these instructions: [Pressure curve OpenTabletDriver](opentabletdriver-pressure.md)

### Smoothing

By default OTD performs no smoothing on the pen data. This is desirable because&#x20;

* it gives you a VERY responsive drawing experience
* Gives you complete control about the smoothing

### Application-level smoothing

To add smoothing back in to your drawing, your first and easiest option is to use the smoothing features in your drawing application.

Learn more here: [**Configure smoothing in applications**](../../drawing/configure-smoothing-in-applications.md)&#x20;

### Driver-level smoothing&#x20;

More here: [**Smoothing with OpenTabletDriver**](opentabletdriver-smoothing.md)&#x20;

## Uninstalling OTD

See the instructions here: [Uninstalling OpenTabletDriver on Windows](uninstalling-opentabletdriver-on-windows.md)

## Resources

* r/huion - [OpenTablet Driver guide for Huion Kamvas 24 4k on windows 10 (but maybe other tablets too) in particular for painting](https://www.reddit.com/r/huion/comments/17q61pl/opentablet\_driver\_guide\_for\_huion\_kamvas\_24\_4k\_on/) 2023/11/07&#x20;
