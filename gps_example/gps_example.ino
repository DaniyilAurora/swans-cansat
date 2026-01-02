#include <SoftwareSerial.h>
#include <TinyGPS++.h>

SoftwareSerial gpsSerial(8, 9);
TinyGPSPlus gps;

double latitude, longitude;
unsigned long lastGPSReceive = 0;

void setup() {
  Serial.begin(9600);
  gpsSerial.begin(9600);
}

void serviceGPS() {
  while (gpsSerial.available()) {
    gps.encode(gpsSerial.read());
  }
}

void loop() {
  serviceGPS();

  // Print at most once per second
  if (gps.location.isUpdated() && millis() - lastGPSReceive > 1000) {
    latitude  = gps.location.lat();
    longitude = gps.location.lng();

    Serial.print("latitude: ");
    Serial.println(latitude, 7);
    Serial.print("longitude: ");
    Serial.println(longitude, 7);
    Serial.println();

    lastPrint = millis();
  }
}
