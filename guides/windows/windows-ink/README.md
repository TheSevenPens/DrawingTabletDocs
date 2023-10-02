# Windows Ink

## **Overview**

**Windows Ink** is an API and set of features in Microsoft Windows that enable using a pen to work with your PC.  More here: [The history of Windows Ink](https://app.gitbook.com/o/-LBUpLETf4LFiwdypBiE/s/Nde0PQIvNcFZNVxuTO0G/\~/changes/2138/guides/windows/windows-ink/the-history-of-windows-ink)&#x20;

Windows Ink is one of two APIs used for Windows to talk to a tablet. The other, older one, is called WINTAB.

In theory, Windows Ink makes it easier for developer to build pen-enabled apps or add pen support for their existing apps.  It also provides a consistent, modern, single interface for an application to deal with pen input.&#x20;

## Coordinating Windows Ink configuration between driver and application

Whichever API you want to use, you have to configure it in two places the same way.

For example if you want to use Windows Ink:

* you have to enable Windows Ink in the tablet driver
* you have to enable Windows Ink in the application &#x20;

## Driver configuration of Windows Ink

A drawing tablet driver will let you use either pen API. In most tablet drivers you can even choose which API on a per-application basis.&#x20;

Read how to [**configure windows ink in tablet drivers**](configure-windows-ink-in-the-tablet-driver.md) &#x20;

## Application configuration of Windows Ink

Applications usually let you specific which API to use with the tablet. Some applications, only use a specific API. For example recent versions of OneNote only use the Windows Ink API.

NOTE: If you reconfigure an application to switch between APIs then you should restart the application.

Read how to [**configure Windows Ink for applications**](configure-windows-ink-for-apps.md)&#x20;

## Why you need to be aware of Windows Ink configuration

Sometimes applications have trouble working with one of the APIs, so switching to the other API can sometimes solve problems.

## Recommended configuration

As of 2023 enough applications on Windows support Windows Ink (or require it) that I suggest this configuration:

* In the tablet driver:
  * Enable Windows Ink for all apps
  * Disable Windows Ink for and specific apps where you want to use the WinTab API
* In the applications
  * Ensure they are configured to use the appropriate API as specified in the tablet driver&#x20;



