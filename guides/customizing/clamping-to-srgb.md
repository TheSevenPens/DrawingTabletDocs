# Clamping wide-gamut displays to sRGB

These days many monitors and pen displays support very wide color gamuts.

While these can look amazing, many people find that they are too intensely saturated. This is often observed with reds, purples, and greens.

Often changing saturation levels or brightness might not do anything to reduce the intensity of these colors.

There are some techniques you can use to reduce the intensity of these colors.

## Option 1 Use the display's sRGB emulation mode

Many monitors and pen displays have an "sRGB emulation mode" that will reduce the intensity of these colors.

This is the first option you should try.

A possible downside is that these displays often not only restrict the color gamut, but also reduce the brightness. If reduced brightness is not working for you, you can try other options.

## Option 2: use the GPU to clamp the gamut to sRGB

## AMD GPUs

* Launch **AMD Radeon Software**
* Click **Settings**
* Click **Display**
* Enable **Custom Color**
* Disable **Temperature Control (CTC)**

## NVidia GPUs

* Use the **novideo\_srgb** tool
* Download the **release.zip** file from here: [https://github.com/ledoge/novideo\_srgb/releases](https://github.com/ledoge/novideo_srgb/releases)
* Extract the files in the **release.zip**
* Launch **novideo\_srgb.exe**
* Click **Clamped**

## References

* **Taming the Wide Gamut using sRGB Emulation** ([https://pcmonitors.info/articles/taming-the-wide-gamut-using-srgb-emulation/](https://pcmonitors.info/articles/taming-the-wide-gamut-using-srgb-emulation/))
* r/Monitors - [sRGB clamp - what is it and how can it affect user experience.](https://www.reddit.com/r/Monitors/comments/qes94q/srgb_clamp_what_is_it_and_how_can_it_affect_user/) 10/24/2021
* r/Monitors - [sRGB clamp for NVIDIA GPUs](https://www.reddit.com/r/Monitors/comments/pakpy9/srgb_clamp_for_nvidia_gpus/) 8/24/2021
* **novideo\_rgb** tool ([https://github.com/ledoge/novideo\_srgb](https://github.com/ledoge/novideo_srgb))
* **Blog: Wide Colour Gamut & SRGB Clamp** ([https://youtu.be/blcWTkv1bvQ](https://youtu.be/blcWTkv1bvQ))
* **What Is sRGB Emulation Mode And Why Is It Important?** ([https://www.displayninja.com/what-is-srgb-emulation-mode/](https://www.displayninja.com/what-is-srgb-emulation-mode/))
