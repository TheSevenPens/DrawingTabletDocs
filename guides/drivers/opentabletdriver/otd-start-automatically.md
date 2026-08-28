# Start OpenTabletDriver automatically

## Overview

OpenTabletDriver (OTD) must be running for your tablet to work. If you quit it, your tablet stops working with OTD.

That makes starting OTD automatically worth setting up, so you do not have to remember to launch it before you draw.

{% hint style="info" %}
This document covers Windows and macOS. Pick the section for your operating system.

Installation instructions are separate:

* [Install OpenTabletDriver on Windows](otd-windows-install.md)
* [Install OpenTabletDriver on macOS](otd-macos-install.md)
{% endhint %}

## Windows

On Windows, you add a shortcut to the **Startup** folder. Anything in that folder runs when you sign in.

Setting the shortcut to run **Minimized** keeps OTD out of your way. It still runs, and you can reach it from the system tray.

* Right-click `OpenTabletDriver.UX.Wpf.exe`.
* Select **Create Shortcut**.
* Right-click the shortcut, then select **Properties**.
* Under **Run**, select **Minimized**.
* Click **OK**.
* Press **Windows** + **R** to open the **Run** window.
* In **Open**, type `shell:startup`.
* This opens a new Explorer window pointing to a folder called **Startup**.
* Move the shortcut to the **Startup** folder in that Explorer window.

{% hint style="warning" %}
Do **not** set the shortcut to **Run as Administrator**. OTD will not work correctly if you run it as administrator.
{% endhint %}

### Confirming it worked on Windows

* Sign out and sign back in, or restart your computer.
* Look for the OTD icon in the system tray, at the right end of the taskbar. You may need to click the **^** arrow to show hidden icons.
* Move your pen on the tablet. The pointer should move.

## macOS

On macOS, you add OTD to **Login Items**. Anything listed there opens when you log in.

* Open **System Settings**.
* Go to **General** > **Login Items & Extensions**.
* Under **Open at Login**, click the **+** button.
* Select **OpenTabletDriver** from **Applications**, then click **Open**.

OTD now starts each time you log in.

### Confirming it worked on macOS

* Log out and log back in, or restart your Mac.
* Move your pen on the tablet. The pointer should move.

{% hint style="info" %}
If the pointer does not move, check that OTD still has the **Input Monitoring** and **Accessibility** permissions. See [Install OpenTabletDriver on macOS](otd-macos-install.md) for those steps, including what to do when a permission looks granted but is not in effect.
{% endhint %}

## Stopping OTD from starting automatically

**Windows**

* Press **Windows** + **R**, type `shell:startup`, then press **Enter**.
* Delete the OpenTabletDriver shortcut from the **Startup** folder.

**macOS**

* Open **System Settings**.
* Go to **General** > **Login Items & Extensions**.
* Under **Open at Login**, select **OpenTabletDriver**, then click the **-** button.

## Related topics

* [OpenTabletDriver](./)
* [Install OpenTabletDriver on Windows](otd-windows-install.md)
* [Install OpenTabletDriver on macOS](otd-macos-install.md)
* [Notes on OpenTabletDriver](otd-notes.md)
