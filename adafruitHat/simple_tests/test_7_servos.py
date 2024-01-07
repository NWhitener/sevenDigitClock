import board
import busio
import adafruit_pca9685
from time import sleep
i2c = busio.I2C(board.SCL,board.SDA)

hat = adafruit_pca9685.PCA9685(i2c)

hat.frequency = 60



from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)


#Testing all seven servos at once 

kit.servo[15].angle = 120

kit.servo[14].angle = 120

kit.servo[13].angle = 120 

kit.servo[12].angle = 120 

kit.servo[11].angle = 120 

kit.servo[10].angle = 120 

kit.servo[9].angle = 120 

sleep(1)



kit.servo[15].angle = 0

kit.servo[14].angle = 0

kit.servo[13].angle = 0

kit.servo[12].angle = 0

kit.servo[11].angle = 0

kit.servo[10].angle = 0

kit.servo[9].angle = 0



