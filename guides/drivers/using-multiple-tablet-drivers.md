# Using multiple tablet drivers on the same computer

## Overview

This might or might not work for you depending on the specific tablets you have and the operating system you use.

## Tablet drivers from the same brand

Sometimes you have two tablets from the same brand. Let's use Wacom in this example. You might have a very old Wacom tabler and a very new Wacom tablet.

It might be the case that the old tablet requires an older version of the Wacom tablet driver that does not work with the newer Wacom tablet. And likewise the newer Wacom drivers don't work with the older Wacom tablet.&#x20;

There is NO WAY to have two different Wacom driver versions installed on the same time. More generally, there is NO WAY to have two different driver versions from the same brand installed on the same time.&#x20;

Even if you try to install both, at the time of installation tablet drivers from a given brand will either refuse to install if another version is installed or they will uninstall the old version, or they will automatically upgrade the old version to the new version.

A **potential alternative** is to use [OpenTabletDriver](opentabletdriver/) which may support both tablets.

## Tablet drivers from different brands

I DO NOT recommend installing multiple tablet drivers from different simultaneously on a single Windows computer. But it might work well on MacOS.

### Microsoft Windows

Tablet drivers from different brands interfere with each other.

In theory if your pen-aware applications use Windows Ink for their tablet API, then there will be no interference.

In practice, even when apps have been correctly configured, have encountered problems on Windows when multiple tablet drivers are installed from different brands.

A **potential alternative** is to use [OpenTabletDriver](opentabletdriver/) which may support all the tablets you want to use.

### Apple MacOS

My experience has been good, I have several MacOS computers with multiple tablet drivers installed simultaneously  (Wacom, Huion, XP-Pen, and Xencelabs). I have had no problems.

However, I have some people have reported that they have encountered issues when different tablet drivers are installed.

So, even for MacOS I don't recommend it, even though I personally have had a good experience.

A **potential alternative** is to use [OpenTabletDriver](opentabletdriver/) which may support all the tablets you want to use.



