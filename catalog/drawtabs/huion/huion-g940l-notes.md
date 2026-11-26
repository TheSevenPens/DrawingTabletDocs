# Huion Inspiroy Giano V2 (G940L) notes

## Overview

OVERALL RATING: VERY GOOD

* The Giano V2 (G940L) is the successor to the [Huion Inspiroy Giano (G930L)](huion-g930l-notes.md). The tablet itself is unchanged. What changed is the pen: it now comes with the excellent [PW600](../../pens/huion-pens/huion-pw600-notes.md) instead of the PenTech 3.0 PW517.
* Key points:
  * The problem with the original Giano was never the tablet, it was the pen. The PW517 is hit and miss - some units are great, some units are not. The PW600 pens are much more consistent, and that's why I have much more confidence in this tablet than the older Giano.
  * If you're looking for an alternative to Wacom at this size, this is a good one. I'd place it above the [XP-Pen Deco Pro XLW GEN2](../xppen/xppen-mt1592b-notes.md) but below the [Wacom Intuos Pro Large](../wacom/wacom-intuos-pro-2025/wacom-ptkx70-notes.md). And it costs about half as much as the Intuos Pro Large.
  * The only negative I found in testing is a little more diagonal wobble than I expected. See below.

### Why this tablet is important

The pen is such an important factor when you buy a tablet. It's one of the most overlooked things and yet it's one of the most important. You have to base your decision not just on the tablet but on the specific pen model that comes with it and which pens it's compatible with.

Just by upgrading the pen, this tablet gets placed at a pretty high level in my recommendations. But I still tested it to make sure the other parts work - I don't want to go on the pen's reputation alone.

This also reflects how I'm ranking Huion tablets going forward:

* A Huion tablet that uses a PW517 pen will only get up to the OK level.
* A Huion tablet has to have a PW600 pen to qualify for the EXCELLENT or even the GOOD category.
* The PW550 is fuzzier. On average I think it's better than the PW517, but I don't think it would ever qualify as excellent. GOOD at best.

As the standards change, we have to evolve how we rank things.

### Before you buy

Wacom has released a new Intuos in China (CTK-4120 small, CTK-6120 medium) that looks to be essentially an Intuos Pro without the buttons. As of October 2026 it isn't available in the United States, but I fully expect it to be. If you're shopping for a pen tablet you'll have to decide whether to wait for it or go ahead and get the Giano V2.

### Links

* [Seven Pens - Unboxing and testing: Huion Inspiroy Giano V2 (G940L)](https://www.youtube.com/watch?v=YBb3G2p7kPM) - 2026-10-26

## Core links

* DrawTabData Explorer: [G940L specs](https://thesevenpens.github.io/DrawTabDataExplorer/entity/huion.tablet.g940l)
* [Product page](https://www.huion.com/products/inspiroy-giano-v2)
* [Store page](https://store.huion.com/products/inspiroy-giano-v2)

## Other links

| Source     | Link                                                                                                        | Date       |
| ---------- | ----------------------------------------------------------------------------------------------------------- | ---------- |
| Seven Pens | [Unboxing and testing: Huion Inspiroy Giano V2 (G940L)](https://www.youtube.com/watch?v=YBb3G2p7kPM) | 2026-10-26 |

## Key changes from the G930L

It comes with the PW600 pen instead of the PW517 that came with the G930L.

Everything else - the active area, physical size, weight, 6 buttons, Bluetooth 5.0 and USB-C port are unchanged.

## Device

* Looks exactly like the older Giano G930L in every way, including the small LCD screen and the side buttons. You would not be able to tell the difference except by looking at the model number on the back.
* It still looks very clean and good. Once you've tried the Intuos Pro 2025, which is very thin, you do start appreciating thinness.
* I bought mine directly from Huion's site in October 2026 for about $200.

### What's in the box

* Giano V2 tablet
* PW600 pen
* Pen stand, with replacement nibs inside
* Drawing glove
* USB-C cable

## Notes on specs

### Digitizer

* The active area is the same as the G930L.
* Compared with the other large pen tablets on the market (the Wacom Intuos Pro Large 2025 and XP-Pen Deco Pro XLW GEN2):
  * The Giano's active area is a little larger than the Intuos Pro Large 2025. But it's almost 16:10, so you may not be able to use that full size once you force proportions to match your display. In practice the Giano is about the same size as the Intuos Pro Large.
  * The XP-Pen Deco Pro XLW GEN2 is noticeably bigger than both.
* It's a big tablet. It may be too big for some people, but that's not its fault - it's designed to be big.

### Pens

* Included pen: [PW600](../../pens/huion-pens/huion-pw600-notes.md) - the full version with three buttons and an eraser. This is the best pen Huion makes with all the features.

### Battery

Huion lists a 2500 mAh battery good for about 18 hours of wireless use.

## Driver

* The tablet was not detected with my existing Huion driver. I had to install the latest driver, released October 13/14 2026, before it was recognized. After that it was recognized with no problems.
* The new v20 drivers look really good. I wish the window could be resized so I could see more.
* On macOS you have to grant the driver several permissions: screen recording, accessibility, and one for bypassing the system private window picker. The screen recording one is scary, but all the tablet drivers need it.
* Settings I changed:
  * Disabled the tablet keys because they would interfere with my drawing.
  * Turned on Screen Ratio (Huion's name for [force proportions](../../../guides/customizing/force-proportions.md)). You should always do this, otherwise you'll get distorted strokes.

## Drawing experience

All testing below was on a MacBook with Krita.

### Pressure control

* Thin to thick and back with pressure - I could maintain control easily. All pen tablets are good these days honestly; I do this to make sure I have confidence in the pen.
* I have about 10 other PW600 pens, and this one felt just like them in my hand.

### IAF

* Very light pressure activates it. Not as little as a Wacom Pro Pen 3, I think, but very light.
* If I had to guess, this specific unit has an IAF around 3 gf instead of 2 gf. I didn't measure it. You also can't go by one pen - you have to test multiple pens.
* I couldn't tell how much force it takes to get to 100%. If I had to guess, 400-something gf.
* Unless you're used to a Pro Pen 2, which has super low IAF, and you draw with very light pressure, I don't think you would notice the difference. I think 99% of people would not notice. I don't think I'd notice the difference honestly.

### Initial dot at stroke start

* Sometimes there's a small dot at the very start of a quick stroke. It doesn't happen every time - it's more often when I hit the surface harder.
* My guess is that the first point registers but it takes a bit longer to get to the next point, and even a light stroke has an impulse of pressure at first contact. It may be specific to the pen as well.
* This is nothing unusual. I've seen it in some Wacom tablets too.

### Pressure scan rate test (many small dots)

* RATING: EXCELLENT
* No dots missed.

### Fast strokes

* RATING: EXCELLENT
* No fast strokes missed.

### Pencil brush test

* Tested a pencil brush with zero stabilization, then a softer pencil brush with a large brush size.
* It feels fine - I have no complaints.

### Low pressure behavior

* With a very large brush (~370px) and very light pressure there is a little pulsing. That's normal - don't be panicked by it. You would not normally see this unless you're doing something kind of crazy. Pro Pen 2 does more of this.
* It has to do with the sensitivity of the sensor, the texture of the surface, your own hand, and the direction you're tilting. I tried pointing the pen toward and away from the direction of travel - maybe the difference isn't that great.
* Most drawing tablet pens are overreactive at low pressure, and this PW600 unit behaves just like the other PW600 units I have.
* **How to fix it:** add a little bit of pressure smoothing and a pressure curve. Pens are hyper sensitive at low pressure. You'll typically want to add a pressure curve for any pen you use.

### Surface texture

* Good texture. Some of you might find it a little gritty.
* No complaint there - it just feels different from a Wacom Intuos Pro surface, which is expected.

### Pointer lag

* Feels responsive. Pretty typical lag - all tablets have lag.

### Diagonal wobble

* RATING: GOOD/OK (TBD - needs retesting on Windows)
* Tested with 10 cm strokes at 45° against a ruler, with basic smoothing turned off.
* I noticed a little bit of diagonal wobble at all stroke speeds. It was more visible on slow strokes and became less as I went faster. I don't think a person would notice unless they are drawing slowly and deliberately looking for it.
* I double-checked against a different straight edge to rule out the ruler. It's not the ruler.
* Comparisons with my previous test files:
  * Wacom Intuos Pro Large (PTH-860): even it shows a little bit of wobble. The Giano V2 has just a little bit more - not a lot.
  * Giano G930L: my test files show less wobble. That's a little disappointing.
* I tested on macOS this time. Maybe there's a difference on Windows. I need to check why there's a difference between these two models.
* This is the only thing that gave me some pause. It still deserves a VERY GOOD rating overall.
* Side note: basic smoothing doesn't seem to help wobble. It might even induce a little bit of it.

## Other inputs

### Pen buttons and Pan/Scroll

* I set the top pen button to Pan/Scroll and tested it in Krita. It worked fine.
* The only time it stopped working was when I lifted the pen out of hover range while holding the button down, then came back down. I think that's normal, or at least somewhat expected.
* TBD: Test Pan/Scroll with a pen button on Windows.

## Working with a large tablet

Large tablets require some adjustment to work with. More here: [Using large pen tablets](../../../guides/general/large-pen-tablets.md)

<!--
Not yet evaluated on stream (add when tested):
- Bluetooth / wireless behavior and sleep settings (see G930L notes)
- LCD auxiliary display
- Tilt compensation
- Pen cross-compatibility with other PW600 / PW600S / PW600L pens
- Diagonal wobble retest on Windows
- Pan/Scroll pen button on Windows
-->
