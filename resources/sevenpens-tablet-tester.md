# SevenPens Tablet Tester

## Overview

This a is a SIMPLE web app that useful for verifying your tablet and its core features work.

Try out the tester: [https://thesevenpens.github.io/WebTabletTesterBasic/](https://thesevenpens.github.io/WebTabletTesterBasic/)

Just open the tester and start drawing in the blue area

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

## Safety and privacy

This tool:

* Does **not** collect any data about you, your computer, etc.
* Does **not** uses no cookies.
* Does **not** track your behavior.
* Does **not** record what you draw.

## OS & Browser compatibility

**Windows**

* Pen API:
  * Needs Windows Ink to be enabled in the tablet driver.
  * If you tablet driver is using only WinTab, no pressure is supported.
* Chrome - WORKS
* Firefox - WORKS

**MacOS**

* Safari - yet to be tested
* Chrome - WORKS

**Linux**

* Chrome - WORKS
* Firefox
  * Wayland - WORKS
  * X11 -
    * use `env MOZ_USE_XINPUT2=1 firefox` to make it work
    * more info on what's going on with the X11 issue:
      * [https://stackoverflow.com/questions/78073830/pen-pointer-events-in-linux-chrome-and-firefox-not-working-as-intended/78764151#78764151](https://stackoverflow.com/questions/78073830/pen-pointer-events-in-linux-chrome-and-firefox-not-working-as-intended/78764151#78764151)
      * [https://bugzilla.mozilla.org/show\_bug.cgi?id=1207700](https://bugzilla.mozilla.org/show_bug.cgi?id=1207700)

**iPadOS**

* Safari - WORKS

**Android**

* Chrome - WORKS

## Open source

The entire source code is on the GitHub repo ([https://github.com/TheSevenPens/WebTabletTesterBasic](https://github.com/TheSevenPens/WebTabletTesterBasic)) . I encourage you to look through it and fork and modify it for your needs.
