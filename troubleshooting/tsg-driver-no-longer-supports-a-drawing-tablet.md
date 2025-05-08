# Troubleshoot driver no longer supports a drawing tablet

As years pass, a manufacturer will periodically publish new versions of their tablet driver.&#x20;

And periodically, these driver updates dfrop support for older models.

You have a couple of options:

* Try an older version of your manufacturer's drivers that does support your tablet. The risks of this approach is that sometimes the older drivers don't work well with newer operating systems.
* Try using **OpenTabletDriver** ([https://opentabletdriver.net/](https://opentabletdriver.net/)). Setting up OpenTabletDriver on Windows can be challenging. I wrote this guide to provide step-by-step instructions: Try [**Using OpenTabletDriver with Windows**](../guides/drivers/opentabletdriver/opentabletdriver-windows.md). OpenTabletDriver has full support for tilt and pressure on Windows but not an MacOS.
* Windows has somer VERY RUDIMENTARY support for tablets (this is called "Windows Plug-and-Play" support) and it works with SOME tablets in a limited way. For those tablets, The PNP support may support pressure and clicking but no pressure and tilt.

