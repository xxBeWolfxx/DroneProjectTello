# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tello import Tello
from TelloBird import TelloBird
import cv2
import time
import datetime




drone = TelloBird()
start = True

try:
    while start:
        if start == True:
            # drone.streamon()
            drone.takeoff()
            print(drone.get_battery())
            start = False
            drone.wait(3)
    # if drone.last_frame is not  None:
    #     data, bbox, straigt_qrcode = detector.detectAndDecode(drone.last_frame)
    #     if bbox is not None:
    #         print(data)



        for i in range(4):
            drone.cw(90)
            drone.wait(3)
            print(drone.get_speed())
        # temp = drone.get_log()
        # print(temp[-1].get_response())
        # if str(temp[-1].get_response()) == "b'ok'":
        #     print("Sztos")
        # drone.takeoff()
        # drone.wait(5)
        drone.land()




except KeyboardInterrupt:
    drone.EmergencyCall()


# drone.streamoff()

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     drone.streamoff()

