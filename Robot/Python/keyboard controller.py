from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

import board
import busio
import time
import keyboard
import os



i2c_bus0=(busio.I2C(board.SCL_1, board.SDA_1))

pca_1 = PCA9685(i2c_bus0, address=0x40)
pca_2 = PCA9685(i2c_bus0, address=0x41)
pca_1.frequency = 60
pca_2.frequency = 60

#1
servo0 = servo.Servo(pca_1.channels[0], min_pulse=500, max_pulse=2500)
servo1 = servo.Servo(pca_1.channels[1], min_pulse=500, max_pulse=2500)
servo2 = servo.Servo(pca_1.channels[2], min_pulse=500, max_pulse=2500)
#27968
servo3 = servo.Servo(pca_1.channels[3], min_pulse=500, max_pulse=2500)
servo4 = servo.Servo(pca_1.channels[4], min_pulse=500, max_pulse=2500)
servo5 = servo.Servo(pca_1.channels[5], min_pulse=500, max_pulse=2500)
#3
servo6 = servo.Servo(pca_2.channels[6], min_pulse=500, max_pulse=2500)
servo7 = servo.Servo(pca_2.channels[7], min_pulse=500, max_pulse=2500)
servo8 = servo.Servo(pca_2.channels[8], min_pulse=500, max_pulse=2500)
#4
servo9 = servo.Servo(pca_2.channels[9], min_pulse=500, max_pulse=2500)
servo10 = servo.Servo(pca_2.channels[10], min_pulse=500, max_pulse=2500)
servo11 = servo.Servo(pca_2.channels[11], min_pulse=500, max_pulse=2500)

#front wheel
servo12 = servo.Servo(pca_1.channels[12], min_pulse=500, max_pulse=2500)
servo13 = servo.Servo(pca_1.channels[13], min_pulse=500, max_pulse=2500)

#back wheel
servo14 = servo.Servo(pca_2.channels[0], min_pulse=500, max_pulse=2500)
servo15 = servo.Servo(pca_2.channels[1], min_pulse=500, max_pulse=2500)

#servo_offsets =  [20, 20, 115, 70, 60, 105, 130, 20, 95, 70, 50, 20]
for degree in range(60): #10 back
    print(degree)
servo0.angle = int(degree)
for degree in range(155): #Backdown 10 up 0
         print(degree)
servo1.angle = int(degree)
for degree in range(88): #down 10 up 0
        print(degree)
servo2.angle = int(degree) 
for degree in range(120): # front 10
                                print(degree)
servo3.angle = int(degree)
for degree in range(20): # down 0 10up
                                print(degree)
servo4.angle = int(degree)
for degree in range(90): # down 0 10 up
                                print(degree)
servo5.angle = int(degree)
for degree in range(70):#10back
                                print(degree)
servo6.angle = int(degree)
for degree in range(170):#10back
                                print(degree)
servo7.angle = int(degree)
for degree in range(90): # up 10
                                print(degree)
servo8.angle = int(degree)
for degree in range(110):# 10 up
                                print(degree)
servo9.angle = int(degree)
for degree in range(10): # up 10 back 0
                                print(degree)
servo10.angle = int(degree)
for degree in range(95): #10dowun
                                print(degree)
servo11.angle = int(degree)
        

    # wheel
for degree in range(100):
        print(degree)
servo12.angle = int(degree)

for degree in range(100):
        print(degree)
servo13.angle = int(degree)

for degree in range(90):
        print(degree)
servo14.angle = int(degree)

for degree in range(90):
        print(degree)
servo15.angle = int(degree)


time.sleep(2)





while True:
        try:
                if keyboard.is_pressed('a'):
                        print("a*30") 
                       
                        for degree in range(100): # up 10
                                print(degree)
                        servo8.angle = int(degree)
                        for degree in range(60):#10back
                                print(degree)
                        servo6.angle = int(degree)



                        for degree in range(80): # down 0 10 up
                                print(degree)
                        servo5.angle = int(degree)
                        for degree in range(140): # front 10
                                print(degree)
                        servo3.angle = int(degree)  

                        time.sleep(0.08)

                        for degree in range(140):#10back
                                print(degree)
                        servo7.angle = int(degree)
                        for degree in range(50): # down 0 10up
                                print(degree)
                        servo4.angle = int(degree)

                        time.sleep(0.08)

                        for degree in range(90): # up 10
                                print(degree)
                        servo8.angle = int(degree)
                        for degree in range(90): # down 0 10 up
                                print(degree)
                        servo5.angle = int(degree)
    

                        time.sleep(0.08)

                        for degree in range(90):#10back
                                print(degree)
                        servo6.angle = int(degree)
                        for degree in range(110): # front 10
                                print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.08)

    


                        for degree in range(120): # front 10
                                print(degree)
                        servo3.angle = int(degree)
                        for degree in range(80):#10back
                                print(degree)
                        servo6.angle = int(degree)



                        time.sleep(0.08)
                        for degree in range(60): #10 back
                                print(degree)
                        servo0.angle = int(degree)
                        for degree in range(155): #Backdown 10 up 0
                                print(degree)
                        servo1.angle = int(degree)
                        for degree in range(88): #down 10 up 0
                                print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(120): # front 10
                                print(degree)
                        servo3.angle = int(degree)
                        for degree in range(20): # down 0 10up
                                print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # down 0 10 up
                                print(degree)
                        servo5.angle = int(degree)
                        for degree in range(80):#10back
                                print(degree)
                        servo6.angle = int(degree)
                        for degree in range(170):#10back
                                print(degree)
                        servo7.angle = int(degree)
                        for degree in range(90): # up 10
                                print(degree)
                        servo8.angle = int(degree)
                        for degree in range(100):# 10 up
                                print(degree)
                        servo9.angle = int(degree)
                        for degree in range(10): # up 10 back 0
                                print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #10dowun
                                print(degree)
                        servo11.angle = int(degree)
    
                        time.sleep(0.1)
                                                
                        


                elif keyboard.is_pressed('s'):
                        print("s")
                        for degree in range(85): #10dowun
                                print(degree)
                        servo11.angle = int(degree)
                        for degree in range(120):# 10 up
                                print(degree)
                        servo9.angle = int(degree)



                        for degree in range(98): #down 10 up 0
                            print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(40): #10 back
                            print(degree)
                        servo0.angle = int(degree)

                        time.sleep(0.08)

                        for degree in range(40): # up 10 back 0
                                print(degree)
                        servo10.angle = int(degree)
                        for degree in range(125): #Backdown 10 up 0
                             print(degree)
                        servo1.angle = int(degree)

                        time.sleep(0.08)

                        for degree in range(88): #down 10 up 0
                            print(degree)
                        servo2.angle = int(degree)
                        for degree in range(95): #10dowun
                                print(degree)
                        servo11.angle = int(degree) 


                        time.sleep(0.08)

                        for degree in range(90):# 10 up
                                print(degree)
                        servo9.angle = int(degree)
                        for degree in range(75): #10 back
                                print(degree)
                        servo0.angle = int(degree)
                        time.sleep(0.08)




                        for degree in range(100):# 10 up
                                print(degree)
                        servo9.angle = int(degree)
                        for degree in range(65): #10 back
                                print(degree)
                        servo0.angle = int(degree)



                        time.sleep(0.05)

                        for degree in range(65): #10 back
                            print(degree)
                        servo0.angle = int(degree)
                        for degree in range(155): #Backdown 10 up 0
                             print(degree)
                        servo1.angle = int(degree)
                        for degree in range(88): #down 10 up 0
                            print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(122): # front 10
                                print(degree)
                        servo3.angle = int(degree)
                        for degree in range(20): # down 0 10up
                                print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # down 0 10 up
                                print(degree)
                        servo5.angle = int(degree)
                        for degree in range(80):#10back
                                print(degree)
                        servo6.angle = int(degree)
                        for degree in range(170):#10back
                                print(degree)
                        servo7.angle = int(degree)
                        for degree in range(90): # up 10
                                print(degree)
                        servo8.angle = int(degree)
                        for degree in range(100):# 10 up
                                print(degree)
                        servo9.angle = int(degree)
                        for degree in range(10): # up 10 back 0
                                print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #10dowun
                                print(degree)
                        servo11.angle = int(degree)

                        time.sleep(0.08)
                
                elif keyboard.is_pressed('t'):
                        print("t")
                        for degree in range(95): #10 back
                                print(degree)
                        servo0.angle = int(degree)
                        for degree in range(130): #Backdown 10 up 0
                                print(degree)
                        servo1.angle = int(degree)
                        for degree in range(90): #down 10 up 0
                                print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(90): # front 10
                                print(degree)
                        servo3.angle = int(degree)
                        for degree in range(40): # down 0 10up
                                print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # down 0 10 up
                                print(degree)
                        servo5.angle = int(degree)
                        for degree in range(95):#10back
                                print(degree)
                        servo6.angle = int(degree)
                        for degree in range(150):#10back
                                print(degree)
                        servo7.angle = int(degree)
                        for degree in range(90): # up 10
                                print(degree)
                        servo8.angle = int(degree)
                        for degree in range(82):# 10 up
                                print(degree)
                        servo9.angle = int(degree)
                        for degree in range(20): # up 10 back 0
                                print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #10dowun
                                print(degree)
                        servo11.angle = int(degree)
    # wheel
                        for degree in range(100):
                            print(degree)
                        servo12.angle = int(degree)

                        for degree in range(100):
                            print(degree)
                        servo13.angle = int(degree)

                        for degree in range(90):
                            print(degree)
                        servo14.angle = int(degree)

                        for degree in range(90):
                            print(degree)
                        servo15.angle = int(degree)


                        time.sleep(2)
                        for degree in range(60): #10 back
                                    print(degree)
                        servo0.angle = int(degree)
                        for degree in range(155): #Backdown 10 up 0
                             print(degree)
                        servo1.angle = int(degree)
                        for degree in range(88):#down 10 up 0
                            print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(130): # front 10
                                print(degree)
                        servo3.angle = int(degree)
                        for degree in range(20): # down 0 10up
                                print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # down 0 10 up
                                print(degree)
                        servo5.angle = int(degree)
                        for degree in range(60):#10back
                                print(degree)
                        servo6.angle = int(degree)
                        for degree in range(160):#10back
                                print(degree)
                        servo7.angle = int(degree)
                        for degree in range(90): # up 10
                                print(degree)
                        servo8.angle = int(degree)
                        for degree in range(110):# 10 up
                                print(degree)
                        servo9.angle = int(degree)
                        for degree in range(10): # up 10 back 0
                                print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #10dowun
                                print(degree)
                        servo11.angle = int(degree)                
        

  
                        time.sleep(2)

                elif keyboard.is_pressed('d'):
                        print("d")
                        for degree in range(60): #10 back
                            print(degree)
                        servo0.angle = int(degree)
                        for degree in range(155): #Backdown 10 up 0
                                 print(degree)
                        servo1.angle = int(degree)
                        for degree in range(88): #down 10 up 0
                                print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(130): # front 10
                                    print(degree)
                        servo3.angle = int(degree)
                        for degree in range(20): # down 0 10up
                                    print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # down 0 10 up
                                    print(degree)
                        servo5.angle = int(degree)
                        for degree in range(60):#10back
                                    print(degree)
                        servo6.angle = int(degree)
                        for degree in range(160):#10back
                                    print(degree)
                        servo7.angle = int(degree)
                        for degree in range(90): # up 10
                                    print(degree)
                        servo8.angle = int(degree)
                        for degree in range(110):# 10 up
                                    print(degree)
                        servo9.angle = int(degree)
                        for degree in range(10): # up 10 back 0
                                    print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #10dowun
                                    print(degree)
                        servo11.angle = int(degree)


                            # wheel
                        for degree in range(100):
                                print(degree)
                        servo12.angle = int(degree)                     

                        for degree in range(100):
                                print(degree)
                        servo13.angle = int(degree)                     

                        for degree in range(90):
                                print(degree)
                        servo14.angle = int(degree)                     

                        for degree in range(90):
                                print(degree)
                        servo15.angle = int(degree)                     


                        time.sleep(2)                   

                        for degree in range(60): #10 back
                                print(degree)
                        servo0.angle = int(degree)
                        for degree in range(155): #Backdown 10 up 0
                                print(degree)
                        servo1.angle = int(degree)
                        for degree in range(88): #down 10 up 0
                                print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(130): # front 10
                                print(degree)
                        servo3.angle = int(degree)
                        for degree in range(20): # down 0 10up
                                print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # down 0 10 up
                                print(degree)
                        servo5.angle = int(degree)
                        for degree in range(30):#10back
                                print(degree)
                        servo6.angle = int(degree)
                        for degree in range(160):#10back
                                print(degree)
                        servo7.angle = int(degree)
                        for degree in range(90): # up 10
                                print(degree)
                        servo8.angle = int(degree)
                        for degree in range(140):# 10 up
                                print(degree)
                        servo9.angle = int(degree)
                        for degree in range(10): # up 10 back 0
                                print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #10dowun
                                print(degree)
                        servo11.angle = int(degree)
                        time.sleep(1)                   

                        for degree in range(150): # down 0 10up
                                print(degree)
                        servo4.angle = int(degree)
                        time.sleep(1)                   
                        for degree in range(130): # front 10
                                print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                                print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5) 
                        for degree in range(130): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(100): # front 10
                            print(degree)
                        servo3.angle = int(degree)
                        time.sleep(0.5)                                         
                         

                elif keyboard.is_pressed('e'):
                        print("e")
                        for degree in range(60): #10 back
                            print(degree)
                        servo0.angle = int(degree)
                        for degree in range(155): #Backdown 10 up 0
                                 print(degree)
                        servo1.angle = int(degree)
                        for degree in range(88): #down 10 up 0
                                print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(130): # front 10
                                    print(degree)
                        servo3.angle = int(degree)
                        for degree in range(20): # down 0 10up
                                    print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # down 0 10 up
                                    print(degree)
                        servo5.angle = int(degree)
                        for degree in range(60):#10back
                                    print(degree)
                        servo6.angle = int(degree)
                        for degree in range(160):#10back
                                    print(degree)
                        servo7.angle = int(degree)
                        for degree in range(90): # up 10
                                    print(degree)
                        servo8.angle = int(degree)
                        for degree in range(110):# 10 up
                                    print(degree)
                        servo9.angle = int(degree)
                        for degree in range(10): # up 10 back 0
                                    print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #10dowun
                                    print(degree)
                        servo11.angle = int(degree)


                            # wheel
                        for degree in range(100):
                                print(degree)
                        servo12.angle = int(degree)                     

                        for degree in range(100):
                                print(degree)
                        servo13.angle = int(degree)                     

                        for degree in range(90):
                                print(degree)
                        servo14.angle = int(degree)                     

                        for degree in range(90):
                                print(degree)
                        servo15.angle = int(degree) 
                elif keyboard.is_pressed('f'):
                        print("f")
                        for degree in range(128,48,-1): #down 10 up 0
                                print(degree)
                        servo2.angle = int(degree)
                        for degree in range(50,130,+1): # up 10
                            print(degree)
                        servo8.angle = int(degree)

                        for degree in range(130,50,-1): # down 0 10 up
                            print(degree)
                        servo5.angle = int(degree)

                        for degree in range(55,135,+1): #10dowun
                            print(degree)
                        servo11.angle = int(degree)
                        time.sleep(0.5)
                        for degree in range(48,128,+1): #down 10 up 0
                                print(degree)
                        servo2.angle = int(degree)
                        for degree in range(130,50,-1): # up 10
                            print(degree)
                        servo8.angle = int(degree)

                        for degree in range(50,130,+1): # down 0 10 up
                            print(degree)
                        servo5.angle = int(degree)

                        for degree in range(135,55,-1): #10dowun
                            print(degree)
                        servo11.angle = int(degree)
                        time.sleep(0.5)                                                                   
                elif keyboard.is_pressed('i'):
                        print("i")
                        for degree in range(50): #1
                            print(degree)
                        servo0.angle = int(degree)
                        for degree in range(130): #
                            print(degree)
                        servo1.angle = int(degree)
                        for degree in range(90): #d
                            print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(130): #
                            print(degree)
                        servo3.angle = int(degree)
                        for degree in range(50): # 
                            print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # 
                            print(degree)
                        servo5.angle = int(degree)
                        for degree in range(50):#10
                            print(degree)
                        servo6.angle = int(degree)
                        for degree in range(140):#1
                            print(degree)
                        servo7.angle = int(degree)
                        for degree in range(100): # 
                            print(degree)
                        servo8.angle = int(degree)
                        for degree in range(130):# 
                            print(degree)
                        servo9.angle = int(degree)
                        for degree in range(40): # 
                            print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #1
                            print(degree)
                        servo11.angle = int(degree)
                        for degree in range(179):
                            print(degree)
                        servo12.angle = int(degree)
                        for degree in range(1):
                            print(degree)
                        servo13.angle = int(degree)
                        for degree in range(179):
                            print(degree)
                        servo14.angle = int(degree)
                        for degree in range(1):
                            print(degree)
                        servo15.angle = int(degree)
                elif keyboard.is_pressed('j'):
                        print("j")
                        for degree in range(50): #1
                            print(degree)
                        servo0.angle = int(degree)
                        for degree in range(130): #
                            print(degree)
                        servo1.angle = int(degree)
                        for degree in range(90): #d
                            print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(130): #
                            print(degree)
                        servo3.angle = int(degree)
                        for degree in range(50): # 
                            print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # 
                            print(degree)
                        servo5.angle = int(degree)
                        for degree in range(50):#10
                            print(degree)
                        servo6.angle = int(degree)
                        for degree in range(140):#1
                            print(degree)
                        servo7.angle = int(degree)
                        for degree in range(100): # 
                            print(degree)
                        servo8.angle = int(degree)
                        for degree in range(130):# 
                            print(degree)
                        servo9.angle = int(degree)
                        for degree in range(40): # 
                            print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #1
                            print(degree)
                        servo11.angle = int(degree)
                        for degree in range(100):
                            print(degree)
                        servo12.angle = int(degree)
                        for degree in range(1):
                            print(degree)
                        servo13.angle = int(degree)
                        for degree in range(179):
                            print(degree)
                        servo14.angle = int(degree)
                        for degree in range(1):
                            print(degree)
                        servo15.angle = int(degree)
                elif keyboard.is_pressed('l'):
                        print("l")
                        for degree in range(50): #1
                            print(degree)
                        servo0.angle = int(degree)
                        for degree in range(130): #
                            print(degree)
                        servo1.angle = int(degree)
                        for degree in range(90): #d
                            print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(130): #
                            print(degree)
                        servo3.angle = int(degree)
                        for degree in range(50): # 
                            print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # 
                            print(degree)
                        servo5.angle = int(degree)
                        for degree in range(50):#10
                            print(degree)
                        servo6.angle = int(degree)
                        for degree in range(140):#1
                            print(degree)
                        servo7.angle = int(degree)
                        for degree in range(100): # 
                            print(degree)
                        servo8.angle = int(degree)
                        for degree in range(130):# 
                            print(degree)
                        servo9.angle = int(degree)
                        for degree in range(40): # 
                            print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #1
                            print(degree)
                        servo11.angle = int(degree)
                        for degree in range(179):
                            print(degree)
                        servo12.angle = int(degree)
                        for degree in range(100):
                            print(degree)
                        servo13.angle = int(degree)
                        for degree in range(179):
                            print(degree)
                        servo14.angle = int(degree)
                        for degree in range(1):
                            print(degree)
                        servo15.angle = int(degree)

                elif keyboard.is_pressed('k'):
                        print("k")
                        for degree in range(50): #1
                            print(degree)
                        servo0.angle = int(degree)
                        for degree in range(130): #
                            print(degree)
                        servo1.angle = int(degree)
                        for degree in range(90): #d
                            print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(130): #
                            print(degree)
                        servo3.angle = int(degree)
                        for degree in range(50): # 
                            print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # 
                            print(degree)
                        servo5.angle = int(degree)
                        for degree in range(50):#10
                            print(degree)
                        servo6.angle = int(degree)
                        for degree in range(140):#1
                            print(degree)
                        servo7.angle = int(degree)
                        for degree in range(100): # 
                            print(degree)
                        servo8.angle = int(degree)
                        for degree in range(130):# 
                            print(degree)
                        servo9.angle = int(degree)
                        for degree in range(40): # 
                            print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #1
                            print(degree)
                        servo11.angle = int(degree)
                        for degree in range(1):
                            print(degree)
                        servo12.angle = int(degree)
                        for degree in range(179):
                            print(degree)
                        servo13.angle = int(degree)
                        for degree in range(1):
                            print(degree)
                        servo14.angle = int(degree)
                        for degree in range(179):
                            print(degree)
                        servo15.angle = int(degree)
                elif keyboard.is_pressed('p'):
                        print("p")
                        for degree in range(50): #1
                            print(degree)
                        servo0.angle = int(degree)
                        for degree in range(130): #
                            print(degree)
                        servo1.angle = int(degree)
                        for degree in range(90): #d
                            print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(130): #
                            print(degree)
                        servo3.angle = int(degree)
                        for degree in range(50): # 
                            print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # 
                            print(degree)
                        servo5.angle = int(degree)
                        for degree in range(50):#10
                            print(degree)
                        servo6.angle = int(degree)
                        for degree in range(140):#1
                            print(degree)
                        servo7.angle = int(degree)
                        for degree in range(100): # 
                            print(degree)
                        servo8.angle = int(degree)
                        for degree in range(130):# 
                            print(degree)
                        servo9.angle = int(degree)
                        for degree in range(40): # 
                            print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #1
                            print(degree)
                        servo11.angle = int(degree)
                        for degree in range(100):
                            print(degree)
                        servo12.angle = int(degree)
                        for degree in range(100):
                            print(degree)
                        servo13.angle = int(degree)
                        for degree in range(90):
                            print(degree)
                        servo14.angle = int(degree)
                        for degree in range(90):
                            print(degree)
                        servo15.angle = int(degree)            
                elif keyboard.is_pressed('g'):
                        print("g")
                        for degree in range(50): #10 back
                            print(degree)
                        servo0.angle = int(degree)
                        for degree in range(170): #Backdown 10 up 0
                                print(degree)
                        servo1.angle = int(degree)
                        for degree in range(90): #down 10 up 0
                                print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(130): # front 10
                                print(degree)
                        servo3.angle = int(degree)
                        for degree in range(10): # down 0 10up
                                print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # down 0 10 up
                                print(degree)
                        servo5.angle = int(degree)
                        for degree in range(50):#10back
                                print(degree)
                        servo6.angle = int(degree)
                        for degree in range(170):#10back
                                print(degree)
                        servo7.angle = int(degree)
                        for degree in range(90): # up 10
                                print(degree)
                        servo8.angle = int(degree)
                        for degree in range(130):# 10 up
                                print(degree)
                        servo9.angle = int(degree)
                        for degree in range(10): # up 10 back 0
                                print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #10dowun
                                print(degree)
                        servo11.angle = int(degree)


                        time.sleep(2)
                        for degree in range(60): #10 back
                                print(degree)
                        servo0.angle = int(degree)
                        for degree in range(155): #Backdown 10 up 0
                                print(degree)
                        servo1.angle = int(degree)
                        for degree in range(88): #down 10 up 0
                                print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(120): # front 10
                                print(degree)
                        servo3.angle = int(degree)
                        for degree in range(20): # down 0 10up
                                print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # down 0 10 up
                                print(degree)
                        servo5.angle = int(degree)
                        for degree in range(70):#10back
                                print(degree)
                        servo6.angle = int(degree)
                        for degree in range(170):#10back
                                print(degree)
                        servo7.angle = int(degree)
                        for degree in range(90): # up 10
                                print(degree)
                        servo8.angle = int(degree)
                        for degree in range(110):# 10 up
                                print(degree)
                        servo9.angle = int(degree)
                        for degree in range(10): # up 10 back 0
                                print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #10dowun
                                print(degree)
                        servo11.angle = int(degree)
                                                    

                        time.sleep(2)                                       
    
                elif keyboard.is_pressed('h'):
                        print("h")
                        for degree in range(169): #10 back
                                print(degree)
                        servo0.angle = int(degree)
                        for degree in range(11): #Backdown 10 up 0
                                print(degree)
                        servo1.angle = int(degree)
                        for degree in range(90): #down 10 up 0
                                print(degree)
                        servo2.angle = int(degree) 
                        for degree in range(11): # front 10
                                print(degree)
                        servo3.angle = int(degree)
                        for degree in range(169): # down 0 10up
                                print(degree)
                        servo4.angle = int(degree)
                        for degree in range(90): # down 0 10 up
                                print(degree)
                        servo5.angle = int(degree)
                        for degree in range(169):#10back
                                print(degree)
                        servo6.angle = int(degree)
                        for degree in range(169):#10back
                                print(degree)
                        servo7.angle = int(degree)
                        for degree in range(90): # up 10
                                print(degree)
                        servo8.angle = int(degree)
                        for degree in range(11):# 10 up
                                print(degree)
                        servo9.angle = int(degree)
                        for degree in range(11): # up 10 back 0
                                print(degree)
                        servo10.angle = int(degree)
                        for degree in range(95): #10dowun
                                print(degree)
                        servo11.angle = int(degree)


                        time.sleep(2)                       
                     

                        for degree in range(179):
                            print(degree)
                        servo12.angle = int(degree)                 

                        for degree in range(1):
                            print(degree)
                        servo13.angle = int(degree)                 

                        for degree in range(179):
                            print(degree)
                        servo14.angle = int(degree)                 

                        for degree in range(1):
                            print(degree)
                        servo15.angle = int(degree)

                     

                        time.sleep(5)      
                elif keyboard.is_pressed('n'):
                        print("n")  
                        for degree in range(100):
                                print(degree)
                        servo12.angle = int(degree)

                        for degree in range(100):
                                print(degree)
                        servo13.angle = int(degree)

                        for degree in range(90):
                                print(degree)
                        servo14.angle = int(degree)

                        for degree in range(90):
                                print(degree)
                        servo15.angle = int(degree)


                        time.sleep(2) 
                elif keyboard.is_pressed('m'):
                        print("m")         
                        for degree in range(1):
                                print(degree)
                        servo12.angle = int(degree)

                        for degree in range(179):
                                print(degree)
                        servo13.angle = int(degree)

                        for degree in range(1):
                                print(degree)
                        servo14.angle = int(degree)

                        for degree in range(179):
                                print(degree)
                        servo15.angle = int(degree)
    
                        time.sleep(5)                            



                else:
                        pass
        except:
                        pass