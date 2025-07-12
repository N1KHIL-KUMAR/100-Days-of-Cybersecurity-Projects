#!/usr/bin/python3

from scapy.all import ICMP, IP, sr1
import ipaddress

def ping_scapy(ip):
    pkt = IP(dst=str(ip))/ICMP()
    reply = sr1(pkt, timeout=1, verbose=0)
    return reply is not None

def sweep_network(network):
    alive = []
    net = ipaddress.ip_network(network, strict=False)

    for ip in net.hosts():
        if ping_scapy(ip):
            print(f"[+] {ip} is up")
            alive.append(str(ip))
        else:
            print(f"[-] {ip} is down")
    return alive

if __name__ == "__main__":
    sweep_network("192.168.1.0/24")

