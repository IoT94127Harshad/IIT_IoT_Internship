#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

// WiFi Credentials
const char* ssid = "ONEPLUS NORD";
const char* password = "1234567890";

// MQTT Broker
const char* mqtt_server = "broker.hivemq.com";

// MQTT Topics
const char* temp_topic = "sensor/temperature";
const char* hum_topic  = "sensor/humidity";

// DHT Sensor
#define DHTPIN 4
#define DHTTYPE DHT11     // Use DHT22 if available

DHT dht(DHTPIN, DHTTYPE);

// WiFi & MQTT Client
WiFiClient espClient;
PubSubClient client(espClient);

// Connect to WiFi
void setup_wifi() {
  Serial.print("Connecting to WiFi");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Connected");
}

// Connect to MQTT
void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP32_Publisher")) {
      Serial.println("Connected");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  setup_wifi();

  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor");
    return;
  }

  char tempStr[8];
  char humStr[8];

  dtostrf(temperature, 6, 2, tempStr);
  dtostrf(humidity, 6, 2, humStr);

  client.publish(temp_topic, tempStr);
  client.publish(hum_topic, humStr);

  Serial.print("Temperature: ");
  Serial.print(tempStr);
  Serial.print(" °C | Humidity: ");
  Serial.print(humStr);
  Serial.println(" %");

  delay(5000);  // publish every 5 seconds
}
