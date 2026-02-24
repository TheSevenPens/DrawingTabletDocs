# Windows Ink

## **Overview**

**Windows Ink** is an API and set of features in Microsoft Windows that enable using a pen to work with your PC.

## Background

More here: [The history of Windows Ink](winink-history.md). Windows Ink is one of two APIs used for Windows to talk to a tablet. The other, older one, is called WinTab.

## Configuring Windows Ink

In general you can configure Windows Ink in two places: In the tablet driver and in an application.

Conceptually the user experience looks like this:

<figure><img src="../../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

For a tablet driver, the Windows Ink configuration is always a single checkbox. For details on the eact user interface in the drivers, look here [Configure Windows Ink in the tablet driver](winink-config-driver.md).&#x20;

For apps, typically the Windows Ink configuration is presented as a set of choices. The simplest set of choices will literally say "Windows Ink" and "WinTab". And sometimes the user interface is just very different from what is shown above. To find exact details for an app, go here: [Configure Windows Ink for apps](winink-config-apps.md)

However, apps can get complicated in how allow you to configure thesd settings

* There can be more than two options, maybe 3 or 4 or 5
  * Multiple items can correspond to "Windows Ink"
  * Multiple items can correspond to "WinTab"
* Apps can call "Windows Ink" by different names. They may call it "Windows Pointer API".
* Some apps do not give you ANY options. They always use Windows Ink or they always use WinTab. And they don't give you any visual feedback about which API they are using.

## How these settings behave

* Tablet drivers&#x20;
  * Tablet drivers ALWAYS work with WinTab. The checkbox has NO EFFECT on whether a tablet driver supports WinTab.
  * The tablet driver Windows Ink checkbox only controls whether they ALSO work with Windows Ink. So if he checkbox is enabled, it means the driver is talking BOTH Windows Ink and WinTab.
  * You DO NOT need to restart the driver if you change this setting.&#x20;
* Applications
  * The choice is mutually exclusive. The app will only using ONE of the two APIs at any given time. It will EITHER use Windows Ink OR ELSE it will use WinTab.
  * If you change this setting, you SHOULD restart the app. For some apps, it doesn't matter. But other apps become very confused if you switch this setting and try to continue drawing.&#x20;

## My recommendation for configuring you system

### Base configuration

* In Tablet Driver - Enable Windows Ink - this means Windows Ink will be available for all apps
* In Each App - Configure the app to use Windows Ink. If you change the setting, restart the app.

<figure><img src="../../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

This configuration will work with most apps.

### Handling apps that can't handle Windows Ink

This covers:

* Apps that ONLY use WinTab
* Apps that are currently having problems with Windows Ink

If you app gives you the choice between Windows Ink and WinTab, switch to WinTab and restart the app.

<figure><img src="../../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

If the app only supports Windows Ink in the first place, you don't need to configure the app at all.

You don't need to change the tablet driver setting because no matter what the checkbox is set to, the driver will ALWAYS allow apps to talk to it with WinTab.

## This configuration  will not work correctly

IN this configuration the tablet driver is being told to ONLY talk in WinTab and the application to only use Windows Ink. These settings DO NOT agree.

<figure><img src="../../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

## App-specific overrides in the tablet driver

As shown above the driver setting is GLOBAL and affects ALL applications that talk with the driver.

However, for advanced cases you can configure your tablet driver to configure the Windows Ink setting for specific apps. However, you should not need to ever need to do this if you follow the recommendations I have given above.

## Tips for troubleshooting

If you are having problems with your tablet on Windows, one of the first things you should verify is how Windows Ink is configured:

* In your application
* In your tablet driver
  * And check if the tablet driver has an app-specific configuration for Windows Ink
