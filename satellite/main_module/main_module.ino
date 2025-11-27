int comPin = 10;

void setup() {
  Serial.begin(9600);
  pinMode(comPin, OUTPUT);
  randomSeed(analogRead(0));
}

long temp;
long hum;

void loop() {
  temp = random(102, 999); // Random temp between 10.2 and 99.9
  hum = random(102, 999); // Random humidity between 10.2 and 99.9
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