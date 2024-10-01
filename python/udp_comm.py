import socket
import sys
from time import sleep

local_ip = socket.gethostbyname(socket.gethostname())
local_ip = socket.gethostbyname(socket.getfqdn())
local_port = 8887

remote_ip = socket.gethostbyname_ex("esp8266.local")[2][0]
remote_port = 8888

MESSAGE = b"okej\n"

# udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# udp.sendto(MESSAGE, (remote_ip, remote_port))
# udp.close()

print(remote_ip)

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((remote_ip, local_port))
data, addr = udp.recvfrom(1024)
print(data)