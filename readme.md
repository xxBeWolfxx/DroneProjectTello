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
***

## Extended module, _TelloBird_
We have extended _easyTello_ modules by adding our module ***TelloBird*** which contains our protocols of missions. Every mission is triggered by QR code, which is exclusive for each task. 

### Features
We have defined a list with all available missions and states of UAV:
```python
class TelloBird(Tello):
    ...
    listOfStates = ["landed", "in-air", "moving", "turning", "too-weak"]
    listOfMissions = ["basicMisssionL", "squareMissionL", "squareMissionT", "takeOffMission","test"]
    ...
```
List of states provides security that we will not be able to run a mission which requires different starting state. For example, we will not able rerun _takeOffMission_ because the drone will already have set a state _in-air_. The last letter in name of a mission says on state of drone:
- L - it means that drone is landed
- T - it means that drone is in air

Some of them need to be run with kind of argument. For example, _squareMissionL_ requires an argument how far UAV has to fly forward. To run properly function you have to create a QR code as **string** as in the pattern: 
```bash
_squareMissionL_ 30
```
***Warning!! Remember, drone has own tolerance of distance. The minimum value which you can pass to command is 20***
In other hand _takeOffMission_ does not need extra argument but every validation of passing mission is checked by the special function:
```python
    def __validadtionCommand__(self, commands):
        if len(commands) > 1:
            return commands
        commands.append("None")
        return commands
```
Next mission, which we have added, is _watingForMission_. 
```python
    def watingForMission(self):
        if self.statusOfMission == True:
            return 0
        if self.last_frame is not None:
            data, self.bbox, straigt_qrcode = self.detector.detectAndDecode(self.last_frame)
        if self.bbox is not None:
            print(data)
            if data != "":
                commands = self.__validadtionCommand__(data.split())
                index = self.listOfMissions.index(commands[0])
                self.statusOfMission = True
                self.startMission(index, commands[1])
        self.bbox = None
```
It provides all features which are necessary to read QR codes and run proper mission. Firstly, the method check if drone is able to run mission. This is not the most important thing but if you will write async function, it becomes needful. In _startMission_ code runs a specific function:
```python
    def startMission(self, chooseMission: int, parametr):
        if chooseMission == 0:
            self.wait(int(self.minimalTimeWaiting*0.75))
            self.basicMisssionL()
        elif chooseMission == 1:
            self.wait(int(self.minimalTimeWaiting*0.75))
            self.squareMissionL(parametr)
        elif chooseMission == 2:
            self.wait(int(self.minimalTimeWaiting*0.75))
            self.squareMissionT(parametr)
        elif chooseMission == 3:
            self.wait(int(self.minimalTimeWaiting*0.75))
            self.takeOffMission()
        elif chooseMission == 4:
            self.wait(int(self.minimalTimeWaiting*0.75))
            self.test(parametr)
```
You can see that we have implemented simply switch case method. Code checks which function has to be executed. Every mission is defined in module. For example:
```python
    def takeOffMission(self):
        if self.currentState == self.listOfStates[0]:
            self.takeoff()
            self.wait(self.minimalTimeWaiting)
            self.currentState = self.listOfStates[1]
            self.__endingMission__()
        else:
            self.__endingMission__()
            return 0
```
The _endingMission_ provides resetting all variables which are essential to run the next mission.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
> MIT License
Copyright (c) [2021] [Arkadiusz Kruszynki Maciej Zawadzki]
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



***
# FAQ
1. Problems with H.264 decoder.
```bash
non-existing PPS 0 referenced
decode_slice_header error
non-existing PPS 0 referenced
decode_slice_header error
no frame!
```
> This error is easy to solve. Packages of information from UAV come with big delay. You have to only wait some time. On the other hand we have managed with this problem and IDE stopped executing program. We suggest changing an IDE. 
```bash
foffefe ""TODO""
```
> This problem is critical. Some cases you will not able to run this code in macOS or windows. On Linux you will have to install special libraries for lib264.

2. Responses from UAV
```bash
Response: error'no imu' TODO
```
> This problem is very complex. Firstly, you have to check state of drone's battery. It must not be too low. Secondly, you have to make calibration in [Tello app](https://play.google.com/store/apps/details?id=com.ryzerobotics.tello&hl=pl&gl=US). Thirdly, you would have to send commands to drone too quickly. You need to increase delay between commands. Moreover, sometimes the environment in which drone is tested, causes this problem. You have to check if lights in room is enough for drone and the base, from which done take off, is enough colourful. **REMEMBER!** Drone uses its camera for stabilization and IMU.
