#!/usr/bin/python3

import socket
import sys

# command line argument port scanner usage : Usage: python script.py <host> <port>

def portscanner():
    if len(sys.argv) < 3:
        print("Usage: python script.py <host> <port>")
        return
    host = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except ValueError:
        print(f"Port must be an integer. Example : Port 80 , 443 , 53")
        return
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((host,port))
        print(f"🔵 Open {port}")
    except:
        print(f"🔴 Close {port}")

portscanner()
