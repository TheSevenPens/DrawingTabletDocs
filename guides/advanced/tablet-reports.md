# Tablet reports

## Overview

There are three kinds of reports:

* Pen reports — for pen position, pressure, tilt, and pen buttons.
* Touch reports — to support multitouch operation.
* Auxiliary input reports — for buttons, dials, and sliders on the tablet.

The tablet sends these reports to the computer at different rates:

* Pen reports are sent at around 200 to 300 reports per second. Your tablet's specifications may list a **report rate**. This refers to pen reports.
* Touch reports, if your tablet supports them, are typically sent 60 to 100 times per second.
* Auxiliary input reports are not sent at a fixed rate. They are only sent when you use an auxiliary input, such as a button or dial.

## Report rate

You can see this often in the specifications for a tablet as "report rate". Here is an example.

<figure><img src="https://1457921496-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNde0PQIvNcFZNVxuTO0G%2Fuploads%2F3PWZrFGq2AmRKehQbamy%2Fimage.png?alt=media&#x26;token=6d001f13-e23e-4898-b283-f03dd25d028d" alt="" width="375"><figcaption></figcaption></figure>

* “RPS” means “reports per second.”&#x20;
* Because this is a value per second, some literature uses the unit Hz. For example, instead of “200 RPS,” you might see “200 Hz.”
* When you see it listed it is referring to pen reports. I'v never seen the touch report rate listed.

## Pen report contents

The exact data format inside a report depends on the tablet and report type. However, reports generally follow some basic patterns. Below are typical examples.

* **Report ID** — a number that identifies the report type. In this case, it identifies a pen report.
* **X, Y position** — the pen's position.
* **Z position** — the pen's hover height.
* **Pressure** — `0` means no pressure. A positive integer indicates pressure.
* **Tilt** — two angle values. These can be X and Y tilt, or altitude and azimuth.
* **Pen buttons** — whether the pen's buttons are pressed.
* **Status flags** — whether the pen is in range (hovering) and the tip is touching.
* **Barrel rotation** — also called twist, for pens that support it.
* **Eraser state**
* **Pen ID**

{% hint style="info" %}
When reading technical drawing-tablet documentation, you may see the term “switches.” It rarely appears in user-facing documentation. This term applies to pen buttons, the tip, and the eraser. For example, documentation often calls the pen tip the “tip switch.”
{% endhint %}

## Higher report rates

As of November 2026, the highest pen report rate seen in drawing tablets is 300 Hz. However, this year, there has been some progress in achieving higher report rates: [Ultra-high report rates](ultra-high-report-rates.md)

## Finding report rates

You can use different tools: Measuring report rate

## Seeing real reports

If you want to look at the actual reports your tablet sends:

* **OpenTabletDriver** has a tablet debugger that shows the raw bytes of each report next to the decoded values.
* On **Linux**, `hid-tools` (`hid-recorder`) prints a device's report descriptor and every report it sends.
* On **Windows**, USB analyzers such as Wireshark with USBPcap can capture the raw traffic.

## References

* [USB Device Class Definition for HID 1.11](https://www.usb.org/document-library/device-class-definition-hid-111) - Section 5.6 (Reports) and Section 6.2.2 (Report Descriptor) explain Report IDs.
* [HID Usage Tables](https://usb.org/document-library/hid-usage-tables-15) - the Digitizers page (`0x0D`) defines the pen and touch usages used above.
* [Microsoft: Pen devices](https://learn.microsoft.com/en-us/windows-hardware/design/component-guidelines/pen-devices) and [Windows Precision Touchpad](https://learn.microsoft.com/en-us/windows-hardware/design/component-guidelines/touchpad-windows-precision-touchpad-collection) - sample descriptors and the usages Windows requires.
* Linux kernel: [`drivers/hid/wacom_wac.c`](https://github.com/torvalds/linux/blob/master/drivers/hid/wacom_wac.c) (Wacom pen, pad, and touch parsing) and [`drivers/hid/hid-uclogic-params.c`](https://github.com/torvalds/linux/blob/master/drivers/hid/hid-uclogic-params.c) (Huion / XP-Pen / UC-Logic initialization and report layouts).
* [OpenTabletDriver configurations](https://github.com/OpenTabletDriver/OpenTabletDriver/tree/master/OpenTabletDriver.Configurations/Configurations) - per-tablet definitions of real report layouts.
