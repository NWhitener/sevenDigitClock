import board
import busio
import adafruit_pca9685
from time import sleep 
i2c = busio.I2C(board.SCL,board.SDA)

hat = adafruit_pca9685.PCA9685(i2c)

hat.frequency = 60 



from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16) 

kit.servo[11].angle = 0





sleep(1)


kit.servo[11].angle = 120 
sleep(1)

kit.servo[11].angle = 0



