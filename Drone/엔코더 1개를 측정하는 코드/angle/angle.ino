const int pulsePin=5; //pwm단자 5번핀에 연걸
float pulseHigh;  //pulseHigh라는 변수 지정
double angle;    // angle 이라는 변수 지정




void setup() {
Serial.begin(115200); //비트레이트가 115200인 시리얼 통신 시작
pinMode(5, INPUT);   // 5번핀 입력

}

void loop() {
pulseHigh = pulseIn(pulsePin,HIGH); //pulsein 이라는 함수를 사용하여 파형이 high인곳의 시간 측정

angle = (float) ((12706-(pulseHigh))/12450)*360; // angle 값을 구하는 식


/*if (angle>180){
angle=angle-360;}
else {
angle=angle;
}*/

Serial.print(" ");
Serial.println(angle);   // angle 값을 출력

}

//Serial.println(pulseHigh);}
