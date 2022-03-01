from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

import board
import busio
import time

i2c_bus0=(busio.I2C(board.SCL_1, board.SDA_1))

pca_1 = PCA9685(i2c_bus0, address=0x40)
pca_2 = PCA9685(i2c_bus0, address=0x41)
pca_1.frequency = 60
pca_2.frequency = 60

#1
servo0 = servo.Servo(pca_1.channels[0], min_pulse=770, max_pulse=2800)
servo1 = servo.Servo(pca_1.channels[1], min_pulse=770, max_pulse=2800)
servo2 = servo.Servo(pca_1.channels[2], min_pulse=770, max_pulse=2800)
#27968
servo3 = servo.Servo(pca_1.channels[3], min_pulse=770, max_pulse=2800)
servo4 = servo.Servo(pca_1.channels[4], min_pulse=770, max_pulse=2800)
servo5 = servo.Servo(pca_1.channels[5], min_pulse=770, max_pulse=2800)
#3
servo6 = servo.Servo(pca_2.channels[6], min_pulse=770, max_pulse=2800)
servo7 = servo.Servo(pca_2.channels[7], min_pulse=770, max_pulse=2800)
servo8 = servo.Servo(pca_2.channels[8], min_pulse=770, max_pulse=2800)
#4
servo9 = servo.Servo(pca_2.channels[9], min_pulse=770, max_pulse=2800)
servo10 = servo.Servo(pca_2.channels[10], min_pulse=770, max_pulse=2800)
servo11 = servo.Servo(pca_2.channels[11], min_pulse=770, max_pulse=2800)

#front wheel
servo12 = servo.Servo(pca_1.channels[12], min_pulse=500, max_pulse=2500)
servo13 = servo.Servo(pca_1.channels[13], min_pulse=500, max_pulse=2500)

#back wheel
servo14 = servo.Servo(pca_2.channels[0], min_pulse=500, max_pulse=2500)
servo15 = servo.Servo(pca_2.channels[1], min_pulse=500, max_pulse=2500)

#servo_offsets =  [150, 160, 115, 70, 60, 105, 130, 160, 95, 70, 50, 90]



while True:
    
   
    
    
   
    
    
    for degree in range(90): #180 back
        print(degree)
    servo0.angle = int(degree)
    for degree in range(90): #Backdown 180 up 0
        print(degree)
    servo1.angle = int(degree)
    for degree in range(90): #down 180 up 0
        print(degree)
    servo2.angle = int(degree) 
    for degree in range(90): # front 180
        print(degree)
    servo3.angle = int(degree)
    for degree in range(90): # down 0 180up
        print(degree)
    servo4.angle = int(degree)
    for degree in range(90): # down 0 180 up
        print(degree)
    servo5.angle = int(degree)
    for degree in range(90):#180back
        print(degree)
    servo6.angle = int(degree)
    for degree in range(90):#180back
        print(degree)
    servo7.angle = int(degree)
    for degree in range(90): # up 180
        print(degree)
    servo8.angle = int(degree)
    for degree in range(90):# 180 up
        print(degree)
    servo9.angle = int(degree)
    for degree in range(90): # up 180 back 0
        print(degree)
    servo10.angle = int(degree)
    for degree in range(90): #180dowun
        print(degree)
    servo11.angle = int(degree)
    


    time.sleep(4)


    #6
    '''
    for degree in range(90): # down 0
        print(degree)
    servo11.angle = int(degree)
    for degree in range(40): # down 0  
        print(degree)
    servo5.angle = int(degree)
    for degree in range(40): #down 180 up 0
        print(degree)
    servo2.angle = int(degree)
    time.sleep(3)
    '''



    '''
    for degree in range(80): # up 0
        print(degree)
    servo11.angle = int(degree)


    for degree in range(90): # down 0
        print(degree)
    servo8.angle = int(degree)
    
    for degree in range(50): #down 180 up 0
        print(degree)
    servo2.angle = int(degree)
    for degree in range(65): #+20
        print(degree)
    servo0.angle = int(degree)
    
    for degree in range(110): #down 180 up 0
        print(degree)
    servo1.angle = int(degree)

    '''
    time.sleep(0.3) 

