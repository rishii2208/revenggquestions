def decode_utf16(encoded_text: str) -> str:
    return ''.join(chr(int(code, 16)) for code in encoded_text.split())

if __name__ == "__main__":
    encoded_input = input()
    print(decode_utf16(encoded_input))
