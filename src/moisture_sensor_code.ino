//soil moisture value
int moistVal = 0;
//analog signal from sensor
int signalPin = A0;

void setup() {
  //initialize transmission over the serial port
  Serial.begin(9600);
}

void loop() {
  //print values over the serial port
  Serial.print("soil moisture = ");
  Serial.println(readMoisture());
  delay(10000);
}

int readMoisture() {
  //read the signal from the sensor
  moistVal = analogRead(signalPin);
  return moistVal;
}
