# Windows PNP driver compatibility testing

Introduction

Not all drawing talbots support Windows PNP drivers. .And even if they do you have to be aware that there are limitations. On this page I will collect. some basic compatibility testing I've done for some tablets. More here: [Windows PNP support for drawing tablets](windows-pnp-support-for-drawing-tablets.md)

If the risk is a specific tablet you'd like me to test .then please contact me and let me know. .If I have the tablet I'd be happy to test it.

## Testing Windows PNP drivers with pen displays (screen tablets)

I plugged in a couple and their basic functionality worked subject to the limitations described earlier.

* Intuos Pro Small (PTH-460) - <mark style="color:red;">**does not work**</mark> (I get the sense this was a deliberate Wacom choice)
* Movink 13 (DTH-135) - does work
* Wacom One M (CTC-6110WL) - does work

## Testing setup

* Surface Pro 8
* Windows 11
* Krita

## Testing results

* Huion HS611
  * Position : works
  * Pressure YES
  * Tilt: YES
  * Lower button: detected
  * Upper button: not detected (?)
* Wacom One Medium (CTC-6100WL) with CP-923 pen
  * Position: works
  * Pressure: YES
  * Tilt: YES
  * Lower button: detected&#x20;
  * Upper button: detected
* Wacom Intuos Pro Small (PTH-460) with Pro Pen 2
  * Nothing works
* Wacom Intuos Pro Medium (PTH-660) with Pro Pen 2
  * Nothing works
* Wacom Intuos Pro Medium (PTH-860) with Pro Pen 2
  * Nothing works
* XP-Pen Deco Pro XLW (MT1592B) with X3 Pro pen
  * Position : works
  * Pressure YES
  * Tilt: YES
  * Lower button: detected
  * Upper button: not detected (?)
* Huion Giano G930L with PW517 pen
  * Position : works
  * Pressure YES
  * Tilt: YES
  * Lower button: detected
  * Upper button: not detected (?)

