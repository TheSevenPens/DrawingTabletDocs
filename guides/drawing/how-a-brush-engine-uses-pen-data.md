# How a brush engine uses pen data

## Introduction

Somewhere between 100 to 250 times a second, you tablet is sending data to your computer.

The tablet driver receives that data, may process it in some way, and then sends it to your operating system and applications

Each report of the tablet contains information like this

* The x,y position of the pen
* The pressure reading. 0 = no pressure or some positive integer if there is pressure
* Tilt - composed of two valaues. x tilt and y tilt

The report contains other interesting things, but these are the critical ones for drawing strokes&#x20;

## Brush engines

In a creative applications that draws strokes - applications such as clip studio paint, krita, or photoshop, there is a component (or set of components) we can refer to as the **brush engine**

Among its responsibilities is to take this pen data and combine it to draw a stroke.

Your drawing apps typically feature different brushes: pen, pencil, watercolor, etc.

A single brush engine could flexible enough to handle these kinds of brushes, but it's probably simpler to think of them as different brush engines - one for each kind of brush.

But what all these brush engines have in common is that they transform the pen data in various ways to affect how the brush works.

Typically these are the ways in which a brush engine can control the stroke

* stroke opacity
* brush size
* brush rotation

And there are lot of other settings

Here is an example from Clip Studio Paint 2.0 for its Calligraphy brush

![](<../../.gitbook/assets/image (309).png>)

Here is an example from Krita

![](<../../.gitbook/assets/image (142).png>)



## Pressure

If you are in a creative application that draws strokes,&#x20;

The most common mapping of pen input to stroke is how pressure is handled. Typically, pressure is either:

* ignored - it has no effect on the brush. this is common for very simple brushes
* brush size - more pressure gives a bigger brush
* brush opacity - more pressure gives a more opaque brush

## Tilt

Tilt typically is treated like this:

* Ignored
* brush size - for example a pencil brushes may get wider as the pen is tilted to simulate how a real pencil makes wider marks on paper as it is tilted.
* brush rotation - enabling the tilt to orient the brush.

