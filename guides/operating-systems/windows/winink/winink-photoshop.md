# Configuring Photoshop to NOT use Windows Ink

## Overview

By default modern versions of Photoshop on Windows require the use of Windows Ink. However, you can configure Photoshop to not use Windows Ink and instead fall back to the WINTAB API.

To do this you need to create a file called "PSUserConfig.txt" file. Below you can see the instructions for creating this file.

The PSUserConfig.txt is used in general for lots of different configurations options. For more general information about the PSUsertConfig.txt, see: [Enable Optional Extensions for Photoshop](https://helpx.adobe.com/photoshop/kb/enable-optional-extensions-photoshop-cc.html)

## **Instructions**

### **STEP 1: Find this folder**

```
[Installation Drive]:\Users\[User Name]\AppData\Roaming\Adobe\[Photoshop_version]\[Photoshop_version]Settings\
```

Mine looks like this

```
C:\Users\TheSevenPens\AppData\Roaming\Adobe\Adobe Photoshop 2022\Adobe Photoshop 2022 Settings
```

### **STEP 2: With notepad create a file in that folder called PSUserConfig.txt**

NOTE: Get the spelling and capitalization of the filename EXACTLY as shown.

So my filename is

```
C:\Users\TheSevenPens\AppData\Roaming\Adobe\Adobe Photoshop 2022\Adobe Photoshop 2022 Settings\PSUserConfig.txt
```

### **STEP 3: Edit the txt of PSUserConfig.txt with the following two lines**

```
# Use WinTab  
UseSystemStylus 0  
```

The first line does not matter but the second does.

Make sure the spelling and capitalization are exactly as shown.

Also make sure there aren't any leading or trailing spaces.

Save the file.

### **STEP 4: Close Photoshop if it is open**

### **STEP 5: Launch Photoshop**

## **Other resources**

**Reddit posts:**

* [https://www.reddit.com/r/wacom/comments/yx5yms/i\_finally\_found\_the\_fix\_for\_my\_photoshop\_input/](https://www.reddit.com/r/wacom/comments/yx5yms/i\_finally\_found\_the\_fix\_for\_my\_photoshop\_input/)&#x20;
* [https://www.reddit.com/r/huion/comments/14hk5yr/help\_photoshop\_wont\_detect\_pen\_pressure\_c\_huion/](https://www.reddit.com/r/huion/comments/14hk5yr/help\_photoshop\_wont\_detect\_pen\_pressure\_c\_huion/)&#x20;
* [https://www.reddit.com/r/wacom/comments/sm7e3z/photoshop\_2022\_slider\_delay/](https://www.reddit.com/r/wacom/comments/sm7e3z/photoshop\_2022\_slider\_delay/)&#x20;
