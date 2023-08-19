# Using OpenTabletDriver on Windows

## **Overview**

This document is for creatives that meet three criteria:

* they use drawing tablets on Microsoft Windows with applications that can use Windows Ink API such as Clip Studio Paint, Krita, Photoshop, etc.&#x20;
* they need creative features such as pressure sensitivity, tilt, etc.
* they cannot use the drivers from tablet manufacturer.

## Introduction to OpenTabletDriver

Read this first: [**OpenTabletDriver**](./)&#x20;

## How does this document relate to the OpenTabletDriver documentation?

This document describes the detailed steps I follow to setup OpenTabletDriver on Windows for drawing and my usage notes about the process.

This document **does not** replace the OpenTabletDriver documentation ([https://opentabletdriver.net/Wiki](https://opentabletdriver.net/Wiki))

## Skills required

Using OpenTabletDriver for doing artwork is an advanced scenario. You should try only if you are confident in your technical skills or can get someone to help you.

## **Windows Pen APIs**

There are two Pen APIs in the Windows ecosystem:

* WinTAB - an older "standard"
* Windows Ink - a built-in feature of Microsoft Windows

OpenTabletDriver does support **Windows Ink**.

OpenTabletDriver does NOT support **WinTab**.&#x20;

As of 2023:

* Most creative apps support Windows Ink and WinTab.&#x20;
* Some apps - for example Microsoft OneNote - only support Windows Ink.&#x20;
* A few apps - usually very old ones - only support WinTab.&#x20;

The apps that are known to support Windows Ink include:

* Clip Studio Paint
* Krita
* Photoshop
* Illustrator

## **Known issues**

* If you want pressure sensitivity, tilt, etc. - you must **you MUST configure OpenTabletDriver to use Windows Ink** and configure your apps to also use Windows Ink.&#x20;
* You must completely **uninstall existing tablet drivers** on your machine. OpenTabletDriver will not work correctly if there are any remnants of other tablet drivers.
* There are some restrictions on what you can bind the pen buttons to. These are described later in the doc.
* <mark style="color:red;">**DO NOT run OpenTabletDriver as administrator**</mark>. It will not work correctly if you do.
* OpenTabletDriver **does not support touch input**.
* OpenTabletDriver **does not support tablet dials**.
* OpenTabletDriver **does not support pen barrel rotation**.

## Usage notes

### System vs application settings

Many manufacturer drivers support having a setting for your entire system and a setting for specific applications. Wacom, Huion, and XP-Pen all support this is their drivers.

For example, you can change have a pen button be a right click for all applications but be a double-click for Krita.

However, OpenTabletDriver only supports system-wide settings. So any settings in OpenTabletDriver will affect EVERY applications.&#x20;

### Pen hover height

By default, OpenTabletDriver **has no restriction on the hover height of your pen**. Most drivers impose an artificial limit of about 10mm for a pen. But you'll often find with OpenTabletDriver that the hover height is increased substantially.&#x20;

The maximum hover height is dependent on the specific model of tablet involved. For example with a Wacom Intuos Pro (PTH-860) my hover height goes from 10mm with the Wacom Driver to 20mm with Open Tablet driver.

You can install a plug-in to control the hover height and have whatever limit you want.

### Installation

Technically, OpenTabletDriver isn't "installed". It's just a tool that you can download and run from any location on your computer. &#x20;

## **Supported tablets**

Although OpenTabletDriver supports many tablets, it does not support all of them.

Consult the list here to verify that your tablet is supported by OpenTabletDriver: [https://opentabletdriver.net/Tablets](https://opentabletdriver.net/Tablets)

In that list, your tablet may be marked as needing "Zadig WinUSB". If so, you will also have to install that component. I do not have any drawing tablets that require Zdig WinUSB so using Zadig WinUSB is NOT covered in this document.

## <mark style="color:red;">**Warning about manufacturer support**</mark>

<mark style="color:red;">**Your tablet manufacturer WILL NOT help or support you in any way when you are using OpenTabletDriver instead of their own drivers.**</mark>&#x20;

## If you need help, join the OpenTabletDriver Discord server

* DO join the OTD Discord server: [https://opentabletdriver.net/Discord](https://opentabletdriver.net/Discord)&#x20;
* DO ask questions in the `#support-windows` channel
* DO NOT ask for support via DMs.

## Important notes

* These instructions are for x64 operating systems only
* The instructions cover this specific version of OTD: v0.6.1.0
* I only tested this on these versions of Windows:
  * Windows 11 64bit (version 10.0.22621)
  * Windows 10 64bit &#x20;
* You MUST enable **Windows Ink** in **OpenTabletDriver** and your drawing applications if you want to use features like pressure sensitivity, tilt, etc.
* You MUST install a driver called **VMulti** in order to use Windows Ink with OpenTabletDriver.
* Installing VMulti requires administrator permissions on your PC.
* OTD works with many tablets, but not all. Please see [**this list of tablets that OTD supports**](https://opentabletdriver.net/Tablets).
* To validate everything working this document uses the Krita painting app. But you can use any app you want.

## **Preparation**

* Uninstall any existing tablet drivers (Wacom, XP-Pen, Huion, etc.)
* NOTE: Uninstalling may require a restart of your system. So get this out of the way before you proceed with the next steps.
* Download and install Krita from https://krita.org/&#x20;

## Uninstalling manufacturer tablet drivers

In order to use OpenTabletDriver, you MUST completely uninstall any other tablet device drivers.

Follow this guide: [Uninstalling manufacturer tablet drivers](../uninstalling-manufacturer-tablet-drivers.md)

## Installing VMulti

* **VMulti** is a prerequisite for using **OpenTabletDriver** correctly on Windows for drawing applications.
* Go to [https://github.com/X9VoiD/vmulti-bin/releases/tag/v1.0](https://github.com/X9VoiD/vmulti-bin/releases/tag/v1.0)&#x20;
* Scroll down on the page, under **Assets** you'll see a file called **Driver.zip**
* Download **Driver.zip**
* Rename Driver.zip to VMulti\_Driver.zip&#x20;
  * NOTE: This renaming step is it make it easier to keep track of these files later
* Move VMulti\_Driver.zip to your Documents folder
* Right click on VMulti\_Driver.zip and select Extract All
* This will create a folder called VMulti\_Driver that contains two folders **32** and **64**
* Right click on the **64** folder and select **Open in Terminal** &#x20;
* The terminal will launch and the current directory will be set to the 64 folder
* run **install\_hiddriver.bat**&#x20;
  * NOTE: this bat file if needed will restart your computer without warning. So close any applications and save any docs before you run this .bat file.

## Installing the version of .NET Runtime needed by OpenTabletDriver

OpenTabletDriver requires a specific version of the .NET Runtime

You can directly download and installed the version of .NET Runtime needed by downloading it from this link: [https://opentabletdriver.net/framework](https://opentabletdriver.net/framework)&#x20;

## Installing OpenTabletDriver

NOTE: Strictly speaking, OpenTabletDriver is not "installed" like a typical application. Instead it is simply downloaded and can be run from any location.&#x20;

* Download **OpenTabletDriver.win-x64.zip** from [https://opentabletdriver.net/Release/Download/OpenTabletDriver.win-x64.zip](https://opentabletdriver.net/Release/Download/OpenTabletDriver.win-x64.zip)&#x20;
* Move this zip file to your **Documents** folder&#x20;
* Right-click on **OpenTabletDriver.win-x64.zip** and click **Extract All**
* This will create a folder called **OpenTabletDriver.win-x64** that contains two files:
  * OpenTabletDriver.UX.Wpf.exe
  * OpenTabletDriver.Daemon.exe
* Launch **OpenTabletDriver.UX.Wpf.exe**
  * If this gives you a message that .NET 6 Desktop Runtime X64 is not installed, then follow its instructions to install that runtime. The installation is quick. Then re-launch OpenTabletDriver.UX.Wpf.exe.
  * This message does not always come up, so I recommend that you install the .NET Runtime before you use OpenTabletDriver.
* You will likely be greeted by a window titled **OpenTabletDriver Guide**.&#x20;
  * If you want to learn about OpenTabletDriver keep clicking **Next** and then finally **Close**.&#x20;
  * If this is your first time with OpenTabletDriver, I highly suggest reading through this guide.&#x20;
  * You can close this window at anytime by clicking X in the upper right hand corner of the window.
  * You can get back to this guide at any time in OpenTabletDriver by navigating to **Help** > **Show guide**.
* If the OpenTablerDriver UI is running you will see it in the notification area on your taskbar
* ![](<../../../.gitbook/assets/image (146).png>)
* ![](<../../../.gitbook/assets/image (103).png>)

## **Detecting your Tablet**

* OpenTabletDriver will automatically try to detect your tablet
* The tablet will be shown in the Window title at the top
* But if you want to force it to detect or re-detect Click **Tablets** > **Detect tablet**

## Checkpoint #1

* **Should work**
  * Open Tablet Driver should know your tablet is there and which model it is
  * OTD should be able to detect the pen position
* **Does not work yet**
  * tablet buttons
  * pen buttons
  * pressure pressure
  * pen tilt

## Installing the Windows Ink plugin in OpenTabletDriver

* In the OpenTabletDriver app, navigate to **Plugins** > **Open Plugin Manager**
* You will see a list of plug-ins
* Find the one called **Windows Ink**, click on it, then click **Install**&#x20;
* One you install it, the Windows Ink plugin will appear at the top of the plugin list
* Close the **Plugin Manager** window

## Configuring Tablet to Display Mapping

* In the OpenTabletDriver App
* In the the Output tab, in the **Tablet** Section
* Right click anywhere in theTablert section and then select **Lock Aspect Ratio**.
* In the the Output tab, in the **Display** Section, right-click anywhere in the **Display** section and select **Set to Display** and then select the specific display you want to use with the tablet.
* ![](<../../../.gitbook/assets/image (9).png>)

## Configuring Windows Ink in OpenTabletDriver

* In the OpenTabletDriver app, on the bottom left there will a drop down that specifies the "mode" OTD is running in
* By default it is set to **Absolute Mode**
* Change it to **Windows Ink Absolute Mode**
  * If you leave it set to Absolute Mode, you will not be able to take advantage of pressure sensitivity and tilt.
  * NOTE: You will only see Windows Ink Absolute Mode listed if you previously enabled the Windows Ink plugin
  * NOTE: "Relative mode" is equiavalent to "Mouse mode"

![](<../../../.gitbook/assets/image (85).png>)

## Configuring the Pen

### Overview

* In the OpenTabletDriver app, navigate to the **Pen Settings** tab
* To summarize, you'll want your Pen Settings to look like this:
* ![](<../../../.gitbook/assets/image (296).png>)

### Configuring the pen tip

* Under **Tip Settings**, next to **Tip Binding** click the THREE DOTS button
  * This opens up the **Advanced Binding Editor** window
  * Change **Type** to **Windows Ink**
  * Change **Button** to **Pen Tip**
  * Click **Apply**

### Configuring the pen buttons

* Under **Pen Buttons**, for each **Pen Button \<NUMBER>**&#x20;
  * Click the THREE DOTS button to open the **Advanced Binding Editor**. The binding editor assigns the button to perform a mouse right-click.
    * Change **Type** to **Windows Ink**
    * Change **Button** to **Pen Button**
    * Click **Apply**

### Configuring the eraser

* Under **Eraser Settings**
  * Next to **Eraser Bindings** click the THREE DOTS button to open the **Advanced Binding Editor**
    * Change **Type** to **Windows Ink**
    * Change **Button** to **Pen Tip**
    * Click **Apply**

## More about pen Buttons

You can bind the pen buttons to several kinds of actions:

![](<../../../.gitbook/assets/image (14).png>)

* **Mouse Button Binding** is not supported
* **Key Binding** is supported
* **Multi-Key Bindings** is supported
* **Windows Ink Bindings** are supported

For **Windows Ink** here are the options:

&#x20;![](<../../../.gitbook/assets/image (239).png>)

If you specify **Pen Button**, the effective behavior you will get in an application is a mouse right-click.

## Tablet Buttons

* OpenTabletDriver does support buttons on your tablet. For example, for a Wacom Intuos Pro Large (PTH-860) all eight button shows up in the **Auxiliary Settings** tab. Each button shows up as an **Auxiliary Binding** in this tab.
* ![](<../../../.gitbook/assets/image (302).png>)
* In the screenshot above one of the buttons has been set to match the "e" key.

## Saving OpenTabletDriver configuration

* Click **Save** at the bottom
* Click **Apply** at the bottom

## Minimize the OpenTabletDriver app

* Click the minimize on the OpenTabletDriver app
* If you need to find the OTD app again, you can find it in the taskbar in the area that is often called the "System Tray".
* ![](<../../../.gitbook/assets/image (181).png>)

## Checkpoint #2

* **Should work**
  * Open Tablet Driver should know your tablet is there and which model it is
  * OTD should be able to detect the pen position
  * tablet buttons
  * pen buttons
  * pressure pressure
  * pen tilt

## Configuration your drawing application

* Go to your drawing app and Enable Windows Ink for that app
* The specific instructions vary per app, but the next section will talk about Krita specifically

### Verifying it all works in Krita

* Download and install Krita from https://krita.org/&#x20;
* Launch Krita
* Go to **Settings** > **Configure Krita**
* Go to **Tablet settings**
* Under **Tablet Input API**
  * Select the Windows Ink option (not the WinTab option)
* Click **OK**
* Restart Krita
  * You MUST restart Krita
* Create a new document
* Pick a brush that supports pressure sensitivity
* Start drawing and verify the brush responds to pressure.

![](<../../../.gitbook/assets/image (271).png>)

## How to automatically start OpenTabletDriver when Windows starts

* Right click on OpenTabletDriver.UX.Wpf.exe
* Select **Create Shortcut**
* Right click on the shortcut, Select Properties
* Under **Run**, Select **Minimized**
* Click **OK**
* Press WINDOWS+R to bring up the **Run** window
* In **Open**, enter **shell:startup**
* This will open a new Explorer window pointing to a folder called **Startup**
* &#x20;Move the OTD shortcut to the **Startup** folder in that explorer window

## Pressure Curve

By default OpenTabletDriver does not use a pressure curve to modify how the pressure data is interpreted. However, you can edit the pressure curve by following these instructions: [Pressure curve OpenTabletDriver](opentabletdriver-smoothing-1.md)

## Smoothing

By default OpenTabletDriver performs no smoothing on the pen data. This is desirable because&#x20;

* it gives you a VERY responsive drawing experience
* Gives you complete control about the smoothing

### Application-level smoothing

To add smoothing back in to your drawing, your first and easiest option is to use the smoothing features in your drawing application.

Learn more here: [**Configure smoothing in applications**](../../drawing/configure-smoothing-in-applications.md)&#x20;

### Driver-level smoothing&#x20;

More here: [**Smoothing with OpenTabletDriver**](opentabletdriver-smoothing.md)&#x20;

## Uninstalling

### Stopping OpenTabletDriver from starting when your computer boots

* Press WINDOWS+R to bring up the **Run** window
* In Open, enter **shell:startup**
* Delete the OpenTabletDriver shortcut

### Uninstalling OpenTabletDriver

* If OpenTabletDriver processes are running, then stop them.
* You can use Task manager for stop the processes, or you can stop the processes with these two Powershell commands

```
stop-process -name OpenTabletDriver.UX.Wpf
stop-process -name OpenTabletDriver.Daemon
```

* Delete the folder that contains OpenTabletDriver

### Uninstalling VMulti

* Navigate to the folder that contains VMulti
* run **uninstall\_hiddriver.bat** as admin

## Application data directory

No matter where OpenTabletDriver is installed, when it is running, it will put its data into a user-specific application data folder on Windows.

The location of the folder is here in Windows: `%localappdata%\OpenTabletDriver` &#x20;

This expands to a path that should look like:

`C:\Users\username\AppData\Local\OpenTabletDriver`

This is what my folder looks like:

<figure><img src="../../../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### ProTip: Quickly get to the AppData folder by pressing WINDOWS+R and typing appdata.

It will open a window directly to that folder.

![](<../../../.gitbook/assets/image (32).png>)



###
