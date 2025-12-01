#include "DHT.h"

#define comPin 2

// In microseconds
#define START_COM_TIME 3000 // 3 ms
#define HIGH_COM_TIME 8000 // 8 ms
#define SPACE_COM_TIME 1500 // 1.5 ms

// In miliseconds
#define LOW_COM_TIME 12 // 12 ms
#define END_COM_TIME 30 // 30 ms
#define DATA_SEPARATION_TIME 60 // 60 ms

#define DHTPIN 5
#define DHTTYPE DHT22

#define COM_PACKET_SIZE 14

DHT dht(DHTPIN, DHTTYPE);

String toBinary(int value) {
  String result = "";
  for (int i = COM_PACKET_SIZE - 1; i >= 0; i--) {
    result += ((value >> i) & 1) ? '1' : '0';
  }
  return result;
}

void sendValue(int value) {
  // Begin communication
  digitalWrite(comPin, HIGH);
  delayMicroseconds(START_COM_TIME);
  digitalWrite(comPin, LOW);
    
  // Space
  delayMicroseconds(SPACE_COM_TIME);

  String binary = toBinary(value);
  
  // Communicate value
  for (int i = 0; i < COM_PACKET_SIZE; i++) {
    if (binary[i] == '1') {
      digitalWrite(comPin, HIGH);
      delayMicroseconds(HIGH_COM_TIME);
      digitalWrite(comPin, LOW);
    }
    else {
      digitalWrite(comPin, HIGH);
      delay(LOW_COM_TIME);
      digitalWrite(comPin, LOW);
    }
    // Space
    delayMicroseconds(SPACE_COM_TIME);
  }

  // Space
  delayMicroseconds(SPACE_COM_TIME);
    
  // End communication
  digitalWrite(comPin, HIGH);
  delay(END_COM_TIME);
  digitalWrite(comPin, LOW);
  delayMicroseconds(SPACE_COM_TIME);
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

  sendValue(101); // Value that is used to determine offset in signalling (if it is present)
  delay(DATA_SEPARATION_TIME);
  sendValue(temp);
  delay(DATA_SEPARATION_TIME);
  sendValue(hum);
  delay(DATA_SEPARATION_TIME);
}