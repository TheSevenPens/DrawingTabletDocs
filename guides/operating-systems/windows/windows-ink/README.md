# Windows Ink

## **Overview**

**Windows Ink** is an API and set of features in Microsoft Windows that enable using a pen to work with your PC.  More here: [The history of Windows Ink](the-history-of-windows-ink.md). Windows Ink is one of two APIs used for Windows to talk to a tablet. The other, older one, is called WinTab.

There are two places to configure Windows Ink and they should be coordinated:

* In your tablet driver - you can configure it for all apps or for specific apps. See [**configure Windows Ink in the tablet driver**](configure-windows-ink-in-the-tablet-driver.md) &#x20;
* In your pen-aware application. See [**configure Windows Ink in an application**](configure-windows-ink-for-apps.md)&#x20;

## Recommended setting

### Baseline configuration: Use Windows INK

In Tablet Driver

* Enable Windows Ink - this means Windows Ink will be available for all apps

In Each Applications

* Configure the app to use Windows Ink
* If you change this setting, restart the app

### Customization for specific apps

You may have an app that is having problems using windows Ink.

In the application

* Configure the application to use Windows Ink
* If you change this setting, restart the app

In tablet driver

* Usually you don't need to do anything&#x20;
* However, it may be necessary in the driver to create an application-specific setting to disable the use for Windows Ink

## Tips for troubleshooting

If you are having problems with your tablet on Windows, one of the first things you should verify is how Windows Ink is configured:

* In your application
* In your tablet driver
  * And check if the tablet driver has an app-specific configuration for Windows Ink

##
