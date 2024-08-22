# Null pressure curve

## Introduction

The null pressure curve is the most important pressure curve - exactly because it does nothing. We can apply the null pressure curve to any pressure profile and it will not shift the profile in any direction.

## Definition

The definition of a null profile is a pressure curve function that takes the input logical pressure and returns that very same value as the output logical pressure. In order words f(p) = p.

<figure><img src="../../.gitbook/assets/Slide_20240722_142454 (2).jpg" alt=""><figcaption></figcaption></figure>

If you take the range of input logical pressures which range from zero to one and plot them on the X axis of a chart. And then you apply the null pressure curve to those values and plot the result of the function on the Y axis - then you get a straight line at 45° that goes from the lower left corner to the upper right corner of the chart.

Anytime you see a chart like this it clearly identifies that null pressure curve. And you can be sure that it does not do anything to a pressure response.

And the chart above you can see there's been no change because the orange line which represents the pressure response after applying the curve has exactly the same shape as the original pressure response.

## null pressure curves are extremely useful.

We encounter pressure curves in tablet drivers and in creative applications. These kinds of applications often use the null pressure curve as the default value for any pressure curves they have. This isn't always true but it is a very common thing to see.

If you're ever trying to solve some problem with the pressure of your pen the knowing about the null pressure curve is useful. Because it might be that somehow your pressure curve was modified and is affecting your pen. So a very common troubleshooting tip is to make sure that your pressure curve has been reset back to the null pressure curve. This way you can be sure it is not affecting what is going on



