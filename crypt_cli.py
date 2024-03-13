import argparse

def crypt(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher CLI Tool")
    parser.add_argument("-d", action="store_true", help="Enable decryption")
    parser.add_argument("-e", action="store_true", help="Enable encryption")
    parser.add_argument("-n", "--message", required=True, help="Message to encrypt/decrypt")
    parser.add_argument("-o", "--offset", required=True, type=int, help="Offset for encryption/decryption")

    args = parser.parse_args()

    if args.d and args.e:
        print("Invalid input. Choose either -d or -e, not both.")
        return

    if not (args.d or args.e):
        print("Invalid input. Choose -d for decryption or -e for encryption.")
        return

    try:
        result = crypt(args.message, args.offset if args.e else -abs(args.offset), 'decrypt' if args.d else 'encrypt')
        print(result)
    except ValueError as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    main()
