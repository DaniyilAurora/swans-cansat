#include "LoRaWan_APP.h"
#include "Arduino.h"

#define RF_FREQUENCY                                915000000 // Hz
#define TX_OUTPUT_POWER                             5        // dBm
#define LORA_BANDWIDTH                              0         // [0: 125 kHz,
#define LORA_SPREADING_FACTOR                       7         // [SF7..SF12]
#define LORA_CODINGRATE                             1         // [1: 4/5,
#define LORA_PREAMBLE_LENGTH                        8         // Same for Tx and Rx
#define LORA_SYMBOL_TIMEOUT                         0         // Symbols
#define LORA_FIX_LENGTH_PAYLOAD_ON                  false
#define LORA_IQ_INVERSION_ON                        false
#define RX_TIMEOUT_VALUE                            1000
#define BUFFER_SIZE                                 30 // Define the payload size here

char txpacket[BUFFER_SIZE];
char rxpacket[BUFFER_SIZE];

double txNumber;

bool lora_idle = true;

static RadioEvents_t RadioEvents;
void OnTxDone( void );
void OnTxTimeout( void );

unsigned long highStart = 0;
bool wasHigh = false;

#define comPin 34
#define AMOUNT_DATAS 3
#define COM_PACKET_SIZE 14

// In microseconds
#define START_COM_TIME 3000 // 3 ms
#define HIGH_COM_TIME 8000 // 8 ms

// In miliseconds
#define LOW_COM_TIME 12 // 12 ms
#define END_COM_TIME 30 // 30 ms

char binary[COM_PACKET_SIZE + 1];

void resetBinary() {
  for (int i = 0; i < COM_PACKET_SIZE; i++) {
    binary[i] = '0';
  }
}

bool isValid(unsigned long value, unsigned long supposedValue) {
  return (value <= (supposedValue + 2000) && value >= (supposedValue - 2000));
}

int bitsToValue(char binary[]) {
    int value = 0;
    for (int i = 0; i < COM_PACKET_SIZE; i++) {
      value = (value << 1) | (binary[i] - '0');
    }

    return value;
}

void setup() {
    Serial.begin(115200);

    // Initialize binary array
    resetBinary();
    binary[COM_PACKET_SIZE] = '\0';  // Null terminator

    Mcu.begin(HELTEC_BOARD,SLOW_CLK_TPYE);
	
    txNumber=0;

    RadioEvents.TxDone = OnTxDone;
    RadioEvents.TxTimeout = OnTxTimeout;
    
    Radio.Init( &RadioEvents );
    Radio.SetChannel( RF_FREQUENCY );
    Radio.SetTxConfig( MODEM_LORA, TX_OUTPUT_POWER, 0, LORA_BANDWIDTH,
                                   LORA_SPREADING_FACTOR, LORA_CODINGRATE,
                                   LORA_PREAMBLE_LENGTH, LORA_FIX_LENGTH_PAYLOAD_ON,
                                   true, 0, 0, LORA_IQ_INVERSION_ON, 3000 ); 
    pinMode(comPin, INPUT_PULLUP);
}

int temp = 0;
int hum = 0;

int datasReceived[AMOUNT_DATAS];
int amountReceived = 0;

unsigned long startTime = 0;
bool isCommunicating = false;

int currentBit = 0;

void loop() {
  Radio.IrqProcess();
  // Read value of comPin
  int value = digitalRead(comPin);
  
  // Start measuring duration of HIGH signal
  if (value == HIGH && startTime == 0) {
    startTime = micros();
  }
  else if (value == LOW && startTime != 0) {
    unsigned long duration = micros() - startTime;

    // Communication Protocol
    if (isValid(duration, START_COM_TIME)) {
      // Begin communication
      isCommunicating = true;
    }
    if (isCommunicating && !isValid(duration, END_COM_TIME * 1000)) {
      // If communicating, and not ending communication
      if (isValid(duration, HIGH_COM_TIME) && currentBit < COM_PACKET_SIZE) {
        binary[currentBit] = '1';
        currentBit++;
      }
      else if (isValid(duration, LOW_COM_TIME * 1000) && currentBit < COM_PACKET_SIZE) {
        binary[currentBit] = '0';
        currentBit++;
      }
    }
    else if (isCommunicating && isValid(duration, END_COM_TIME * 1000)) {
      isCommunicating = false;
      currentBit = 0;
      int value = bitsToValue(binary);

      resetBinary();

      // Use value
      datasReceived[amountReceived] = value;
      amountReceived++;
    }

    // Reset for next communication
    startTime = 0;
  }

  if(lora_idle == true) {
    if (amountReceived == AMOUNT_DATAS) {
      delay(10);

      // Combine all of the datas into one string
      String combined = "";
      for (int i = 0; i < amountReceived; i++) {
        if (i > 0) combined += ".";
        combined += datasReceived[i];
      }

      const char* result = combined.c_str();

      Radio.Send( (uint8_t *)result, strlen(result) ); //send the package out	
      lora_idle = false;
    }
  }
}

void OnTxDone( void )
{
	Serial.println("TX done......");
	lora_idle = true;
  amountReceived = 0;
  
  for (int i = 0; i < AMOUNT_DATAS; i++) {
    datasReceived[i] = 0;
  }
}

void OnTxTimeout( void )
{
    Radio.Sleep( );
    Serial.println("TX Timeout......");
    lora_idle = true;
}