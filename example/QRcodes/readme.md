# TelloBird QRcodeReader example
### CAUTION
To run the drone smoothly after starting the code, you need to wait until GUI with the camera view from the drone showed up. Everything is executed by the computer not a drone. 
## Example run
### STEP 1
Prepare appropriate QR codes (you can uses [QRcodeGenerator](https://github.com/xxBeWolfxx/DroneProjectTello/blob/main/QRcodes/QRcodeGenerator.py)). In this script, you have to define missions with parameters if they are required of course. As default parameters are set:
```python
listOfMissions = ["basicMisssionL", "squareMissionL"]
seed(1)
for x in listOfMissions:
    value = randint(15, 70)
    data = x + " "+str(value)
    img = qrcode.make(data)
    img.save(data+".png")
```
The script makes two QR codes with random values of parameters, which are chosen between 15 and 70. Then QR codes are saved as PNG files.
### STEP 2 
Open terminal and run
```bash
python3 TelloBird.py
```
> __CAUTION__
> To run the drone smoothly after starting the code, you need to wait until GUI with the camera view from the drone showed up.

### STEP 3 
Show QR code to drone's camera, the correct command will be listed in the terminal.
Some missions take longer, because of time lag input. It is necessary to give the drone time to stabilize itself. Lower time can cause some errors like:
```bash
Response: error'no valid imu'
```
### STEP 4
Wait until the drone mission is ended and repeat steps 3-4.
***
## EMERGENCY SHUT DOWN
If something wrong happened, you can use the ctrl+C keyboard interrupt in the terminal to stop drone motors. 
#### CAUTION
Be careful about your surroundings. Emergency stops can make some damage (even destroy Dji Tello) if used in not properly adapted environment.

