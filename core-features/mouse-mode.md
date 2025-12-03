# Mouse mode

&#x20;            &#x20;

## Introduction

For some occasions and for some people they would prefer if a drawing tablet pen behaved more like a mouse.

For this reason drawing tablet drivers offer something that is called **mouse mode**.

## Mouse mode uses relative positioning

Drawing tablets are absolute positioning devices. But enabling mouse mode will make them behave like a relative positioning device like a mouse.

Learn more here: [Absolute versus relative positioning](absolute-versus-relative-positioning.md)

## How does mouse mode affect the tablet?

Mouse mode is implemented in the tablet driver has no effect on the tablet hardware.

The tablet continues to use absolute positioning internally.&#x20;

## How does mouse mode affect the driver?

The driver takes the absolute positioning information it receives from the tablet and then translates that into relative positioning data when it sends data position data to the operating system.

## How does mouse mode affect drawing quality?

In theory it shouldn't affect the quality of drawing.

In practice, it depends on what the driver is exactly doing.

Here's an example of the Wacom driver vs Huion driver in Krita on Windows.

<div align="left"><figure><img src="../.gitbook/assets/image (410).png" alt="" width="563"><figcaption></figcaption></figure></div>

As you can see the Wacom driver creates very jerky position data when mouse mode is enabled. It does not have to be like this, they could do better like Huion does.

Also, this difference is not due to hardware. I tested the same Wacom tablet with OpenTabletDriver also set to mouse mode (OTD calls this "Relative mode") and the lines were smooth.

## How mouse mode affect pen features

This section is incomplete

* XP-Pen (ver 3.4.7): Enabling Mouse Mode loses pressure sensitivity on Windows
* Wacom: TBD
* Huion: TBD

## Windows Ink

On Windows, Mouse Mode in some drivers may disable Windows Ink

You may need to restart an drawing application if you change the mouse mode setting.&#x20;

##

## Configuring mouse mode

### Wacom

In **Wacom Tablet Properties** app, select your pen, navigate to the **Mapping** tab, then under the Mode area you will see a setting you can switch between **Pen** and **Mouse**&#x20;

<div align="left"><figure><img src="../.gitbook/assets/image (272).png" alt="" width="375"><figcaption></figcaption></figure></div>

Once you enable mouse mode, you'll see some new configuration options.

<div align="left"><figure><img src="../.gitbook/assets/image (319).png" alt="" width="375"><figcaption></figcaption></figure></div>

### Huion

In the Huion driver, click **Digital Pen**, then enable or disable **Mouse Mode** at the bottom&#x20;

<div align="left"><figure><img src="../.gitbook/assets/image (236).png" alt="" width="563"><figcaption></figcaption></figure></div>

## Restarting apps after mouse mode

Some drawing applications may get confused if they are running and mouse mode is switched on or switched off. So you may need to restart those apps.

## Mouse mode on pen displays

Most often, tablet drivers dot not offer mouse mode option for a pen display.&#x20;

There isn't a technical limitation. In theory, pen displays could support mouse mode just as well as a pen tablet. I believe it isn't offered typically because most users would would be confused by the discrepancy in the position of the mouse pointer on the screen and the physical position of the tip of the pen.

Nonetheless, some people do request mouse mode for their pen displays. If you do really want mouse mode, consider using OpenTabletDriver instead of your manufacturer tablet driver.

More here: [**OpenTabletDriver**](../guides/drivers/opentabletdriver/)   &#x20;



&#x20;
