# Install OpenTabletDriver on Windows+

## **Overview**

This document is for CREATIVES interested in using OpenTabletDriver on Windows and need features such as pressure sensitivity and tilt.

{% hint style="info" %}
If you don't know about OpenTabletDriver or why you might want or need to use it, read: [**OpenTabletDriver**](./).&#x20;

Familiarize yourself with the [**My notes on OpenTabletDriver**](notes-on-opentabletdriver.md).

How to uninstall on Windows: [Uninstalling OpenTabletDriver on Windows](uninstalling-opentabletdriver-on-windows.md)&#x20;
{% endhint %}

{% hint style="info" %}
What follows are the detailed steps I personally use to install OTD on Windows. This document **does not** replace the official OTD documentation ([https://opentabletdriver.net/Wiki](https://opentabletdriver.net/Wiki)
{% endhint %}

### Some expertise is required

Using OTD for doing artwork is an advanced scenario. Try this only if you are confident in your technical skills or can get someone to help you.

### **Supported tablets**

* OTD supports 300+ tablets from different brands (as of November 2025)&#x20;
* Consult the complete list of supported tablets: [https://opentabletdriver.net/Tablets](https://opentabletdriver.net/Tablets)
* In that list, your tablet may be marked as needing "Zadig WinUSB". There are special requirements for this case. My instructions here DO NOT include those instructions.

### Version information

#### OTD version

* The instructions cover this specific version of OTD: v0.6.6.2

#### Windows versions

* These instructions are for Windows x64 systems only.&#x20;
* OTD does not support 32-bit versions of Windows.
* OTD does NOT support ARM on Windows
* I tested these instructions on Windows 11 (Version 10.0.26200 Build 26200) on 2025/11/20

## PHASE  1: Preparation

### STEP 1.1: Verify that OTD supports your tablet

* Find your tablet here: [https://opentabletdriver.net/Tablets](https://opentabletdriver.net/Tablets)
  * Note that some tablets are listed by name and some by model number
  * To find your tablet's model number: [Finding the model number of your drawing tablet](../../general/finding-the-model-number-of-your-drawing-tablet.md)

{% hint style="warning" %}
On the list of supported tablets, if your tablet is marked as "Zadig WinUSB" - there are special requirements to install this that are NOT covered in this document. Consult the OTD docs for help.
{% endhint %}

### STEP 1.1: Uninstall existing tablet drivers

{% hint style="danger" %}
<mark style="color:red;">You</mark> <mark style="color:red;"></mark><mark style="color:red;">**MUST**</mark> <mark style="color:red;"></mark><mark style="color:red;">uninstall any existing tablet drivers on your computer. If you leave them installed they will interfere with OTD.</mark>
{% endhint %}

* Follow these instructions: [**Uninstalling tablet drivers**](../../../basics/uninstalling-tablet-drivers.md)&#x20;
* To ensure nothing remains, run this tool[**Tablet driver cleanup tool**](../tablet-driver-cleanup-tool.md).

### STEP 1.2: Create a folder for OTD

* Create a folder somewhere on your computer called `OpenTabletDriver`
* I prefer to use `C:\OpenTabletDriver`&#x20;
* All the instructions in this document will use `C:\OpenTabletDriver`&#x20;

### STEP 1.3: Download the VMulti driver

{% hint style="danger" %}
<mark style="color:red;">You MUST install</mark> <mark style="color:red;"></mark><mark style="color:red;">**VMulti driver**</mark> <mark style="color:red;"></mark><mark style="color:red;">if you want pressure sensitivity & tilt to work with your tablet on Windows.</mark>
{% endhint %}

* Download `Multi.Driver.zip` from this location:
  * [https://github.com/X9VoiD/vmulti-bin/releases/download/v1.0/VMulti.Driver.zip](https://github.com/X9VoiD/vmulti-bin/releases/download/v1.0/VMulti.Driver.zip)
* Place the zip file inside `C:\OpenTabletDriver`&#x20;
* Right-click the zip file, then select **Extract All**.&#x20;
  * This creates a `C:\OpenTabletDriver\VMulti.Driver` folder&#x20;

### STEP 1.4 Install the VMulti driver

{% hint style="danger" %}
<mark style="color:red;">This next step file may restart your computer without warning. So, close any applications before you install VMUlti.</mark>&#x20;
{% endhint %}

* Close all applications.
* In the `C:\OpenTabletDriver\VMulti.Driver` folder, right click on `install_hiddriver.bat`, then select **Run as Administrator**

### STEP 1.5: Install the .NET Runtime&#x20;

{% hint style="warning" %}
OTD requires a specific version of the .NET Runtime to be installed on your computer. It won't work otherwise.
{% endhint %}

* Click on this link [https://opentabletdriver.net/Framework](https://opentabletdriver.net/Framework)&#x20;
  * It will take you to a page that lists differerent verions of the .NET framework for OTD to use
* Under "Windows" click on the link labelled "x64".
  * A download will start for `windowsdesktop-runtime-8.0.22-win-x64.exe`&#x20;
* Once the exe file is downloaded, run it to install the .NET Runtime.

### STEP 1.6: Download OpenTabletDriver

* Open a browser to this location:
  * [https://github.com/OpenTabletDriver/OpenTabletDriver/releases/latest](https://github.com/OpenTabletDriver/OpenTabletDriver/releases/latest)
* Scroll down the page to a section labelled "Assets"
* Look for a file with a name like this `OpenTabletDriver-0.6.6.2_win-x64.zip`&#x20;
* Download that zip file.
* Move the zip file into the  `C:\OpenTabletDriver`  folder
* Right-click on the zip file, then select **Extract All**.&#x20;
  * This creates a folder with a name like `C:\OpenTabletDriver\OpenTabletDriver-0.6.6.2_win-x64`&#x20;

## PHASE 2: OTD Basics and connecting to a tablet

### STEP 2.1: Launch the OpenTabletDriver app for the first time

{% hint style="warning" %}
DO NOT launch the OTD app with "Run as Administrator". This will cause problems with OTD.
{% endhint %}

* In the `C:\OpenTabletDriver\OpenTabletDriver-n.n.n.n_win-x64` folder, `launch OpenTabletDriver.UX.Wpf.exe`.&#x20;
  * This launches the OTD app. (Do not launch it as Administrator)
* If you see a message that ".NET X Desktop Runtime X64 is not installed", then follow its instructions to install that runtime. Then launch `OpenTabletDriver.UX.Wpf.exe` again.&#x20;
  * This message should not appear because you install edthe .NET Runtime ina previous step.
* The **OpenTabletDriver Guide** will automatically start&#x20;
* Click the X in the upper right hand corner to close the guide.
* You can get back to this guide at any time in OTD by navigating to **Help** > **Show guide**.

### STEP 2.2 Minimizing the OTD app&#x20;

{% hint style="info" %}
This is an important thing to learn, because you will be doing it a lot.
{% endhint %}

* You can keep the OTD app running without it being on the desktop my minimizing it.
* Once it is minimized, you can find it in the taskbar
* Click on the OTD icon in the taskbar to open the OTD app

<div align="left"><figure><img src="../../../.gitbook/assets/image (70).png" alt="" width="375"><figcaption></figcaption></figure></div>

### **STEP** 2.&#x33;**: Understanding the OTD app on Windows**

For you to use OTD on Windows, the OTD app MUST always be running.

Although it must always be running, You don't have to always have the visible on your screen, you can  minimize the app and find it later in the task bar.

### **STEP 2.4: Detect your tablet with OTD**

* When the OTD app starts, it will automatically try to detect your tablet.
* The tablet will be shown in the Window title at the top and at the bottom left of the application window
* If needed, you can force detection click **Tablets** > **Detect tablet**

### **STEP 2.5: Checkpoint**

At this point, moving the pen on the tablet should move the mouse pointer.

Do not worry about which monitor the mouse is on. We will cover that soon.

Pressure and will not work right now. We will cover that soon.&#x20;

## PHASE 3: Configuring OTD to work with your tablet

### STEP 3.1: Configure tablet to display mapping

* In the OTD App, go to **Output** > **Tablet** Section
* In **Output** > **Display**, right-click anywhere and pick **Set to Display** \<displayname> where \<displayname> is specific display you want to use with the tablet.
* In **Output > Tablet**, right click anywhere, and then select **Lock Aspect Ratio**.
* ![](<../../../.gitbook/assets/image (108).png>)
* At this point moving the pen will move the pointer on exactly 1 display.&#x20;
* Also there will be no stroke distortion - for example a circle on tablet makes a circle on the monitor with no distortion/stretching
* Press APPLY and then press SAVE.&#x20;

### STEP 3.2: Understanding APPLY and SAVE&#x20;

The instructions have already asked you to press APPLY and SAVE. Let's take a moment to understand these actions a bit better.

SAVE

* SAVE will save current settings, even if you haven't clicked apply and loads them the next time you open OTD.&#x20;
* You can test this out by clicking SAVE without clicking APPLY applying and starting the OTD app again. It will load the settings that were saved.

APPLY

* APPLY will load the current settings you have set in the user interface. Until you click APPLY no changes you have made in the UI will be in effect.

To keep things simple for you for now, I suggest you always click APPLY then SAVE whenever you make a change in the OTD app.

### STEP 3.3: Install the Windows Ink plugin

* In the OTD app, navigate to **Plugins** > **Open Plugin Manager**
* Click on the **Windows Ink** plugin, then click **Install**&#x20;
* The Windows Ink plugin will appear at the top of the plugin list
* Close the **Plugin Manager** window

### STEP 3.4: Configure Windows Ink mapping mode

* In the OTD app, on the bottom, change the **mode** dropdown:
  * from **Absolute Mode**&#x20;
  * to **Windows Ink Absolute Mode**
  * click **APPLY** then click **SAVE**&#x20;

{% hint style="info" %}
NOTE: You will only see **Windows Ink Absolute Mode** listed if you previously enabled the Windows Ink plugin.
{% endhint %}

### STEP 3.5: Configure the pen

Navigate to the **Pen Settings** tab

By default the will be configured as shown below

<figure><img src="../../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

What to notice here: The tip settings, eraser settings, and the buttons have been configured "Adaptive Binding". For now leave these alone.

Click **SAVE** and **APPLY**.

NOTE: You cannot assign the pen buttons to take MOUSE actions such as right-click and left-click, etc.

### STEP 3.6: Configure your drawing application to use Windows Ink

* The specific instructions vary per app.&#x20;
* Instructions for specific apps: [Configure Windows Ink for apps](../../operating-systems/windows/windows-ink/configure-windows-ink-for-apps.md)

### STEP 3.7 Checkpoint

At this point you should be able to effectively draw with OTD. Pressure and Tilt should work.

I suggest you install Krita and configure it to use Windows Ink&#x20;

Try some basic drawing and see if everything is working

## PHASE 4: Optional customization

### STEP 4.1 Start OpenTabletDriver when Windows starts

* Right-click on OpenTabletDriver.UX.Wpf.exe
* Select **Create Shortcut**
* Right click on the shortcut, then select **Properties**
* Under **Run**, select **Minimized**
* Click **OK**
* Press WINDOWS+R to bring up the **Run** window
* In **Open**, type `shell:startup`
* This will open a new Explorer window pointing to a folder called **Startup**
* Move the shortcut to the **Startup** folder in that explorer window

### STEP 4.2 Pressure curves

By default OTD does not use a pressure curve to modify how the pressure data is interpreted. However, you can edit the pressure curve by following these instructions: [Pressure curves in OpenTabletDriver](opentabletdriver-pressure.md)

### STEP 4.3 Smoothing

By default OTD performs no smoothing on the pen data. This is desirable because&#x20;

* it gives you a VERY responsive drawing experience
* Gives you complete control about the smoothing

Two ways to introduce smoothing

* **Application-level smoothing** - To add smoothing back in to your drawing, your first and easiest option is to use the smoothing features in your drawing application. Learn more here: [**Configure smoothing in applications**](../../drawing/configure-smoothing-in-applications.md)&#x20;
* **Driver-level smoothing in OTD** - this will be a little more complex to do. More here: [**Smoothing with OpenTabletDriver**](opentabletdriver-smoothing.md)&#x20;

### STEP 4.4 Configure tablet buttons

* Open the **Auxiliary Settings** tab
* each button shows up as an **Auxiliary Binding**.
* In the screenshot above, one of the buttons has been set to match the "e" key.

<figure><img src="../../../.gitbook/assets/image (622).png" alt="" width="563"><figcaption></figcaption></figure>

### STEP 4.5 Display toggle

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

<figure><img src="../../../.gitbook/assets/image (250).png" alt=""><figcaption></figcaption></figure>

ProTip: Quickly get to the AppData folder by pressing WINDOWS+R and typing appdata. It will open a window directly to that folder.

![](<../../../.gitbook/assets/image (131).png>)





dd
