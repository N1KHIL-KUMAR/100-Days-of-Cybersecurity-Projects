#!/usr/bin/python3

import hashlib

def hash_string(input_string):
    print("MD5:    ->> ", hashlib.md5(input_string.encode()).hexdigest())
    print("SHA1:   ->> ", hashlib.sha1(input_string.encode()).hexdigest())
    print("SHA224: ->> ", hashlib.sha224(input_string.encode()).hexdigest())
    print("SHA256: ->> ", hashlib.sha256(input_string.encode()).hexdigest())
    print("SHA384: ->> ", hashlib.sha384(input_string.encode()).hexdigest())
    print("SHA512: ->> ", hashlib.sha512(input_string.encode()).hexdigest())

def main():
    print("---- Hash Identifier Tool -----")
    user_input = input("[+] Enter a string to hash: ")
    hash_string(user_input)

if __name__ == "__main__":
    main()

