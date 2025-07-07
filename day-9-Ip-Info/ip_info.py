#!/usr/bin/python3

import requests
import socket

#function 
def ip_location(ip_or_host):
    try:
        # Try to resolve if user entered a domain name
        resolved_ip = socket.gethostbyname(ip_or_host)
    except socket.gaierror:
        print(f"[!] Could not resolve hostname: {ip_or_host}")
        return

    url = f"https://ipinfo.io/{resolved_ip}?token=ce829153bdbed1"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        logs = r.json()
        print(f"\n[+] Location Info for: {ip_or_host} ({resolved_ip})")
        for key, value in logs.items():
            print(f"{key.capitalize()} : {value}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Error fetching IP info: {e}")

if __name__ == "__main__":
    ip = input("Enter IP or Hostname: ")
    ip_location(ip)
