# Measuring diagonal wobble

I measure [**diagonal wobble**](../core-features/diagonal-wobble.md) using a simple procedure

## Resources

**Diagonal template image** - a standard PNG file created with using Adobe Illustrator. This provides visual guides that make it easier for the testing. Image is shown later in this doc.

**Ruler** - I use a simple plastic ruler. I do not use metal rulers because they might interfere with the EMR tech in the pen.

**Driver** - I use the latest manufacturer driver. For very old tablets that don't have recent drivers, I use OpenTabletDriver.

**Application** - Krita&#x20;

## Testing process

* Verify the plastic ruler has no rough spots or bumps that would affect the measurement. It should be smooth.
* Tablet configuration
  * For pen tablets, set the active area to a single display.
  * For pen tablets, set the driver to match the aspect ratio of the tablet to the display.
* App configruation
  * Load the diagonal template image
  * Set Krita zoom to 100%.
  * Set Brush to **Ink-2 Fineliner** with default brush settings and set size to 5 pixels.
  *

      <div align="left">

      <figure><img src="../.gitbook/assets/image (462).png" alt="" width="320"><figcaption></figcaption></figure>

      </div>
* Drawing
  * The template requires 3 sets of lines drawn at different speeds - 3 lines for each speed
  * Draw the line from the lower left to the upper right.
    * Follow the specified speed as much as possible
    * pen tilt = about 30 to 40 degrees from vertical.
* Save as a PNG

## Evaluation wobble (DRAFT)

**Considerations**

* **MAGNITUDE** - how wobble is physical displaced from "center" of line.
* **VELOCITY** - Is wobble visible in slow, medium, fast strokes

**Scale**

* **VERY LOW** - Strokes easily confused for a perfectly straight line
* **LOW** - lines mostly straight with occasional and minor wobble
* **MEDIUM** - moderate Wobble visible in majority of lines
* **HIGH** - moderate wobble available in lots of lines
* **VERR HIGH** - lots of wobbling in lines

## Wobble testing template image

<figure><img src="../.gitbook/assets/Wobble Template V7.png" alt=""><figcaption></figcaption></figure>

