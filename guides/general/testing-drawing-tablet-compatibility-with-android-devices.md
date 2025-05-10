# Testing Drawing Tablet Compatibility with Android devices

## Testing criteria&#x20;

* Pressure sensitivity&#x20;
* Tilt support&#x20;
* Active area mapping works in both landscape and portrait&#x20;
* Active area mapping automatically matches aspect ratio of android device&#x20;

## Pen tablet testing results

<table><thead><tr><th width="267.75">Device </th><th width="148.6666259765625">Android version </th><th width="113.3333740234375">Tablet</th><th>Status </th></tr></thead><tbody><tr><td>Google Pixel 9a </td><td>15 </td><td>PTH-660 </td><td>WORKS </td></tr><tr><td>Google Pixel 9a </td><td>15 </td><td>PTK-670 </td><td>WORKS </td></tr><tr><td>Google Pixel 9a </td><td>15 </td><td>CTL-672 </td><td>DOES NOT WORK </td></tr><tr><td>Samsung Galaxy Tab S8 Ultra </td><td>14 </td><td>PTH-660 </td><td>WORKS </td></tr><tr><td>Samsung Galaxy Tab S8 Ultra </td><td>14 </td><td>PTK-670 </td><td>WORKS </td></tr><tr><td>Samsung Galaxy Tab S8 Ultra </td><td>14 </td><td>CTL-672 </td><td>DOES NOT WORK </td></tr><tr><td>Samsung S24 Ultra </td><td>15 </td><td>PTH-660 </td><td>WORKS </td></tr><tr><td>Samsung S24 Ultra </td><td>15 </td><td>PTK-670 </td><td>WORKS </td></tr><tr><td>Samsung S24 Ultra </td><td>15 </td><td>CTL-672 </td><td>DOES NOT WORK </td></tr></tbody></table>



## Pen display results

**Setup 1: Huion Kamvas 13 + Samsung Galaxy Tab S8 Ultra**

The following setup below worked for me.

* For this setup, I used a **Microsoft Surface Thunderbolt 4 Dock**&#x20;
* Samsung S8 Ultra connected to the dock via the dock's attached Thunderbolt 3 cable
* Huion Kamvas top USB-C port connected with Huion 3-in-1 cable:&#x20;
  * 3-in-1 cable red USB-A end (for power) connected to dock.
  * 3-in-1 cable black USB-A end (for data ) connected to dock.
  * 3-in-1 cable HDMI end not connected
* Huion Kamvas 13 lower USB-C port connected to the USB-C port on dock using a Thunderbolt 3 cable.

**Step 2: Samsung Galaxy S9 FE**&#x20;

Samsung Galaxy S9 FE does not work with an external monitor. Because of this,  I was unable to get it to work a pen display.
