def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isupper():
            encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isupper():
            decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message

def main():
    message = input("Enter the message to encrypt/decrypt: ")
    shift = int(input("Enter the shift value (an integer between 1 and 25): "))

    encrypted_message = encrypt(message, shift)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
