#!/usr/bin/python3

import  random
import string

char = " "+string.ascii_letters + string.digits + string.punctuation

char = list(char)

key = char.copy()

random.shuffle(key)

ecrypted_massage = input("Enter a massage to encryption: ")

cipher_text = ""

for letter in ecrypted_massage:
    index = key.index(letter)
    cipher_text += char[index]
print(f"original massage : {ecrypted_massage}")
print(f"encrypted massage {cipher_text}")

