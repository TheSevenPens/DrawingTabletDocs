# TSG: Driver no longer supports a drawing tablet

## Overview

As years pass, a manufacturer will periodically publish new versions of their tablet driver.

And periodically, these driver updates drop support for older models.

You have a couple of options.

## OPTION 1: An older driver

Try an older version of your manufacturer's drivers that does support your tablet.

The risk of this approach is that sometimes the older drivers don't work well with newer operating systems. You may be left in a situation where some features don't work.

## OPTION 2: Use **OpenTabletDriver**

Setting up and configuring OpenTabletDriver can be challenging. On the other hand, it works with over 200 tablets - some over 20 years old.

OpenTabletDriver has full support for tilt and pressure on Windows and on macOS.

More here: [OpenTabletDriver](../guides/drivers/opentabletdriver/)

## OPTION 3: Use Windows PNP drivers

Windows has some VERY RUDIMENTARY support for tablets (this is called "Windows Plug-and-Play" support - shortened to PNP) and it works with SOME tablets in a limited way. It may be enough for the core features of some tablets. But it may not work well or at all with other tablets.

macOS does NOT have an equivalent to Plug-and-Play for drawing tablets.

More here: [Windows PNP support](../guides/platforms/windows/windows-pnp-support.md)
