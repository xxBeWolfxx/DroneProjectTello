# Tello project
This repository contains university project. We have based our idea on repository of **[easyTello](https://github.com/Virodroid/easyTello)** on GitHub. We have created project to control a Tello drone by special QR codes which contains a special mission for UAV. **Warning! We wrote code on Linux operating system!** We haven’t tested code in other platforms so maybe not every feature will have worked correctly on your computer.
### Installation
TelloBird uses Python 3 and OpenCV with dev-kits, which is necessary to read QR code. Communication with drone is based on UDP protocol and special commands, which are described in [DJI Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf) documentation.
**Don’t use:**
```bash
pip3 install opencv-python
```
This installation wouldn’t install all necessary modules. We suggest to use for example this [tutorial](https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/) for installing openCV.
To communicate with drone, you have to have _socket_ and _threading_ modules, which should be installed with Python by default. Unless they are installed, you have to use:
```bash
pip3 install socket threading
```
All communiaction tasks are solved by ***easyTello*** module.

## Extended module, _TelloBird_
We have extended _easyTello_ modules by adding our module ***TelloBird*** which contains our protocols of missions. Every mission is triggered by QR code, which is exclusive for each task. 
