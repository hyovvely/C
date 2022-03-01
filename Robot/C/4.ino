#include <SoftwareSerial.h> //시리얼 통신 라이브러리 호출
#include "Servo.h" //서보 라이브러리

int blueTx=53;   //Tx (블투 보내는핀 설정)
int blueRx=52;   //Rx (블투 받는핀 설정)
SoftwareSerial mySerial(blueTx, blueRx);  //시리얼 통신을 위한 객체선언
String myString=""; //받는 문자열

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

int servoPin1 = 12;//오 뒤 앞으로180 뒤로 0
int servoPin2 = 3;//왼 뒤 앞으로 0 뒤로 180
int servoPin3 = 9;//오 앞 앞으로 180 뒤로 0
int servoPin4 = 6;//왼 앞  앞으로 0 뒤로 180
int servoPin5 = 11;//오 뒤 위 안쪽으로 180 밖으로 0 밖으로 많이 안뻗음
int servoPin6 = 2;//왼 뒤 위 안쪽으로 0 밖으로 180 밖으로 많이 뻗음
int servoPin7 = 8;//오 앞 위 안쪽으로 0 밖으로 180 밖으로 많이 뻗음
int servoPin8 = 5;//왼 앞 위 안쪽으로 180 밖으로 0 밖으로 많이 뻗음
int servoPin9 = 13;//오 뒤 밑 뒤로 0 앞으로 180 앞으로 별로안옴 조립필수
int servoPin10 = 4;//왼 뒤 밑 뒤로 180 앞으로 0 앞으로 별로안옴 조립필수
int servoPin11 = 10;//오 앞 밑 뒤로 0 앞으로 180 앞으로 별로안옴 조립필수
int servoPin12 = 7;//왼 뒤 밑 뒤로 180 앞으로 0 앞으로 별로안옴 조립필수

void setup() {
 
  h1.attach(servoPin1);
  h2.attach(servoPin2);
  h3.attach(servoPin3);
  h4.attach(servoPin4);
  h5.attach(servoPin5);
  h6.attach(servoPin6);
  h7.attach(servoPin7);
  h8.attach(servoPin8);
  h9.attach(servoPin9);
  h10.attach(servoPin10);
  h11.attach(servoPin11);
  h12.attach(servoPin12);
  mySerial.begin(9600); //블루투스 시리얼 개방

  }

  void loop() {
  while(mySerial.available())  //mySerial 값이 있으면
  {
    char myChar = (char)mySerial.read();  //mySerial int형식의 값을 char형식으로 변환
    myString+=myChar;   //수신되는 문자열을 myString에 모두 붙임 (1바이트씩 전송되는 것을 모두 붙임)
    delay(5);           //수신 문자열 끊김 방지
  }
  
  if(!myString.equals(""))  //myString 값이 있다면
  {
    Serial.println("input value: "+myString); //시리얼모니터에 myString값 출력
 
      if(myString=="on")  //myString 값이 'on' 이라면
      {
        h1.write(50);//앞
  h2.write(110);//앞
  h3.write(50);//앞
  h4.write(130);//앞
  

  h9.write(160);//앞
  h10.write(20);//앞
  h11.write(180);//앞
  h12.write(0);//앞
  h5.write(10);//앞
  h6.write(60);//앞
  h7.write(60);//앞
  h8.write(130);////앞

  delay(1000);
  h9.write(90);//앞
  h10.write(70);//앞
  h11.write(120);//앞
  h12.write(60);//앞
  h5.write(10);//앞
  h6.write(40);//앞
  h7.write(60);//앞
  h8.write(130);////앞
      } 
    myString="";  //myString 변수값 초기화
  }
}
