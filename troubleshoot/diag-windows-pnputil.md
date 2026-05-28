# DIAG: Get Windows PnPUtil device and driver info

Open a Terminal as Administrator.

Run the following commands:

```
pnputil /enum-drivers > %USERPROFILE%/Documents/drivers.txt
pnputil /enum-devices /connected /drivers > %USERPROFILE%/Documents/devices.txt
explorer "%USERPROFILE%/Documents"
```

These commands will create two files in your Documents folder:

* drivers.txt
* devices.txt

And then it will open a file explorer window to your Documents folder.
