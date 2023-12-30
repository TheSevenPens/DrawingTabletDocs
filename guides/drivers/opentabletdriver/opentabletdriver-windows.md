# Install OpenTabletDriver on Windows

## **Overview**

This document is for creatives that meet three criteria:

* they use drawing tablets on Microsoft Windows with applications that can use Windows Ink API such as Clip Studio Paint, Krita, Photoshop, etc.&#x20;
* they need creative features such as pressure sensitivity, tilt, etc.
* they cannot use the drivers from tablet manufacturer.

## Introduction to OpenTabletDriver

Read this first: [**OpenTabletDriver**](./)&#x20;

## OpenTabletDriver documentation

This document describes the detailed steps I follow to setup OTD on Windows for drawing and my usage notes about the process.

This document **does not** replace the official OTD documentation ([https://opentabletdriver.net/Wiki](https://opentabletdriver.net/Wiki))

## Skills required

Using OTD for doing artwork is an advanced scenario. You should try only if you are confident in your technical skills or can get someone to help you.

## Usage notes

### **Windows Ink & WinTab**&#x20;

* There are two Pen APIs in the Windows ecosystem: **WinTab** which is older, and **Windows Ink** which is newer.
* OTD only supports **Windows Ink** so any apps you want to use it with must also support Windows Ink.
* Most creative apps support Windows Ink - Clip Studio Paint, Krita, Photoshop.
* If you want pressure sensitivity, tilt, etc. - you must **you MUST configure OTD to use Windows Ink** and configure your apps to also use Windows Ink.&#x20;

### Tablet features not supported by OpenTabletDriver

* OTD does NOT support touch input.
* OTD does NOT support tablet rotary dials.
* OTD does NOT support pen barrel rotation.
* OTD does NOT support bluetooth connections.

### System vs application settings

Many manufacturer drivers support having a setting for your entire system and a setting for specific applications. Wacom, Huion, and XP-Pen all support this is their drivers.

For example, you can change have a pen button be a right click for all applications but be a double-click for Krita.

However, OTD only supports system-wide settings. So any settings in OTD will affect EVERY application.&#x20;

### Pen hover height

By default, OTD **has no restriction on the hover height of your pen**. Most drivers impose an artificial limit of about 10mm for a pen. But you'll often find with OTD that the hover height is increased substantially.&#x20;

The maximum hover height is dependent on the specific model of tablet involved. For example with a Wacom Intuos Pro (PTH-860) my hover height goes from 10mm with the Wacom Driver to 20mm with Open Tablet driver.

You can install a plug-in to control the hover height and have whatever limit you want.

### Installation

Technically, OpenTabletDriver isn't "installed". It's just a tool that you can download and run from any location on your computer. &#x20;

### **Running OTD as admin**

* <mark style="color:red;">**DO NOT run OTD as administrator**</mark>.&#x20;
* OTD will not work correctly if you do.

## **Supported tablets**

Although OTD supports many tablets, it does not support all of them.

Consult the list here to verify that your tablet is supported by OpenTabletDriver: [https://opentabletdriver.net/Tablets](https://opentabletdriver.net/Tablets)

In that list, your tablet may be marked as needing "Zadig WinUSB". If so, you will also have to install that component. I do not have any drawing tablets that require Zdig WinUSB so using Zadig WinUSB is NOT covered in this document.

## Getting help

### Use the OTD discord to get help

* If you need help, join the OpenTabletDriver Discord server: [https://opentabletdriver.net/Discord](https://opentabletdriver.net/Discord)&#x20;
* DO ask questions in the `#support-windows` channel
* DO NOT ask for support via DMs.

### Do not get help from your tablet manufacturer

<mark style="color:red;">**Your tablet manufacturer WILL NOT help or support you in any way when you are using OpenTabletDriver instead of their own drivers.**</mark>&#x20;

## Important notes

* The instructions cover this specific version of OTD: v0.6.3.0
* These instructions are for x64 operating systems only. OTD does not support 32-bit versions of Windows.
* I only tested this on these versions of Windows:
  * Windows 11 64-bit (version 10.0.22621)
  * Windows 10 64-bit &#x20;

## **Prepare your computer**

* Uninstall any existing tablet drivers (Wacom, XP-Pen, Huion, etc.).&#x20;
  * To be absolutely sure you have completely removed the drivers follow this guide: [Uninstalling manufacturer tablet drivers](../uninstalling-manufacturer-tablet-drivers.md)
* Uninstalling may require a restart of your system. So get this out of the way before you proceed with the next steps.
* Download and install Krita from [https://krita.org/](https://krita.org/) . We will use Krita to test that OTD is installed correctly.
* Create a folder somehere on your computer called "OpenTabletDriver". I will use "C:\OpenTabletDriver" for the examples in this doc.&#x20;

## Install VMulti driver

* <mark style="color:red;">You MUST install</mark> <mark style="color:red;"></mark><mark style="color:red;">**VMulti**</mark> <mark style="color:red;"></mark><mark style="color:red;">if you want pressure sensitivity & tilt to work with your tablet.</mark>
* NOTE: Installing VMulti requires administrator permissions on your computer.
* Download **VMulti.Driver.zip** from this location
  * [https://github.com/X9VoiD/vmulti-bin/releases/download/v1.0/VMulti.Driver.zip](https://github.com/X9VoiD/vmulti-bin/releases/download/v1.0/VMulti.Driver.zip)
* Right click on VMulti.Driver.zip and select **Extract All**
* This will create folder called **VMulti.Driver**&#x20;
* Copy the VMulti.Driver folder to the C:\OpenTabletDriver
* Start a CMD shell running with Administrator privileges and CD to the C:\OpenTabletDriver\VMulti.Driver folder&#x20;
* run **install\_hiddriver.bat**&#x20;
  * NOTE: This bat file - if needed - may restart your computer without warning. So, close any applications and save any docs before you run this .bat file.

## Install the .NET Runtime&#x20;

* OTD requires a specific version of the .NET Runtime
* You can directly download and installed the version of .NET Runtime needed by downloading it from this link: [https://opentabletdriver.net/framework](https://opentabletdriver.net/framework)&#x20;

## Install OpenTabletDriver

NOTE: Strictly speaking, OTD is not "installed" like a typical application. Instead it is simply downloaded and can be run from any location.&#x20;

* Download **OpenTabletDriver.win-x64.zip** from [https://github.com/OpenTabletDriver/OpenTabletDriver/releases/latest/download/OpenTabletDriver.win-x64.zip](https://github.com/OpenTabletDriver/OpenTabletDriver/releases/latest/download/OpenTabletDriver.win-x64.zip)
* Move this zip file to your **Documents** folder&#x20;
* Right-click on **OpenTabletDriver.win-x64.zip** and click **Extract All**
* This will create a folder called **OpenTabletDriver.win-x64** that contains two files:
  * OpenTabletDriver.UX.Wpf.exe
  * OpenTabletDriver.Daemon.exe
* Copy the **OpenTabletDriver.win-x64** folder to c:\OpenTabletDriver&#x20;

## Launch OpenTabletDriver for the first time

* Launch **OpenTabletDriver.UX.Wpf.exe**
  * If you see a message that .NET 6 Desktop Runtime X64 is not installed, then follow its instructions to install that runtime. Then launch OpenTabletDriver.UX.Wpf.exe.
  * This message does not always come up, so I recommend that you install the .NET Runtime before you use OTD.
* You will likely be greeted by a window titled **OpenTabletDriver Guide**.&#x20;
  * Click the X in the upper right hand corner to close the guide.
  * You can get back to this guide at any time in OTD by navigating to **Help** > **Show guide**.
* If the OTD UI is running you will see it in the notification area on your taskbar

![](<../../../.gitbook/assets/image (146).png>)![](<../../../.gitbook/assets/image (103).png>)

## **Detect your tablet**

* OTD will automatically try to detect your tablet
* The tablet will be shown in the Window title at the top
* To force detection click **Tablets** > **Detect tablet**

## Checkpoint #1

* **Should work**
  * OTD should detect your tablet is there and which model it is
  * OTD should be able to detect the pen position
* **Does not work yet**
  * tablet buttons
  * pen buttons
  * pressure pressure
  * pen tilt

## Install the Windows Ink plugin

* In the OTD app, navigate to **Plugins** > **Open Plugin Manager**
* Click on the **Windows Ink** plugin , then click **Install**&#x20;
* The Windows Ink plugin will appear at the top of the plugin list
* Close the **Plugin Manager** window

## Configure tablet to display mapping

* In the OTD App, go to **Output** > **Tablet** Section
* In **Output** > **Display**, right-click anywhere and pick **Set to Display** \<displayname> where \<displayname> is specific display you want to use with the tablet.
* In **Output > Tablet**, right click anywhere, and then select **Lock Aspect Ratio**.
* ![](<../../../.gitbook/assets/image (9).png>)

## Configure Windows Ink

* In the OTD app, on the bottom left there will a drop down that specifies the "mode" OTD is running in
* By default it is set to **Absolute Mode**
* Change it to **Windows Ink Absolute Mode**
  * If you leave it set to Absolute Mode, you will not be able to take advantage of pressure sensitivity and tilt.
  * NOTE: You will only see Windows Ink Absolute Mode listed if you previously enabled the Windows Ink plugin.

![](<../../../.gitbook/assets/image (85).png>)

## Configure the pen

### Overview

* In the OTD app, navigate to the **Pen Settings** tab
* To summarize, you'll want your Pen Settings to look like this:

<figure><img src="../../../.gitbook/assets/image (296).png" alt=""><figcaption></figcaption></figure>





| Setting                               | Value                                                                                                                      |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Tip Settings** >**Tip Binding**     | <p><strong>Type</strong> -> <strong>Windows Ink</strong></p><p><strong>Button</strong> -> <strong>Pen Tip</strong></p>     |
| **Pen Buttons** > **Pen Binding 1**   | <p><strong>Type</strong> -> <strong>Windows Ink,</strong></p><p><strong>Button</strong> -> <strong>Pen Button</strong></p> |
| **Pen Buttons** > **Pen Binding 2**   | <p><strong>Type</strong> -> <strong>Windows Ink</strong></p><p><strong>Button</strong> -> <strong>Pen Button</strong></p>  |
| **Eraser Settings > Eraser Bindings** | <p><strong>Type</strong> -> <strong>Windows Ink</strong></p><p><strong>Button</strong> -> <strong>Pen Tip</strong></p>     |

At the bottom of the OTD UI, click **Apply**.

## Tablet buttons

* OTD does support buttons on your tablet.&#x20;
* In the **Auxiliary Settings** tab, each button shows up as an **Auxiliary Binding**.
* ![](<../../../.gitbook/assets/image (302).png>)
* In the screenshot above one of the buttons has been set to match the "e" key.

## Save OpenTabletDriver configuration

* Click **Save** at the bottom
* Click **Apply** at the bottom

## Minimize the OpenTabletDriver app

* You don't have to keep the OTD app visible all the time, you can minimize the app at any time
* If you need to open OTD app again, you can find it in the taskbar

![](<../../../.gitbook/assets/image (181).png>)

## Checkpoint #2

* **Should work**
  * OTD should know your tablet is there and which model it is
  * OTD should be able to detect the pen position
  * tablet buttons
  * pen buttons
  * pressure pressure
  * pen tilt

## Verify everything works in Krita

* Download and install Krita from https://krita.org/&#x20;
* Launch Krita
* Go to **Settings** > **Configure Krita > Tablet settings > Tablet Input API**
* Select the **Windows Ink** option (not the **WinTab** option)
* Click **OK**
* Restart Krita (You MUST restart Krita)
* Create a new document
* Pick a brush that supports pressure sensitivity
* Start drawing and verify the brush responds to pressure.

## Configure your drawing application to use Windows Ink

* The specific instructions vary per app.&#x20;
* Instructions for specific apps: [Configure Windows Ink for apps](../../windows/windows-ink/configure-windows-ink-for-apps.md)

## Automatically start OpenTabletDriver when Windows starts

* Right click on OpenTabletDriver.UX.Wpf.exe
* Select **Create Shortcut**
* Right click on the shortcut, Select Properties
* Under **Run**, Select **Minimized**
* Click **OK**
* Press WINDOWS+R to bring up the **Run** window
* In **Open**, enter **shell:startup**
* This will open a new Explorer window pointing to a folder called **Startup**
* &#x20;Move the OTD shortcut to the **Startup** folder in that explorer window

## Configure Pressure curve

By default OTD does not use a pressure curve to modify how the pressure data is interpreted. However, you can edit the pressure curve by following these instructions: [Pressure curve OpenTabletDriver](opentabletdriver-pressure.md)

## Configure Smoothing

By default OTD performs no smoothing on the pen data. This is desirable because&#x20;

* it gives you a VERY responsive drawing experience
* Gives you complete control about the smoothing

### Application-level smoothing

To add smoothing back in to your drawing, your first and easiest option is to use the smoothing features in your drawing application.

Learn more here: [**Configure smoothing in applications**](../../drawing/configure-smoothing-in-applications.md)&#x20;

### Driver-level smoothing&#x20;

More here: [**Smoothing with OpenTabletDriver**](opentabletdriver-smoothing.md)&#x20;

## Appendix

### Uninstalling

See the instructions here: [Uninstalling OpenTabletDriver on Windows](uninstalling-opentabletdriver-on-windows.md)

### More about pen buttons

You can bind the pen buttons to several kinds of actions:

![](<../../../.gitbook/assets/image (14).png>)

* **Mouse Button Binding** is not supported
* **Key Binding** is supported
* **Multi-Key Bindings** is supported
* **Windows Ink Bindings** are supported

For **Windows Ink** here are the options:

&#x20;![](<../../../.gitbook/assets/image (239).png>)

If you specify **Pen Button**, the effective behavior you will get in an application is a mouse right-click.

### Application data directory

* OTD stores information in its application data directory
* More here: [OpenTabletDriver application data directory](opentabletdriver-application-data-directory.md)
* If you are doing more advanced things with OTD you should be familiar with this folder.

## Resources

* r/huion - [OpenTablet Driver guide for Huion Kamvas 24 4k on windows 10 (but maybe other tablets too) in particular for paintin](https://www.reddit.com/r/huion/comments/17q61pl/opentablet\_driver\_guide\_for\_huion\_kamvas\_24\_4k\_on/)g 2023/11/07&#x20;
