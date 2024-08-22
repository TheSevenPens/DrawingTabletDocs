# Windows Ink

## **Overview**

**Windows Ink** is an API and set of features in Microsoft Windows that enable using a pen to work with your PC.  More here: [The history of Windows Ink](the-history-of-windows-ink.md). Windows Ink is one of two APIs used for Windows to talk to a tablet. The other, older one, is called WinTab.

## Coordinating Windows Ink in the driver and application

Whichever API you want to use, **you must configure it in two places (app and driver) the same way**.

* To use Windows Ink
  * Enable Windows Ink in the driver
  * Enable Windows Ink in the app
* To use WinTab instead
  * Enable WinTab in the driver
  * Enable WinTab Ink in the app

Instructions:

* How to [**configure Windows Ink in the tablet driver**](configure-windows-ink-in-the-tablet-driver.md) &#x20;
* How to [**configure Windows Ink in an application**](configure-windows-ink-for-apps.md)&#x20;
  * NOTE: If you change between Windows Ink and WinTab in app, you should restart the app.

## Tip: Be aware of Windows Ink configuration

Sometimes applications have trouble working with one of the APIs, so switching to the other API can sometimes solve problems.

## Recommended configuration

As of 2023 enough applications on Windows support Windows Ink (or require it) that I suggest this configuration:

* In the tablet driver:
  * Enable Windows Ink for all apps
  * Disable Windows Ink for and specific apps where you want to use the WinTab API
* In the applications
  * Ensure they are configured to use the appropriate API as specified in the tablet driver&#x20;
