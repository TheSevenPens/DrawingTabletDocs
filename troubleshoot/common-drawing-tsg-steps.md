# Common drawing troubleshooting steps

## Restart the computer

Sometimes systems and drivers just get into confused states.

A restart will often clear up problems. If one or two restarts do not fix the problem, move on to other troubleshooting steps.

## Check drivers

* Are you running the latest tablet drivers? The driver software will usually have somewhere that shows which version it is.
* Try uninstalling, restarting the computer, and reinstalling the latest drivers.
* Sometimes the drivers you have do not completely uninstall themselves. To fully uninstall them, see [Tablet Driver Cleanup tool](../guides/drivers/tablet-driver-cleanup-tool.md).

## Try an older driver

* Sometimes newer drivers themselves introduce new problems that were not there before.
* Try installing an older tablet driver to see if that fixes the problem.

## Test the tablet with other applications

Often, the problem might be due to a specific app, so you should try other apps to see whether they replicate it.

* Krita
* Clip Studio Paint
* Photoshop
* Microsoft OneNote

NOTES:

* I recommend always testing with Krita because it is free and has configurable brushes that let you test pen features such as pressure and tilt.

## Test with my online tablet tester

Drawing apps do complex things. My tablet tester is much simpler, and I know exactly what it does. See whether you can replicate the behavior there.

GO HERE: [SevenPens Tablet Tester](../resources/sevenpens-tablet-tester.md)

## Windows > Windows PNP drivers

Try this: [DIAG: Testing with Windows PNP drawing tablet drivers](diag-windows-pnp-tablet-drivers.md)

Often it can be a clue to what is going on.

## Windows > Windows Ink

If you are using a Mac, skip this section. It does not apply to you.

If you are using a Windows computer, you need to be aware of a component called [Windows Ink](../guides/platforms/windows/winink/).

See these docs:

* [Configure Windows Ink in the tablet driver](../guides/platforms/windows/winink/winink-config-driver.md)
* [Configure Windows Ink for apps](../guides/platforms/windows/winink/winink-config-apps.md)

## Pressure

* If you are having pressure problems, check pressure in the driver: [DIAG: Testing pressure in the tablet driver](diag-pressure-in-tablet-driver.md)
* In Windows, if the tablet driver detects pressure but the pressure is not working in an app, it often indicates that Windows Ink is configured inconsistently between the two.
* It is important to see where pressure is working and where it is not.
  * Is it working in a specific app but not working in others?
  * Or is it not working in all apps?

## Look through the other troubleshooting guides

GO HERE: [Troubleshooting](./)
