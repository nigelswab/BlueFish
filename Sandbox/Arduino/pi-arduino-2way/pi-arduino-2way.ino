/*
Program: Receive Strings From Raspberry Pi
*/
 
void setup(){
  // Set the baud rate  
  Serial.begin(9600);
}
 
void loop(){
 
  if(Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.print("Hi Raspberry Pi! You sent me: ");
    Serial.println(data);
  }
}
