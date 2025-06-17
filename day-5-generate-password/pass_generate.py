import random
import string

def generate_password(length):
    # Combine letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters from the combined string
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for desired password length
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Please enter a positive number.")
    else:
        print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
