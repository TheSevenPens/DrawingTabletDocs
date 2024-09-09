# Disable the press-and-hold ring in Windows

## Windows 11

### Get to the Pen and Touch settings

* Open Control Panel
* Type in "pen" and search
* You'll find a section called "Pen and Touch"
* Click on **Change tablet pen settings**

![](<../../.gitbook/assets/image (269).png>)



* The **Pen and Touch** dialog will launch

#### OPTION Getting to the Pen and Touch dialog from the command line

If you are comfortable using the command line, you can get to the Pen and Touch dialog directly.

```
"C:\WINDOWS\system32\rundll32.exe" shell32.dll,Control_RunDLL TabletPC.cpl @0,pen
```

### Configure the Press and Hold setting

* Navigate to the **Touch** tab
* Select **Press and Hold**
* Click **Settings**

![](<../../.gitbook/assets/image (311).png>)

* The **Press and Hold Settings** dialog will launch
* Disable **Enable press and hold for right-clicking**

![](<../../.gitbook/assets/image (245).png>)

* Click **OK** to close the **Press and Hold Settings** dialog
* Click **OK** to close the Pen and Touch dialog
