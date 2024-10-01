from paho.mqtt import client
from paho.mqtt import publish
import random

broker_ip   = "f30aecedfa9d4b97a6d732678e116680.s2.eu.hivemq.cloud"
broker_port = 8883
msg_content = ""
msg_length = 32
for x in range(msg_length):
    msg_content = msg_content + chr(int.from_bytes(random.randbytes(1))%127 + 32)

print(msg_content, "\nmessage length:", msg_length)

client1 = client.Client("control1")
client1.username_pw_set(username="", password="")
client1.connect(broker_ip, broker_port, )
client1.publish("/cmd/out", msg_content)
