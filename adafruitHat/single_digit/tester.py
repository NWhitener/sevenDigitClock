
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


activateServo(15, True)

activateServo(14, True)

activateServo(13, False) 

activateServo(12, False) 

activateServo(11, False) 

activateServo(10, False) 

activateServo(9, False) 



sleep(1)



activateServo(15, True)

activateServo(14, True)

activateServo(13, True)


activateServo(12, False)

activateServo(11, False)

activateServo(10, False)

activateServo(9, True)


 
