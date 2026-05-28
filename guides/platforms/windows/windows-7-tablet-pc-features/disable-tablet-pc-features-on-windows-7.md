# Disable Tablet PC features on Windows 7

## Important

"Tablet PC" pen features are the original name for what today is called "Windows Ink".

These instructions were written in 2011 for Windows 7. Most people who used drawing tablets found that the Tablet PC features interfered with their creative applications.

And so, they needed instructions on how to turn it off.

Since Windows 7 the situation has evolved.

Modern tablet drivers that use Windows Ink usually have a checkbox to disable Windows Ink. So these instructions should no longer be necessary unless you are using a very old driver.

## **Overview**

* When Windows 7 detects that your PC is connected to a Wacom tablet, it automatically activates several Tablet PC features. More here: [Windows 7 Tablet PC features](./)
* These features would be helpful if you were using a Tablet PC, but can be rather annoying or really interfere with your use of creative applications such as Photoshop.
* The following instructions show you how to manually disable these features.

## Instructions

### Step 1: Install the latest drivers

The Wacom drivers are available here: [https://www.wacom.com/en-us/support/product-support/drivers](https://www.wacom.com/en-us/support/product-support/drivers).

### Step 2: Disable the Tablet PC Input Panel

Go to **Control Panel** > **Tablet PC Settings**

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2d6/1348194573062/1000w/12513771_image5.png)

Click on the **Other** tab

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2d8/1348194574187/1000w/12513771_image6.png)

On the **Other** tab, under **Tablet PC Input Panel** options, click **Go to Input Panel Settings**

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2da/1348194574076/1000w/12513771_image7.png)

Disable all the checkboxes under **Choose where to show the Input Panel icons and tab** and then click **OK**.

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2dc/1348194575033/1000w/12513771_image8.png)

### Step 3: Disable pen flicks

Open the **Pen and Touch** control panel

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2e4/1348194577837/1000w/12513771_image12.png)

Click on the **Flicks** tab

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2e6/1348194578427/1000w/12513771_image13.png)

Uncheck **Use flicks to perform common actions quickly and easily**

Uncheck **Display flicks icon in the notification area**

Press **OK**.

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2e8/1348194579003/1000w/12513771_image14.png)

### Step 4: Disable Press-and-Hold

To disable this…

In **Control Panel** go to **Pen and Touch**

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2eb/1348194579797/1000w/12513771_image15.png)

Under **Pen Options**, select **Press and Hold** and click **Settings**

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2ed/1348194580423/1000w/12513771_image16.png)

Uncheck **Enable press and hold for right-clicking**

Press OK

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2ef/1348194580933/1000w/12513771_image17.png)

### Step 5: Disable Dynamic Feedback

There’s no UI to disable Dynamic Feedback in Windows 7.

Instead, you have to modify the Windows Registry.

Open Notepad and create a new text file with the text below.

```
Windows Registry Editor Version 5.00
[HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\TabletPC] 
"TurnOffPenFeedback"=dword:00000001

[HKEY_CURRENT_USER\Software\Policies\Microsoft\TabletPC] 
"TurnOffPenFeedback"=dword:00000001 
```

Save the file as `disable-pen-feedback.reg`.

Make sure it has the extension **.reg** and not `.reg.txt`.

Right-click on `disable-pen-feedback.reg` and select **Merge**.

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2f4/1348194581983/1000w/12513771_image19.png)

Windows will warn you, but just click **Run**

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2f6/1348194582603/1000w/12513771_image20.png)

And Windows will warn you again, just press **Yes**.

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2f8/1348194583223/1000w/12513771_image21.png)

Finally, it will tell you that it has merged the settings.

![image](https://static1.squarespace.com/static/5005b450c4aa8b4d97612392/t/615291b02b34b67da526a2fa/1348194583076/1000w/12513771_image22.png)

### Step 6: Optionally, force Windows to accept the changes if needed

Sometimes all these changes will take place immediately. Sometimes it takes a little longer.

There are three options to trigger the change if it’s taking longer than expected:

* Option 1: Log off and then log back on.
* Option 2: Restart your machine.
* Option 3: (Expert) restart the “Tablet PC Input Service”
