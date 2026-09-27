# TSG: Tablet is sensitive to how the USB-C cable is plugged in

## Overview

The tablet works, but is very sensitive to how the USB-C cable is plugged into the USB-C port on the tablet. You might have to jiggle the cable to get it working, or it might feel loose in the port.

## Normal behavior

USB-C cables are not LOCKED into the port unlike some connector types. Almost always the connection has a slight "play". While there is some play, I do not recommend that you try to test the limits of the movement. It is best to avoid moving it around or placing too much strain on the cable because that strain can affect the port.

## Abnormal behavior

Sometimes tablets can develop a certain sensitivity to how the cable is positioned in the port. For example:

* Tablet disconnects and reconnects when the cable moves
* The pen stops responding until you wiggle the plug
* Knocking the cable triggers clicks or button presses
* The cable needs to be angled in a certain way to work
* A pen display's screen flickers or goes black when the cable is touched

## USB-C ports are prone to these problems

In theory any port can become sensitive to how a cable sits in it - USB-A, DisplayPort, HDMI. In practice those are much more robust. Their connectors are bigger, and some lock in place. USB-C connectors are small, and the port does not sit deep in the tablet's body. That's why I think we see this mostly with USB-C ports.

## The key question

Is the problem the **cable** or is it the **port** on the tablet?

Most of the time, if the tablet is sensitive to the cable's position, it is due to the port itself.

It is possible it is the cable, and that is worth checking, but typically it is the port.

## What is the cause of a port problem?

If the problem is in the port, it can be because the port connector inside the tablet has gotten loose so it is moving too much, or it is damaged in such a way that only a particular amount and direction of force from the cable can keep it working.

Thus, this is usually a physical problem with a port connector.

## Ruling out the cable

To check that it's not the cable, here are some things you can try:

* Connect the USB-C cable directly - Remove any hubs, adapters and extension cables, and plug the tablet straight into the computer. Make sure every end is pushed all the way in. If you're using a 3-in-1 cable, check all three ends, not just the one going into the tablet. See: [TSG: Tablet driver does not detect the tablet](tsg-tablet-driver-does-not-detect-tablet.md)
* Try a different port on the computer - If the problem only happens on one port, the problem is that port, not the tablet.
* Try a different cable - Swap in a cable you know works.
  * **Pen tablets** - any good USB data cable with the right connector will do. See: [Using 3rd-party cables with your drawing tablet](../guides/connecting/3rd-party-cables-for-drawtab/)
  * **Pen displays** - ask the manufacturer's customer support which cable to get. See: [TSG: Replacing a lost tablet cable](tsg-replace-lost-tablet-cable.md)
* If you're already using a 3rd-party cable, try the manufacturer's cable. Some USB-C ports expect a slightly longer connector than a 3rd-party cable has. The connection works, but it feels loose and disconnects if the cable moves.

## Dealing with a port problem

If it happens with a known-good cable, on a different port, connected directly, then the port on the tablet is worn or damaged. This is not something you can fix with settings or drivers.

Your options:

* With the help of an electronics expert you could in theory replace the USB port connector. See: [Replacing the USB port on a drawing tablet](../guides/customizing/replace-usb-port.md)
* Contact your tablet manufacturer's customer support. If the tablet is old and no longer supported, this may be the point where it's time to replace it.

## Preventing it

* Don't leave the cable plugged in when you carry the tablet around. It can push and pull on the port and loosen it. See: [Transporting your drawing tablet](../guides/maintain/transporting-drawtab.md)
* Don't put excessive strain on the USB-C cable - there shouldn't be any tension on it.
