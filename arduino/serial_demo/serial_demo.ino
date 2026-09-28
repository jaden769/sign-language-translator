void setup() {
  Serial.begin(9600);
  Serial.println("Glove started");
}

void loop() {
  int sensorReading = analogRead(A0);

  Serial.print("Sensor reading: ");
  Serial.println(sensorReading);

  delay(500);
}
