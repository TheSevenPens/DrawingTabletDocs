# Clamping wide-gamut displays to sRGB

These days many monitors and pen displays support very wide colors gamuts.

While these can look amazing, many people often find that they are too intensely saturated. This is often observed with reds, purples, and greens.

Often changing saturation levels or brightness might not do anything to reduce the intensity of these colors.

There are some techniques you can use to reduce the intensity of these colors

## Option 1 Use the display's sRGB emulation mode

Many monitors an pen displays have an "sRGB emulation mode" that will rude the intensity of these colors.

This is the first option you should try.

A possible negative is that often these displays not only restrict the color gamut, but also keep reduce the brightness. If reduced brightness is not working for you you can try other options

## Option 2: use the GPU to clamp the gamut to sRGB

## AMD GPUs

* Launch **AMD Radeon Software**&#x20;
* Click **Settings**
* Click **Display**
* Enable **Custom Color**&#x20;
* Disable **Temperature Control (CTC)**

## NVidia GPUs

* Use the **novideo\_srgb** tool
* Download the **release.zip** file from here: [https://github.com/ledoge/novideo\_srgb/releases](https://github.com/ledoge/novideo\_srgb/releases)  &#x20;
* Extract the files in the **release.zip**&#x20;
* Launch **novideo\_srgb.exe**
* Click **Clamped**

## References

* **Taming the Wide Gamut using sRGB Emulation** ([https://pcmonitors.info/articles/taming-the-wide-gamut-using-srgb-emulation/](https://pcmonitors.info/articles/taming-the-wide-gamut-using-srgb-emulation/))
* **sRGB clamp - what is it and how can it affect user experience** ([https://www.reddit.com/r/Monitors/comments/qes94q/srgb\_clamp\_what\_is\_it\_and\_how\_can\_it\_affect\_user/](https://www.reddit.com/r/Monitors/comments/qes94q/srgb\_clamp\_what\_is\_it\_and\_how\_can\_it\_affect\_user/))
* **sRGB clamp for NVIDIA GPUs** ([https://www.reddit.com/r/Monitors/comments/pakpy9/srgb\_clamp\_for\_nvidia\_gpus/](https://www.reddit.com/r/Monitors/comments/pakpy9/srgb\_clamp\_for\_nvidia\_gpus/))
* **novideo\_rgb** tool ([https://github.com/ledoge/novideo\_srgb](https://github.com/ledoge/novideo\_srgb))
* **Blog: Wide Colour Gamut & SRGB Clamp** ([https://youtu.be/blcWTkv1bvQ](https://youtu.be/blcWTkv1bvQ))
* **What Is sRGB Emulation Mode And Why Is It Important?** ([https://www.displayninja.com/what-is-srgb-emulation-mode/](https://www.displayninja.com/what-is-srgb-emulation-mode/))
