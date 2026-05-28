# Uninstall OpenTabletDriver on Windows

## Overview

{% hint style="info" %}
For information on OpenTabletDriver: [OpenTabletDriver](./)

For information on how to install it on Windows: [Install OpenTabletDriver on Windows](otd-windows-install.md)
{% endhint %}

## STEP 1: Stop OpenTabletDriver from starting when your computer boots

* You only need to do this step if you previously configured OTD to run at startup.
* Press WINDOWS+R to open the **Run** window.
* In **Open**, enter `shell:startup`.
* Delete the OpenTabletDriver shortcut.

## STEP 2: Uninstall OpenTabletDriver

* If OpenTabletDriver processes are running, then stop them.
* You can use Task Manager to stop the processes, or you can run these two PowerShell commands:

```
stop-process -name OpenTabletDriver.UX.Wpf
stop-process -name OpenTabletDriver.Daemon
```

* Delete the folder that contains OpenTabletDriver.

## STEP 3: Uninstall VMulti

* Navigate to the folder that contains VMulti.
* Run **uninstall\_hiddriver.bat** as an administrator.
