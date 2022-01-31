import qrcode
from random import seed
from random import randint



listOfMissions = ["squareMissionT"]
seed(1)
for x in listOfMissions:
    
    value = randint(50, 51)
    data = x + " "+str(value)
    img = qrcode.make(data)
    img.save(data+".png")
