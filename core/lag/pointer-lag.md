# Pointer lag

## Overview

* For a general introduction to lag, see [Lag](./).
* For lag specifically related to stroke rendering, see [Brush lag](lag.md).

<div align="left"><figure><img src="../../.gitbook/assets/image-000512.png" alt="" width="563"><figcaption></figcaption></figure></div>

## What is it?

**Pointer lag** is the delay between the physical position of the pen and the position reported by the operating system. It manifests as the cursor trailing behind the physical pen tip.

## How to demonstrate it

Pointer lag is most apparent when moving the pen across the desktop. The faster the pen moves, the greater the trailing distance (lag) becomes.

## Affected devices

All drawing tablets exhibit pointer lag to some degree; it is an inherent property of digital input systems.

* **Pen tablets (screenless):** Generally have lower latency. Lag is also less noticeable because there is no direct visual comparison between the pen tip and the cursor.
* **Pen displays:** Often have slightly higher latency. The lag is highly visible because the cursor and pen tip are on the same plane.
* **Standalone tablets:** Mobile devices (e.g., iPad, Samsung Galaxy Tab) often exhibit lower pointer lag than desktop pen displays due to highly integrated hardware and software stacks.

## "Zero Lag" claims

Claims of "zero lag" are technically incorrect.

* **All tablets have pointer lag.**
* **All pen displays show visible lag during fast movement.**

Reviews claiming "no lag" often demonstrate slow movements where the lag is minimal. During faster strokes, the gap between the pen and the cursor remains visible on all current commercial hardware.

## OS vs. Application lag

Applications receive pen data from the operating system. Consequently, an application cannot have less pointer lag than the OS itself. If lag is visible on the desktop, it will persist in every application.

## Variance between models

* **Pen tablets (screenless):** Variance is minimal. While some models may feel slightly more "floaty" than others, the difference is rarely significant to the user.
* **Pen displays:** Variance is more pronounced. Generally, smaller pen displays tend to have less perceived lag than larger models.

## Technical contributors

Pointer lag is determined by three primary factors:

* **Position smoothing:** Filtering used to stabilize pen data and reduce jitter.
* **Latency:** The time required to transmit and process data across the system.
* **Sampling rates:** How frequently the tablet reports position and how frequently the display refreshes.

## Real vs. Perceived lag

**Real lag** is the physical distance the pointer trails behind the pen, caused by processing latencies and smoothing filters.

**Perceived lag** is the user's subjective experience of that delay. Lower refresh rates (e.g., 30Hz vs. 60Hz) do not necessarily increase the physical trailing distance, but they make the movement appear choppier, which the brain interprets as increased lag.

## Specific contributors

* **Firmware smoothing:** Done on the tablet hardware to combat electromagnetic noise.
* **Driver smoothing:** Some drivers apply additional filtering for stability.
* **Report rate:** The frequency at which the tablet sends data to the PC.
* **Display refresh rate:** A higher refresh rate (e.g., 120Hz) significantly reduces perceived lag compared to standard 60Hz displays.

## Can pointer lag be reduced?

Reduction is possible but limited by hardware constraints.

### Display settings
* **Increase refresh rate:** If your display supports higher refresh rates (e.g., 144Hz), enabling it will reduce perceived lag.

### Hardware choices
* **Wacom Intuos Pro:** These tablets do not apply firmware-level smoothing, resulting in very low latency.
* **Non-Wacom brands:** Often apply a small amount of smoothing. While technically higher, it is often imperceptible to most users.

### Driver options
* **OpenTabletDriver:** This third-party driver allows users to disable most software-level smoothing.
  * **Intuos Pro:** Shows a noticeable reduction in lag, though tracking may become noisier.
  * **Cintiq Pro:** Shows minimal improvement, as the lag is primarily baked into the hardware firmware to compensate for display-induced noise.

### Application settings
* **No.** Applications cannot reduce pointer lag, as they are dependent on the data provided by the OS.

## Measuring lag

Lag is not a single constant; it is a function of speed.

* **At rest:** Zero lag.
* **Slow movement:** Minimal lag.
* **Fast movement:** Maximum lag.

Because of this, lag is best represented as a **lag curve** rather than a single number.

## Research and future measurement

I am currently researching methods to objectively measure pointer lag and establish "lag curves" for various pen displays. This work began in early 2026.

## EMR vs. Apple Pencil (iPad)

The Apple Pencil on iPad typically exhibits lower perceived lag than desktop EMR tablets. This is likely due to:

* **Vertical integration:** Apple optimizes the entire stack (hardware, firmware, OS).
* **Sensor proximity:** The Apple Pencil's active components are closer to the tip than in most EMR pens, potentially requiring less aggressive smoothing.
* **Reduced parallax:** A thinner stack between the digitizer and the display panel reduces visual interference.
* **Prediction algorithms:** iPads use predictive tracking to "guess" where the pen will be, reducing the visual gap at the cost of slight inaccuracy during sudden direction changes.



