#!/usr/bin/python3


import whois
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="WHOIS Lookup - Simple Command Line Tool",
        usage="Usage: %(prog)s -d example.com"
    )
    parser.add_argument("-d", help="Domain for the WHOIS lookup", dest="domain", required=True)
    args = parser.parse_args()
    domain = args.domain
    try:
        who = whois.whois(domain)
        print(f"[+] Domain Name: {who.domain_name}")
        print(f"[+] IP : {who.ip}")
        print(f"[+] Registrar: {who.registrar}")
        print(f"[+] Creation Date: {who.creation_date}")
        print(f"[+] Expiration Date: {who.expiration_date}")
        print(f"[+] Name Servers: {who.name_servers}")
        print(f"[+] Emails: {who.emails}")
        print(f"[+] State:{who.state}")
        print(f"[+] Country: {who.country}")
    except Exception as e:
        print(f"Error {e}")
if __name__ == "__main__":
    main()
