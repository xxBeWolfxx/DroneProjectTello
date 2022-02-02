# TelloBird example
### CAUTION
To run drone smoothly after starting code, you need to wait until GUI with the camera view from drone show up. 
## Example run
### STEP 1
Prepare appropriate QR codes (you can uses [QRcodeGenerator](https://github.com/xxBeWolfxx/DroneProjectTello/blob/main/QRcodes/QRcodeGenerator.py))
### STEP 2 
Open terminal and run
```bash
python3 TelloBird.py
```
#### CAUTION
To run drone smoothly after starting code, you need to wait until GUI with the camera view from drone show up. 

### STEP 3 
Show QRcode to drone camera, correct command will be listed in terminal.
Some missions take longer, because of time lag input. It is neccesary to give drone time to stablizate itself. Lower time can couse some error like
```bash
Response: error'no valid imu'
```
### STEP 4
Wait until drone mission is ended and repeat steps 3-4

### EMERGENCY SHUT DOWN
If something wrong happend, you can use ctrl+C keyboard interrupt in terminal to stop drone motors. 
#### CAUTION
Be careful about surroundings. Emergency stop can make some damage (even destroy Dji Tello) if used in not properly adapted environment.
