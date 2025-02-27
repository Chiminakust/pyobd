# ![PYOBD](/pyobd.gif) PYOBD 

This is the remake of the program PYOBD. It works on Python3 and all new libraries. It was tested on Linux, Windows, and it should work on Mac too. You just need an ELM327 USB or bluetooth device and a PC(laptop preferably).

NOTE: On Windows you will need a suitable driver for your ELM327 device(on Linux it is not needed). You can download drivers from here:  http://www.totalcardiagnostics.com/support/Knowledgebase/Article/View/1/0/how-to-install-elm327-usb-cable-on-windows-and-obd2-software

> pyOBD (aka pyOBD-II or pyOBD2) is an OBD-II compliant car diagnostic tool. It is designed to interface with low-cost ELM 32x OBD-II diagnostic interfaces such as ELM327. It will basically allow you to talk to your car's ECU,... display fault codes, display measured values, read status tests, etc. All cars made since 1996 (in the US) or 2001 (in the EU) must be OBD-II compliant, i.e. they should work with pyOBD.

### Video presentation on YouTube(click on it):
[![PYOBD Youtube video 2021](https://img.youtube.com/vi/l_220gVh2lY/0.jpg)](https://www.youtube.com/watch?v=l_220gVh2lY)

On Debian 10 type these commands to install the requirements:

> sudo apt-get install dpkg-dev build-essential libjpeg-dev libtiff-dev libsdl1.2-dev libgstreamer-plugins-base1.0 libnotify-dev freeglut3 freeglut3-dev libsm-dev libgtk-3-dev libwebkit2gtk-4.0-dev libxtst-dev

> pip3 install wxpython

> pip3 install pyserial

> pip3 install matplotlib

The program is run by typing: 
> python3 pyobd.py

The ignition must be on, to connect to the car and display data(key turned one level before engine start). Although most of the sensors display data only when the engine is running. If you connected and then turn the engine on, you must connect to the car again.

The program works nice and I will also add new functionalities to it. I am working on adding graphs and data export/saving(and bugfixes ofcourse).

TO DO LIST:<br />
-add graphs<br />
-check if there are any bugs when displaying DTC error codes<br />
-add monitor mode<br />
-add terminal<br />
-add custom commands<br />
-display freeze frame data<br />
-add sensor data exporting<br />
-add car data like VIN, model, etc.<br />

![ELM327](/elm327.jpg)
