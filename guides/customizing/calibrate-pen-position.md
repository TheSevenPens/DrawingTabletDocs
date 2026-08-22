# Calibrating pen position

## Overview

On a pen display, you may point at one location with the pen, but the pointer appears somewhere else. This could be due to the pen being incorrectly calibrated to the display. If you see the word "Calibrate" or "Calibration" anywhere in a tablet driver UI - it almost always is referring to Calibration pen position. For other kinds of calibration, see [Calibrating a drawing tablet](calibrating-color.md)

## Feature availability

Most pen displays offer a pen calibration feature. However, some pen displays like the Wacom Cintiq Pro 27, do not offer this calibration because they are designed to be well-calibrated when you get them and not require additional adjustment.

Calibrating pen position is NOT offered on pen tablets because they don't have screens so there is nothing to calibrate the pen position to.

## General workflow

First you must initiate the calibration process. This is usually done with a "Calibration" button somewhere in the driver UI.

Once the process starts, your tablet screen should go blank (typically all white) and you'll be directed to touch several spots on the screen. Usually this will be between 4 to 9 points. Once you have clicked all the points, the calibration data will be used to make the pen position match the pointer more closely.

Important notes when you perform this calibration:

* Hold the pen the normal way you would as you draw. For most people this will mean the pen is tilted around 45 degrees. DO NOT hold the pen vertically. That will produce less accurate results.
* Sit in your natural drawing posture. Do NOT move you eyes close to the tip of the pen. That will produce less accurate results.&#x20;

## Instructions

{% tabs %}
{% tab title="XP-Pen" %}
* Open the XP-Pen **Pentablet** app
* Under **Work area** > **Screen**, press **Calibrate**
* Follow the calibration steps
{% endtab %}

{% tab title="Huion" %}
* Open the **HuionTablet** app
* Under **Pen Display** > **Working Area**, press **Monitor Calibration**
* Follow the calibration steps
{% endtab %}

{% tab title="Wacom" %}
Not all Wacom tablets have a calibration feature.

Some newer Wacom tablets also allow you to tweak the offset between the pen and pointer.\
\
More here: [https://developer-support.wacom.com/hc/en-us/articles/9354483629335-Pen-gap-offset-problems](https://developer-support.wacom.com/hc/en-us/articles/9354483629335-Pen-gap-offset-problems)
{% endtab %}
{% endtabs %}
