#!/usr/bin/python3


from netaddr import IPNetwork

# Iterate over all IPs in the network
for ip in IPNetwork("127.0.0.0/24"):
    print(ip)
