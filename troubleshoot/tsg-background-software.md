# TSG: Background software interfering with the tablet driver

## Symptoms

On Windows, your tablet misbehaves and the usual fixes don't help. For example:

* Reinstalling the tablet driver doesn't fix it, or the fix doesn't last
* The problem appeared suddenly - for example overnight - with no change you can name
* Lag, the pen not responding, or the driver not detecting the tablet

In this case, other software running in the background may be interfering with the tablet driver.

## Check the usual causes first

Background software is not the first thing to check. Before you go down this path:

* Rule out the cable and the port. See: [TSG: Tablet driver does not detect the tablet](tsg-tablet-driver-does-not-detect-tablet.md)
* Do a clean reinstall of the tablet driver. See: [Tablet Driver Cleanup tool](../guides/drivers/tablet-driver-cleanup-tool.md)
* Make sure you don't have tablet drivers from other brands installed. See: [Using multiple tablet drivers on the same computer](../guides/drivers/multiple-tablet-drivers.md)

But if those don't fix it, check for background software before concluding the tablet is faulty.

## What kind of software

* **RGB lighting control software** - I have seen this cause tablet driver problems myself.
* **Laptop manufacturer utilities** - for example, one user reported that Lenovo Vantage was the cause of their tablet lag. This has not been confirmed.

## Things to try

1. Disable your startup apps. In Windows 11, go to **Settings** > **Apps** > **Startup**, or open **Task Manager** and go to **Startup apps**.
2. Restart the computer.
3. Reinstall the tablet driver. See: [Tablet Driver Cleanup tool](../guides/drivers/tablet-driver-cleanup-tool.md)
4. If the problem is gone, turn your startup apps back on one at a time to find the one causing it.

{% hint style="warning" %}
Closing an app to the system tray is NOT the same as disabling it. An app in the system tray is still running.
{% endhint %}
