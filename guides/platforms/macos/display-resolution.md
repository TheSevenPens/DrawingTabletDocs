# Fuzzy text on displays with MacOS

## Introduction

Just like a monitor a pen display contains a display panel with a native display resolution.

## Typical resolutions

Modern pen displays mostly use a small number of resolutions. The vast majority of pen displays use these three resolutions:

* Full HD = 1920x1080
* 2.5K  = 2560x1440
* 4K = 3840x2160

A few pen displays use resolutions such as 2560 x 1600.

## Considerations

### **Seeing pixels**

* Some people are very sensitive to seeing pixels.
* When drawing on a pen display you'll be much closer to it than when you are using a monitor
* So you might notice the pixels more due to this proximity

### **Compatibility**

The resolution with the least compatibility issues is 2K. This format has the least issues with ports, cables, GPUs, adapters, etc. As you start getting into higher resolutions, you have to be more careful about compatibility and ensure everything is going to work.

For example:

* Not all HDMI cables support 4K
* Some laptops struggle to support an external 4K display
* Macintoshes have difficulty supporting 2.5K resolutions
* Some systems support the higher resolutions but not a high-enough refresh rate. For example one of my laptops supports 4K but only at 30Hz instead of the standard 60Hz.

## Pixel density :Pixels-per-inch (PPI)&#x20;

<table><thead><tr><th width="96.50002034505206">Diagonal size</th><th width="175">FullHD 1920x1080</th><th width="162.25">2.5K 2560x1440</th><th>4K 3840x2160</th></tr></thead><tbody><tr><td>13"</td><td>169.45</td><td>225.94</td><td>338.91 </td></tr><tr><td>16"</td><td>137.68</td><td>183.58</td><td>275.36 </td></tr><tr><td>22"</td><td>100.13</td><td>133.51</td><td>200.26 </td></tr><tr><td>24"</td><td>91.79</td><td>122.38</td><td>183.58 </td></tr><tr><td>27"</td><td>81.59</td><td>108.79</td><td>163.18 </td></tr><tr><td>32"</td><td>68.84</td><td>91.79 </td><td>137.68 </td></tr></tbody></table>

## **Picking between 2.5K vs 4K resolution**&#x20;

People often ask about picking between these two resolutions. Overall I think 2.5K is the best value for your money.&#x20;

Especially at the 13" and 16" sizes, a 2.5K delivers a massive increase over 2K. At these size, higher resolutions only provide very incremental benefits.

## My experience and recommendations

Based on my experience here's what I think works. Overall the pattern is a PPI between 150ppi and 180ppi is what I think works the best.

<table><thead><tr><th width="126.20001220703125">Diagonal Size</th><th>Full HD (1920x1080)</th><th>2.5K (2560x1440)</th><th>4K (3840x2160)</th></tr></thead><tbody><tr><td>13"</td><td><p>~169ppi</p><p>works fine</p></td><td><p>~226ppi</p><p>works fine</p></td><td><p>~339ppi</p><p>definitely too much</p></td></tr><tr><td>16"</td><td><p>~138ppi</p><p>works fine</p></td><td><p>~184ppi</p><p>works great (ideal)</p></td><td><p>~275ppi</p><p>definitely too much</p></td></tr><tr><td>19"</td><td><p>~115ppi</p><p>not enough</p></td><td><p>~155ppi</p><p>should work great</p></td><td><p>~231ppi</p><p>works great (ideal)</p></td></tr><tr><td>22"</td><td><p>~100ppi</p><p>definitely not enough</p></td><td><p>~133ppi</p><p>works great</p></td><td><p>~220ppi</p><p>works great (ideal)</p></td></tr><tr><td>24"</td><td><p>~92ppi</p><p>definitely not enough</p></td><td><p>~122ppi</p><p>works fine</p></td><td><p>~184ppi</p><p>works great (ideal)</p></td></tr><tr><td>27"</td><td><p>~82ppi</p><p>definitely not enough</p></td><td><p>~109ppi</p><p>probably not enough</p></td><td><p>~163ppi</p><p>works great (ideal)</p></td></tr></tbody></table>

## Overview

MacOS text rendering can appear not work OK by default with certain combinations size and resolutions. This can be addressed with an app called Better Display.

## Video

{% embed url="https://www.youtube.com/watch?v=1z6SU-eyYQE" %}

##



