#include <ESP8266WiFi.h>
#include <WiFiClient.h>
// #include <Ethernet.h>
//#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
// #include <WiFiUDP.h>
//#include "OSCMessage.h"

#ifndef STASSID
#define STASSID ""
#define STAPSK  ""
#endif

/*
D5 14
D6 12
D7 13
D8 15
 */
 
// declaring modules usage
WiFiUDP UDP;

// creating pinout variables
const int led = 13;
const int adc = A0;
const int d0 = 15; //d8
const int d1 = 13; //d7
const int d2 = 12; //d6

// networking
const char* ssid     = STASSID;
const char* password = STAPSK;
uint16_t port_number = 10001;
IPAddress receiver_IP = 0;
int size = 0;

size_t msg_buf_size = 24;
// serial connection
const int baudRateValue = 9600;

// variables for ADC
int adcVal = 0;

// delay for uc steps debug
float step_time = 0;
float total_loop_delay = 1000;


void setup() {
  // begin setup
  
  // bulit-in diode pinout mode
  pinMode(led, OUTPUT);
  
  // pinouts for binary counter for mx 
  pinMode(d0, OUTPUT);
  pinMode(d1, OUTPUT);
  pinMode(d2, OUTPUT);

  // starting WiFi
  WiFi.mode(WIFI_STA);

  // starting serial
  Serial.begin(baudRateValue);
  WiFi.begin(ssid, password);
  
  Serial.println();
  Serial.println("connecting to ");
  Serial.println(ssid);
  // connecting to WiFi
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print("_");
    delay(800);
    Serial.print(".");
  }
  Serial.println("connected to ");
  Serial.println(ssid);
  Serial.print("my IP is  ");
  Serial.println(WiFi.localIP());
  Serial.print("my MAC is ");
  Serial.println(WiFi.macAddress());
  Serial.print("and host IP is ");
  Serial.println(WiFi.gatewayIP());

  // starting UDP
  if (UDP.begin(port_number)) {
    Serial.println("started udp");
  }
  

  // end of setup
  }

void loop() {
  // beign loop
// check if not connected, connect else normal operation
  // Serial.println(WiFi.status());
  if(WiFi.status() != WL_CONNECTED) {
//if(WiFi.status() == WL_IDLE_STATUS)
    delay(100);
    Serial.print("_");
    delay(800);
    Serial.print(".");
  }
else {

  char value[4];
  char out_buffer[msg_buf_size] = " ";
  
  strcat(out_buffer, " ");
  digitalWrite(d0, LOW);
  digitalWrite(d1, LOW);
  digitalWrite(d2, LOW); // mx 2
  // gather data from 2
  adcVal = analogRead(adc); //1024
  dtostrf(adcVal, 8, 0, value);
  strcat(out_buffer, value);
  //  strcat(out_buffer, ";");
  delay(step_time);


  strcat(out_buffer, " ");
  digitalWrite(d0, LOW);
  digitalWrite(d1, LOW);
  digitalWrite(d2, HIGH); // mx 4
  // gather data from 4
  adcVal = analogRead(adc); //1024
  dtostrf(adcVal, 8, 0, value);
  strcat(out_buffer, value);
  //  strcat(out_buffer, ";");
  delay(step_time);


  strcat(out_buffer, " ");
  digitalWrite(d0, LOW);
  digitalWrite(d1, HIGH);
  digitalWrite(d2, LOW); // mx 6
  // gather data from 6
  adcVal = analogRead(adc); //1024
  dtostrf(adcVal, 8, 0, value);
  strcat(out_buffer, value);
  //  strcat(out_buffer, ";");
  delay(step_time);

  
  
  //    CREATE BUFFER FOR SENDING TO UDP
// how to do this efficiently on this hardware?
  // notice UDP reception and establish address
  size = UDP.parsePacket();
  if (size > 0) 
  { 


    


    Serial.println("received UDP packet of size:");
    Serial.println(size);
    Serial.println("from IP:");
    Serial.println(UDP.remoteIP());

    while(size--) 
    {
      UDP.read();
      Serial.println(UDP.read());
      
    }
  
  // send to UDP
    UDP.beginPacket(UDP.remoteIP(), port_number);
    UDP.write(out_buffer, msg_buf_size);

    Serial.println("sending packets to:");
    Serial.println(UDP.destinationIP());

    
    UDP.endPacket();
    UDP.flush();
    Serial.println(out_buffer);

    // print values


  }
  


  if (Serial.available() > 0) {
  //     read the incoming byte:
  //       out_buffer = Serial.read();

    // say what you got:
    Serial.println("received:");
    
    }    
 
} //end of else from connection status
  delay(total_loop_delay);
 
  // end of loop
}
