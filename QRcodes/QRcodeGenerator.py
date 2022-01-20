import qrcode
from random import seed
from random import randint


listOfMissions = ["basicMisssionL", "squareMissionL", "squareMissionT", "takeOffMission","test"]
seed(1)
for x in listOfMissions:
    
    value = randint(15, 70)
    data = x + " "+str(value)
    img = qrcode.make(data)
    img.save(data+".png")
