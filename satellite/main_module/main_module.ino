#include "DHT.h"

#define comPin 2
#define START_COM_TIME 10
#define HIGH_COM_TIME 20
#define LOW_COM_TIME 50
#define END_COM_TIME 80
#define SPACE_COM_TIME 5

#define DATA_SEPARATION_TIME 60

#define DHTPIN 5
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

String toBinary(int value) {
  String result = "";
  for (int i = 9; i >= 0; i--) {
    result += ((value >> i) & 1) ? '1' : '0';
  }
  return result;
}

void sendValue(int value) {
  // Begin communication
  digitalWrite(comPin, HIGH);
  delay(START_COM_TIME);
  digitalWrite(comPin, LOW);
    
  // Space
  delay(SPACE_COM_TIME);

  String binary = toBinary(value);
  
  // Communicate value
  for (int i = 0; i < 10; i++) {
    if (binary[i] == '1') {
      digitalWrite(comPin, HIGH);
      delay(HIGH_COM_TIME);
      digitalWrite(comPin, LOW);
    }
    else {
      digitalWrite(comPin, HIGH);
      delay(LOW_COM_TIME);
      digitalWrite(comPin, LOW);
    }
    // Space
    delay(SPACE_COM_TIME);
  }

  // Space
  delay(SPACE_COM_TIME);
    
  // End communication
  digitalWrite(comPin, HIGH);
  delay(END_COM_TIME);
  digitalWrite(comPin, LOW);
  delay(SPACE_COM_TIME);
}

void setup() {
  pinMode(comPin, OUTPUT);
  digitalWrite(comPin, LOW);
  Serial.begin(9600);
  dht.begin();
}

long temp;
long hum;

void loop() {
  float rtemp = dht.readTemperature();
  float rhum = dht.readHumidity();
  temp = (long)(rtemp * 10);
  hum = (long)(rhum * 10);
  sendValue(temp);
  delay(DATA_SEPARATION_TIME);
  sendValue(hum);
  delay(DATA_SEPARATION_TIME);
}