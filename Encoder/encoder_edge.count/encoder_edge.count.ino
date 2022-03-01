#define outputA 5
#define outputB 6
int counter = 0;
int aState;
int aLastState;
void setup() {
  pinMode(outputA,INPUT_PULLUP);
  pinMode(outputB,INPUT_PULLUP);

  Serial.begin(115200); //출력 A의 초기 상태를 읽는다.
  aLastState = digitalRead(outputA);
}

void loop() {
  aState = digitalRead(outputA); //출력의 현재상태를 읽는다.
  //출력 A의 초기 상태와 현재 상태가 다르면 펄스가 발생한다.
  if (aState != aLastState){ //두 연산자의 값이 같지 않은지를 비교하는 연산자: !=
    //출력 B 상태가 출력 A 상태와 다르면 인코더가 시계 방향으로 회전하고 있음을 의미
    if(digitalRead(outputB) != aState){
      counter ++;
    } else{
      counter --;
    }
    Serial.print("Position: ");
    Serial.println(counter);
  }
  aLastState = aState; // 출력  A의 이전 상태를 현재 상태로 업데이트한다. 
}
