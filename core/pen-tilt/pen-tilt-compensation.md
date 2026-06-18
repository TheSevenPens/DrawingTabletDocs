# Pen tilt compensation

To correctly represent the position of the pen, the tablet has to perform something called tilt compensation. This means adjusting the pointer position depending on how much the pen is tilted.

<figure><img src="../../.gitbook/assets/image-000415.png" alt="" width="375"><figcaption></figcaption></figure>

This is very important for EMR tablets because the digitizer senses an inductor inside the pen. That inductor is not close to the tip of the pen. It is deeper inside the pen.

Some other pen technologies do not have as much separation. For example, the Apple Pencil does not have as much separation as EMR tablets.

No tablet does tilt compensation perfectly. I have seen some very old tablets do this very badly, almost as if they do not compensate for tilt at all. These days, a modern EMR drawing tablet usually does a decent job compensating for tilt. The pointer does not usually shift too far away from the pen tip, but there is still some variation. Some tablets are better at this than others.
