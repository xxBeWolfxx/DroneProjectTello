from TelloBird import TelloBird
import cv2

drone = TelloBird()
start = True


try:
    while start:
        if start == True:
            drone.streamon()
            start = False



        drone.squareMissionL(30)


except KeyboardInterrupt:
    drone.EmergencyCall()








