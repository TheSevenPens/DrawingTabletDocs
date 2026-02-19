# Windows Ink

## **Overview**

**Windows Ink** is an API and set of features in Microsoft Windows that enable using a pen to work with your PC. &#x20;

## Background

More here: [The history of Windows Ink](winink-history.md). Windows Ink is one of two APIs used for Windows to talk to a tablet. The other, older one, is called WinTab.

## Configuring Windows Ink

You can configure Windows Ink in two places.

My recommendation is to configure it in the application. And only change it in the driver if absolutely necessary.

* [Configure Windows Ink for apps](winink-config-apps.md)&#x20;
* [Configure Windows Ink in the tablet driver](winink-config-driver.md)

## My recommendation

### Base configuration: Use Windows Ink

* In Tablet Driver - Enable Windows Ink - this means Windows Ink will be available for all apps
* In Each App - Configure the app to use Windows Ink. If you change the setting, restart the app.

### For specific apps that don't work well with Windows Ink

* In the App - configure the app to NOT use Windows Ink. If you change this setting, restart the app
* In tablet driver - Usually you don't need to do anything. However, it may be necessary in the driver to create an application-specific setting to disable the use for Windows Ink

## Tips for troubleshooting

If you are having problems with your tablet on Windows, one of the first things you should verify is how Windows Ink is configured:

* In your application
* In your tablet driver
  * And check if the tablet driver has an app-specific configuration for Windows Ink
