# Measuring PWM Flicker

## Overview

This doc describes how I test for PWM flicker in a display. To learn more about PWM flicker, see [PWM Flicker](../../core/pwm-flicker.md).

## Process for measuring

* Get a smartphone
* Set the photo mode to "Pro."
* Set the shutter speed as fast as possible. For example, `1/12000s`.
* Point the smartphone camera at a display to test for PWM flicker
* Set the display brightness to the lowest setting (0%)
* Now steadily increase the display brightness from 0% to max brightness (100%) and look at the phone's camera preview
* If there is PWM flicker:
  * you will see it as horizontal black bars that move up and down the display
  * The black bars will be thicker when the brightness is lower
*
