# Common drawing troubleshooting steps

## Restart the computer

Sometimes systems and drivers just get into confused states.

A restart will often clear up problems. If a restart or two doesn't fix the problem then move on to other troubleshooting steps.

## Check drivers

* Are you running the latest tablet drivers? The driver software will usually have some place where it says which version it it.
* Try uninstalling, restarting the computer, and reinstalling the latest drivers.&#x20;
* Sometimes the drivers you have don't completely uninstall themselves. To completely uninstall the drivers see this guide: [**Uninstalling manufacturer tablet drivers**](../guides/drivers/uninstalling-manufacturer-tablet-drivers.md).

## Try an older driver

* Sometime newer drivers themselves introduce new problems that were not there before.
* Try installing an older tablet driver to see if that fixes the problem.

## Test the tablet with other applications

Often the problems you experience might be due to a specific app so you should try other apps to see if they replicate the problem.&#x20;

* Krita
* Clip Studio Paint
* Photoshop&#x20;
* Microsoft OneNote

NOTES:

* I recommend always testing with Krita because Krita is free and has configurable brushes that let you test our specific pen features such as pressure and tilt.

## Windows > Windows PNP drivers

Try this: [Testing with Windows PNP drawing tablet drivers](testing-with-windows-pnp-drawing-tablet-drivers.md)

Often it can be a clue to what is going on.

## Windows > Windows Ink

If you are using a Mac, skip this section. It does not apply to you.

If you are using a Windows computer you need to be aware of a component called [Windows Ink](../guides/operating-systems/windows/windows-ink/).

See these docs:

* [Configure Windows Ink for in the tablet driver](../guides/operating-systems/windows/windows-ink/configure-windows-ink-in-the-tablet-driver.md)
* [Configure Windows Ink for apps](../guides/operating-systems/windows/windows-ink/configure-windows-ink-for-apps.md)

## Pressure

* If you are having pressure problems check the pressure in the driver: [Testing pressure in the tablet driver](testing-pressure-in-the-tablet-driver.md)
* In Windows, If the tablet driver detects pressure but the pressure is not working in an app, it often indicates that Windows Ink is configured consistently between the two.
* It's important here to see if the where the pressure is working or not
  * Is it working in a specific app but working in others?
  * Or is it nor working in all apps?

