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
#servo_offsets =  [150, 160, 115, 70, 60, 105, 130, 160, 95, 70, 50, 90]



while True:
    
    for degree in range(160): #down 180 up 0
        print(degree)
    servo1.angle = int(degree)
    
    for degree in range(1): # down 0
        print(degree)
    servo4.angle = int(degree)
   
    for degree in range(150):
        print(degree)
   
    servo7.angle = int(degree)
    
    for degree in range(10): # up 180
        print(degree)
    servo10.angle = int(degree)
    
    
    
    for degree in range(60): #down 180 up 0
        print(degree)
    servo2.angle = int(degree)
    
    for degree in range(70): # down 0
        print(degree)
    servo5.angle = int(degree)
    for degree in range(60):
        print(degree)
   
    servo11.angle = int(degree)
    
    for degree in range(70): # up 180
        print(degree)
    servo8.angle = int(degree)
    


    for degree in range(20):
        print(degree)
    servo0.angle = int(degree)
    
    for degree in range(120): # front 180
        print(degree)
    servo3.angle = int(degree)
    
    for degree in range(30):
        print(degree)
    servo6.angle = int(degree)
    
    for degree in range(110):
        print(degree)
    servo9.angle = int(degree)
 

    
    '''
    for degree in range(80):
        print(degree)
    servo0.angle = int(degree)
    for degree in range(90):
        print(degree)
    servo6.angle = int(degree)
    
    for degree in range(50):
        print(degree)
    servo9.angle = int(degree)
    for degree in range(60): # front 180
        print(degree)
    servo3.angle = int(degree)
    '''
    
    '''
    time.sleep(1)
    for degree in range(90,135, +1): #180 back  ffff 140
        print(degree)
        servo1.angle = int(degree)
    for degree in range(80): #180 back  ffff 140
        print(degree)
        servo0.angle = int(degree)
    time.sleep(1)    
    for degree in range(135,105, -1): #180 back  ffff 140
        print(degree)
        servo1.angle = int(degree)
    for degree in range(90): #180 back  ffff 140
        print(degree)
        servo0.angle = int(degree)
    time.sleep(1)
    for degree in range(105,90, -1): #180 back  ffff 140
        print(degree)
        servo1.angle = int(degree)
    for degree in range(60): #180 back  ffff 140
        print(degree)
        servo0.angle = int(degree)
    '''
    
    '''
    for degree in range(120,80, -1): #180 back  ffff 140
        print(degree)
        servo0.angle = int(degree)
    
    time.sleep(0.5)
    for degree in range(135,45, -1): #180 back  ffff 140
        print(degree)
        servo1.angle = int(degree)
    
    for degree in range(80,120, +1): #180 back  ffff 140
        print(degree)
        servo0.angle = int(degree)
    '''
    
    
    
    
    
    '''
    for degree in range(120,150, +1): #180 back  ffff
      for degree1 in range(40,10,-1):     #0 back
        print(degree)
        print(degree1)
    servo1.angle = int(degree)
    servo10.angle = int(degree1)
    
    time.sleep(1)
    
    for degree in range(150,120, -1) :
      for degree1 in range(10,40,+1):
        print(degree)
        print(degree1)
    servo1.angle = int(degree)
    servo10.angle = int(degree1)
    
    time.sleep(1)
    
    for degree in range(0,30, +1): #0 back
        for degree1 in range(130,100, -1):
          print(degree)
          print(degree1)
    servo4.angle = int(degree)
    servo7.angle = int(degree1)

   
    time.sleep(1)  

    for degree in range(30,0, -1):
        for degree1 in range(100,130, +1):
          print(degree)
          print(degree1)
    servo4.angle = int(degree)
    servo7.angle = int(degree1)

    time.sleep(1)
    '''




