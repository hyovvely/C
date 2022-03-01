const int pulsePinx= 3; //pwm단자 3번핀에 연걸 1번 엔코더
const int pulsePiny= 5; //pwm단자 5번핀에 연걸 3
const int pulsePinz= 7; //pwm단자 7번핀에 연걸2
float pulseHighx;  //pulseHigh라는 변수 지정
float pulseHighy;  //pulseHigh라는 변수 지정
float pulseHighz;  //pulseHigh라는 변수 지정
double anglex;    // angle 이라는 변수 지정
double angley;
double anglez;

void setup() {
Serial.begin(115200); //비트레이트가 115200인 시리얼 통신 시작
pinMode(3, INPUT);   // 3번핀 입력
pinMode(5, INPUT);   // 5번핀 입력
pinMode(7, INPUT);   // 7번핀 입력


}

void loop() {
pulseHighx = pulseIn(pulsePinx,HIGH); //pulsein 이라는 함수를 사용하여 파형이 high인곳의 시간 측정
pulseHighy = pulseIn(pulsePiny,HIGH);
pulseHighz = pulseIn(pulsePinz,HIGH);
anglex = (float) ((12883-(pulseHighx))/12648)*360; // angle 값을 구하는 식
angley = (float) ((12777-(pulseHighy))/12513)*360;
anglez = (float) ((12706-(pulseHighz))/12453)*360;
//한주기 듀에 보드 12883 인터럽트 235
// 2번 엔코더 12706 253 360 약간 넘어감
// 3번 12777 264

//Serial.print("x angle = "); //angle= 이라는 문구 출력
Serial.print(anglex);   // angle 값을 출력
Serial.print("  "); //angle= 이라는 문구 출력
Serial.print(angley);
Serial.print("  "); //angle= 이라는 문구 출력
Serial.println(anglez);
//Serial.println(pulseHigh);
  
}
