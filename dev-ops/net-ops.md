# network operations
net-tools network-manager arp arp-scan traceroute tracepath nmap ping

---
## device&driver management

### ifconfig

### nmtui & nmcli

### ip

---
## reconaissance

- CIDR - Classless Inter-Domain Routing notation: 192.168.0.0/24 - ip/mask; mask is : /24 is 255.255.255.0 subnet, 16 is 255.255.0.0 etc..
  
### nmap
Active network scanning
- ```nmap <ip>/<subnet>```

### arp-scan
Active scanning, sending ARP requests
- ```arp-scan --localnet```
- ```arp-scan <ip>```


### arp
Manipulating ARP cache

---
## data transmission

### netstat

### netcat
Sending and receiving TCP
- ```nc <ip> <port>``` - establish connection, send data
- ```nc -l <port>``` - listen on port

Sending and receiving UDP
- ```nc -ul <ip> <port>```