import codecs
import base64

MORSE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def caesar_cipher(text, shift, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            offset = -shift if decrypt else shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result


def vigenere_cipher(text, key, decrypt=False):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord("a")
            if decrypt:
                shift = -shift
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result


def rot13(text):
    return codecs.encode(text, "rot_13")


def base64_encode(text):
    return base64.b64encode(text.encode()).decode()


def base64_decode(text):
    return base64.b64decode(text.encode()).decode()


def morse_encode(text):
    return " ".join(MORSE_DICT.get(char.upper(), "") for char in text)


def morse_decode(code):
    reverse_dict = {v: k for k, v in MORSE_DICT.items()}
    return "".join(reverse_dict.get(char, "") for char in code.split())


def main():
    print("Welcome to the Encryption Tool!")
    print("1. Encrypt with Caesar")
    print("2. Decrypt with Caesar")
    print("3. Encrypt with Vigenère")
    print("4. Decrypt with Vigenère")
    print("5. Encode with ROT13")
    print("6. Encode with Base64")
    print("7. Decode Base64")
    print("8. Encode with Morse")
    print("9. Decode Morse")
    choice = input("Choose an option (1-9): ")

    text = input("Enter your message: ")

    if choice == "1":
        shift = int(input("Enter shift value: "))
        print("🔒 Encrypted:", caesar_cipher(text, shift))
    elif choice == "2":
        shift = int(input("Enter shift value: "))
        print("🔓 Decrypted:", caesar_cipher(text, shift, decrypt=True))
    elif choice == "3":
        key = input("Enter keyword: ")
        print("🔒 Encrypted:", vigenere_cipher(text, key))
    elif choice == "4":
        key = input("Enter keyword: ")
        print("🔓 Decrypted:", vigenere_cipher(text, key, decrypt=True))
    elif choice == "5":
        print("🔁 ROT13:", rot13(text))
    elif choice == "6":
        print("📦 Base64 Encoded:", base64_encode(text))
    elif choice == "7":
        print("📦 Base64 Decoded:", base64_decode(text))
    elif choice == "8":
        print("📡 Morse Encoded:", morse_encode(text))
    elif choice == "9":
        print("📡 Morse Decoded:", morse_decode(text))
    else:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
