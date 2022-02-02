import time

from tello import Tello
import cv2
import csv
import math

class TelloBird(Tello):
    currentState = "landed"
    statusOfMission = False
    listOfStates = ["landed", "in-air", "moving", "turning", "too-weak"]
    listOfMissions = ["basicMisssionL", "squareMissionL", "squareMissionT", "takeOffMission", "circleMissionL","eightMissionL","circleCurveMissionL", "test"]
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

    def __validadtionCommand__(self, commands):
        if len(commands) > 1:
            return commands
        commands.append("None")
        return commands

    def __getData__(self):
        self.battery = self.get_battery()
        """TODO: Add more settings"""

    def EmergencyCall(self):
        print("Emergency call!!!")
        self.__saveLogs__()
        self.emergency()
        self.streamoff()
        self.land()


    def basicMisssionL(self) -> int:
        if self.currentState == self.listOfStates[0]:
            self.sendingCommand(self.takeoff(), 1)
            self.currentState = self.listOfStates[1]
            self.sendingCommand(self.land(), 1)
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
            self.currentState = self.listOfStates[1]
            self.sendingCommand(self.forward(int(distance)), 2)
            self.sendingCommand(self.cw(180), 1)
            self.sendingCommand(self.forward(int(distance)),2)
            self.sendingCommand(self.land(),1)
            self.currentState = self.listOfStates[0]
            self.__endingMission__()
            return 1
        else:
            print("I can't start a mission, I am flying")
            self.__endingMission__()
            return 0

    def squareMissionL(self, distance):
        if self.currentState == self.listOfStates[0]:
            self.sendingCommand(self.takeoff(),1)
            self.currentState = self.listOfStates[1]
            for i in range(4):
                self.sendingCommand(self.forward(distance),2)
                self.sendingCommand(self.cw(90),1)
            self.sendingCommand(self.land(),1)
            self.currentState = self.listOfStates[1]
        else:
            print("Something went wrong mate :(")
        self.__endingMission__()

    def squareMissionT(self, distance):
        if self.currentState == self.listOfStates[1]:
            for i in range(4):
                self.sendingCommand(self.forward(int(distance)),1)
                self.sendingCommand(self.cw(90),1)
            self.sendingCommand(self.land(),1)
            self.currentState = self.listOfStates[1]
            self.__endingMission__()
        else:
            print("Something went wrong mate :(")
        self.__endingMission__()

    def takeOffMission(self):
        if self.currentState == self.listOfStates[0]:
            self.sendingCommand(self.takeoff(),1)
            self.currentState = self.listOfStates[1]
            self.__endingMission__()
        else:
            return 0

    def circleMissionL(self, radius):
        if self.currentState == self.listOfStates[0]:
            radius = int(radius)
            self.sendingCommand(self.takeoff(), 1)
            self.sendingCommand(self.up(150), 1)
            radius = int(radius * math.sqrt(2.0))
            self.sendingCommand(self.curve(radius,0,0,radius,radius,0,20), 1)
            self.sendingCommand(self.curve(-radius, 0, 0, -radius, -radius, 0, 20), 1)
            self.sendingCommand(self.land(),1)
            self.__endingMission__()
        else:
            self.__endingMission__()
            return 0

    def circleCurveMissionL(self, radius):
        if self.currentState == self.listOfStates[0]:
            radius = int(radius)
            self.sendingCommand(self.takeoff(), 1)
            radius = int(radius * math.sqrt(2.0))
            self.sendingCommand(self.curve(radius,0,40,radius,radius,60,20), 1)
            self.sendingCommand(self.curve(-radius, -40, 0, -radius, -radius, -60, 20), 1)
            self.sendingCommand(self.land(),1)
            self.__endingMission__()
        else:
            self.__endingMission__()
            return 0

    def eightMissionL(self, radius):
        if self.currentState == self.listOfStates[0]:
            radius = int(radius)
            self.sendingCommand(self.takeoff(), 1)
            self.sendingCommand(self.up(100), 1)
            radius = int(radius * math.sqrt(2.0))
            self.sendingCommand(self.curve(radius, 0, 0, radius, radius, 0, 30), 1.5)
            self.sendingCommand(self.curve(-radius, 0, 0, -radius, -radius, 0, 30), 1.5)
            self.sendingCommand(self.curve(-radius, 0, 0, -radius, radius, 0, 30), 1.5)
            self.sendingCommand(self.curve(radius, 0, 0, radius, -radius, 0, 30), 1.5)
            self.sendingCommand(self.land(), 1)
            self.__endingMission__()
        else:
            self.__endingMission__()
            return 0





    def startMission(self, chooseMission: int, parametr):
        if chooseMission == 0:
            self.wait(int(self.minimalTimeWaiting * 0.75))
            self.basicMisssionL()
        elif chooseMission == 1:
            self.wait(int(self.minimalTimeWaiting * 0.75))
            self.squareMissionL(parametr)
        elif chooseMission == 2:
            self.wait(int(self.minimalTimeWaiting * 0.75))
            self.squareMissionT(parametr)
        elif chooseMission == 3:
            self.wait(int(self.minimalTimeWaiting * 0.75))
            self.takeOffMission()

        elif chooseMission == 4:
            self.wait(int(self.minimalTimeWaiting * 0.75))
            self.circleMissionL(parametr)

        elif chooseMission == 5:
            self.wait(int(self.minimalTimeWaiting * 0.75))
            self.eightMissionL(parametr)

        elif chooseMission ==6:
            self.wait(int(self.minimalTimeWaiting * 0.75))
            self.circleCurveMissionL(parametr)

        elif chooseMission == 7:
            self.wait(int(self.minimalTimeWaiting * 0.75))
            self.test(parametr)

    def sendingCommand(self, command, scaleTime):
        self.wait(int(self.minimalTimeWaiting * scaleTime))
        command

    def __saveLogs__(self):
        with open('logs.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Id', 'Command', 'Response', 'Start_time', 'End_time', 'Duration'])
            for item in self.log:
                writer.writerow([item.id, item.command, item.response, item.start_time, item.end_time, item.duration])
