# Aspect ratio math

## Find size from the diagonal and aspect ratio

```python
import math

def get_size_from_ar( ar, d) :
    w = math.sqrt( (d*d) / ( 1 + (1/ar)*(1/ar)) )
    h = math.sqrt( (d*d) / (1 + (ar)*(ar)) )
    return (w,h)
    
print( get_size_from_ar( 16/9, 16) )
```
