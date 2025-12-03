# Install OpenTabletDriver on Windows+

## **Overview**

This document is for CREATIVES interested in using OpenTabletDriver on Windows and need features such as pressure sensitivity and tilt.

{% hint style="info" %}
If you don't know much about OpenTabletDriver, read this introduction first: [**OpenTabletDriver**](./).&#x20;

You should also familiarize yourself with these [**usage notes for OpenTabletDriver**](opentabletdriver-usage-notes.md).

For information on how to install on Windows: [Installing OpenTabletDriver on Windows](opentabletdriver-windows.md)&#x20;

For information on how to uninstall on Windows: [Uninstalling OpenTabletDriver on Windows](uninstalling-opentabletdriver-on-windows.md)&#x20;
{% endhint %}

{% hint style="info" %}
What follows are the detailed steps I personally use to install OTD on Windows. This document **does not** replace the official OTD documentation ([https://opentabletdriver.net/Wiki](https://opentabletdriver.net/Wiki)
{% endhint %}

### Some expertise is required

Using OTD for doing artwork is an advanced scenario. You should try only if you are confident in your technical skills or can get someone to help you.

### **Supported tablets**

* OTD supports many (300+ as of November 2025) tablets but not all of them.&#x20;
* Consult the complete list here: [https://opentabletdriver.net/Tablets](https://opentabletdriver.net/Tablets)
* In that list, your tablet may be marked as needing "Zadig WinUSB". There are special requirements for this case. My instructions here DO NOT include those instructions.

### OTD version

* The instructions cover this specific version of OTD: v0.6.6.2

### Supported Windows versions

* These instructions are for Windows x64 systems only.&#x20;
* OTD does not support 32-bit versions of Windows.
* OTD does NOT support ARM on Windows
* I tested these instructions on Windows 11 (Version 10.0.26200 Build 26200) on 2025/11/20

## STEP 1: Uninstall existing tablet drivers

{% hint style="danger" %}
<mark style="color:red;">You</mark> <mark style="color:red;"></mark><mark style="color:red;">**MUST**</mark> <mark style="color:red;"></mark><mark style="color:red;">uninstall any existing tablet drivers on your computer. If you leave them installed they will interfere with OTD.</mark>
{% endhint %}

* Follow the instructions here: [**Uninstalling tablet drivers**](../../../basics/uninstalling-tablet-drivers.md)&#x20;
* To ensure nothing remains, use the [**Tablet driver cleanup tool**](../tablet-driver-cleanup-tool.md).

## STEP 2: Create a folder for OTD

* Create a folder somewhere on your computer called "OpenTabletDriver".&#x20;
* I prefer to use `C:\OpenTabletDriver`&#x20;
* All the instructions in this document will use `C:\OpenTabletDriver`&#x20;

## STEP 3: Install the VMulti driver

{% hint style="danger" %}
<mark style="color:red;">You MUST install</mark> <mark style="color:red;"></mark><mark style="color:red;">**VMulti driver**</mark> <mark style="color:red;"></mark><mark style="color:red;">if you want pressure sensitivity & tilt to work with your tablet on Windows.</mark>
{% endhint %}

* Download **VMulti.Driver.zip** from this location:
  * [https://github.com/X9VoiD/vmulti-bin/releases/download/v1.0/VMulti.Driver.zip](https://github.com/X9VoiD/vmulti-bin/releases/download/v1.0/VMulti.Driver.zip)
* Copy the zip  file to`C:\OpenTabletDriver`&#x20;
* Right-click the zip file, then select **Extract All**. This creates a `VMulti.Driver` folder .&#x20;
* WARNING This next step file may restart your computer without warning. So, close any applications and save any docs before before the next step.&#x20;
* In the `VMulti.Driver` folder, right click on `install_hiddriver.bat`, then select **Run as Administrator**
  * NOTE: This bat file may restart your computer without warning. So, close any applications and save any docs before you run it.

## STEP 4: Install the .NET Runtime&#x20;

* OTD requires a specific version of the .NET Runtime to be installed on your computer. It won't work otherwise.
* Click on this link [https://opentabletdriver.net/Framework](https://opentabletdriver.net/Framework) to download the version that OTD needs.
* Once it is downloaded, then install it.

## STEP 5: Download and extract OpenTabletDriver

* Open a browser to this location:
  * [https://github.com/OpenTabletDriver/OpenTabletDriver/releases/latest](https://github.com/OpenTabletDriver/OpenTabletDriver/releases/latest)
* Look for a file with a name like this OpenTabletDriver-0.6.6.2\_win-x64.zip, and download it.
* Move the zip file into the  `C:\OpenTabletDriver`  folder
* Right-click on the zip file, then select **Extract All**. This creates a folder with a name like OpenTabletDriver-0.6.6.2\_win-x64&#x20;

## STEP 6: Launch the OpenTabletDriver app for the first time

* In the `C:\OpenTabletDriver\OpenTabletDriver-n.n.n.n_win-x64` folder, `launch OpenTabletDriver.UX.Wpf.exe`. This launches the OTD application.
* DO NOT launch the OTD app with "Run as Administrator". This will cause problems with OTD.
* If you see a message that ".NET X Desktop Runtime X64 is not installed", then follow its instructions to install that runtime. Then launch `OpenTabletDriver.UX.Wpf.exe` again. This message does not always come up, so I recommend that you install the .NET Runtime before you use OTD.
* The **OpenTabletDriver Guide** may automatically start&#x20;
  * Click the X in the upper right hand corner to close the guide.
  * You can get back to this guide at any time in OTD by navigating to **Help** > **Show guide**.
* When the OTD app is running, this icon will appear in your taskbar

<figure><img src="../../../.gitbook/assets/image (134).png" alt="" width="375"><figcaption></figcaption></figure>

## **STEP 7: Understanding the OTD app**

**For you to use OTD on Windows the OTD app MUST always be running.**

**Although it must always be running , You don't have to always have the visible on your screen, you can  minimize the app and find it later in the task bar.**

## **STEP 8: Detect your tablet with OTD**

* When the OTD app starts, it will automatically try to detect your tablet a
* The tablet will be shown in the Window title at the top and at the bottom left of the application window
* If needed, you can force detection click **Tablets** > **Detect tablet**

## **STEP 9: Checkpoint**

At this point, moving the pen on the tablet should move the mouse pointer.

Do not worry about which monitor the mouse is on. We will cover that soon.

Pressure and will not work right now. We will cover that soon.&#x20;

## STEP 10: Configure tablet to display mapping

* In the OTD App, go to **Output** > **Tablet** Section
* In **Output** > **Display**, right-click anywhere and pick **Set to Display** \<displayname> where \<displayname> is specific display you want to use with the tablet.
* In **Output > Tablet**, right click anywhere, and then select **Lock Aspect Ratio**.
* ![](<../../../.gitbook/assets/image (173).png>)
* At this point moving the pen will move the pointer on exactly 1 display.&#x20;
* Also there will be no stroke distortion - for example a circle on tablet makes a circle on the monitor with no distortion/stretching
* Press APPLY and then press SAVE.&#x20;



## STEP 11: Understanding APPLY and SAVE&#x20;

The instructions have already asked you to press APPLY and SAVE. Let's take a moment to understand these actions a bit better.

SAVE

* SAVE will save current settings, even if you haven't clicked apply and loads them the next time you open OTD.&#x20;
* You can test this out by clicking SAVE without clicking APPLY applying and starting the OTD app again. It will load the settings that were saved.

APPLY

* APPLY will load the current settings you have set in the user interface. Until you click APPLY no changes you have made in the UI will be in effect.

To keep things simple for you for now, I suggest you always click APPLY then SAVE whenever you make a change in the OTD app.

## STEP 12: Install the Windows Ink plugin

* In the OTD app, navigate to **Plugins** > **Open Plugin Manager**
* Click on the **Windows Ink** plugin, then click **Install**&#x20;
* The Windows Ink plugin will appear at the top of the plugin list
* Close the **Plugin Manager** window

## STEP 13: Configure Windows Ink mapping mode

* In the OTD app, on the bottom, change the **mode** dropdown:
  * from **Absolute Mode**&#x20;
  * to **Windows Ink Absolute Mode**
  * click **APPLY** then click **SAVE**&#x20;

{% hint style="info" %}
NOTE: You will only see **Windows Ink Absolute Mode** listed if you previously enabled the Windows Ink plugin.
{% endhint %}

## STEP 13: Configure the pen

Navigate to the **Pen Settings** tab

By default the will be configured as shown below

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

What to notice here: The tip settings, eraser settings, and the buttons have been configured "Adaptive Binding". For now leave these alone.

Click **SAVE** and **APPLY**.

NOTE: You cannot assign the pen buttons to take MOUSE actions such as right-click and left-click, etc.



## STEP 14: Configure your drawing application to use Windows Ink

* The specific instructions vary per app.&#x20;
* Instructions for specific apps: [Configure Windows Ink for apps](../../operating-systems/windows/windows-ink/configure-windows-ink-for-apps.md)

## STEP 15: Checkpoint

At this point you should be able to effectively draw with OTD. Pressure and Tilt should work.

I suggest you install Krita and configure it to use Windows Ink&#x20;

Try some basic drawing and see if everything is working

## STEP 16: Optional customization

### Automatically start OpenTabletDriver when Windows starts \[OPTIONAL]

* Right-click on OpenTabletDriver.UX.Wpf.exe
* Select **Create Shortcut**
* Right click on the shortcut, then select **Properties**
* Under **Run**, select **Minimized**
* Click **OK**
* Press WINDOWS+R to bring up the **Run** window
* In **Open**, type `shell:startup`
* This will open a new Explorer window pointing to a folder called **Startup**
* Move the shortcut to the **Startup** folder in that explorer window

### Pressure curves

By default OTD does not use a pressure curve to modify how the pressure data is interpreted. However, you can edit the pressure curve by following these instructions: [Pressure curves in OpenTabletDriver](opentabletdriver-pressure.md)

### Smoothing

By default OTD performs no smoothing on the pen data. This is desirable because&#x20;

* it gives you a VERY responsive drawing experience
* Gives you complete control about the smoothing

Two ways to introduce smoothing

* **Application-level smoothing** - To add smoothing back in to your drawing, your first and easiest option is to use the smoothing features in your drawing application. Learn more here: [**Configure smoothing in applications**](../../drawing/configure-smoothing-in-applications.md)&#x20;
* **Driver-level smoothing in OTD** - this will be a little more complex to do. More here: [**Smoothing with OpenTabletDriver**](opentabletdriver-smoothing.md)&#x20;

### Configure tablet buttons

* Open the **Auxiliary Settings** tab
* each button shows up as an **Auxiliary Binding**.
* In the screenshot above, one of the buttons has been set to match the "e" key.

<figure><img src="../../../.gitbook/assets/image (689).png" alt="" width="563"><figcaption></figcaption></figure>

### Display toggle

To allow rapid switching between monitors you have two options:

* the **Monitor toggle** plug-in - I've never used this plug-in so I don't have any instructions for it.
* Switching presets - a hotkey can be used to switch between presets

## Other topics

### Uninstalling OTD

See the instructions here: [Uninstalling OpenTabletDriver on Windows](uninstalling-opentabletdriver-on-windows.md)

### OTD application data directory

No matter where OpenTabletDriver is installed, when it is running, it will put its data into a user-specific application data folder on Windows.

The location of the folder is here:&#x20;

`%localappdata%\OpenTabletDriver` &#x20;

This expands to a path that should look like:

`C:\Users\username\AppData\Local\OpenTabletDriver`

This is what my folder looks like:

<figure><img src="../../../.gitbook/assets/image (315).png" alt=""><figcaption></figcaption></figure>

ProTip: Quickly get to the AppData folder by pressing WINDOWS+R and typing appdata. It will open a window directly to that folder.

![](<../../../.gitbook/assets/image (196).png>)





dd
