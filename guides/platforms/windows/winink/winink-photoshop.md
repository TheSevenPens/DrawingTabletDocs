# Configuring Photoshop to NOT use Windows Ink

## Overview

By default, modern versions of Photoshop on Windows require the use of Windows Ink. However, you can configure Photoshop to not use Windows Ink and instead fall back to the WINTAB API.

To do this, you need to create a file called `PSUserConfig.txt`. Below are the instructions for creating this file.

`PSUserConfig.txt` is used in general for lots of different configuration options. For more general information about `PSUserConfig.txt`, see: [Enable Optional Extensions for Photoshop](https://helpx.adobe.com/photoshop/kb/enable-optional-extensions-photoshop-cc.html)

## **Instructions**

### **STEP 1: Find this folder**

```
[Installation Drive]:\Users\[User Name]\AppData\Roaming\Adobe\[Photoshop_version]\[Photoshop_version]Settings\
```

Mine looks like this:

```
C:\Users\TheSevenPens\AppData\Roaming\Adobe\Adobe Photoshop 2022\Adobe Photoshop 2022 Settings
```

### **STEP 2: With Notepad, create a file in that folder called PSUserConfig.txt**

NOTE: Get the spelling and capitalization of the filename EXACTLY as shown.

So my filename is:

```
C:\Users\TheSevenPens\AppData\Roaming\Adobe\Adobe Photoshop 2022\Adobe Photoshop 2022 Settings\PSUserConfig.txt
```

### **STEP 3: Edit the contents of PSUserConfig.txt with the following two lines**

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

* [**r/wacom - I finally found the fix for my Photoshop input lag on sliders and small movements**](https://www.reddit.com/r/wacom/comments/yx5yms/i_finally_found_the_fix_for_my_photoshop_input/) 2022-11-16
* [**r/huion - Help, Photoshop won't detect pen pressure :c Huion Gt-190**](https://www.reddit.com/r/huion/comments/14hk5yr/help_photoshop_wont_detect_pen_pressure_c_huion/) 2023-06-23
* [**r/wacom - Photoshop 2022 slider delay**](https://www.reddit.com/r/wacom/comments/sm7e3z/photoshop_2022_slider_delay/) 2022-02-06
