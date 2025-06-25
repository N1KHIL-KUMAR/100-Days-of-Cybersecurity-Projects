#!/usr/bin/python3

import requests

def find_subdomains(domain, wordlist_file, output_file):
    try:
        with open(wordlist_file, 'r') as words:
            wordlist = words.read().splitlines()
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist_file}' not found.")
        return

    found = []

    for word in wordlist:
        subdomain = f"http://{word}.{domain}"
        try:
            response = requests.get(subdomain, timeout=2)
            if response.status_code < 400:
                print(f"[+] Found: {subdomain}")
                found.append(subdomain)
        except requests.RequestException:
            pass  

    with open(output_file, 'w') as f:
        for sub in found:
            f.write(sub + '\n')

    print(f"\nSaved {len(found)} subdomains to '{output_file}'.")


target_domain = "example.com"
wordlist = "wordlist.txt"  
output = "found_subdomains.txt"

find_subdomains(target_domain, wordlist, output)
