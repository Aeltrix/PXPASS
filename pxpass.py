import os
import base64
import zlib
import hashlib
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
from colorama import init, Fore
import pyfiglet

init()

WHITE = "\033[1;37m"
CYAN = "\033[1;36m"
BLUE = "\033[1;34m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"

# مفتاح ثابت (سيتم توليده باستخدام SHA-256 لضمان الطول 32 بايت)
static_key = "thisisaverystrongkey1234"  
key = hashlib.sha256(static_key.encode()).digest()

def encode_chacha_compressed(message):
    compressed_message = zlib.compress(message.encode('utf-8'), level=9)
    nonce = get_random_bytes(8)  # توليد nonce عشوائي
    cipher = ChaCha20.new(key=key, nonce=nonce)
    encrypted_message = cipher.encrypt(compressed_message)
    return base64.b64encode(nonce + encrypted_message).decode('utf-8')

def decrypt_chacha_compressed_multiple_nonces(encoded_message):
    try:
        decoded_data = base64.b64decode(encoded_message)
        encrypted_message = decoded_data[8:]  # استخراج النص المشفر
        potential_nonces = [decoded_data[:8]]  # إضافة الـnonce المخزن في النص المشفر
        potential_nonces.append(get_random_bytes(8))  # إضافة nonce عشوائي للمحاولة

        # محاولة فك التشفير باستخدام nonces متعددة
        for nonce in potential_nonces:
            try:
                cipher = ChaCha20.new(key=key, nonce=nonce)  # استخدام الـnonce في عملية فك التشفير
                decrypted_message = cipher.decrypt(encrypted_message)  # فك التشفير
                return zlib.decompress(decrypted_message).decode('utf-8')  # إذا تم فك التشفير بنجاح
            except Exception:
                continue  # إذا فشل فك التشفير بـnonce، نجرب الـnonce التالي

    except Exception:
        return None  # في حالة حدوث خطأ عام

    return None  # إذا فشل فك التشفير بكل الـnonces

def main():
    os.system('clear')

    print(WHITE)
    print(pyfiglet.figlet_format('PXPASS', font="slant"))

    print(CYAN + "════════════════════════════════════════════════════")
    print(Fore.LIGHTBLACK_EX + " ✨This tool was made by 'BOYARB🍷'")
    print(" ✨The tool is open source. Strong safety force ")
    print(CYAN + "════════════════════════════════════════════════════")
    print(WHITE)

    while True:
        print(CYAN)
        print("╔════════════════════════════════════════════════╗")
        print("║  1 : Text encryption                           ║")
        print("║                                                ║")
        print("║  2 : To decrypt text                           ║")
        print("║                                                ║")
        print("║  3 : Contact me                                ║")
        print("║                                                ║")
        print("║  4 : Exit                                      ║")
        print("╚════════════════════════════════════════════════╝")
        print(BLUE)

        choice = input("Enter the number: ")
        print(WHITE)

        if choice == "1":
            message = input("Enter text to encrypt it: ")
            if not message.strip():
                print(RED + "Error: No text entered. Please enter some text to encrypt.")
            else:
                encoded_message = encode_chacha_compressed(message)
                print(YELLOW + f"Encrypted text: [{encoded_message}]")

        elif choice == "2":
            encoded_message = input("Enter the ciphertext: ")
            decoded_message = decrypt_chacha_compressed_multiple_nonces(encoded_message)
            if decoded_message:
                print(YELLOW + f"Decrypted text: [{decoded_message}]")
            else:
                print(RED + """Error: Invalid input. Unable to decode the text.
Please check and try again.""")

        elif choice == "3":
            print(WHITE + "\nConnect with me on Facebook:")
            print(WHITE + """https://www.facebook.com/profile.php?id=100095163105482&mibextid=ZbWKwL""")
            print()

        elif choice == "4":
            print(RED + "Exit")
            break

        else:
            print(RED + "Invalid choice, please try again.")

if __name__ == "__main__":
    main() 
