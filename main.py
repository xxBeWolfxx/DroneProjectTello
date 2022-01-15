# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from TelloBird import TelloBird
import cv2
import time
import datetime

drone = TelloBird()

start = True
bbox = None

try:
    while True:
        if start == True:
            drone.streamon()
            # drone.takeoff()
            # print(drone.get_battery())
            start = False


        drone.WatingForMission()






except KeyboardInterrupt:
    # drone.EmergencyCall()
    drone.streamoff()




