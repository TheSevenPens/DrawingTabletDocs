# Uninstall OpenTabletDriver

## Overview

This document covers removing OpenTabletDriver (OTD) from Windows and macOS. Pick the section for your operating system.

{% hint style="info" %}
For information on OpenTabletDriver: [OpenTabletDriver](./)

Installation instructions are separate:

* [Install OpenTabletDriver on Windows](otd-windows-install.md)
* [Install OpenTabletDriver on macOS](otd-macos-install.md)
{% endhint %}

{% hint style="info" %}
There is no uninstaller on either platform. On Windows, OTD runs from a folder you created. On macOS, it runs from an app you dragged into **Applications**. In both cases you remove it by hand.
{% endhint %}

## Windows

### STEP 1: Stop OpenTabletDriver from starting when your computer boots

* You only need to do this step if you previously configured OTD to run at startup.
* Press WINDOWS+R to open the **Run** window.
* In **Open**, enter `shell:startup`.
* Delete the OpenTabletDriver shortcut.

### STEP 2: Uninstall OpenTabletDriver

* If OpenTabletDriver processes are running, then stop them.
* You can use Task Manager to stop the processes, or you can run these two PowerShell commands:

```
stop-process -name OpenTabletDriver.UX.Wpf
stop-process -name OpenTabletDriver.Daemon
```

* Delete the folder that contains OpenTabletDriver.

### STEP 3: Uninstall VMulti

* Navigate to the folder that contains VMulti.
* Run **uninstall\_hiddriver.bat** as an administrator.

## macOS

### STEP 1: Stop OpenTabletDriver from starting when you log in

* You only need to do this step if you previously configured OTD to start at login.
* Open **System Settings**.
* Go to **General** > **Login Items & Extensions**.
* Under **Open at Login**, select **OpenTabletDriver**, then click the **-** button.

### STEP 2: Uninstall OpenTabletDriver

* Quit the OpenTabletDriver app.
* Drag `OpenTabletDriver` from **Applications** to the Trash.

### STEP 3: Remove the settings and cache folders

* Remove its settings folder at `~/Library/Application Support/OpenTabletDriver`.
* Remove its cache folder at `~/Library/Caches/OpenTabletDriver`.

### STEP 4: Remove the permissions

* Open **System Settings**, then go to **Privacy & Security**.
* Under **Input Monitoring**, select the OpenTabletDriver entry and click the **-** button.
* Under **Accessibility**, do the same.

## Going back to your manufacturer driver

If you want your manufacturer driver back, install it after removing OTD, then restart your computer.

## Related topics

* [OpenTabletDriver](./)
* [Install OpenTabletDriver on Windows](otd-windows-install.md)
* [Install OpenTabletDriver on macOS](otd-macos-install.md)
* [Start OpenTabletDriver automatically](otd-start-automatically.md)
* [Notes on OpenTabletDriver](otd-notes.md)
