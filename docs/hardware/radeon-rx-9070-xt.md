---
published: true
---
# Radeon RX 9070 XT

## 🪲 Graphic bugs in desktop applications
The Adrenalin graphics driver (confirmed for versions 25.3.1 and later) causes graphic bugs in various desktop applications when hardware acceleration is enabled. The bug does not appear if

1. The [PRO Edition](https://www.amd.com/en/resources/support-articles/faqs/PDH-INSTALL.html) drivers are installed or
2. No AMD drivers are installed

### [Visual Studio Code](https://code.visualstudio.com/)
With Light Themes, the mouse cursor “disappears” in the editor area ([GitHub Issue](https://github.com/microsoft/vscode/issues/204103)). 

#### Workaround
In the file `%USERPROFILE%\.vscode\argv.json` add (uncomment) the row `"disable-hardware-acceleration": true`.

Alternatively disable *multi plane overlay* ([source](https://community.amd.com/t5/pc-drivers-software/problem-with-hardware-acceleration-in-chromium-browsers/td-p/589225)):

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Dwm]
"OverlayTestMode"=dword:00000005
```

### [Datacrow (Java)](https://datacrow.org/)
After right-clicking on an image in an entry (and moving the mouse) or attempting to filter by tag, the GUI elements seem to "move around".

#### Workaround
Disable hardware acceleration by starting the application with `java -Dsun.java2d.noddraw=true -jar datacrow-client-5.0.0.jar` ([source](https://superuser.com/questions/373290/disable-java-hardware-acceleration-in-windows)).

## 🪲 OpenCL applications crash on startup
Some applications that uses OpenCL crash on startup (confirmed for Adrenalin graphics driver versions 26.5.2 and later).

### [Darktable](https://www.darktable.org/)
The Workaround is to launch the program with `darktable.exe --disable-opencl` .