#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

int comPin = 10;

void setup() {
  Serial.begin(9600);
  pinMode(comPin, OUTPUT);

  dht.begin();
}

long temp;
long hum;

void loop() {
  float rtemp = dht.readTemperature();
  float rhum = dht.readHumidity();

  temp = (long)(rtemp * 10);
  hum = (long)(rhum * 10);

  // Starting communication
  digitalWrite(comPin, HIGH);
  delay(70); 
  digitalWrite(comPin, LOW);
  
  // Delay to separate HIGH and LOW signals from each other
  delay(10);

  // Sending temperature
  digitalWrite(comPin, HIGH);
  delay(temp);
  digitalWrite(comPin, LOW);

  // Separator delay
  delay(10);

  // Sending humidity
  digitalWrite(comPin, HIGH);
  delay(hum);
  digitalWrite(comPin, LOW);

  // Delay again to separate HIGH and LOW
  delay(10);
  
  // Ending communication
  digitalWrite(comPin, HIGH);
  delay(100);
  digitalWrite(comPin, LOW);

  // Last delay to separate HIGH and LOW
  delay(10);
}