import base64

def base64_fun(choice):
    try:
        if choice == 1:
            encode_user = input("Enter your value to encode: ")
            base64_bytes = base64.b64encode(encode_user.encode("ascii"))
            return f"Encoded Base64: {base64_bytes.decode('ascii')}"
        
        elif choice == 2:
            decode_user = input("Enter your Base64 value to decode: ")
            decoded_bytes = base64.b64decode(decode_user)
            return f"Decoded Text: {decoded_bytes.decode('ascii')}"
        
        else:
            return "[+] Invalid Choice"

    except Exception as e:
        return f"[+] Error: {e}"

if __name__ == "__main__":
    print("1. Encode")
    print("2. Decode")
    try:
        choice = int(input("Enter Your Choice: "))
        print(base64_fun(choice))
    except ValueError:
        print("[+] Please enter a valid number.")

