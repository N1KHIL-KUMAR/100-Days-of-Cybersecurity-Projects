#!/usr/bin/python3

import requests

def dir_brute_force(url):
    try:
        with open('wordlist.txt', 'r') as file:
            for word in file:
                word = word.strip()
                dir_url = f"{url}/{word}/"
                try:
                    r = requests.get(dir_url, timeout=5)
                    print(f"[-_-] Status Code {r.status_code}: {dir_url}")
                except requests.exceptions.HTTPError as e:
                    print("HTTP Error:", e)
                except requests.exceptions.ConnectionError as e:
                    print("Connection Error:", e)
                except requests.exceptions.Timeout as e:
                    print("Timeout Error:", e)
                except requests.exceptions.RequestException as e:
                    print("Other Request Error:", e)
    except FileNotFoundError:
        print("[-] wordlist.txt not found!")

if __name__ == "__main__":
    url = input("[+] Enter your URL: ").strip()
    dir_brute_force(url)

