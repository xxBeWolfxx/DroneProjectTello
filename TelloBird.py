import time

from tello import Tello
import cv2


class TelloBird(Tello):
    currentState = "landed"
    statusOfMission = False
    listOfStates = ["landed", "in-air", "moving", "turning", "too-weak"]
    listOfMissions = ["basicMisssionL", "squareMissionL", "squareMissionT", "takeOffMission"]
    minimalTimeWaiting = 3.0

    def __init__(self):
        super().__init__()
        self.detector = cv2.QRCodeDetector()
        self.wait(self.minimalTimeWaiting)
        self.land()
        self.__getData__()
        self.bbox = None
        if self.battery <= 10:
            print("Too low battery, recharge: ", self.battery)
            self.currentState = self.listOfStates[-1]

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

    def __endingMission__(self):
        self.statusOfMission = False
        self.streamon()

    def __validadtionCommand__(self, commands):
        if len(commands) > 1:
            return commands
        commands.append("None")
        return commands

    def __getData__(self):
        self.battery = self.get_battery()
        """TODO: Add more settings"""

    def EmergencyCall(self):
        print("Spadamy w dol")
        self.emergency()
        self.streamoff()
        self.land()

    def basicMisssionL(self) -> int:
        if self.currentState == self.listOfStates[0]:
            self.sendingCommand(self.takeoff())
            self.currentState = self.listOfStates[1]
            self.sendingCommand(self.land())
            self.currentState = self.listOfStates[0]
            self.__endingMission__()
            return 1
        else:
            print("I can't start a mission, I am flying")
            self.__endingMission__()
            return 0

    def test(self, distance):
        if self.currentState == self.listOfStates[0]:
            self.takeoff()
            self.wait(self.minimalTimeWaiting)
            self.currentState = self.listOfStates[1]
            self.forward(int(distance))
            print(self.get_speed())
            self.wait(self.minimalTimeWaiting)
            self.land()
            self.currentState = self.listOfStates[0]
            self.__endingMission__()
            return 1
        else:
            print("I can't start a mission, I am flying")
            self.__endingMission__()
            return 0

    def squareMissionL(self, distance):
        if self.currentState == self.listOfStates[0]:
            self.sendingCommand(self.takeoff())
            self.currentState = self.listOfStates[1]
            for i in range(2):
                self.sendingCommand(self.forward(int(distance)))
                time.sleep(1)
                self.sendingCommand(self.cw(90))
            self.sendingCommand(self.land())
            self.currentState = self.listOfStates[1]
        else:
            print("Something went wrong mate :(")
        self.__endingMission__()

    def squareMissionT(self, distance):
        distance = 30
        if self.currentState == self.listOfStates[1]:
            for i in range(4):
                self.sendingCommand(self.forward(int(distance)))
                self.sendingCommand(self.cw(90))
            self.sendingCommand(self.land())
            self.currentState = self.listOfStates[1]
            self.__endingMission__()
        else:
            print("Something went wrong mate :(")
        self.__endingMission__()

    def takeOffMission(self):
        if self.currentState == self.listOfStates[0]:
            self.takeoff()
            self.wait(self.minimalTimeWaiting)
            self.currentState = self.listOfStates[1]
            self.__endingMission__()
        else:
            return 0

    def startMission(self, chooseMission: int, parametr):
        if chooseMission == 0:
            self.wait(self.minimalTimeWaiting)
            self.basicMisssionL()
        elif chooseMission == 1:
            self.wait(self.minimalTimeWaiting)
            self.squareMissionL(parametr)
        elif chooseMission == 2:
            self.wait(self.minimalTimeWaiting)
            self.squareMissionT(parametr)
        elif chooseMission == 3:
            self.wait(self.minimalTimeWaiting)
            self.takeOffMission()

    def sendingCommand(self, command):
        while self.log[-1].get_response() != "b'ok'":
            print(self.log[-1].get_response())
            time.sleep(1)
            if self.log[-1].get_response() == "b'error No valid imu'":
                self.send_command(self.commandsHistory[-1])
        command
        self.previousCommand = command
