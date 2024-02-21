# Using multiple drawing tablets at the same time

## It DOES work

You CAN use multiple drawing tablets at the same time with your computer. However, you need to be aware about the specific scenarios in which this will work and some issues that might encounter.

## Notes on MacOS

I have not tested it with MacOS.&#x20;

## Notes on Windows

### The scenario that works

Let's be explicit on the scenario that works:

* 2 or more drawing tablets attached to the same computer
* where you are using then pen with only one of them at one time

### You must use a single tablet driver

For you to use multiple tablets, a single driver must be installed and that driver must be compatible with each tablet.&#x20;

You cannot successfully use two separate tablet drivers even if you successfully install them.

### Cross-brand usage

Owing to the restriction of having a single driver, you cannot mix an match tablet brands. For example, you cannot use both a Wacom and Huion tablet.

### The driver must let you manage the tablets individually

* The driver will need to identify and let you configure each tablet separately.
* In the Wacom Tablet Properties app you will see the tablets shown at the top&#x20;
* In the Huion app, you can switch at the bottom
* In the XP-Pen app, you can switch in the upper left

### Pen compatibility

Each tablet can use a different pen. Of course, if you intend to switch between tablets it is convenient if you can use the same pen with each tablet.&#x20;

### Tablet types

You can use both pen tablets and pen displays together with the same computer&#x20;

### The tablet driver can get confused

Tablet drivers can occasionally get confused when you have multiple tablets. In my experience this has happened when I've been plugging them in and unplugging them back in very rapidly.

In those cases, I saw issues like it wouldn't let me use one of the tablets. The issues were was resolved by just restarting the tablet driver or restarting the computer.

In general I have not seen this kind of problem simply not rapidly attaching and detaching tablets to a computer.

### Simultaneous drawing will not work

Sometimes people want to use two tablets on a computer because they have two children and want each to be able to draw at the same time. This scenario does not work.

Let's suppose both children are drawing simultaneous on their individual tablet. The pens will "fight" and the pointer will bounce back and forth rapidly and it will be impossible to draw.&#x20;

### Support by brand

* Wacom - YES
* Huion - YES
* XP-Pen - YES
* Xencelabs - NO. As of September 2023, If you try it, the driver will tell you it is not yet supported. So in the future I do expect this to work.

### Setups I tested on Windows

**Wacom Setup 1** (tested in September 2023)

* Wacom Cintiq Pro 27 (DTH-271)
* Wacom One 13 touch (DTH-134)
* Wacom One 12 (DTC-121)
* Wacom Intuos Pro Large (PTH-860)
* Wacom Intuos M (CTC-6100WL)

**Wacom Setup 2** (tested in September 2023)

* Wacom Intuos Pro Large (PTH-860)
* Wacom Intuos 4 XL (PTK-1240)

**Huion Setup 1** (tested in September 2023)

* Huion Kamvas 22 Plus (GS2202)
* Huion Giano (G930L)
* Huion Kamvas 13 (GS1331)

**Huion Setup 2** (tested in September 2023)

* Huion Kamvas 24 Pro 4K (GT2401)
* Huion Kamvas 13 (GS1331)

**XP-Pen Setup 1** (tested in September 2023)

* XP-Pen Artist Pro 16 GEN2 (MD160QH)
* XP-Pen Deco Pro XLW GEN2 (MT1592B)

**Xencelabs Setup 1** (tested in September 2023)

THIS DOES NOT WORK - the driver explicitly says it doesn't support multiple tablets

* Xencelabs Pen Tablet Medium
* Xencelabs Pen Display 24
