# 7P notes: Huion Kamvas Pro 19 (GT1902)

## Summary

I do recommend this tablet. The drawing experience is the best Huion's ever had.&#x20;

Is it as good as a Wacom Cintiq Pro? No. But it is VERY GOOD overall with only a few limitations and minor issues you should be aware of.

## Basics

* Resolution: 4K (3840x2160)
* PenTech 4.0
* New AG glass
* Multi-touch (for Windows only)
* Comes with 2 pens: PW600 and PW600S
* Diagonal size: 19"&#x20;
  * Actually 18.57"
* Released: Jan 2024

## PenTech 4.0

Definitely an improvement over PenTech 3.0. Especially noticable in how pressure is handled.



## Pens

Comes with 2 pens: PW600 and PW600S. More manufacturers should do this!

Cross compatibility

* Older Huion PenTech 3.0 pens DO NOT work with this tablet
* The newer PenTech 4.0 pens DO NOT work with older tablets

**Notes on backwards compatibility with the older PW517 pen** - not compatible. Or at least not completely compatible. The PW517 pen will move the pointer, but not there is no pressure detected so drawing is useless.

## Drawing Experience

* **Corner/Edge accuracy** - NORMAL. This is only visible in the last 2mm and did not affect my normal usage of the tablet. It was so minor, I didn't even bother performing any calibration to address it.
* **Pointer lag** - NORMAL - standard for modern pen displays.
* **Parallax** - NORMAL - standard for modern pen displays.
* **Pen maximum pressure** - VERY GOOD. I measured both pens at 510gf (slightly \*more\* than the 500gf that Huion specified). This amount of variance is normal.
* **Pressure Transition Instability** - VERY GOOD. You may remember the issues I pointed out with the Huion Inspiroy 2 L and the Wacom One M. That the problem is not visible with this tablet and pen. Remember: All tablets have some amount of it. Desirable tablets just have a very small amount of it and you have to construct situations to reveal it. This tablet so far seems comparable to what I see with the Wacom Intuos Pro & Cintiq Pro tablets. more here: [**pressure transition stability**](../../../guides/core-features/pen-pressure-transition-stability.md)&#x20;
* **Pen button stroke interruptions** - While drawing with older Huion pens the buttons would might interrupt the drawing - even if you disabled the buttons in the driver. With the new pens, the buttons do not interfere with the stroke.
* **Pen tilt compensation** - VERY GOOD. The pointer stays where the nib is during normal ranges of tilt with some deviation only at extreme angles. more here: [**pen tilt compensation**](../../../guides/core-features/pen-tilt-compensation.md).

## **Display**

**Refresh rate** - NORMAL. Up to 60Hz which is standard for pen displays in 2024. Does not support 120Hz.

**Anti-Glare sparkle** - OK. This is a BIG IMPROVEMENT over some older Huion models. Slightly noticeable at 6 inches. At normal drawing distance for me not noticeable. I am very happy with the outcome. In comparison the Wacom Cintiq Pro 16 (DTK-167) has a little less AG sparkle.

**Sharpness** - OK. the anti-glare treatment diffuses the light coming from the display. The result is that the pixels on the display are "soft" and not as crisp as on comparable 16" or 22" displays. Several other people with this tablet have commented on the same thing. For me this is not a problem. In comparison, even the Wacom Cintiq Pro 16 (DTK-167) has a slightly soft experience, this Huion has a little more softness than that.

<figure><img src="../../../.gitbook/assets/GT1902_softness.jpg" alt=""><figcaption></figcaption></figure>

**Brightness** - seems as advertised. I thought it was fine. It's not especially bright - but I thought it was bright enough at 100%.

**Parallax** - VERY GOOD. It has very little parallax. As good as - maybe even a little better than the Wacom Cintiq Pro 22 in my observation.

##

## **Connections and cabling**

**Single USB-C cable connection?**

No ... but some people have made it work.

This gets a little confusing. Let me summarize buy saying: (1) I have not gotten it to work with 1 cable and (2) at least one person has. (3) And as of 2024/02/28 Huion's documentation on this topic indicates that the tablet does require an additional cable for power.&#x20;

I could not use it with a single USB-C cable. Huion did not say that single-cable operation was a feature - so I am not surprised. Tablets above 16 inches generally require additional power.

* Power: I have it connected with its USB-C power cable to the provided power adapter.
* Data and display signal: I used the supplied USB-C cable to connect it to my Microsoft Surface Thunderbolt Dock. I connected the dock to a Microsoft Surface Pro 8. For MacOS testing I connected the dock to an M3 MacBook Pro.

However this user got it to work with by plugging the single cable into a ASUS ThunderboltEX 4 expansion card: [https://www.reddit.com/r/huion/comments/1b22sia/huion\_kamvas\_pro\_19\_usbc\_cables/](https://www.reddit.com/r/huion/comments/1b22sia/huion\_kamvas\_pro\_19\_usbc\_cables/)

And here is Huion's document where they list the tablet as requiring additional power:

[https://support.huion.com/en/support/solutions/articles/44002011098-list-of-compatible-devices-support-usb-c-to-usb-c-connection-with-huion-displays](https://support.huion.com/en/support/solutions/articles/44002011098-list-of-compatible-devices-support-usb-c-to-usb-c-connection-with-huion-displays)

**Using third party USB-C cables for display signal & data**

I tried a Cable Matters USB-C Thunderbolt cable. It did work, however sometimes slight movements of the cable cause the tablet to lose the display signal and data.

Upon closer examination, the Huion USB-C cable plug is slightly longer than the CableMatters cable. So there is a slight difference on how some third party cables can connect.

For this reason I recommend using the supplied Huion USB-C cable.

## Touch

* **Touch on MacOS** - DOES NOTHING. Which is what Huion said it would do. So, no surprise.
* **Touch on Windows** - Still under evaluation.
  * By default, touch on the tablet will normally map to whichever display is your "main monitor".&#x20;
  * You can map touch back to the tablet when it is not the main monitor. See this document from Huion: [How to make finger gestures control Kamvas Studio 16/Kamvas Pro 19/Kamvas Pro 27 instead of the external monitor](https://support.huion.com/en/support/solutions/articles/44002416035-how-to-make-finger-gestures-control-kamvas-studio-16-kamvas-pro-19-kamvas-pro-27-instead-of-the-exter). When I first tried this, it fixed the touch problem, but it had an odd interaction with the pen - when I used the pen on the tablet, the pointer always stayed near the top border. After I uninstalled the driver, restarted the computer, and reinstalled the driver, the problem went away and the pen worked normally.
* **Palm rejection**: OK. Very TYPICAL for Touch on pen displays.&#x20;
  * Touch support is not comparable to an iPad's touch support which is EXCELLENT. Too often I accidentally pressed something on the screen because of my palm.&#x20;
  * I would say it's very on par with the Cintiq Pro 22 and Cintiq Pro 27.  I didn't try to use a drawing glove yet.&#x20;
  * Brad Colbow in his review of the Kamvas Pro 27 noticed that the palm rejection didn't seem to result in accidental drawing, but rather accidental clicks. I had the same experience.
  * Note: I used the tablet without using any drawing glove. In theory a drawing glove would help with the palm-rejection.&#x20;

## **Ergonomics**

**Weight** - lighter than I expected. I noticed it immediately when I picked up the box.&#x20;

**VESA mounting** - YES. There are 75 mm × 75 mm VESA holes for mounting on the back.&#x20;

**Legs** - YES. Two legs

**Noise** - EXCELLENT. No noise because no fans

**Heat** - EXCELLENT. After running at 100% brightness for one month days without turning off the tablet, the tablet stays cool. Roughly the same temperature as the Wacom Cintiq Pro 22 - maybe very very slightly warmer. Just very slightly warmer on the right than the left side.&#x20;

**Stand** - It does not come with a stand. Instead, I used separately-purchased Huion ST100A stand which attaches to this pen display using the VESA mounting holes.&#x20;

**Surface texture** - it feels slightly more textured than the Huion Kamvas Pro 24 4K

## Pens and Pressure

**Pens** - comes with the PW600 and PW600S pens.&#x20;

**Driver & Pens** - the driver knows that there are two different pen models and has separate button settings for each. However settings like the driver pressure curve are the shared across both pens.&#x20;

**Pen buttons** - GOOD. the PW600 has 3 buttons. The PW600S has two buttons.

**Pen button feel** - GOOD. the buttons on both pens have a nicer "crisper" clicking action than the buttons of the PW517 which feel a bit soft/mushy in comparison

**Pen IAF** - GOOD. Huion says 2gf for both pens. Seems accurate. A little more sensitive than the PW517 pen which is at about 3gf.



**PW600/PW600S compatibility with older tablets** - The new pens are NOT compatible with older Huion tablets.

**Pen weight** - I measured with a digital scale

* PW517 = 14g
* PW600 = 16g
* PW600S = 14g

**Issue with the PW600 pen & nib** - On the third day of using the tablet the PW600 pen would click or draw even when it was hovering. I did drop the pen at some point during the third day and that may have triggered something. I removed the nib, saw the nib was bent and replaced it with a fresh nib and the problem went away.&#x20;

**Default nib** - The default pre-installed nib on both the PW600 and PW600s pens is the felt nib, no the plasti nib.&#x20;

**Pen eraser** - the PW600 and PW600S pens do have an eraser. I don't user erasers so don't have any particular comment on it.



## Diagonal wobble

GOOD. LOW amounts of wobble in stroke.

<figure><img src="../../../.gitbook/assets/Huion Kamvas Pro 19 (GT1902) wobble (1).png" alt=""><figcaption></figcaption></figure>

## Compared to the Huion Kamvas Pro 24 4K (GT2401)

The Huion Kamvas Pro 24 4K (GT2401) was Huion's flagship pen display for a few years. And now the the Kamvas Pro 19 and Kamvas Pro 27 tablets represent the new flagship tablets.  &#x20;

The new tablets have clear improvements in these areas.

* Pressure handling through the new PenTech 4.0  is clearly better.
* The new pens have an eraser and that night be important for you
* The new tablets have less AG sparkle&#x20;
* The new tablets have touch&#x20;

There are a few areas that might not compare as well though

* The new anti-glare treatment gives a slightly soft look to the pixels in the Kamvas Pro 19 at least. I didn't test the Kamvas Pro 27 so not sure how much the softness is present in that model.
* Currently there is no exact match in terms of size to the 24". Drawing on 19" feels very different than 24".&#x20;
* The new tablets are a bit more expensive for their size.

But for other areas, the Kamvas Pro 24 4K was already a good pen display. So for this reason, if you already have a Huion Kamvas Pro 24 4K (GT2401) then these new tablets are NOT an immediate "MUST BUY". If you are happy with how your Kamvas Pro 24 4K is working, then keep it. I would suggest at least waiting to see if Huion releases something closer to a 24" size.&#x20;

## Other topics

**Sound** - there's a headphone jack for audio. Some of you may find this convenient.

In Windows if you connect the tablet, it may **appear** that windows has lost sound output. What is happening here is Windows can automatically switch its default audio to a new audio device - which is what this tablet is. Of course, it doesn't have speakers, so you won't hear anything unless you have a headphone connected.&#x20;

**Driver > Active Area mapping on resume from sleep on Windows** - On Windows, when resuming from sleep the Huion driver can occasionally become be confused about how to map the active area of the tablet to the screen. It may choose the wrong screen. It map span across both screens. When it does this it may not track the pen position correctly. This is resolved just by restarting Windows. This is a well-known issue with Huion drivers. Not a serious problem but a minor irritation.&#x20;

**Can you use it as a pen tablet?**

Yes. In Windows, you can tell windows to "disconnect" the display in the tablet and you will no longer see anything on the tablet. It will say "no signal" for few seconds then go dark. However, you can still use the pen on the tablet - just like a normal pen tablet (screenless tablet).

NOTE: If you press the button to power down the tablet, it will turn off the display AND it will stop the pen from working.

