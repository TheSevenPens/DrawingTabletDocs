# DIAG: Windows Get PnPUtil Device and Driver Info

Open a Terminal as Administrator.

Run the following commands:

```
pnputil /enum-drivers > %USERPROFILE%/Documents/drivers.txt
pnputil /enum-devices /connected /drivers > %USERPROFILE%/Documents/devices.txt
explorer "%USERPROFILE%/Documents"
```

You should see a file explorer window pop up.&#x20;

Find the drivers.txt and devices.txt in your Documents folder folder and upload them here.
