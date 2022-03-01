#include <Servo.h>//걷기

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

int servoPin1 = 12;//오른쪽 뒤 윗다리 앞으로180 뒤로 0
int servoPin2 = 3;//왼쪽 뒤 윗다리 앞으로 0 뒤로 180
int servoPin3 = 9;//오른쪽 앞 윗다리 앞으로 180 뒤로 0
int servoPin4 = 6;//왼쪽 앞  윗다리 앞으로 0 뒤로 180
int servoPin5 = 11;//오른쪽 뒤 어깨 안쪽으로 180 밖으로 0 밖으로
int servoPin6 = 2;//왼쪽 뒤 어깨 안쪽으로 0 밖으로 180 밖으로
int servoPin7 = 8;//오른쪽 앞 어깨 안쪽으로 0 밖으로 180 밖으로
int servoPin8 = 5;//왼쪽 앞 어깨 안쪽으로 180 밖으로 0 밖으로
int servoPin9 = 13;//오른쪽 뒤 밑다리 뒤로 0 앞으로 180 앞으로
int servoPin10 = 4;//왼쪽 뒤 밑다리 뒤로 180 앞으로 0 앞으로
int servoPin11 = 10;//오른쪽 앞 밑다리 뒤로 0 앞으로 180 앞으로
int servoPin12 = 7;//왼쪽 앞 밑다리 뒤로 180 앞으로 0 앞으로




void setup() {
 
  h1.attach(servoPin1);//서보모터 12개 핀 설정
  h2.attach(servoPin2);//1,2,3,4 윗다리
  h3.attach(servoPin3);
  h4.attach(servoPin4);
  h5.attach(servoPin5);//5,6,7,8 어깨
  h6.attach(servoPin6);
  h7.attach(servoPin7);
  h8.attach(servoPin8);
  h9.attach(servoPin9);//9,10,11,12 밑다리
  h10.attach(servoPin10);
  h11.attach(servoPin11);
  h12.attach(servoPin12);

  }

void loop() {

  h1.write(65);//서있기
  h2.write(105);
  h3.write(50);
  h4.write(130);
  h5.write(80);
  h6.write(90);
  h7.write(60);
  h8.write(130);
  h9.write(160);
  h10.write(20);
  h11.write(180);
  h12.write(0);


  delay(1000);//1초 후 오른쪽 앞발 앞으로 뻗기
  
  h11.write(180);//오른쪽 앞 밑다리
  h3.write(90);오른쪽 앞 윗다리
  
  delay(200);
  
  h11.write(150);//오른쪽 앞 밑다리 각도 조절
  
  h10.write(20);//동시에 왼쪽 뒤 밑다리 뻗기
  h2.write(65);//왼쪽 뒤 윗다리
  delay(200);
  

   h11.write(180);//오른쪽 앞 밑다리
   h3.write(50);//오른쪽 앞 윗다리

   h10.write(50);//동시에 왼쪽 뒤 밑다리 각도 조절
  
  delay(200);
  h10.write(20);//왼쪽 뒤 밑다리 각도 조절
  h2.write(105);//왼쪽 뒤 윗다리

  
  delay(200);

  h12.write(0);//왼쪽 앞 밑다리 뻗기
  h4.write(90);//왼쪽 앞  윗다리
  
  delay(200);
  
  h12.write(30);//왼쪽 앞 밑다리 각도 조절

  h9.write(160);//동시에오른쪽 뒤 밑다리 뻗기
  h1.write(105);
  delay(200);
  
   h12.write(0);//왼쪽 앞 밑다리
   h4.write(130);//왼쪽 앞  윗다리

   h9.write(120);//오른쪽 뒤 밑다리
  
  delay(200);
  h9.write(160);//오른쪽 뒤 밑다리
  h1.write(65);//오른쪽 뒤 밑다리
  delay(200);
  


  
}
