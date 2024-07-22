# Absolute versus relative positioning

## Drawing tablets use absolute positioning

That means the tablet knows the (x,y) location of the pen precisely on the active area of the tablet.

The pen does not even have to touch the tablet. As long as the pen is close - about 10 mm typically - to the active area and within the bounds of the active area, the tablet knows the pen's position. This position detection without touching is typically called "support for hover".

## Mice use relative positioning

That means that a mouse does not know its exact position on your desktop. The mouse has no idea what surface it is in contact with. In a general sense a mouse only knows that it is moving in relation to some surface.

The mouse does not now its location. The mouse only knows about changes in position - i.e. either it is moving or it is not moving.

The mouse reports this movement as a change in x position and a change in Y position (dx, dy)

## No movement

What happens if you simply keep a pen or a mouse perfectly still and don't move them at all.

Drawing tablet will continuously report the (x,y) position of the pen.

In theory a mouse will report (0,0) indicating no movement. In practice mice don't even report the (0,0) because that data doesn't provide any interesting information to the computer.

## Sudden jumps

One of the ways absolute and relative positioning really stand out is what happens when the input device jumps from one location to another

With the drawing tablet if you hold your pen let's say at the bottom left of the tablet - that means the operating system pointer will also be at the bottom left of your display. If you then pull the pen straight up and away from the tablet so that the tablet does not sense the pen's location and then you move the pen to the upper right hand, then suddenly the operating system pointer will suddenly appear at the upper right hand corner of the display

For a mouse if you try the equivalent thing something different will happen. If the pointer is at the bottom left and you suddenly pull the mouse away from the surface and then place it anywhere else, then you'll see that the pointer does not move.          &#x20;

## Mouse mode in drawing tablets

Drawing tablets can simulate relative positioning when talking to a computer. This is called mouse mode. More here: [**Mouse mode**](mouse-mode.md)&#x20;
