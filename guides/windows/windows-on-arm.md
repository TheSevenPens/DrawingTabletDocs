# Windows on ARM

## Overview

We are now seeing Windows computers running on ARM processors. This holds gives us the possibility for cooler running, high-performance machines with great battery life.

## Drawing tablets compatibility with Windows on ARM

Unfortunately, As of 2024/06/18 no drawing tablets work when used with Windows on ARM processors. I had been hoping that tablet manufacturers would have already updated their drivers in preparing for the widespread availability of ARM PCs in June of 2024. However that did not happen. And existing intel tablet drivers do not work correctly.

I do expect this situation will be addressed quickly with driver updates. And I will update this page as the situation evolves.

### June 2024 update video

{% embed url="https://www.youtube.com/watch?v=3RGkj0vs-z0" %}

### Manufacturer driver testing results

I did all my testing an a Surface Laptop 15 inch (7th edition) using the Snapdragon X Elite processor.&#x20;

### WACOM drivers

**Wacom ARM driver status** - Wacom is aware of the issue and is working on ARM drivers - [Does Wacom have a driver for PCs that run Windows 11 on ARM processors (e.g. Snapdragon X)? ](https://support.wacom.com/hc/en-us/articles/23838303808407-Does-Wacom-have-a-driver-for-PCs-that-run-Windows-11-on-ARM-processors-e-g-Snapdragon-X)

* driver version 6.4.6-2&#x20;
  * status: <mark style="color:red;">**DOES NOT WORK**</mark> - installer says the operating system is not supported.
  * tested on 2024/06/18

### XP-PEN drivers

**XP-Pen ARM driver status** - I contacted XP-Pen support and they have not communicated any plans about an ARM driver

* driver version 4.0.1.240520&#x20;
  * status: <mark style="color:red;">**DOES NOT WORK**</mark> - installs but driver UI crashes, pen does not move pointer
  * tested on 2024/06/18&#x20;
* driver version 3.4.14.240603&#x20;
  * status: <mark style="color:red;">**DOES NOT WORK**</mark> - installs but driver UI crashes, pen does not move pointer
  * tested on 2024/06/18

### HUION drivers

**Huion ARM driver status** - They are actively working on a ARM driver.

* driver version v15.7.6.1073&#x20;
  * status: <mark style="color:red;">**DOES NOT WORK**</mark> - driver UI does not launch, pen does not move pointer
  * tested on 2024/06/18

## XENCELABS drivers

Xencelabs ARM driver status - they are actively working on an ARM driver and have a beta version you can try out at on their driver download page [https://www.xencelabs.com/support/download-drivers](https://www.xencelabs.com/support/download-drivers)

## Older Windows ARM devices

Microsoft previously released versions of the Surface Pro with using the SQ1 and SQ2 ARM processors.   Interestingly, the new Windows improvements for ARM processors seem to be improving performance on these old devices.

See this reddit thread: [https://www.reddit.com/r/Surface/comments/1czcxoc/windows\_11\_24h2\_update\_made\_my\_arm\_tablet\_faster/](https://www.reddit.com/r/Surface/comments/1czcxoc/windows\_11\_24h2\_update\_made\_my\_arm\_tablet\_faster/)

## Native ARM applications

Your best performance will be with those apps that are built for ARM.

Go to [https://armrepo.ver.lt/](https://armrepo.ver.lt/) for a list of apps that are available with native ARM support.

&#x20;
