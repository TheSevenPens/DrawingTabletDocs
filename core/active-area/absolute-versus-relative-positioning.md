# Absolute versus relative positioning

## Drawing tablets use absolute positioning

That means the tablet knows the `(x, y)` location of the pen on the active area.

The pen does not even have to touch the tablet. As long as it is close, typically about 10 mm, and within the bounds of the active area, the tablet knows the pen's position. This kind of position detection without touching is typically called **hover**.

## Mice use relative positioning

That means a mouse does not know its exact position on your desktop. The mouse has no idea what surface it is touching. In general, a mouse only knows that it is moving relative to some surface.

The mouse does not know its location. It only knows about changes in position. In other words, it only knows whether it is moving or not.

The mouse reports this movement as a change in x position and a change in y position: `(dx, dy)`.

## No movement

What happens if you keep a pen or mouse perfectly still and do not move it at all?

A drawing tablet continuously reports the `(x, y)` position of the pen.

In theory, a mouse reports `(0, 0)` to indicate no movement. In practice, mice often do not report `(0, 0)` because that data does not provide useful information to the computer.

## Sudden jumps

One clear difference between absolute and relative positioning appears when the input device jumps from one location to another.

With a drawing tablet, if you hold the pen at the bottom left of the tablet, the operating system pointer will also be at the bottom left of your display. If you then lift the pen away so the tablet no longer senses it, and move it to the upper-right area, the pointer will suddenly appear at the upper-right corner of the display.

For a mouse, the equivalent action behaves differently. If the pointer is at the bottom left and you lift the mouse off the surface, then place it somewhere else, the pointer does not move.

## Mouse mode in drawing tablets

Drawing tablets can simulate relative positioning when talking to a computer. This is called mouse mode. More here: [Mouse mode](mouse-mode.md)
