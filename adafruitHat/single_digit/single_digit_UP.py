#Imports and set up 
import board
import busio
import adafruit_pca9685
from time import sleep 
i2c = busio.I2C(board.SCL,board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)
hat.frequency = 60 
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16) 

#Mapping of servos to position on board

servo1 = 15
servo2 = 14 
servo3 = 13
servo4 = 12
servo5 = 11 
servo6 = 10 
servo7 = 9


#Def to set servo to on or off 
def activateServo(servo_number, on):
    if on: 
        kit.servo[servo_number].angle = 120 
    else :  
        kit.servo[servo_number].angle = 0 



def reset():
    activateServo(servo1, False)
    activateServo(servo2, False)
    activateServo(servo3, False)
    activateServo(servo4, False)
    activateServo(servo5, False)
    activateServo(servo6, False)
    activateServo(servo7, False)
 
#def for digit of 1 
def one(): 
    print(servo1)
    print(servo2)
    activateServo(servo1, True) 
    activateServo(servo2, True) 
    activateServo(servo3, False)
    activateServo(servo4, False)
    activateServo(servo5, False)
    activateServo(servo6, False)
    activateServo(servo7, False)

def two(): 
    activateServo(servo1, False)
    activateServo(servo2, True)
    activateServo(servo3, True) 
    activateServo(servo4, False)
    activateServo(servo5, True) 
    activateServo(servo6, True) 
    activateServo(servo7, True) 

def three(): 
    activateServo(servo1, True) 
    activateServo(servo2,True) 
    activateServo(servo3, True) 
    activateServo(servo4, False) 
    activateServo(servo5, False) 
    activateServo(servo6, True) 
    activateServo(servo7, True) 

def four(): 
    activateServo(servo1, True) 
    activateServo(servo2, True) 
    activateServo(servo3, False) 
    activateServo(servo4, True) 
    activateServo(servo5, False) 
    activateServo(servo6, False) 
    activateServo(servo7, True) 

def five(): 
    activateServo(servo1, True) 
    activateServo(servo2, False) 
    activateServo(servo3, True) 
    activateServo(servo4, True) 
    activateServo(servo5, False) 
    activateServo(servo6, True)
    activateServo(servo7, True)

def six(): 
    activateServo(servo1, True) 
    activateServo(servo2, False) 
    activateServo(servo3, True) 
    activateServo(servo4, True) 
    activateServo(servo5, True) 
    activateServo(servo6, True) 
    activateServo(servo7, True) 

def seven(): 
    activateServo(servo1, True) 
    activateServo(servo2, True) 
    activateServo(servo3, True) 
    activateServo(servo4, False) 
    activateServo(servo5, False) 
    activateServo(servo6, False) 
    activateServo(servo7, False) 

def eight(): 
    activateServo(servo1, True) 
    activateServo(servo2, True)
    activateServo(servo3, True)
    activateServo(servo4, True)
    activateServo(servo5, True)
    activateServo(servo6, True)
    activateServo(servo7, True)

def nine(): 
    activateServo(servo1, True)
    activateServo(servo2, True)
    activateServo(servo3, True)
    activateServo(servo4, True) 
    activateServo(servo5, False)
    activateServo(servo6, False)
    activateServo(servo7, True)

def zero(): 
    activateServo(servo1, True)
    activateServo(servo2, True)
    activateServo(servo3, True)
    activateServo(servo4, True)
    activateServo(servo5, True)
    activateServo(servo6, True)
    activateServo(servo7, False)    


def main(): 
    reset()
    one()
    sleep(1)
    two()
    sleep(1)
    three()
    sleep(1)
    reset()
if __name__=="__main__": 
    main()
