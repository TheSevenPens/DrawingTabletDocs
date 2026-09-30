# TSG: Strokes look stair-stepped

## Symptoms

Your strokes come out looking tightly stair-stepped, as if the pen position were snapping to a coarse grid.

* The stairs are small and sudden - not smooth and spread out
* It is more obvious when the pen moves diagonally
* It is more visible when you draw slowly
* It happens on Windows. I've never seen it occur on MacOS.

This effect is called **coordinate quantization**. For a full explanation of what it is and why it happens, see: [Coordinate quantization](../core/digitizer-vs-screen-coordinates.md)

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption><p>brush width varies by pressure</p></figcaption></figure>

## Quantization vs diagonal wobble?

Diagonal wobble can look similar similar to quantization. But there are few key differences

* Diagonal wobble is more gentle, smooth, and and wave-like. Quantization is occurs in sudden tight steps.
* Diagonal wobble is caused by the tablet hardware and can occur in any tablet on any OS. Quantization is a software problem due to the resolution of the pen coordinates used by application on Windows.

More here: [Diagonal wobble](../core/diagonal-wobble.md)

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

## Options for fixing stroke quantization

1. Restart the computer.
2. Switch the pen API the app is using then restart the app, and try drawing. See: [Configure Windows Ink for apps](../guides/platforms/windows/winink/winink-config-apps.md)
3. Reinstall or update the tablet driver.

Note that it is POSSIBLE for quantization to be visible with BOTH APIs.

## Why does quantization suddenly appear?

Your strokes can look normal, then suddenly the next time you start drawing they are quantized.

This is indeed mysterious. I've had it happen many times. Usually what fixed it for me was switching APIs.

I don't have a great theory about the reason it suddenly occurs. It seems to be some weird interaction between Windows, apps and drivers, with no clear way to detect what triggered the change.
