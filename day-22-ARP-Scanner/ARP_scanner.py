#!/usr/bin/python3

# Arp Scanner

from scapy.all import ARP, Ether, srp

# Target IP range
target_ip = "172.168.70.0/24"


arp_request = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff") # mac 

packet = ether / arp_request #checking 

result = srp(packet, timeout=2, verbose=0)[0]


for sent, received in result:
    print(f"IP: {received.psrc}, MAC: {received.hwsrc}")
