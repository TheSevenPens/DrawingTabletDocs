# Tablet Driver Cleanup tool

## Overview

On **Windows**, manufacturer tablet drivers sometimes uninstalling a manufacturer tablet isn't enough. Occasionally the drivers leave bits of themselves around. The **TableDriverCleanup** tool created by user [**X9VoiD**](https://github.com/X9VoiD) can help remove these leftover bits.

If you want to see the source code to understand exactly what it does then go here: [https://github.com/X9VoiD/TabletDriverCleanup](https://github.com/X9VoiD/TabletDriverCleanup)&#x20;

Unfortunately I do not know of an equivalent tool for MacOS. But on the other hand, I don't see that it is needed on MacOS.

## Step 1: Follow the normal uninstall procedures

* Navigate to **Add/Remove programs** and uninstall your existing tablet drivers.&#x20;
* Note that you may be required to restart your computer.

## Step 2: Restart if needed

If Step 1 did not require a restart of your computer, then restart your computer now.

## Step 3: Run the TabletDriverCleanup tool

* Download [TabletDriverCleanup.zip](https://github.com/X9VoiD/WinUSBCleanup/releases/latest)&#x20;
* Extract all contents of the zip file to any location
* Right-click on `TabletDriverCleanup.exe` and click **Run as administrator**&#x20;
* The cleanup tool will open a terminal window and show the results of its cleaning. In the example below it did not find any leftover driver components to uninstall.
  * ![](<../../.gitbook/assets/Screenshot 2023-03-01 125517.png>)

