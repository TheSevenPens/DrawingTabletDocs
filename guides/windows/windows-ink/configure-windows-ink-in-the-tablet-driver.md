# Configure Windows Ink in the tablet driver

## Global and Application specific configuration

You can configure driver's use Windows Ink:

* For all applications
* For specific applications

This allows you to have a baseline configuration and then modify the behavior for specific applications as needed.&#x20;

In general for the tablet driver I recommend:

* Enabling Windows Ink for all applications
* Disabling Windows Ink for specific applications that need it.

Every driver has a different way of configuring it in their UI:

* **Wacom:** Wacom Tablet Properties > Application
* **Huion**: The drop-down with the gear icon at the top.
* **OpenTabletDriver**: N/A - OTD does not support per-application Windows Ink configuration

## Wacom Driver > Wacom Tablet Properties

* Open the **Wacom Tablet Properties** app
* Under **Tool** select your pen
* If you have a pen tablet, go to the **Mapping** tab.&#x20;
* Or if you have a pen display, go to the **Calibrate** tab.
* Set **Use Windows Ink** to turn on or off **Windows Ink** in the driver

![](<../../../.gitbook/assets/image (164).png>)

## Wacom Driver > Wacom Center

<div align="left">

<figure><img src="../../../.gitbook/assets/image (450).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

## Huion Driver > Huion Tablet app

* Open the **HuionTablet** app
* Navigate to **Digital Pen**&#x20;
* Under Press Key, set the **Enable Windows Ink** to turn on or off **Windows Ink** in the driver

<div align="left">

<figure><img src="../../../.gitbook/assets/image (187).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

## XP-Pen driver > PenTablet App

* Open the **PenTablet** app
* Navigate to **Digital settings**&#x20;
* Set the **Windows Ink** to turn on or off **Windows Ink** in the driver

<div align="left">

<figure><img src="../../../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

## Xencelabs Driver

<div align="left">

<figure><img src="../../../.gitbook/assets/image (449).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

## OpenTabletDriver

NOTE: To see the Windows Ink option, you have to install the OTD Windows Ink plug-in first.

![](<../../../.gitbook/assets/image (122).png>)

