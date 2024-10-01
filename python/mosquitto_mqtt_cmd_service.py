# subscribe as new process
# set timer interval for 1 minute
# check file for new line with command
# if new line appeared, close subscription execute command with stdout to FILE, clear line, publish FILE
# if not, publish READY message

import subprocess
import os
from paho.mqtt import client

broker_url = "f30aecedfa9d4b97a6d732678e116680.s2.eu.hivemq.cloud"
broker_port = 8883

cmd_file = open("mqtt_command", "r")
cmd = cmd_file.readline().strip()
if cmd != "":
    try:
        std_output = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as error:
        std_output = error.returncode            
    cmd_file.close()
    open("mqtt_command", "w").close()
    cmdd = "mosquitto_pub -h  -p 8883 -u  -P  -t /cmd/out -m '" + std_output.decode("utf-8") + "'"
else:
    std_output = "READY"
    cmdd = "mosquitto_pub -h  -p 8883 -u  -P  -t /cmd/out -m '" + std_output + "'"
    cmd_file.close()


ok = subprocess.check_output(cmdd, shell=True)

#client1 = client.Client("control1", protocol=client.MQTTv5)
#client1.username_pw_set(username="", password="")
#client1.connect(broker_url, broker_port)
#client1.publish("/cmd/out", std_output)
#client1.disconnect()
print(std_output)
