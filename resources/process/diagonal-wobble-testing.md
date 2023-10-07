# Diagonal wobble testing

I measure diagonal wobble using a simple procedure

## Resources

**Template** - I built a standard 1000x1000 pixel PNG I use that has gridlines at every 100 pixels. A Python script generates these images.

**Ruler** - I use a simple plastic ruler. I do not use metal rulers because they might interfere with the EMR tech in the pen.

**Driver** - I use the latest manufacturer driver. For very old tablets that don't have recent drivers, I use OpenTabletDriver.

**Application** - I use Krita&#x20;

## Testing process

* Verify the plastic ruler has no rough spots or pumps that would affect the measurement. It should be smooth.
* For pen tablets, set the active area to a single display.
* For pen tablets, set the driver to match the aspect ratio of the tablet to the display.
* Set Krita zoom to 100%.
* Trace usually at least five 10cm lines at 45 degrees using the plastic ruler.&#x20;
  * Draw the line from the lower left to the upper right.
  * Take 3 seconds to draw the line.
  * The pen is tilted at about 30 to 40 degrees from vertical.
  * To make it simple, I use load a PNG template to help guide the lines.
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



## Template

This is version 3 of my wobble template. This is a 4000x2000 PNG image.

<figure><img src="../../.gitbook/assets/Wobble Template V3.png" alt=""><figcaption></figcaption></figure>
