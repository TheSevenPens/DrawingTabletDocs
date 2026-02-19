# Uninstall OpenTabletDriver on Windows

## Overview

{% hint style="info" %}
For information on OpenTabletDriver: [OpenTabletDriver](./)

For information on how to install on Windows: [Install OpenTabletDriver on Windows](otd-windows-install.md)&#x20;
{% endhint %}

## STEP 1: Stop OpenTabletDriver from starting when your computer boots

* You only need to do this step if you configured running OTD on startup previously.
* Press WINDOWS+R to bring up the **Run** window
* In Open, enter **shell:startup**
* Delete the OpenTabletDriver shortcut

## STEP 2: Uninstall OpenTabletDriver

* If OpenTabletDriver processes are running, then stop them.
* You can use Task manager for stop the processes, or you can stop the processes with these two Powershell commands

```
stop-process -name OpenTabletDriver.UX.Wpf
stop-process -name OpenTabletDriver.Daemon
```

* Delete the folder that contains OpenTabletDriver

## STEP 3: Uninstall VMulti

* Navigate to the folder that contains VMulti
* run **uninstall\_hiddriver.bat** as admin
