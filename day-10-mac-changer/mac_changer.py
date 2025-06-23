#!/usr/bin/python3

import os

def macchanger(interface,new_mac):
    try:
        print(f"[+] Changing MAC address for {interface} to {new_mac}")

        os.system(f"sudo ifconfig {interface} down")
        os.system(f"sudo ifconfig {interface} hw ether {new_mac}")
        os.system(f"sudo ifconfig {interface} up")
        print("[+] MAC address changed successfully ")
    except Exception as e:
        print(f"Error {e}")
if __name__ == "__main__":
    interface = input("[+]Enter interface (e.g., eth0 or wlan0): ")
    new_mac = input("[+]Enter new MAC address (e.g., 00:11:22:33:44:55): ")
    macchanger()
