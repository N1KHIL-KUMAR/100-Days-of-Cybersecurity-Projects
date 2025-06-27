#!/usr/bin/python3

import requests
from urllib.parse import urlparse, urlencode, urljoin

redirect_params = ["next", "url", "redirect", "return", "dest", "destination"]


test_url = "http://evil.com"

def check_open_redirect(base_url):
    for param in redirect_params:
        payload = {param: test_url}
        full_url = f"{base_url}?{urlencode(payload)}"

        try:
            response = requests.get(full_url, allow_redirects=False, timeout=5)
            
            if "Location" in response.headers:
                location = response.headers["Location"]
                if test_url in location:
                    print(f"[VULNERABLE] Possible open redirect found: {full_url}")
                else:
                    print(f"[OK] Redirects elsewhere: {full_url}")
            else:
                print(f"[SAFE] No redirect: {full_url}")

        except Exception as e:
            print(f"[ERROR] Could not test {full_url}: {e}")

target = input("Enter base URL (e.g. https://example.com/login): ")
check_open_redirect(target)

