# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tello import Tello
import cv2

drone = Tello()
detector = cv2.QRCodeDetector()
start = True
while True:
    if start == True:
        drone.streamon()
        start = False
    if drone.last_frame is not None:        
        data, bbox, straigt_qrcode = detector.detectAndDecode(drone.last_frame) 
        if bbox is not None:
            print(data)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.streamoff()
