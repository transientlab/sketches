#include <ESP8266WiFi.h>
#include <Ticker.h>
// #include <WiFiClient.h>



// pinout
#define LED 2
#define O1  5  //d1
#define O2  4  //d2
#define O3  14 //d5
#define O4  12 //d6
#define O5  13 //d7
#define O6  15 //d8
#define O7  3  //tx  
#define O8  1  //tx
#define Ain A0 //a0
#define AD0 16 //d0
#define AD1 0  //d3
#define AD2 10 //s3

// serial port parameters
#define BAUDRATE 9600

// wifi parameters
#define STASSID ""
#define STAPSK  ""

WiFiServer server(80);
Ticker timer1;
Ticker timer2;
int sys_div = 0;
char sbuff[32];

String header;
// Current time
unsigned long currentTime = millis();
// Previous time
unsigned long previousTime = 0; 
// Define timeout time in milliseconds (example: 2000ms = 2s)
const long timeoutTime = 2000;

void configure_pins(void)
{
  pinMode(LED, OUTPUT);
  pinMode(O1, OUTPUT);
  pinMode(O2, OUTPUT);
  pinMode(O3, OUTPUT);
  pinMode(O4, OUTPUT);
  pinMode(O5, OUTPUT);
  pinMode(O6, OUTPUT);
  pinMode(O7, OUTPUT);
  pinMode(O8, OUTPUT);
  pinMode(AD0, OUTPUT);
  pinMode(AD1, OUTPUT);
  pinMode(AD2, OUTPUT);
}
void configure_serial(void)
{
  Serial.begin(BAUDRATE);
}
void sys_mx(void)
{
  switch(sys_div)
  {
    case 0:
    {
      digitalWrite(AD0, 0);
      digitalWrite(AD1, 0);
      digitalWrite(AD2, 0);
      break;
    }
    case 1:
    {
      digitalWrite(AD0, 1);
      digitalWrite(AD1, 0);
      digitalWrite(AD2, 0);
      break;
    }
    case 2:
    {
      digitalWrite(AD0, 0);
      digitalWrite(AD1, 1);
      digitalWrite(AD2, 0);
      break;
    }
    case 3:
    {
      digitalWrite(AD0, 1);
      digitalWrite(AD1, 1);
      digitalWrite(AD2, 0);
      break;
    }
    case 4:
    {
      digitalWrite(AD0, 0);
      digitalWrite(AD1, 0);
      digitalWrite(AD2, 1);
      break;
    }
    case 5:
    {
      digitalWrite(AD0, 1);
      digitalWrite(AD1, 0);
      digitalWrite(AD2, 1);
      break;
    }
    case 6:
    {
      digitalWrite(AD0, 0);
      digitalWrite(AD1, 1);
      digitalWrite(AD2, 1);
      break;
    }
    case 7:
    {
      digitalWrite(AD0, 1);
      digitalWrite(AD1, 1);
      digitalWrite(AD2, 1);
      break;
    }
  }
  sys_div+=1;
  if (sys_div == 8)
  {
    sys_div = 0;
  }
}
void sys_tick(void)
{
  digitalWrite(LED, 0);
  itoa(sys_div, sbuff, 16);
  Serial.println(sbuff);
  sys_mx();

  delay(1);
  digitalWrite(LED, 1);
}

void run_ticker(void)
{
  timer1.attach_ms(1000, sys_tick);
}
void run_wifi(void)
{
  WiFi.mode(WIFI_STA);
  WiFi.begin(STASSID, STAPSK);
  while (WiFi.status() != WL_CONNECTED) 
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("connected to    ");
  Serial.println(WiFi.SSID());
  Serial.print("my IP is        ");
  Serial.println(WiFi.localIP());
  Serial.print("my MAC is       ");
  Serial.println(WiFi.macAddress());
  Serial.print("and host IP is  ");
  Serial.println(WiFi.gatewayIP());
}

void setup() 
{
  delay(1000);
  configure_pins();
  configure_serial();
  
  run_wifi();
  
  run_ticker();

}

void loop() 
{ 
  WiFiClient client = server.available();
  if (client) {                             // If a new client connects,
    Serial.println("New Client.");          // print a message out in the serial port
    String currentLine = "";                // make a String to hold incoming data from the client
    currentTime = millis();
    previousTime = currentTime;
    while (client.connected() && currentTime - previousTime <= timeoutTime) { // loop while the client's connected
      currentTime = millis();         
      if (client.available()) {             // if there's bytes to read from the client,
        char c = client.read();             // read a byte, then
        Serial.write(c);                    // print it out the serial monitor
        header += c;
        if (c == '\n') {                    // if the byte is a newline character
          // if the current line is blank, you got two newline characters in a row.
          // that's the end of the client HTTP request, so send a response:
          if (currentLine.length() == 0) {
            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
            // and a content-type so the client knows what's coming, then a blank line:
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println("Connection: close");
            client.println();
            
            // if (header.indexOf("GET /5/on") >= 0) {
            //   Serial.println("GPIO 5 on");
            //   output5State = "on";
            //   digitalWrite(output5, HIGH);
            // } else if (header.indexOf("GET /5/off") >= 0) {
            //   Serial.println("GPIO 5 off");
            //   output5State = "off";
            //   digitalWrite(output5, LOW);
            // } 
            
            // Display the HTML web page
            client.println("<!DOCTYPE html><html>");
            client.println("<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">");
            client.println("<link rel=\"icon\" href=\"data:,\">");
            // CSS to style the on/off buttons 
            // Feel free to change the background-color and font-size attributes to fit your preferences
            client.println("<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}");
            client.println(".button { background-color: #195B6A; border: none; color: white; padding: 16px 40px;");
            client.println("text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}");
            client.println(".button2 {background-color: #77878A;}</style></head>");
            
            // Web Page Heading
            client.println("<body><h1>ESP8266 Web Server</h1>");
            client.println("</body></html>");
            // The HTTP response ends with another blank line
            client.println();
            break;
          } else { // if you got a newline, then clear currentLine
            currentLine = "";
          }
        } else if (c != '\r') {  // if you got anything else but a carriage return character,
          currentLine += c;      // add it to the end of the currentLine
        }
      }
    }
    // Clear the header variable
    header = "";
    // Close the connection
    client.stop();
    Serial.println("Client disconnected.");
    Serial.println("");
  }

}
