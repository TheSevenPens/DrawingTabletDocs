# DIAG: Windows Get PnPUtil Device and Driver Info

Open a Terminal as Administrator.

Run the following commands:

```
pnputil /enum-drivers > %USERPROFILE%/Documents/drivers.txt
pnputil /enum-devices /connected /drivers > %USERPROFILE%/Documents/devices.txt
explorer "%USERPROFILE%/Documents"
```

These commands will create two files in your documents folder:

* drivers.txt
* devices.txt&#x20;

And then it will open a file explorer window to your Documents folder.
