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

## **STEP 1: Prepare a folder to keep OTD in**

* Create a folder somewhere on your computer called "OpenTabletDriver".&#x20;
* The examples in this doc use `C:\OpenTabletDriver`&#x20;

## STEP 2: Uninstall existing tablet drivers

{% hint style="info" %}
You MUST uninstall any existing tablet drivers on your computer. If you leave them installed they will interfere with OTD.
{% endhint %}

* Follow the instructions here: [**Uninstalling tablet drivers**](../../../basics/uninstalling-tablet-drivers.md)&#x20;
* Some tablet drivers leave bits of themselves installed, even after an uninstallation process. To ensure nothing remains, use the [**Tablet driver cleanup tool**](../tablet-driver-cleanup-tool.md).

## STEP 2: Install the VMulti driver

<mark style="color:red;">You MUST install</mark> <mark style="color:red;"></mark><mark style="color:red;">**VMulti driver**</mark> <mark style="color:red;"></mark><mark style="color:red;">if you want pressure sensitivity & tilt to work with your tablet on Windows.</mark>

* Download **VMulti.Driver.zip** from: [https://github.com/X9VoiD/vmulti-bin/releases/download/v1.0/VMulti.Driver.zip](https://github.com/X9VoiD/vmulti-bin/releases/download/v1.0/VMulti.Driver.zip)
* Right-click the zip file and select **Extract All**. This will create folder called **VMulti.Driver**.&#x20;
* Copy the `VMulti.Driver` folder to the **`C:\OpenTabletDriver`**.
* Right click on `install_hiddriver.bat` and select **Run as Administrator**
  * NOTE: This bat file may restart your computer without warning. So, close any applications and save any docs before you run it.

## STEP 3: Install the .NET Runtime&#x20;

* OTD requires a specific version of the .NET Runtime to be installed on your computer. It won't work otherwise.
* Click on this link [https://opentabletdriver.net/Framework](https://opentabletdriver.net/Framework) to download the version that OTD needs. Then install it.

## STEP 4: Download and extract OpenTabletDriver

* Download [**OpenTabletDriver.win-x64.zip**](https://github.com/OpenTabletDriver/OpenTabletDriver/releases/latest/download/OpenTabletDriver-0.6.5.1_win-x64.zip)&#x20;
* Put the OTD zip file intp your **Documents** folder&#x20;
* Right-click on `OpenTabletDriver.win-x64.zip`, then select **Extract All**. This creates a folder called `OpenTabletDriver.win-x64`.
* Copy the `OpenTabletDriver.win-x64` folder to `c:\OpenTabletDriver`.&#x20;

## STEP 5: Launch the OpenTabletDriver app for the first time

* In the `C:\OpenTabletDriver\OpenTabletDriver.win-x64` folder, `launch OpenTabletDriver.UX.Wpf.exe`. This launches the OTD application.
* If you see a message that ".NET X Desktop Runtime X64 is not installed", then follow its instructions to install that runtime. Then launch `OpenTabletDriver.UX.Wpf.exe` again. This message does not always come up, so I recommend that you install the .NET Runtime before you use OTD.
* The **OpenTabletDriver Guide** may automatically start&#x20;
  * Click the X in the upper right hand corner to close the guide.
  * You can get back to this guide at any time in OTD by navigating to **Help** > **Show guide**.
* When the OTD app is running, this icon will appear in your taskbar

<figure><img src="../../../.gitbook/assets/image (70).png" alt="" width="188"><figcaption></figcaption></figure>

## **STEP 6: Detect your tablet with OTD**

* OTD will automatically try to detect your tablet
* The tablet will be shown in the Window title at the top
* If needed, you can force detection click **Tablets** > **Detect tablet**

## STEP 7: Install the Windows Ink plugin

* In the OTD app, navigate to **Plugins** > **Open Plugin Manager**
* Click on the **Windows Ink** plugin, then click **Install**&#x20;
* The Windows Ink plugin will appear at the top of the plugin list
* Close the **Plugin Manager** window

## STEP 8: Configure tablet to display mapping

* In the OTD App, go to **Output** > **Tablet** Section
* In **Output** > **Display**, right-click anywhere and pick **Set to Display** \<displayname> where \<displayname> is specific display you want to use with the tablet.
* In **Output > Tablet**, right click anywhere, and then select **Lock Aspect Ratio**.
* ![](<../../../.gitbook/assets/image (108).png>)

## STEP 8: Configure Windows Ink

* In the OTD app, on the bottom, change the **mode** dropdown from **Absolute Mode** to **Windows Ink Absolute Mode**

{% hint style="info" %}
NOTE: You will only see **Windows Ink Absolute Mode** listed if you previously enabled the Windows Ink plugin.
{% endhint %}

![](<../../../.gitbook/assets/image (184).png>)

## STEP 9: Configure the pen

### Overview

* In the OTD app, navigate to the **Pen Settings** tab
* To summarize, you'll want your Pen Settings to look like this:

<div align="left"><figure><img src="../../../.gitbook/assets/image (395).png" alt="" width="375"><figcaption></figcaption></figure></div>



| Setting                               | Value                                                                                                                      |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Tip Settings** >**Tip Binding**     | <p><strong>Type</strong> -> <strong>Windows Ink</strong></p><p><strong>Button</strong> -> <strong>Pen Tip</strong></p>     |
| **Pen Buttons** > **Pen Binding 1**   | <p><strong>Type</strong> -> <strong>Windows Ink,</strong></p><p><strong>Button</strong> -> <strong>Pen Button</strong></p> |
| **Pen Buttons** > **Pen Binding 2**   | <p><strong>Type</strong> -> <strong>Windows Ink</strong></p><p><strong>Button</strong> -> <strong>Pen Button</strong></p>  |
| **Eraser Settings > Eraser Bindings** | <p><strong>Type</strong> -> <strong>Windows Ink</strong></p><p><strong>Button</strong> -> <strong>Pen Tip</strong></p>     |

At the bottom of the OTD app, click **Apply**.

## STEP 10: Configure tablet buttons

* In the **Auxiliary Settings** tab, each button shows up as an **Auxiliary Binding**.
* ![](<../../../.gitbook/assets/image (401).png>)
* In the screenshot above, one of the buttons has been set to match the "e" key.

## STEP 11: Save the OTD configuration

* Click **Save** at the bottom
* Click **Apply** at the bottom

## STEP 12: Minimize the OTD app

* You don't have to keep the OTD app visible all the time, you can minimize the app at any time
* If you need to open OTD app again, you can find it in the taskbar

![](<../../../.gitbook/assets/image (280).png>)

## STEP 13: Configure your drawing application to use Windows Ink

* The specific instructions vary per app.&#x20;
* Instructions for specific apps: [Configure Windows Ink for apps](../../operating-systems/windows/windows-ink/configure-windows-ink-for-apps.md)

## STEP 14: Automatically start OpenTabletDriver when Windows starts \[OPTIONAL]

* Right-click on OpenTabletDriver.UX.Wpf.exe
* Select **Create Shortcut**
* Right click on the shortcut, then select **Properties**
* Under **Run**, select **Minimized**
* Click **OK**
* Press WINDOWS+R to bring up the **Run** window
* In **Open**, type `shell:startup`
* This will open a new Explorer window pointing to a folder called **Startup**
* Move the shortcut to the **Startup** folder in that explorer window

## STEP 15: Customizing your experience

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

## Display toggle

To allow rapid switching between monitors you have two options:

* the **Monitor toggle** plug-in
* Swiching presets
  * NOTE: The ability to use a hotkey to switch presents is expect to arrive by Oct 2025.

## Uninstalling OTD

See the instructions here: [Uninstalling OpenTabletDriver on Windows](uninstalling-opentabletdriver-on-windows.md)

## Resources

* r/huion - [OpenTablet Driver guide for Huion Kamvas 24 4k on windows 10 (but maybe other tablets too) in particular for painting](https://www.reddit.com/r/huion/comments/17q61pl/opentablet_driver_guide_for_huion_kamvas_24_4k_on/) 2023/11/07&#x20;
