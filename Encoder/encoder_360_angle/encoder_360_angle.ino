#define outputA 5
#define outputB 6
unsigned int a=0; //unsigned = 음수값을 양수로 바꿔 데이터 저장양을 늘린다.
double counter = 0;
int aState;
int aLastState;
char data = 0; //시리얼 데이터 받는거 초기값
const int IN1 = 10;
const int IN2 = 11;
const int pulsePin = 3;
void setup() {
  pinMode(outputA,INPUT_PULLUP);
  pinMode(outputB,INPUT_PULLUP);

  Serial.begin(115200); //출력 A의 초기 상태를 읽는다.
  aLastState = digitalRead(outputA);
}

void loop() {
  while(1){
  aState = digitalRead(outputA); //출력의 현재상태를 읽는다.
  //출력 A의 초기 상태와 현재 상태가 다르면 펄스가 발생한다.
  if (aState != aLastState){ //두 연산자의 값이 같지 않은지를 비교하는 연산자: !=
    //출력 B 상태가 출력 A 상태와 다르면 인코더가 시계 방향으로 회전하고 있음을 의미한다.
    if(digitalRead(outputB) != aState){
      counter ++;
    } else{
      counter --;
    }
    if(a%10==0){ //나머지 연산 -> why? 카운터 양에비해 프린터되는 값이 적어 줄임
    Serial.print("Position: ");
    Serial.println(counter*360/(27*26));} //카운터값을 360도 각도로 나눠주기위해 엔코더 한바퀴에 펄스수 26 * 기어비 1/27
  }
  a=a+1;
  aLastState = aState; // 출력  A의 이전 상태를 현재 상태로 업데이트한다.
if(Serial.available())
{
  data = Serial.read();
  if(data == '1'){
    digitalWrite(IN1, HIGH); //HH,LL는 정지 H,L는 정방향 L,H는 역방향
    digitalWrite(IN2, LOW);
    analogWrite(3,50);
    Serial.print("역회전 ");
  }
  else if(data == '2')
  {
    digitalWrite(IN1, LOW); 
    digitalWrite(IN2, HIGH);
    analogWrite(3,50);
    Serial.print("역회전 ");
  }
  else if(data == '0')
  {
    digitalWrite(IN1, LOW); 
    digitalWrite(IN2, LOW);
    analogWrite(3,0);
    Serial.print("정지 ");
  }
  else if(data == '5')
  {
    digitalWrite(IN1, LOW); 
    digitalWrite(IN2, LOW);
    analogWrite(3,0);
    counter = 0; // 정지와 동시에 카운터 초기값 0으로 만들어주기
  }
  }
}
}
