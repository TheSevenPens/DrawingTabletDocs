# Troubleshoot difficult to reach maximum pressure

## Symptoms

If you are looking at a pressure reading while using your pen, you may see that it is either very difficult or impossible to reach 100% pressure.

<figure><img src="../.gitbook/assets/image (538).png" alt="" width="563"><figcaption></figcaption></figure>

This can be caused by several things

## Information to collect

Does this problem manifest in the driver?

Does it manifest in an application like Krita?

## Pen hardware issue

If it happens in the driver at all, then most likely there is something wrong with the pen hardware itself.

Occasionally pen hardware can sometimes have a very high maximum pressure that is very large (I've seen up to about 5X) what is normal for a pen.&#x20;

### Example of a pen with abnormal max pressure

For example one of my Wacom pens requires so much force to get to 100% that, if I tried, I'm sure I would damage the pen.

Below you can see how different the pressure response of this pen is compared to every other pen I have.&#x20;

<figure><img src="../.gitbook/assets/image (540).png" alt=""><figcaption></figcaption></figure>

### How to address

Because you cannot physically fix the problem, you have two options:

* Use pressure curves to address this problem
* Contact support for help and potentially get a replacement

### Using a pressure curve to a pen hardware problem

Try adjusting the pressure curve in the driver until the problem goes away. Specifically you are looking for a pressure curve that "constrains the output". This means the right edge of the curve does not go up to the full height of the pressure curve. More here: [**Pressure curves that constrain output**](../core-features/pen-pressure-curve/pressure-curves-that-constrain-output.md)

**Keep in mind:**

* The number pressure reading in the driver may not take the pressure curve into account
* So to check if this is fully working for you, should verify in an application

Here are some examples below.

<figure><img src="../.gitbook/assets/image (543).png" alt="" width="563"><figcaption></figcaption></figure>

## Software issue

If the problem does NOT appear in the driver, then it is possible that another pressure curve in the application is causing it. Check all the pressure curves and reset them to null pressure curve.&#x20;

More here: [**null pressure curve**](../core-features/pen-pressure-curve/null-pressure-curve.md) &#x20;
