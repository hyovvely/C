//x 3번 엔코더
const int pulsePin=4;
float pulseHigh;
double angle;
const int numReadingsx = 100; //표본의 수(100개를 추출해서 평균을 낼것)
int readingsx[numReadingsx];
int readIndexroll = 0;
float totalx = 0; //합한 값
float averagex = 0; //평균값 즉, 출력


//y 1번 엔코더
const int pulsePin1=3; 
float pulseHigh1;
double angle1;
const int numReadingsy= 100;
int readingsy[numReadingsy];
int readIndexpitch = 0;
float totaly = 0;
float averagey = 0;


 //z 2번 엔코더
const int pulsePin2=6;
float pulseHigh2;
double angle2;
const int numReadingsz= 100;
int readingsz[numReadingsz];
int readIndexyaw = 0;
float totalz = 0;
float averagez = 0;







void setup() {
  Serial.begin(115200);
pinMode(pulsePin, INPUT);   // 5번핀 입력
pinMode(pulsePin1, INPUT);
pinMode(pulsePin2, INPUT);

for (int thisReadingx = 0; thisReadingx < numReadingsx; thisReadingx++) {readingsx[thisReadingx] = 0; }
for (int thisReadingy = 0; thisReadingy < numReadingsy; thisReadingy++) {readingsy[thisReadingy] = 0; }
for (int thisReadingz = 0; thisReadingz < numReadingsz; thisReadingz++) {readingsz[thisReadingz] = 0; }
    
}

void loop() {

  if (Serial.available() > 0) {command = Serial.readStringUntil('\n');command_process(); }
pulseHigh = pulseIn(pulsePin,HIGH); //pulsein 이라는 함수를 사용하여 파형이 high인곳의 시간 측정
pulseHigh1 = pulseIn(pulsePin1,HIGH);
pulseHigh2 = pulseIn(pulsePin2,HIGH);
angle = (double) ((12777-(pulseHigh))/12513)*360; // angle 값을 구하는 식
angle1 = (double) ((12883-(pulseHigh1))/12648)*360;
angle2 = (double) ((12706-(pulseHigh2))/12450)*360;


totalx = totalx - readingsx[readIndexroll];
readingsx[readIndexroll] = angle;
totalx = totalx+readingsx[readIndexroll];
readIndexroll = readIndexroll + 1;
if (readIndexroll >= numReadingsx) {readIndexroll = 0;}
averagex = totalx / numReadingsx;
if(averagex>180)
{averagex=360-averagex;}
else {averagex=averagex;}

/*
if(angle1>180)
{angle1=360-angle1;}
else {angle1=angle1;}
if(angle2>180)
{angle2=360-angle2;}
else {angle2=angle2;}
*/



totaly = totaly - readingsy[readIndexpitch];
readingsy[readIndexpitch] = angle1;
totaly = totaly + readingsy[readIndexpitch];
readIndexpitch = readIndexpitch + 1;
if (readIndexpitch >= numReadingsy) {readIndexpitch = 0;}
averagey = totaly / numReadingsy;
if(averagey>180)
{averagey=360-averagey;}
else {averagey=averagey;}


totalz = totalz - readingsz[readIndexyaw];
readingsz[readIndexyaw] = angle2;
totalz = totalz + readingsz[readIndexyaw];
readIndexyaw = readIndexyaw + 1;
if (readIndexyaw >= numReadingsz) {readIndexyaw = 0;}
averagez = totalz / numReadingsz;
if(averagez>180)
{averagez=360-averagez;}
else {averagez=averagez;}

Serial.print(" "); Serial.print(averagex);Serial.print(" ");Serial.print(averagey);Serial.print(" ");Serial.println(averagez);

}
