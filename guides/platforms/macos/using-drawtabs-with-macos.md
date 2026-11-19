# Using a drawing tablet on macOS

## Summary

Drawing tablets generally work well with macOS. All the major tablet brands provide macOS drivers, and once the driver is installed and given the permissions it needs, the experience is very similar to Windows.

## Drivers

### Manufacturer tablet drivers versus macOS built-in support

Unlike Windows, macOS does not have a built-in Plug-and-Play driver for drawing tablets. Without the manufacturer's driver, a tablet may at best move the pointer like a basic mouse, with no pressure sensitivity and none of the tablet's buttons or settings. You should always install the manufacturer-provided tablet driver.

If the manufacturer no longer supports your tablet, an alternative is [OpenTabletDriver](https://docs.sevenpens.com/opentabletdriver), which supports pressure and tilt on macOS.

### Only install one tablet driver

I don't recommend installing two different tablet drivers. For example, do not install a Huion driver AND a Wacom driver.

To be fair, my own experience on macOS has been good: I have several Macs with multiple tablet drivers installed at the same time without problems. However, other people have reported issues, so I still don't recommend it. For more details, see [Using multiple tablet drivers on the same computer](../../drivers/multiple-tablet-drivers.md).

### Apple Silicon vs Intel

Macs come in two kinds: older Macs with Intel processors and newer Macs with Apple Silicon (M-series) processors.

Current drivers from the major tablet brands run natively on Apple Silicon. Some older drivers were built only for Intel Macs. These may run on Apple Silicon through Apple's Rosetta translation layer, but they may also not work at all, because a tablet driver is more deeply tied to the operating system than a normal app. If you have an Apple Silicon Mac, use a driver version that the manufacturer lists as supporting Apple Silicon.

### macOS version support

Every year Apple releases a new version of macOS, and tablet manufacturers periodically drop support for older macOS versions in their newest drivers. In the other direction, older drivers may not work on the newest macOS versions.

* If you have an older Mac that cannot run a recent version of macOS, you may need to use an older driver. See [Using older tablet drivers](../../drivers/older-tablet-drivers.md).
* Before upgrading to a new major version of macOS, check that your tablet manufacturer has released a driver that supports it.

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

## Common problems

### Pen stops working after a macOS update

After a major macOS update, the pen may stop responding or lose pressure, even though nothing else changed. Try these steps:

* Check that the permissions above are still granted. If they look correct, try switching them off and on again, or removing and re-adding the driver's entries.
* Install the latest driver from your tablet manufacturer, in case the old driver does not support the new macOS version.
* Restart your computer.

### Pointer offset or wrong display with multiple displays

If you use a pen display alongside other monitors, the pen may move the pointer on the wrong display, or the pointer may be offset from the pen tip. Usually the tablet's active area is mapped to the wrong display, or to all displays combined. Fix this in your tablet driver's display mapping settings.

* [TSG: Pointer on wrong display](../../../troubleshoot/tsg-pointer-on-wrong-display.md)
* [Mapping active area to a display](../../customizing/map-active-area-to-display.md)
