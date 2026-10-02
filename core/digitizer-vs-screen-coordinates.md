# Digitizer vs screen coordinates

## Overview

Drawing tablets use two coordinate systems.

* **Digitizer coordinates** are high-resolution coordinates sensed by the tablet’s digitizer. A typical 2026 drawing tablet senses 5,080 points per inch, or 200 points per millimeter.
* **Screen coordinates** map to pixels on your monitor. They have much lower resolution, typically 150 to 300 points per inch.

In simple terms, the tablet’s digitizer senses many points for every display pixel.

## Quality strokes need digitizer coordinates

High-resolution digitizer coordinates are essential for producing quality artwork strokes.

The example below shows two groups of strokes drawn with a one-pixel brush.

* The strokes on the left use screen coordinates
* The strokes on the right use digitizer coordinates

The strokes on the left have sharp stair-stepping. They are not as smooth as the strokes on the right, which use digitizer coordinates. This tight stair-stepping is a hallmark of drawing with screen coordinates.

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption><p>Brush width is constant (one pixel).</p></figcaption></figure>

The examples below use a pressure-sensitive brush. The varying width makes the difference harder to see. Look closely at the left strokes, which use screen coordinates. Their edges are rough and stair-stepped. The strokes on the right use digitizer coordinates and look much smoother.

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption><p>Brush width varies with pressure.</p></figcaption></figure>

## Which coordinates do apps use?

On Windows, applications can use either coordinate system. Drawing apps typically use digitizer coordinates because they produce smoother strokes. Some pen-aware apps do not use digitizer coordinates.

Windows applications can sometimes switch coordinate systems. You might see smooth strokes one day and rough, stair-stepped strokes the next. If this happens, use this troubleshooting guide:

[TSG: Strokes look stair-stepped](../troubleshoot/tsg-strokes-stair-stepped.md)

## Screen coordinates versus diagonal wobble

Screen-coordinate artifacts can look similar to diagonal wobble. However, they have different causes, fixes, and diagnostic procedures.

Strokes using screen coordinates look different from diagonal wobble. Wobble is smoother, more wave-like, and spread across the stroke.

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

|            | Use of screen coordinates                           | Diagonal wobble                                           |
| ---------- | --------------------------------------------------- | --------------------------------------------------------- |
| Shape      | Angular, tight stair-steps, like snapping to a grid | Smooth, regular oscillation                               |
| Worst at   | Any angle, most visible on diagonals                | 45 degrees; none at 0 or 90 degrees                       |
| Platform   | Windows                                             | Any                                                       |
| Cause      | The pen API path in software                        | How the tablet senses and interpolates the pen's position |
| Fix        | Restart, switch pen API, reinstall the driver       | Cannot be fixed, only mitigated                           |
| Present on | Some setups                                         | Every tablet, in varying amounts                          |

Both are more visible when you draw slowly or diagonally. Those traits do not distinguish them. Instead, check:

* **The shape** — Quantization creates tight, sudden steps. Wobble creates a smooth wave.
* **Whether it goes away** — If restarting or switching the pen API fixes it, it was quantization. Wobble persists.

Learn more: [Diagonal wobble](diagonal-wobble.md)

## Real-world usage notes

* In mathematical terms, high-resolution digitizer coordinates are quantized into low-resolution screen coordinates. This works for drawing a mouse pointer. Delicate, pressure-sensitive strokes need digitizer coordinates.
* Here, _quantization_ means converting high-resolution coordinates to lower-resolution coordinates. A stroke may therefore have a “quantized look.”
* In theory, rough, stair-stepped strokes can occur while using digitizer coordinates. For example, flawed brush-engine math can quantize high-resolution coordinates to lower-resolution values.
* Canvas-scaling errors can also create a stair-stepped, quantized look. This can be difficult to distinguish from coordinate quantization without experience assessing rendered strokes.
