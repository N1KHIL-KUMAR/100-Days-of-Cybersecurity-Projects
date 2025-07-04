#!/usr/bin/python3

# tcp listener 

import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("0.0.0.0",4444))
s.listen(1)
print("Listening On Ip (0.0.0.0) .....")

conn,addr = s.accept()
print(f"connection recv form {addr}")

conn.close()
s.close()
