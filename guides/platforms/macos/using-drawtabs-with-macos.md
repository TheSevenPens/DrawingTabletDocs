# Using a drawing tablet on macOS

## Summary

Drawing tablets generally work well with macOS. All the major tablet brands provide macOS drivers, and once the driver is installed and given the permissions it needs, the experience is very similar to Windows.

## Drivers

### You MUST install tablet drivers&#x20;

MacOS does not have any built-in tablet drivers. So, you MUST install your tablet manufacturer's tablet drivers to use your tablet.&#x20;

This is different from Windows which does have some limited form of built-in tablet drivers.

### macOS upgrades

As newer versions of macOS appear, the tablet driver you are using with your macOS machine may have problems.

* The driver may still support your tablet but now your tablet doesn't work correctly. In this case, check for newer drivers.
* If you download and install a newer driver - it may no longer support the tablet you have - in this case  consider [OpenTabletDriver](https://docs.sevenpens.com/opentabletdriver)&#x20;

Before upgrading to a new major version of macOS, check that your tablet manufacturer has released a driver that supports it.

The safest thing to do if you see a new macOS version - is to wait. Let other tablet users try it out for a while before you upgrade.

### Only install one tablet driver

I don't recommend installing two different tablet drivers. For example, do not install a Huion driver AND a Wacom driver.

HOWEVER, to be fair, my own experience on macOS has been good: I have several Macs with multiple tablet drivers installed at the same time without problems (Wacom, Huion, XP-Pen) . However, other people have reported issues, so I still don't recommend it. For more details, see [Using multiple tablet drivers on the same computer](../../drivers/multiple-tablet-drivers.md).

### Apple Silicon vs Intel

Current drivers from the major tablet brands run natively on Apple Silicon. Some older drivers were built only for Intel Macs. These may run on Apple Silicon through Apple's Rosetta translation layer, but they may also not work at all. If you have an Apple Silicon Mac, use a driver version that the manufacturer lists as supporting Apple Silicon.

### Older macOS versions

If you have an older Mac that cannot run a recent version of macOS, you may need to use an older driver. See [Using older tablet drivers](../../drivers/older-tablet-drivers.md).

## Permissions

macOS requires you to explicitly give a tablet driver permission to control your computer. If these permissions are not granted, the driver may be installed but the pen will not work correctly. This is the most common source of problems with tablets on macOS.

The driver installer usually prompts you for these, but if you dismissed the prompts you can grant them yourself in **System Settings** > **Privacy & Security**. The exact names vary between macOS versions, but look for:

* **Accessibility** - allows the driver to move the pointer and send clicks and keystrokes.
* **Input Monitoring** - allows the driver to see input from the tablet and its buttons.
* **System extension approval** - some drivers install a system or driver extension, which macOS blocks until you allow it in **Privacy & Security**. This may require a restart.

Make sure the tablet driver's entries (there may be more than one) are listed and switched on. Restart your computer after changing these settings.

## Uninstalling and cleaning up old drivers

When switching brands or troubleshooting, uninstall the old driver first. Most brands provide an uninstaller with the driver or a utility app, and simply deleting the app from the **Applications** folder may leave parts of the driver behind.

After uninstalling, also check **System Settings** > **Privacy & Security** and remove any leftover entries for the old driver from Accessibility and Input Monitoring.

For brand-specific steps, see [Uninstalling tablet drivers](../../drivers/uninstalling-tablet-drivers.md).
