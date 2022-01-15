from tello import Tello
import cv2


class TelloBird(Tello):
    currentState = "landed"
    statusOfMission = False
    listOfStates = ["landed", "in-air","moving","turning","too-weak"]
    listOfMissions = ["BasicMisssionL", "SquareMissionL"]
    minimalTimeWaiting = 3.0



    def __init__(self):
        super().__init__()
        self.detector = cv2.QRCodeDetector()
        self.wait(self.minimalTimeWaiting)
        self.land()
        self.__getData__()
        if self.battery <= 10:
            print("Too low battery, recharge: ", self.battery)
            self.currentState = self.listOfStates[-1]
        
    def WatingForMission(self):
        if self.statusOfMission == True:
            return 0
        if self.last_frame is not None:
                data, bbox, straigt_qrcode = self.detector.detectAndDecode(self.last_frame)
        if bbox is not None:
            print(data)
            commands = self.__validadtionCommand__(data.split())
            index = self.listOfMissions.index(commands[0])
            self.StartMission(index,commands[1])
            self.statusOfMission = True

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
        print("Spadamy w dol")
        self.emergency()
        self.streamoff()
        self.land()

    def BasicMisssionL(self) -> int:
        if self.currentState == self.listOfStates[0]:
            self.takeoff()
            self.wait(self.minimalTimeWaiting)
            self.currentState = self.listOfStates[1]
            self.land()
            self.currentState = self.listOfStates[0]
            self.__endingMission__()
            return 1
        else:
            print("I can't start a mission, I am flying")
            self.__endingMission__()
            return 0


    def SquareMissionL(self, distance):
        if self.currentState == self.listOfStates[0]:
            self.takeoff()
            self.currentState = self.listOfStates[1]
            self.wait(self.minimalTimeWaiting)
            for i in range(4):
                self.forward(distance)
                self.wait(self.minimalTimeWaiting)
                self.cw(90)
            self.land()
            self.currentState = self.listOfStates[1]
        else:
            print("Something went wrong mate :(")
        self.__endingMission__()


    def StartMission(self, chooseMission: int, parametr):
        if chooseMission == 0:
            self.wait(self.minimalTimeWaiting)
            self.BasicMisssionL()
        elif chooseMission == 1:
            self.wait(self.minimalTimeWaiting)
            self.SquareMissionL(parametr)



