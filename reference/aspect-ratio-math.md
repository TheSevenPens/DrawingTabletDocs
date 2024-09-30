# Aspect ratio math

## Overview

This is some miscellaneous code I need when evaluating tablets.

## Find size from the diagonal and aspect ratio

Often we are presented with size information from a manufacturer like resolution and diagonal length.

For example the a pen display is specified as HD (1920x1080) with a diagonal length of 13.3". But we may not be given the physical height and width. This function calculates the height and width given the aspect ratio and the diagonal length.

In this case it would be called like this (this assumes the pixels are square):

```
get_size_from_ar( 1920/1080, 13.3) 
```

Or if you know the aspect ratio is 16/9

```
get_size_from_ar( 16/9, 13.3) 
```

&#x20;

```python
import math

def get_size_from_ar( ar, d) :
    w = math.sqrt( (d*d) / ( 1 + (1/ar)*(1/ar)) )
    h = math.sqrt( (d*d) / (1 + (ar)*(ar)) )
    return (w,h)
    
print( get_size_from_ar( 16/9, 16) )
```
