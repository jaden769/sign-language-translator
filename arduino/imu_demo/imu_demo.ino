#include <Arduino_BMI270_BMM150.h>

void setup() {
  Serial.begin(9600);
  
  while (!Serial) {

  }
  if (!IMU.begin()) {
    Serial.println("Failed to start the IMU");
    while (true) {

    }
  }

  Serial.println("IMU started");
}

void loop() {
  float x;
  float y;
  float z;

  if(IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);
    if (z > 0.8) {
      Serial.println("Orientation: flat");
    }
    else if ( x > 0.8) {
      Serial.println("Orientation: short edge");
    }
    else if ( y > 0.8) {
      Serial.println("Orientation: long edge");
    }
    else {
      Serial.println("Orientation: unknown");
    }
  }

  delay(200);
}
