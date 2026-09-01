# Windows on ARM

## Overview

We are now seeing Windows computers running on ARM processors. This gives us the possibility of cooler-running, high-performance machines with great battery life.

**SUMMARY:** Although Windows on ARM laptops work well for office productivity, as of mid-2026 they still run into compatibility and performance issues with other software. For example, in my experience Discord is much more sluggish on Windows on ARM. This is based on my experience with the Microsoft Surface Laptop 7, but I think the issues apply in general to Windows on ARM devices.

**MY RECOMMENDATION**

* Avoid Windows on ARM for now
* If you MUST use a Windows on ARM laptop, verify that it works with all your apps and hardware.

## Drawing tablets compatibility with Windows on ARM

Windows on ARM devices require special ARM-compatible tablet drivers. Below you can see the current state of tablet driver support for Windows on ARM.

As of 2025-02-12:

* **Xencelabs (ARM support available)**
  * Separate ARM driver available since version 1.3.4-75 (released on 2024-09-27)
    * NOTE: For Xencelabs, the ARM driver is a separate download.
  * I have tested this driver on a Windows 11 ARM PC and can confirm it works.
* **Wacom (ARM support available)**
  * ARM support is available since driver version 6.4.9-2 (released on 2025-02-12)
  * I have tested this driver on a Windows 11 ARM PC and can confirm it works.
* **XP-Pen (ARM support available)**
  * ARM support is available starting with driver version 4.0.6.241211 (released on 2025-01-14)
  * I have tested this driver on a Windows 11 ARM PC and can confirm it works.
* **Huion (ARM support in progress)**
  * Huion is actively working on an ARM driver.
  * It is not available for download yet.

## Older Windows ARM devices

Microsoft previously released versions of the Surface Pro using the SQ1 and SQ2 ARM processors. Interestingly, recent Windows improvements for ARM seem to be improving performance on these older devices.

See this Reddit thread: [**r/Surface - Windows 11 24H2 update made my ARM tablet faster!**](https://www.reddit.com/r/Surface/comments/1czcxoc/windows_11_24h2_update_made_my_arm_tablet_faster/) 2024-05-23

## Native ARM applications

You will get the best performance from apps that are built for ARM.

Go to [https://armrepo.ver.lt/](https://armrepo.ver.lt/) for a list of apps with native ARM support.
