# subscribe as new process
# set timer interval for 1 minute
# check file for new line with command
# if new line appeared, close subscription execute command with stdout to FILE, clear line, publish FILE
# if not, publish READY message

import subprocess
import os
from paho.mqtt import client

broker_url = ""
broker_port = 8883

cmd_file = open("mqtt_command", "r")
cmd = cmd_file.readline().strip()
if cmd != "":
    try:
        std_output = subprocess.check_output(cmd)
    except subprocess.CalledProcessError as error:
        std_output = error.returncode            
    cmd_file.close()
    open("mqtt_command", "w").close()
else:
    std_output = "READY"
    cmd_file.close()

# subprocess.call("mosquitto_pub -h  -p 8883 -u  -P  -t /cmd/out -m 'hej'")

client1 = client.Client("control1", protocol=client.MQTTv5)
client1.username_pw_set(username="", password="")
client1.connect(broker_url, broker_port)
client1.publish("/cmd/out", std_output)
client1.disconnect()
# print(std_output)
