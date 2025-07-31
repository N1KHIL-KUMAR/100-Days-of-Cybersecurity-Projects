#!/usr/bin/python3

import argparse # argument for
import socket #connection 

def convert_ip(url):
    try: #keyword for error handling 
        ip = socket.gethostbyname(url)
        return ip
    except socket.gaierror:
        return "Invalid domain or connection issue."

def main():
    parser = argparse.ArgumentParser(
        description="IP extractor from domain",
        usage="Example: %(prog)s -d google.com"
    )
    parser.add_argument("-d", "--domain", help="Only enter domain name", required=True)
    args = parser.parse_args()

    ip_address = convert_ip(args.domain)
    print(f"[+] IP Address of {args.domain} is: {ip_address}")

if __name__ == "__main__":
    main()

