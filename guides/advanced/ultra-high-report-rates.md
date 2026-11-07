# Ultra-high report rates

## Current state-of-the-art

As of November 2026, the highest pen report rate seen in drawing tablets is 300 Hz. This specific report rate is achieved with a Wacom Intuos Pro 2025 pen tablet (PTK-x70 series). A more much typical value is 200Hz to 250Hz.

<figure><img src="../../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

### The motivation for higher report rates

For artists the motivation is simple: strokes should look less segmented especially as you draw a very fast stroke and in theory this extra data should be useful in making the strokes look better especially as a stroke makes fast transitions in pressure for example at the beginning or end of a stroke.

For example here's an artifact called shoelacing that appears as a stroke ends - and the pen is moving very fast and moves through a wide pressure range. It is thought that a much higher report rate would help make such strokes look better.

<figure><img src="../../.gitbook/assets/image (74).png" alt="" width="188"><figcaption></figcaption></figure>

Gamers who use mice have been used to mice that have a report rate on the order of 500, 1000, or 4000 thousand Hertz. So for those players that like to use a drawing tablet to play a game like **osu!**, you can understand there's a natural motivation to have their drawing tablets perform as well as a mouse.

### Are higher report rates possible?

Yes.&#x20;

People have wanted higher report rates for a very long time but no one's ever been able to achieve these higher report rates beyond what a manufacturer provides.

In late 2026, tablet experts and enthusiasts began modifying drawing-tablet firmware. They produced patches with report rates of 500 Hz, 700 Hz, and slightly above 1,000 Hz.

I've tested this firmware out and can confirm that they have indeed achieved these ultra high report rates.

### Are higher report rates useful?

It depends on what you want to do.

* For gamers - especially osu players: YES.
* For artists - not yet.

## Benefits for osu! players

The firmware-hacking community initially explored high report rates to play a game called osu!. Players often use drawing tablets for osu and an ultra-high report rate can benefit serious players.

However, you must keep in mind that playing this game has different priorities than drawing. For example, an osu! player does not need pressure or tilt sensitivity. The game does not use those pen capabilities.&#x20;

{% hint style="info" %}
Some osu players do use the pen tip - but they are not interested in pressure sensitivity - just detection that ANY pressure is used - i.e. that they "clicked"
{% endhint %}

## Limiting factors for artists

There is a practical limit to the data a pen can send to the tablet. I think of this limit as a "budget" that depends on the energy the tablet can deliver to the pen and the data the pen can reliably transmit.&#x20;

So far, it seems that getting pressure to reported at these higher refresh rates is still difficult. While the report rate can be 1000Hz, the pressure is not being updated with every report.

In fact in my initial testing, LESS pressure data was being reported at 1000Hz and the strokes actually looked WORSE than before. Strokes looked "blobby" and not smooth.

Based on current testing, these higher report rates are not yet helpful for artists. This needs further investigation.

## Upper limit to artistic improvement

Even if the pen supplies all desired data at very high report rates, strokes may not improve based on what an artist sees.&#x20;

**Any improvements may not be obvious**&#x20;

Modern creative applications perform substantial work to render good-looking smooth strokes. Increasing the report rate might not make strokes look better in practice. This area needs further investigation.

**Inherent limitations to pen data**

Drawing tablets are incredibley precise. They are capable of sensing very very tiny changes in pen position. See: [Digitizer vs screen coordinates](../../core/digitizer-vs-screen-coordinates.md)

Drawing tablet EMR pens are capable many distinguishing between many pressure levels. Modern EMR pens support at least 8000 levels of pressure - which is well above what I think artists need or are capable of noticing.

However, tilt is NOT as sensitive as pressure. Drawing tablets can (as far as I have seen) only sense tilt is whole degrees. So instead of thousands of levels of tilt - we have about 60. Ultra-high report rates will not make tilt work better.&#x20;

## Dangers

Achieving these high report rates involves patching a drawing tablet's firmware.

No drawing-tablet brand explicitly supports firmware patching.

Doing so has several potential problems and risks:

* No drawing-tablet manufacturer will support you if you use modified firmware.
* It likely violates the end-user license agreement you accepted.
* Creating or using modified firmware may infringe the manufacturer's intellectual property rights.
* Installing modified firmware may temporarily or permanently brick your drawing tablet.

For these reasons, I do not recommend that the average person modify their drawing tablet's firmware.

Perhaps, in the future, enough experience will make modified firmware safer to try. For now, I do not recommend using modified firmware on your drawing tablet.
