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

{% hint style="info" %}
Most tablets connect over USB and describe their reports using the USB HID ("Human Interface Device") standard, the same standard used by mice and keyboards. Bluetooth tablets usually use the same HID report model. This page uses USB HID terms throughout.
{% endhint %}

## Report rate

You can see this often in the specifications for a tablet as "report rate". Here is an example.

<figure><img src="https://1457921496-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNde0PQIvNcFZNVxuTO0G%2Fuploads%2F3PWZrFGq2AmRKehQbamy%2Fimage.png?alt=media&#x26;token=6d001f13-e23e-4898-b283-f03dd25d028d" alt="" width="375"><figcaption></figcaption></figure>

“RPS” means “reports per second.”

Because this is a value per second, some literature uses the unit Hz. For example, instead of “200 RPS,” you might see “200 Hz.”

The report rate in a tablet's specifications is the rate of **pen** reports. Touch, buttons, and dials are sent at their own rates, described in [When reports are sent](tablet-reports.md#when-reports-are-sent) below.

## One device, several kinds of reports

A single tablet can contain several logical input devices. When you plug it in, the operating system may see a pen digitizer, a touch device, and a keyboard or "consumer control" device, all belonging to the same physical tablet.

This happens at two levels.

### Report IDs

Every HID device sends a **report descriptor** when it connects. The descriptor is a small program that tells the computer exactly what each report looks like: which bits are buttons, which bytes are X and Y, how many bits encode pressure, and so on.

A descriptor can declare several kinds of reports. Each one is given a **Report ID**, which is sent as the **first byte** of every report. The computer reads that first byte to know which layout the remaining bytes follow. Each Report ID has its own fixed length.

So a pen report and an ExpressKey report are not parts of one big packet. They are separate, smaller reports that take turns on the same connection, each starting with its own Report ID.

The values are chosen by the manufacturer. The numbers used in the examples on this page (`0x02` for pen, `0x03` for pad, `0x04` for touch) are only illustrations. Real tablets use many different numbers, and the same brand often changes them between generations.

## Report contents

The exact data format inside a report depends on the tablet and report type. However, reports generally follow some basic patterns. Below are typical examples.

### Pen reports

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

As of November 2026, the highest pen report rate seen in drawing tablets is 300 Hz. However, this year, there has been some progress in achieving higher report rates: Ultra-high report rates

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
