#!/usr/bin/python3

import sys
import hashlib

# Sample password list
pass_list = ["admin", "kalu", "admin123", "kamu12"]

def md5_hash_cracker():
    try:
        if len(sys.argv) < 2:
            print("Usage: python script.py <md5_hash>")
            return

        target_hash = sys.argv[1] 

        for password in pass_list:
            hashed = hashlib.md5(password.encode()).hexdigest()
            if hashed == target_hash: #conditional statement checking equal 
                print(f"[+] Password Found: {password}")
                return

        print("[-] Password Not Found in List.")

    except Exception as e:
        print(f"Error: {e}")

md5_hash_cracker()
