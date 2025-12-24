
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include <time.h>
#include "secrets.h"

#include <SPI.h>
#include <MFRC522.h>

//AWS
#define AWS_IOT_PUBLISH_TOPIC   "esp8266/cps/pub"
#define AWS_IOT_SUBSCRIBE_TOPIC "esp8266/cps/state"
 
WiFiClientSecure net;
 
BearSSL::X509List cert(cacert);
BearSSL::X509List client_crt(client_cert);
BearSSL::PrivateKey key(privkey);
 
PubSubClient client(net);

time_t now;
time_t nowish = 1510592825;
 
unsigned long lastMillis = 0;
unsigned long previousMillis = 0;
const long interval = 5000; 
 
void NTPConnect(void)
{
  Serial.print("Setting time using SNTP");
  configTime(20700, 0 * 3600, "pool.ntp.org", "time.nist.gov"); //5.75 (5:45) * 3600
  now = time(nullptr);
  while (now < nowish)
  {
    delay(500);
    Serial.print(".");
    now = time(nullptr);
  }
  Serial.println("done!");
  struct tm timeinfo;
  gmtime_r(&now, &timeinfo);
  Serial.print("Current time: ");
  Serial.print(asctime(&timeinfo));
}
 

void messageReceived(char *topic, byte *payload, unsigned int length)
{
  Serial.print("Received [");
  Serial.print(topic);
  Serial.print("]: ");
  for (int i = 0; i < length; i++)
  {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}
 
 
void connectAWS()
{
  delay(3000);
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
 
  Serial.println(String("Attempting to connect to SSID: ") + String(WIFI_SSID));
 
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(1000);
  }
 
  NTPConnect();
 
  net.setTrustAnchors(&cert);
  net.setClientRSACert(&client_crt, &key);
 
  client.setServer(MQTT_HOST, 8883);
  client.setCallback(messageReceived);
 
 
  Serial.println("Connecting to AWS IOT");
 
  while (!client.connect(THINGNAME))
  {
    Serial.print(".");
    delay(1000);
  }
 
  if (!client.connected()) {
    Serial.println("AWS IoT Timeout!");
    return;
  }
  // Subscribe to a topic
  client.subscribe(AWS_IOT_SUBSCRIBE_TOPIC);
 
  Serial.println("AWS IoT Connected!");
}
 
 
void publishMessage(String* tagID)
{
  StaticJsonDocument<200> doc;
  doc["UID"] = *tagID;
  char jsonBuffer[512];
  serializeJson(doc, jsonBuffer); // print to client
  client.publish(AWS_IOT_PUBLISH_TOPIC, jsonBuffer);
}

////




//test
byte readCard[4];
String tagID = "";
/////

constexpr uint8_t RST_PIN = 5;//D1;       
constexpr uint8_t SS_PIN = 4;//D2;      

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

void setup() {
	Serial.begin(115200);		// Initialize serial communications with the PC
	while (!Serial);		  // Do nothing if no serial port is opened
	delay(1000);
  Serial.println("\n\nSerial has begun");
  connectAWS(); //AWS
  SPI.begin();			    // Init SPI bus
	mfrc522.PCD_Init();		// Init MFRC522
  Serial.println("Setup has ended!!");
}

void loop() {

  //Wait until new tag is available
  while (getUID(&tagID)) 
  {
    Serial.println(tagID);
    if (!client.connected()){
      connectAWS();
    } else {
      client.loop();
        publishMessage(&tagID);
    }
    delay(1000);
  }
  
  	
}

boolean getUID(String* tagID) //taking a ref of tagId
  {
    *tagID=""; //emptying previous buffer
    // Getting ready for reading Tags
    if ( ! mfrc522.PICC_IsNewCardPresent()) {   //If a new tag is placed close to the RFID reader, continue
    return false;
    }
    if ( ! mfrc522.PICC_ReadCardSerial()) {     //When a tag is placed, get UID and continue
    return false;
    }
    Serial.println("RFID Noticed!!");
    for ( uint8_t i = 0; i < 4; i++) {                  // The MIFARE tag in use has a 4 byte UID
    tagID->concat(String(mfrc522.uid.uidByte[i], HEX));  // Adds the 4 bytes in a single string variable
    }
    tagID->toUpperCase(); //not sure why *tagId. doesn't work
    mfrc522.PICC_HaltA(); // Stop reading
    return true;
  }