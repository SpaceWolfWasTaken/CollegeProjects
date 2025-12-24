#include <Wire.h>

#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include <time.h>
#include "secrets.h"

//AWS
#define AWS_IOT_PUBLISH_TOPIC   "dustbin/pub"
#define AWS_IOT_SUBSCRIBE_TOPIC "dustbin/sub"
 
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
  configTime(20000, 0 * 3600, "pool.ntp.org", "time.nist.gov");
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
 
 
void publishMessage(int filled)
{
  StaticJsonDocument<200> doc;
  doc["distance"] = filled;
  char jsonBuffer[512];
  serializeJson(doc, jsonBuffer); // print to client
  client.publish(AWS_IOT_PUBLISH_TOPIC, jsonBuffer);
}

void setup() {
	Serial.begin(115200);		// Initialize serial communications with the PC
	while (!Serial);		  // Do nothing if no serial port is opened 
	delay(1000);
    Serial.println("\n\nSerial has begun");
    connectAWS(); //AWS
    Wire.begin(D1, D2); /* join i2c bus with SDA=D1 and SCL=D2 of NodeMCU */ //D1 - 5, D2 - 4
    Serial.println("Setup has ended!!");
}

void loop() {

 Wire.requestFrom(8, 13); 

 int distance = Wire.read();
 if (!client.connected()){
      connectAWS();
    } else {
      client.loop();
      if (distance < 10 && distance > 0){
        Serial.println(distance);
        publishMessage(distance);
      }
    }
  delay(1000);
}

