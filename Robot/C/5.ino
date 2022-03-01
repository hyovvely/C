#include <Servo.h>//후진

Servo h1;
Servo h2;
Servo h3;
Servo h4;
Servo h5;
Servo h6;
Servo h7;
Servo h8;
Servo h9;
Servo h10;
Servo h11;
Servo h12;

int servoPin1 = 12;//오 뒤
int servoPin2 = 3;//왼 뒤
int servoPin3 = 9;//오 앞
int servoPin4 = 6;//왼 앞
int servoPin5 = 11;//왼 앞 위
int servoPin6 = 2;//오 앞 위
int servoPin7 = 8;//왼 뒤 위
int servoPin8 = 5;//오 뒤 위
int servoPin9 = 13;//왼 앞 밑
int servoPin10 = 4;//오 앞 밑
int servoPin11 = 10;//왼 뒤 밑
int servoPin12 = 7;//오 뒤 밑
int angle1 = 0;
int angle2 = 0;


void setup() {
  h1.attach(servoPin1);
  h2.attach(servoPin2);
  h3.attach(servoPin3);
  h4.attach(servoPin4);
  h5.attach(servoPin5);
  h5.write(angle2);
  h6.attach(servoPin6);
  h6.write(angle2);
  h7.attach(servoPin7);
  h7.write(angle2);
  h8.attach(servoPin8);
  h8.write(angle2);
  h9.attach(servoPin9);
  h9.write(angle1);
  h10.attach(servoPin10);
  h10.write(angle2);
  h11.attach(servoPin11);
  h11.write(angle1);
  h12.attach(servoPin12);
  h12.write(angle2);


}

void loop() {

 h4.write(100);//앞
  h1.write(75);//뒤
  h2.write(125);//앞
  h3.write(50);//뒤
  delay(500);
  h4.write(125);//뒤
  h1.write(50);//앞
  h2.write(100);//뒤
  h3.write(75);//앞
  delay(500);
  
for(angle2 = 45; angle2 < 50; angle2++){//위에 고정하는 각도//6오뒤위2 7왼앞위8
  
    h7.write(angle2);
    h6.write(angle2);
 
    
  }
  for(angle2 = 50; angle2 > 45; angle2--){
    
    h7.write(angle2);
    h6.write(angle2);
    
    
  }
  for(angle1 = 20; angle1 < 25; angle1++){//왼뒤위11
    h5.write(angle1);
   
  }
  for(angle1 = 25; angle1 >20; angle1--){
    h5.write(angle1);
    
  }
 for(angle2 = 140; angle2 < 145; angle2++){//오앞위 5
    h8.write(angle2);
    
  }
  for(angle2 = 145; angle2 > 140; angle2--){
    h8.write(angle2);
    
  }
  for(angle1 = 170; angle1 < 180; angle1++){//밑에 네다리 고정//왼뒤밑13 왼앞밑 10
    h9.write(angle1);
    h11.write(angle1);
   
  }
  for(angle1 = 180; angle1 >170; angle1--){
    h9.write(angle1);
    h11.write(angle1);
    
  }
  for(angle2 = 10; angle2 < 40; angle2++){//오뒤밑4 오앞밑 7
    h10.write(angle2);
    h12.write(angle2);
   
  }
  for(angle2 = 40; angle2 > 10; angle2--){
    h10.write(angle2);
    h12.write(angle2);
    
  }
 

}
