# Choosing the right display resolution for a pen display

## Overview

Pen displays have an embedded display panel that has a native resolution. In this document I'll share some thoughts about how to pick a resolution that will work for your needs.&#x20;

## Summary

* In general, as a tablet gets bigger it's useful to have a higher resolution
* At small sizes having a very high resolution does not help
* Some resolutions require some extra work to use well with MacOS

## Typical resolutions

Modern pen displays mostly use a small number of resolutions.

The vast majority of pen displays use these three resolutions:

* Full HD = 1920x1080
* 2.5K  = 2560x1440
* 4K = 3840x2160

But, a few pen displays use resolutions such as 2560 x 1600.

## My experience and recommendations

Based on my experience here's what I think works. Overall the pattern is a PPI between 150ppi and 180ppi is what I think works the best.

<table><thead><tr><th width="126.20001220703125">Diagonal Size</th><th>Full HD (1920x1080)</th><th>2.5K (2560x1440)</th><th>4K (3840x2160)</th></tr></thead><tbody><tr><td>13"</td><td><p>~169ppi</p><p>works fine</p></td><td><p>~226ppi</p><p>works fine</p></td><td><p>~339ppi</p><p>definitely too much</p></td></tr><tr><td>16"</td><td><p>~138ppi</p><p>works fine</p></td><td><p>~184ppi</p><p>works great (ideal)</p></td><td><p>~275ppi</p><p>definitely too much</p></td></tr><tr><td>19"</td><td><p>~115ppi</p><p>not enough</p></td><td><p>~155ppi</p><p>should work great</p></td><td><p>~231ppi</p><p>works great (ideal)</p></td></tr><tr><td>22"</td><td><p>~100ppi</p><p>definitely not enough</p></td><td><p>~133ppi</p><p>works great</p></td><td><p>~220ppi</p><p>works great (ideal)</p></td></tr><tr><td>24"</td><td><p>~92ppi</p><p>definitely not enough</p></td><td><p>~122ppi</p><p>works fine</p></td><td><p>~184ppi</p><p>works great (ideal)</p></td></tr><tr><td>27"</td><td><p>~82ppi</p><p>definitely not enough</p></td><td><p>~109ppi</p><p>probably not enough</p></td><td><p>~163ppi</p><p>works great (ideal)</p></td></tr></tbody></table>

## MacOS&#x20;

MacOS text rendering can appear not work OK by default with certain combinations size and resolutions. This can be addressed with an app called Better Display.

{% embed url="https://www.youtube.com/watch?v=1z6SU-eyYQE" %}

