def encode_utf16(text: str) -> str:
    """
    Converts each character in the input text to its UTF-16 hexadecimal representation.
    """
    return ' '.join(f'{ord(char):04X}' for char in text)  # Convert each character to a 4-digit uppercase hex code

if __name__ == "__main__":
    input_text = input()  # Read input string from the user
    print(encode_utf16(input_text))  # Print the UTF-16 encoded string
