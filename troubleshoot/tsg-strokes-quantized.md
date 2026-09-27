# TSG: Strokes look stair-stepped (quantization)

## Symptoms

Your strokes come out looking tightly stair-stepped, as if the pen position were snapping to a coarse grid.

* The stairs are small and sudden - not smooth and spread out
* It is more obvious when the pen moves diagonally
* It is more visible when you draw slowly
* It happens on Windows

This is called stroke quantization. For a full explanation of what it is and why it happens, see: [Stroke quantization](../core/stroke-quantization.md)

## Is it quantization or diagonal wobble?

Diagonal wobble can look similar, but it is a smooth oscillation rather than tight steps, it happens on every platform, and it cannot be fixed. If the steps go away after trying the fixes below, it was quantization. See: [Diagonal wobble](../core/diagonal-wobble.md)

## Options for fixing it

1. Restart the computer.
2. Switch the app to the other pen API, restart the app, and try again.
   * If the app is using Windows Ink, switch to WinTab
   * If the app is using WinTab, switch to Windows Ink
   * How to do this for common apps: [Configure Windows Ink for apps](../guides/platforms/windows/winink/winink-config-apps.md)
3. Reinstall or update the tablet driver.

Note that it is POSSIBLE for quantization to be visible with BOTH APIs.

## Why does quantization suddenly appear when it didn't before?

This is indeed mysterious. I've had it happen many times. Usually what fixed it for me was switching APIs.

I don't have a great theory about the reason. It seems to be some weird interaction between Windows, apps and drivers, with no clear way to detect what triggered the change.
