import os
import base64
from colorama import init, Fore
import pyfiglet

init()

WHITE = "\033[1;37m"
CYAN = "\033[1;36m"
BLUE = "\033[1;34m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"

os.system('clear')

print(WHITE)
print(pyfiglet.figlet_format('PXPASS', font="slant"))

print(CYAN + "════════════════════════════════════════════════════")
print(Fore.LIGHTBLACK_EX + " ✨This tool was made by 'BOYARB🍷'")
print(" ✨The tool is open source!!")
print(CYAN + "════════════════════════════════════════════════════")
print(WHITE)

def encode_base64(message):
    return base64.b64encode(message.encode('utf-8')).decode('utf-8')

def decode_base64(encoded_message):
    try:
        return base64.b64decode(encoded_message.encode('utf-8')).decode('utf-8')
    except Exception:
        return None  


def main():
    while True:
        print(CYAN)
        print("╔════════════════════════════════════════════════╗")
        print("║  1 : Text encryption                           ║")
        print("║                                                ║")
        print("║  2 : To decrypt text                           ║")
        print("║                                                ║")
        print("║  3 : Exit                                      ║")
        print("╚════════════════════════════════════════════════╝")
        print(BLUE)

        choice = input("Enter the number: ")
        print(WHITE)

        if choice == "1":
            message = input("Enter text to encrypt it: ")
            if not message.strip():  
                print(RED + "Error: No text entered. Please enter some text to encrypt.")
            else:
                encoded_message = encode_base64(message)
                print(YELLOW + f"Encrypted text: [{encoded_message}]")

        elif choice == "2":
            encoded_message = input("Enter the ciphertext: ")
            decoded_message = decode_base64(encoded_message)
            if decoded_message:
                print(YELLOW + f"Decrypted text: [{decoded_message}]")
            else:
                print(RED + """Error: Invalid input. Unable to decode the text.
Please check and try again.""")

        elif choice == "3":
            print(RED + "Exit")
            break

        else:
            print(RED + "Invalid choice, please try again.")


if __name__ == "__main__":
    main()
