# Tello project
This repository contains university project. We have based our idea on repository of [easyTello](https://github.com/Virodroid/easyTello) on GitHub. We have created project to control a Tello drone by special QR codes which contains a special mission for UAV.
## Instalation
TelloBird uses Python 3 and OpenCV with dev-kits, which is necessary to read QR code. Communication with drone is based on UDP protocole and special commands, which are described in [DJI Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf) documentation.

## Extended module
We have extended _easyTello_ modules by adding our module TelloBird which contains our protocols of missions. Every mission is triggered by QR code, which is exclusive for each task. 
