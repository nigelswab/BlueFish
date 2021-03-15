/*
Program: Receive Strings From Raspberry Pi
*/
/*GLOBAL VARIABLES*/
volatile unsigned int DEPTH;     // depth for hold depth mode [m]
volatile unsigned int ALTITUDE;  // altititude for hold altidtude mode [m]
volatile int MODE;               // 1 = dive
                                 // 2 =  constant_depth
                                 // 3 =  constant_altitude
                                 // 4 = surface

 
void setup(){
  // Set the baud rate  
  Serial.begin(9600);
}
 
void loop(){
 
  if(Serial.available() > 0) {
    String temp = Serial.readStringUntil(',');
    DEPTH = temp.toFloat();
    temp = Serial.readStringUntil(',');
    ALTITUDE = temp.toFloat();
    temp = Serial.readStringUntil('\n');
    MODE = temp.toInt();
    Serial.print(String(DEPTH) + ',');
    Serial.print(String(ALTITUDE) + ',');
    Serial.println(String(MODE));
  }
}
