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
            start = False

        drone.watingForMission()



except KeyboardInterrupt:
    drone.EmergencyCall()








