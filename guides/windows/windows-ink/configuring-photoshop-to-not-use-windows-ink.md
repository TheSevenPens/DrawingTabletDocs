# Configuring Photoshop to NOT use Windows Ink

This is a way to disable Windows Ink in recent. Photoshop. Though for some versions of Photoshop it seems to have no effect.

**STEP 1: Find this folder**

```
[Installation Drive]:\Users\[User Name]\AppData\Roaming\Adobe\[Photoshop_version]\[Photoshop_version]Settings\
```

Mine looks like this

```
C:\Users\TheSevenPens\AppData\Roaming\Adobe\Adobe Photoshop 2022\Adobe Photoshop 2022 Settings
```

**STEP 2: With notepad create a file in that folder called PSUserConfig.txt**

NOTE: Get the spelling and capitalization of the filename EXACTLY as shown.

So my filename is

```
C:\Users\TheSevenPens\AppData\Roaming\Adobe\Adobe Photoshop 2022\Adobe Photoshop 2022 Settings\PSUserConfig.txt
```

**STEP 3: Edit the txt of PSUserConfig.txt with the following two lines**

```
# Use WinTab  
UseSystemStylus 0  
```

The first line does not matter but the second does.

Make sure the spelling and capitalization are exactly as shown.

Also make sure there aren't any leading or trailing spaces.

Save the file.

**STEP 4: Close Photoshop if it is open**

**STEP 5: Launch Photoshop**
