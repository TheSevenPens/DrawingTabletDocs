# Pen input APIs

### **Windows**

* **Windows Third-party: WinTab** [https://developer-support.wacom.com/hc/en-us/articles/12844524637975-Wintab](https://developer-support.wacom.com/hc/en-us/articles/12844524637975-Wintab) This is the older but still heavily used API. Even though the API is defined by Wacom, other graphics tablet manufacturers use this same API. More here [WinTab API](wintab-api.md).
* **Windows Built-in APIs (aka. Windows Ink)**
  * WIN32 - [GetPointerPenInfo](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getpointerpeninfo)
  * WPF - [StylusPointProperties](https://docs.microsoft.com/en-us/dotnet/api/system.windows.input.styluspointproperties)
  * UWP - [PointerPointProperties](https://docs.microsoft.com/en-us/uwp/api/windows.ui.input.pointerpointproperties)
  * WinUI3 - UNKNOWN (As of Aug 2024 I do not think WINUI3 supports pens)
* Windows resources:
  * [WinTab vs Windows Ink](wintab-vs-winink.md)

## Linux

* GTK - [GdkDevice](https://developer.gnome.org/gdk3/stable/GdkDevice.html#gdk-device-get-axis-value)
* Qt - [QTabletEvent](https://doc.qt.io/qt-5/qtabletevent.html)

## MacOs

* [NSEvent](https://developer.apple.com/documentation/appkit/nsevent/1534543-pressure?language=objc)
* [PencilKit](https://developer.apple.com/documentation/pencilkit/pkstrokepoint)

## Web

* [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent)
* [HID Explorer](https://nondebug.github.io/webhid-explorer/)
