#include "LoRaWan_APP.h"
#include "Arduino.h"


#define RF_FREQUENCY                                915000000 // Hz

#define TX_OUTPUT_POWER                             5        // dBm

#define LORA_BANDWIDTH                              0         // [0: 125 kHz,
                                                              //  1: 250 kHz,
                                                              //  2: 500 kHz,
                                                              //  3: Reserved]
#define LORA_SPREADING_FACTOR                       7         // [SF7..SF12]
#define LORA_CODINGRATE                             1         // [1: 4/5,
                                                              //  2: 4/6,
                                                              //  3: 4/7,
                                                              //  4: 4/8]
#define LORA_PREAMBLE_LENGTH                        8         // Same for Tx and Rx
#define LORA_SYMBOL_TIMEOUT                         0         // Symbols
#define LORA_FIX_LENGTH_PAYLOAD_ON                  false
#define LORA_IQ_INVERSION_ON                        false


#define RX_TIMEOUT_VALUE                            1000
#define BUFFER_SIZE                                 30 // Define the payload size here

char txpacket[BUFFER_SIZE];
char rxpacket[BUFFER_SIZE];

double txNumber;

bool lora_idle=true;

static RadioEvents_t RadioEvents;
void OnTxDone( void );
void OnTxTimeout( void );

unsigned long highStart = 0;
bool wasHigh = false;

int comPin = 34;

void setup() {
    Serial.begin(115200);
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
    Serial.println("[START] Start");
}

bool isTempReceived = false;
bool isHumReceived = false;
int temp = 0;
int hum = 0;

void loop() {
  Radio.IrqProcess();
  int value = digitalRead(comPin); // HIGH = 1, LOW = 0 (because of pullup)

  // When pin goes HIGH (and wasn't HIGH before)
  if (value == HIGH && !wasHigh) {
    highStart = millis();  // record start time
    wasHigh = true;
  }

  // When pin goes LOW after being HIGH
  if (value == LOW && wasHigh) {
    unsigned long duration = millis() - highStart;  // difference
    wasHigh = false;

    if (duration >= 68 && duration <= 72) {
      Serial.println("[COMMUNICATION] Communication has started.");
    }
    else if (duration >= 98 && duration <= 102) {
      Serial.println("[COMMUNICATION] Communication has ended.");
      isTempReceived = false;
    }
    else if (!isTempReceived) {
      Serial.println("[COMMUNICATION] Data has been received. Temperature: " + String(duration));
      temp = duration;
      isTempReceived = true;
    }
    else {
      Serial.println("[COMMUNICATION] Data has been received. Humidity: " + String(duration));
      hum = duration;
      isHumReceived = true;
    }

    if (isTempReceived && isHumReceived) {
        if(lora_idle == true)
        {
          delay(1000);

          String combined = String(temp) + "." + String(hum);
          const char* result = combined.c_str();

          Radio.Send( (uint8_t *)result, strlen(result) ); //send the package out	
          lora_idle = false;
        }
    }
  }
}

void OnTxDone( void )
{
	Serial.println("TX done......");
	lora_idle = true;
  isTempReceived = false;
  isHumReceived = false;
}

void OnTxTimeout( void )
{
    Radio.Sleep( );
    Serial.println("TX Timeout......");
    lora_idle = true;
}