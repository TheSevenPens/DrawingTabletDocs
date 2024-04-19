# Windows PNP support for drawing tablets

## Introduction

In Microsoft Windows, for SOME tablets, even if you don't install a tablet driver, the drawing tablet can be used in a very rudimentary way through its built-in PNP support. PNP = "Plug-and-Play".&#x20;

## Identifying if the Windows using PNP support with your tablet

The easiest way to see if this how Windows is interacting with your tablet is to look at the system pointer.

Normally your pointer will look like this when you are using the mouse or when you have a tablet driver installed.&#x20;

![](../../.gitbook/assets/Snap1.png)

But if Windows is using its PNP support the pointer will look like this.

![](<../../.gitbook/assets/PXL\_20230902\_135357961 (1).jpg>)

(NOTE: It's hard to do a screen capture of this pointer, so I had to rely on a phone camera)

## Limitations of PNP mode

Windows PNP mode might seem like a really cool thing. But it's really not very useful for drawing tablets.

There are a large set of limitations that come with windows PNP mode. And many of the things you will need to configure with a drawing tablet simply are not available through PNP mode.

* There is no pressure sensitivity
* There is no tilt support
* You cannot control how to map the active area of your tablet to a display in any way
* You cannot control what the buttons on the pen does
* You cannot control what the buttons on the tablet do&#x20;

## When should you use PNP drivers?

If your manufacturer tablet driver is having problems, the PNP drivers may be a "last resort".

## Using PNP mode for testing and diagnosing problems

If you are having problems with your tablet, trying PNP mode can be a good diagnostic test to help identify if the problem is related to the manufacturer tablet driver or not. More here: [**Testing with Windows PNP drawing tablet drivers**](../../troubleshooting/testing-with-windows-pnp-drawing-tablet-drivers.md)&#x20;

## Interactions between tablet drivers and PNP mode

When you install a tablet driver, basically the tablet driver takes over handling the tablet and windows no longer uses its PNP mode.

And so the PNP mode will not affect you anymore.

Every now and then I have windows use PNP mode even though a driver is installed. Typically this seems to happen when:

* Windows is starting up and the tablet driver hasn't been started yet. For a little bit of time maybe a few seconds maybe 30 seconds you might see the PNP mode cursor. But then the tablet driver will start and it will go back to normal. I might see this happen once or twice a year on my windows machines
* Sometimes when the tablet driver is having problems working with windows then you might see the PNP mode being used. &#x20;

## Notes

Windows supports PNP for lots of devices. For example mice or monitors. PNP is not limited to just tablets.&#x20;

