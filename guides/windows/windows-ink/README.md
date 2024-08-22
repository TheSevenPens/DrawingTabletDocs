# Windows Ink

## **Overview**

**Windows Ink** is an API and set of features in Microsoft Windows that enable using a pen to work with your PC.  More here: [The history of Windows Ink](the-history-of-windows-ink.md). Windows Ink is one of two APIs used for Windows to talk to a tablet. The other, older one, is called WinTab.

## Coordinating Windows Ink in the driver and application

Whichever API you want to use, **you must configure it in two places (app and driver) the same way**.

* To use Windows Ink
  * Enable Windows Ink in the driver
  * Enable Windows Ink in the app
* To use WinTab instead
  * Disable Windows Ink in the driver (this enables WinTab)
  * Disable Windows Ink in the app (choosing WinTab instead)

Instructions:

* How to [**configure Windows Ink in the tablet driver**](configure-windows-ink-in-the-tablet-driver.md) &#x20;
* How to [**configure Windows Ink in an application**](configure-windows-ink-for-apps.md)&#x20;
  * NOTE: If you change between Windows Ink and WinTab in app, you should restart the app.

## Notes the user experience

Drivers and apps typically present the Windows Ink vs WinTab choice in different ways.

Drivers show it most often as a Windows Ink checkbox. If the box is checked, then Windows Ink is used. If the box is unchecked, then WinTab is used. The driver UI does not show the literal phrase "WinTab" anywhere. &#x20;

Here's an example from the Wacom Tablet properties app.

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

Apps usually express it as an API choice and let you can see Windows Ink or WinTab in their UX. Here's an example from Krita.

<figure><img src="../../../.gitbook/assets/image (6).png" alt="" width="375"><figcaption></figcaption></figure>

Another thing Krita demonstrates is that Windows Ink can go by different names.

Here's what it looks like in Clip Studio paint.&#x20;

<figure><img src="../../../.gitbook/assets/image (5).png" alt="" width="298"><figcaption></figcaption></figure>

## Tip: Be aware of Windows Ink configuration

Sometimes applications have trouble working with one of the APIs, so switching to the other API can sometimes solve problems.

## Initial Default Configuration

This diagram shows the typical initial configuration for apps and drivers. Usually every app and driver is configured by default to Use Windows Ink.

<figure><img src="../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>



## Recommended configuration

As of 2023 enough applications on Windows support Windows Ink (or require it) that I suggest this configuration:

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

* In the tablet driver:
  * Enable Windows Ink for all apps
  * Disable Windows Ink for and specific apps where you want to use the WinTab API
* In the applications
  * Ensure they are configured to use the appropriate API as specified in the tablet driver&#x20;

## Application support for Windows Ink

In the years since Windows Ink has been available, here's how apps have adopted it.

* The vast majority of apps support using either Windows Ink or WinTab
  * Almost all of these apps, by default use Windows Ink
  * For almost all apps, switching to WinTab is easy.&#x20;
  * For some apps though switching to WinTab is complicated. For example, for Adobe deliberately makes it complicated to switch to WinTab.
* Some apps ONLY support Windows Ink. For example: Microsoft OneNote.
* Some apps ONLY support WinTab. These tend to be older apps that have not been updates.

