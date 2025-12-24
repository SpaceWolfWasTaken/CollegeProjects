#include <Servo.h>
#include <Wire.h>


Servo servo;     
int trigPinD = 7; //down    
int echoPinD = 6;   

int trigPinF = 8;    //forward
int echoPinF = 9;  

int servoPin = 5;

long durationF,durationD;
long distanceF = 0;
long distanceD = 0;

void setup() {       
  Wire.begin(8);                /* join i2c bus with address 8 */
  //Wire.onReceive(receiveEvent); /* register receive event */
  Wire.onRequest(requestEvent); /* register request event */
  Serial.begin(115200);
    servo.attach(servoPin);  
    pinMode(trigPinD, OUTPUT);  
    pinMode(echoPinD, INPUT);  
    pinMode(trigPinF, OUTPUT);  
    pinMode(echoPinF, INPUT);  
    servo.write(0);         //close cap on power on
    delay(100);
    //servo.detach(); 
} 

void measureDown() {  
 digitalWrite(10,HIGH);
digitalWrite(trigPinD, LOW);
delayMicroseconds(5);
digitalWrite(trigPinD, HIGH);
delayMicroseconds(15);
digitalWrite(trigPinD, LOW);
pinMode(echoPinD, INPUT);
durationD = pulseIn(echoPinD, HIGH);
distanceD = (durationD/2) / 29.1;    //obtain distance
}

void measureForward() {  
 digitalWrite(10,HIGH);
digitalWrite(trigPinF, LOW);
delayMicroseconds(5);
digitalWrite(trigPinF, HIGH);
delayMicroseconds(15);
digitalWrite(trigPinF, LOW);
pinMode(echoPinF, INPUT);
durationF = pulseIn(echoPinF, HIGH);
distanceF = (durationF/2) / 29.1;    //obtain distance
}

void requestEvent() {
 Wire.write((int)distanceD); 
}
void loop() { 
  measureDown();
  measureForward();

  if(distanceD < 15) {
    Serial.print("Distance Down is: ");
    Serial.println(distanceD);
  }
  if (distanceF < 20){
    delay(50);
    servo.write(90);
    delay(2000);
    servo.write(0);

  }
  Serial.print("Distance Forward is: ");
    Serial.println(distanceF);
    delay(500);

}