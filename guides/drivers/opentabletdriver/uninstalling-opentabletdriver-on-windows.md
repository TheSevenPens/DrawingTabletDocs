# Uninstalling OpenTabletDriver on Windows

## Stopping OpenTabletDriver from starting when your computer boots

* Press WINDOWS+R to bring up the **Run** window
* In Open, enter **shell:startup**
* Delete the OpenTabletDriver shortcut

## Uninstalling OpenTabletDriver

* If OpenTabletDriver processes are running, then stop them.
* You can use Task manager for stop the processes, or you can stop the processes with these two Powershell commands

```
stop-process -name OpenTabletDriver.UX.Wpf
stop-process -name OpenTabletDriver.Daemon
```

* Delete the folder that contains OpenTabletDriver

## Uninstalling VMulti

* Navigate to the folder that contains VMulti
* run **uninstall\_hiddriver.bat** as admin
