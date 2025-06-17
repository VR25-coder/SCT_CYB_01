# caesar_cipher.py

def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - shift_base + offset) % 26 + shift_base)
        else:
            result += char
    return result

message = input("Enter message: ")
shift = int(input("Enter shift value: "))
mode = input("Mode (encrypt/decrypt): ").lower()

print("Result:", caesar_cipher(message, shift, mode))
