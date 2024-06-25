# Windows on ARM



## Overview

We are now seeing Windows computers running on ARM processors. This holds gives us the possibility for cooler running, high-performance machines with great battery life.

Unfortunately, As of 2024/06/18 no drawing tablets work when used with Windows on ARM processors. I had been hoping that tablet manufacturers would have already updated their drivers in preparing for the widespread availability of ARM PCs in June of 2024. However that did not happen. And existing intel tablet drivers do not work correctly.

I do expect this situation will be addressed quickly with driver updates. And I will update this page as the situation evolves.

## June 2024 update video

{% embed url="https://www.youtube.com/watch?v=3RGkj0vs-z0" %}

## Manufacturer driver testing results

I did all my testing an a Surface Laptop 15 inch (7th edition) using the Snapdragon X Elite processor.&#x20;

### WACOM drivers

Wacom is aware of the issue and is working on ARM drivers - [Does Wacom have a driver for PCs that run Windows 11 on ARM processors (e.g. Snapdragon X)? ](https://support.wacom.com/hc/en-us/articles/23838303808407-Does-Wacom-have-a-driver-for-PCs-that-run-Windows-11-on-ARM-processors-e-g-Snapdragon-X)

* driver version 6.4.6-2&#x20;
  * status: <mark style="color:red;">**DOES NOT WORK**</mark> - installer says the operating system is not supported.
  * tested on 2024/06/18

### XP-PEN drivers

* driver version 4.0.1.240520&#x20;
  * status: <mark style="color:red;">**DOES NOT WORK**</mark> - installs but driver UI crashes, pen does not move pointer
  * tested on 2024/06/18&#x20;
* driver version 3.4.14.240603&#x20;
  * status: <mark style="color:red;">**DOES NOT WORK**</mark> - installs but driver UI crashes, pen does not move pointer
  * tested on 2024/06/18

### HUION drivers

* driver version v15.7.6.1073&#x20;
  * status: <mark style="color:red;">**DOES NOT WORK**</mark> - driver UI does not launch, pen does not move pointer
  * tested on 2024/06/18

&#x20;
