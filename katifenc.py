import base64, binascii, urllib.parse, codecs, os, time, random, html
from colorama import Fore, Style, init

init(autoreset=True)

# Colors for banner and name animation
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
reset = Style.RESET_ALL
blink = '\033[5m'

def banner():
    color = random.choice(colors)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(color + f"""
██╗  ██╗ █████╗ ████████╗██╗███████╗              ███████╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗
██║ ██╔╝██╔══██╗╚══██╔══╝██║██╔════╝              ██╔════╝████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
█████╔╝ ███████║   ██║   ██║█████╗      █████╗    █████╗  ██╔██╗ ██║██║     ██║   ██║██║  ██║█████╗  ██████╔╝
██╔═██╗ ██╔══██║   ██║   ██║██╔══╝      ╚════╝    ██╔══╝  ██║╚██╗██║██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
██║  ██╗██║  ██║   ██║   ██║██║                   ███████╗██║ ╚████║╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║    ██╗██╗
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝                   ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝

                          
                                   THE ENCODING / DECODING IN YOUR TERMINAL :)
""" + reset)

def blink_name():
    for _ in range(1):  # 3 baar blink hoga color change ke sath
        color = random.choice(colors)
        print(f"{blink}{color}                                    Created by Katif ahmad ~ katif_Enc Tool          {reset}")
        time.sleep(0.5)

# Encoder/Decoder Functions
def base64_encode(text): return base64.b64encode(text.encode()).decode()
def base64_decode(text): return base64.b64decode(text.encode()).decode()
def base32_encode(text): return base64.b32encode(text.encode()).decode()
def base32_decode(text): return base64.b32decode(text.encode()).decode()
def hex_encode(text): return binascii.hexlify(text.encode()).decode()
def hex_decode(text): return binascii.unhexlify(text.encode()).decode()
def url_encode(text): return urllib.parse.quote(text)
def url_decode(text): return urllib.parse.unquote(text)
def rot13_encode(text): return codecs.encode(text, 'rot_13')
def rot13_decode(text): return codecs.encode(text, 'rot_13')
def binary_encode(text): return ' '.join(format(ord(c), '08b') for c in text)
def binary_decode(text): return ''.join([chr(int(b, 2)) for b in text.split()])
def ascii_encode(text): return ' '.join(str(ord(c)) for c in text)
def ascii_decode(text): return ''.join([chr(int(c)) for c in text.split()])
def base85_encode(text): return base64.b85encode(text.encode()).decode()
def base85_decode(text): return base64.b85decode(text.encode()).decode()
def html_encode(text): return ''.join(f'&#{ord(c)};' for c in text)
def html_decode(text):
    return html.unescape(text)
# Menu and selection
def main():
    while True:
        banner()
        blink_name()
        print(Fore.YELLOW + """
[1] Base64 Encode/Decode
[2] Base32 Encode/Decode
[3] Hex Encode/Decode
[4] URL Encode/Decode
[5] ROT13 Encode/Decode
[6] Binary Encode/Decode
[7] ASCII Encode/Decode
[8] Base85 Encode/Decode
[9] HTML Encode/Decode
[0] Exit
""")

        choice = input(Fore.CYAN + "Enter your choice: ")

        if choice == '0':
            print(Fore.GREEN + "Thanks for using Katif_Enc Tool 💻")
            break

        text = input(Fore.BLUE + "Enter text: ")
        action = input(Fore.CYAN + "Do you want to Encode (E) or Decode (D)? ").lower()

        try:
            if choice == '1':
                result = base64_encode(text) if action == 'e' else base64_decode(text)
            elif choice == '2':
                result = base32_encode(text) if action == 'e' else base32_decode(text)
            elif choice == '3':
                result = hex_encode(text) if action == 'e' else hex_decode(text)
            elif choice == '4':
                result = url_encode(text) if action == 'e' else url_decode(text)
            elif choice == '5':
                result = rot13_encode(text) if action == 'e' else rot13_decode(text)
            elif choice == '6':
                result = binary_encode(text) if action == 'e' else binary_decode(text)
            elif choice == '7':
                result = ascii_encode(text) if action == 'e' else ascii_decode(text)
            elif choice == '8':
                result = base85_encode(text) if action == 'e' else base85_decode(text)
            elif choice == '9':
                result = html_encode(text) if action == 'e' else html_decode(text)
            else:
                print(Fore.RED + "Invalid choice!")
                continue

            print(Fore.GREEN + "\n" + "="*40)
            print(Fore.MAGENTA + "Result 🔥 : ", Fore.CYAN + result)
            print(Fore.GREEN + "="*40 + "\n")
            input(Fore.YELLOW + "Press Enter to continue...")

        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
