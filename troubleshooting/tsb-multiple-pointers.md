# TSB: Multiple pointers

## Overview

Using your drawing tablet occasionally you may run into a situation where you see 2 pointers simultaneously. One pointer will be moved by your drawing tablet pen. And the other pointer may also move in a similar way or stay still. And typically both pointers are flickering on and off very quickly.

## Cause

Having multiple pointers like this is not a hardware problem. It is a software problem and usually has to do with tablet drivers. Specifically, it occurs when there are multiple tablet drivers installed.

## Operating system

In my experience this is something that has only happened with Windows. I've never encountered anyone who has observed this on Mac OS.

## Steps to fix (Windows)

This problem seems to happen when there are multiple tablet drivers on your windows computer.

The first thing to do is uninstall every tablet driver on your computer.

Then restart the computer.

Sometimes uninstalling a tablet driver leaves little "bits" of the tablet driver behind. So I recommend running the [Tablet Driver Cleanup tool](../guides/drivers/tablet-driver-cleanup-tool.md).

Once the tool is done, restart your computer.

Then finally install the tablet driver for your tablet.

To be safe, restart your computer one more time even if your tablet driver does not ask you to.

If these steps don't fix the problem then you need to contact support.

