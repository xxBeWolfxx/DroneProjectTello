from tello import Tello


class TelloBird(Tello):
    currentState = "landed"
    listOfStates = ["landed", "in-air","moving","turning","too-weak"]
    minimalTimeWaiting = 3.0



    def __init__(self):
        super().__init__()
        self.wait(self.minimalTimeWaiting)
        self.land()
        self.getData()
        if self.battery <= 10:
            print("Too low battery, recharge: ", self.battery)
            self.currentState = self.listOfStates[-1]
        



    def getData(self):
        self.battery = self.get_battery()
        """TODO: Add more settings"""

    def EmergencyCall(self):
        print("Spadamy w dol")
        self.emergency()
        self.streamoff()
        self.land()

    def BasicMisssionL(self) -> int:
        if self.currentState == "landed":
            self.takeoff()
            self.wait(self.minimalTimeWaiting)
            self.currentState = self.listOfStates[1]
            self.land()
            self.currentState = self.listOfStates[0]
            return 1
        else:
            print("I can't start a mission, I am flying")
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
            print("Something goes wrong mate :(")





