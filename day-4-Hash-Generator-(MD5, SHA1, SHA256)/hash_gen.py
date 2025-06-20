#!/user/bin/python3
#Hash Generator (MD5, SHA1, SHA256)

import hashlib

def hash_gen(hash):
    if choice == 1:
        try:
            hash_gen = hashlib.md5(hash.encode()).hexdigest()
            return f"md5 hash :{hash_gen}"
        except Exception as e:
            return f"Error{e}"
    elif choice == 2:
        try:
            hash_gen = hashlib.sha1(hash.encode()).hexdigest()
            return f"Sha1 hash :{hash_gen}"
        except Exception as e:
            return f"Error{e}"
    elif choice == 3:
        try:
            hash_gen = hashlib.sha1(hash.encode()).hexdigest()
            return f"Sha256 hash :{hash_gen}"
        except Exception as e:
            return f"Error{e}"

if __name__ == "__main__":
    print("------- Hash Generator (MD5, SHA1, SHA256) -------")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")

    try:
        choice = int(input("\n[+] Enter Your choice (like 1): "))
    except ValueError:
        print(f"\n[error] 'int' value (choice : 1)")
        exit()
    if choice >= 4:
        print(f"[error] Not Valid Choice : {choice} ")
        exit()
    hash = (input("\n[+] Enter Your value : "))
    print(hash_gen(hash))

