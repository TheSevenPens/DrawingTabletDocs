# Inspecting a drawing tablet

## Overview

This is a list of some things you should check when you (a) first set up your drawing tablet or (b) have an opportunity to inspect the drawing tablet before you purchase it.

This will save you a lot of headaches and disappointment later on.

## Testing before you setup the tablet

*   Tablets usually have a list of things they come with. This list will include things like cables cleaning cloths, pen nibs , etc. The list might be printed on the box, or it might be on a piece of paper inside the box, or it might be a list on the website of the tablet brand.

    Verify that you have all the things you're supposed to have.
* Examine the screen carefully with your eyes. You're looking for scratches or areas where the surface is worn out. If it's a new tablet you shouldn't see anything like that.
* Sometimes it might be difficult to see scratches so you might want to shine a bright light across the surface at an angle to identify any scratches.

## Getting prepared for functional testing

In order to perform test the tablet actually works you'll need to set it up. Follow this guide: [**Get started with a drawing tablet**](../basics/getting-started-with-a-drawing-tablet.md).

Then install any applications you need. I strongly suggest you install Krita from Krita.org. It's free and its behavior is consistent so it makes it an ideal application to test the functionality of a drawing tablet. So even if you don't plan on using Krita it's a very useful tool for troubleshooting.

Mobile phones can interfere with the operation of a tablet. Keep them away.

Ensure there isn't anything magnetic underneath the tablet. Some stands use magnets. Don't place the tablet on top of an electronic device like a laptop.&#x20;

## **Basic functional testing**&#x20;

### Connectivity

* Conduct the tests with a wired connection.
* Any then verify they work with wireless connection

### Drawing

* Check if the pen can draw in all locations on the active area
  * Just draw a lot of lines alll over the screen. You want to ensure that there aren't any gaps were you can't draw and that the position of the pen is accurately tracked.
* Check if the pressure going from 0% to 100%&#x20;
  * First do this in the driver. They usually have some regio where you can test the pressure.
  * Then do this in an application. I suggest using Krita.
  * You want to ensure that:
    * The pen isn't "stuck" at 0% pressure or 100% pressure
  * You may notice that the pressure is "jumpy" any low pressure this is normal for EMR pens. You can use pressure curves to control this.
* Check tilt works in all directions
  * draw some strokes and tilt the pen in different directions.
  * do this in multiple locations across the active area

## Pen display pen tracking accuracy

* With the pen held vertically and not moving, check that the pointer is close to the tip of the pen.
* With the pen held at a 45 degree angle and not moving, check that tilt compensation is working. As you tilt the pen check to make sure the pointer doesn't deviate too far from the tip of the pen. A little bit of drift is normal. Keeping the pen at 45 degrees, rotate the pen in a full circle.&#x20;
* Check that location of pen is tracked accurately in over the entire surface of the tablet

## **Express keys**

* Check if all the buttons, dials, work. A quick way to test this is to map the buttons to keypresses. Then you can open a notepad app and press the express keys and see it typing things

## **Pen display features**

* Check for stuck or dead pixels
* Check for basic color and brightness
* All tablets have some pointer lag. Usually it is very obvious in pen displays. Verify if you are OK with the amount it has.
* All pen displays have some minor edge and corner inaccuracy in tracking the pen location. Check this to see how much there is and if you are OK with this.&#x20;
* Verify you are OK with the anti-glare sparkle on the screen. Some people are very sensitive to this.
* Verify that the display does not have a color tint on the edges. More here: [Color tint on edges of display](../guides/pen-displays/color-tint-on-edges-of-display.md).

## **Surface**

Take your pen and move it around the surface.

There should be no rough patches. There should be no cuts or scratches deep enough that you can feel them through the pen. More here:&#x20;

* [surface wear on pen tablets](../guides/caring-for-your-tablet/surface-wear-on-pen-tablets.md)
* [surface wear on pen displays](../guides/caring-for-your-tablet/surface-wear-on-pen-displays.md)&#x20;

