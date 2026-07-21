# Testing drawing experience

## Overview

Here are the things I look for when evaluating a drawing tablet's drawing experience.

### Expressiveness

There are three "sensors" available to make expressive strokes that respond to what your hand is doing:

* Pressure
* Tilt
* Barrel rotation

Apps map those sensors to different brush properties to provide the feeling you want. Typical mappings include:

* Pressure to brush size or brush opacity
* Tilt to brush size, usually along one dimension, or brush rotation
* Barrel rotation to brush rotation

What I am generally looking for:

* **Smooth pressure transition** - Strokes move from low to high pressure without weird hiccups.
* **Artifacts at low pressure** - EMR pens are generally over-reactive near the IAF. This means drawing at low pressure can produce weird blobby pressure response. This is very common but also correctable with pressure smoothing or curving. See: [Drawing at low physical pressure](../core/pressure/drawing-low-pressure.md)
* **Pressure scan rate** - A high rate means fast dots and quick strokes are not missed.

### Positioning

* **Pointer tracking accuracy (vertical and static)** - When holding a pen still and perpendicular to the tablet surface, is the pointer directly under the pen tip?
* [Tilt compensation](../core/pen-tilt/pen-tilt-compensation.md)
* [Diagonal wobble](../core/diagonal-wobble.md)
* [Parallax](../guides/pen-displays/parallax.md)
* [Pointer lag](../core/pointer-lag.md)

## Resources

[Teoh on Tech - About those line tests in my drawing tablet reviews](https://www.youtube.com/watch?v=KTLsWe08Bd0) 2026-06-24

This video covers:

* Which software is used and why
* Various tests, including IAF and diagonal wobble

<br>
