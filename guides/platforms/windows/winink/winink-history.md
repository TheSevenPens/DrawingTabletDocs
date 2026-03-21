# The history of Windows Ink

## Background

Windows Ink is the evolution of the pen/stylus capabilities that started appearing in Windows in the early 2000s. This was an era when Microsoft was focusing on building products around a **Tablet PC** concept - what we might call a **pen computer** today. And as a tablet, it was thought that using a pen with these devices would be critical for tasks such as note taking, marking up documents, electronic signatures, etc.

And this support is extended not only to computers that have a screen that can be used with a pen, but also tablet devices that attach to computers such as pen tablets pen displays.

## Adoption

This has been a bit of a rough journey in Windows.

**Before Windows Vista**

When the first tablet PC features appeared they could easily interfere with drawing tablets.

**Windows Vista (2007)**

You can see some of how the pen input evolved in this document from Microsoft describing [**Pen and Touch Input in Windows Vista**](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ms702418\(v=vs.85\)?redirectedfrom=MSDN) ([archive link](https://archive.is/0I3tB)). But it was easy to disable those tablet PC features.

**Windows 7 (2009)**

By the time Windows 7 appeared, the ability to disable Tablet PC features via the Windows user interface started going away. People were forced to edit registry keys.

**Windows 8 (2012)**

By Windows 8, Windows stopped listening to the registry keys. So the previous workaround to disable these features no longer worked. At the release of Windows 8 it was essentially not possible to correctly use a drawing tablet with Windows.&#x20;

Eventually tablet drivers started offering a checkbox to disable the use of Windows Ink features and then we could all draw again.

At this point many apps only used WINTAB. So, many people just disabled Windows Ink entirely on their computer. And this was a workable solution for the vast majority of people.

**Windows 10 (2015)**

As we progressed to Windows 10, several things happened:

* Some apps started to ONLY work with Windows Ink. Microsoft OneNote is a great example.
* Some apps work with BOTH Windows Ink and WINTAB
* Most modern apps handle Windows Ink.
* There are are still some apps that only work with WINTAB.

So these days the best option is to ENABLE Windows Ink in the driver, but disable it for specific apps using the driver's app-specific settings.

## The future (updated on 2024)

Writing this in April 2024, we may be looking at more disruptive changes.

Windows on ARM CPUs seems to be coming. I expect this may affect the driver situation:

* It's unclear if older drivers can work with Windows on ARM.&#x20;
* If that is the case, it is unclear how long a drawing tablet manufacturer will take to have updated drivers
* When they do have updated drivers, they may drop support for older tablets.

When Windows-on-ARM computers start appearing, I'll get one and start experimenting.



