# OpenTabletDriver usage notes

### Limitations of OpenTabletDriver

* OTD does NOT support touch input.
* OTD does NOT support tablet rotary dials.
* OTD does NOT support pen barrel rotation.
* OTD does NOT support wireless or bluetooth connections.
* OTD does NOT support per-application configuration. All OTD settings are system-wide.

### **Windows Ink & WinTab**&#x20;

* There are two Pen APIs in the Windows ecosystem: **WinTab** which is older, and **Windows Ink** which is newer.
* OTD only supports **Windows Ink** so any apps you want to use it with must also support Windows Ink.
* Most creative apps support Windows Ink - Clip Studio Paint, Krita, Photoshop.
* If you want pressure sensitivity, tilt, etc. - you must **you MUST configure OTD to use Windows Ink** and configure your apps to also use Windows Ink.&#x20;

### Pen hover height

By default, OTD **has no restriction on the hover height of your pen**. Most drivers impose an artificial limit of about 10mm for a pen. But you'll often find with OTD that the hover height is increased substantially.&#x20;

The maximum hover height is dependent on the specific model of tablet involved. For example with a Wacom Intuos Pro (PTH-860) my hover height goes from 10mm with the Wacom Driver to 20mm with Open Tablet driver.

You can install a plug-in to control the hover height and have whatever limit you want.

### Application data directory

* OTD stores information in its application data directory
* More here: [OpenTabletDriver application data directory](opentabletdriver-application-data-directory.md)
* If you are doing more advanced things with OTD you should be familiar with this folder.
