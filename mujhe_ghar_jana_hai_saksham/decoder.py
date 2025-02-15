# Morse Code Decoder
# Replaces "<" with "." and ">" with "-" to decode Morse code

MORSE_CODE_DICT = {
    '.<': 'A', '>...': 'B', '>.>.': 'C', '>..': 'D', '.': 'E', '..>.': 'F', '>>.': 'G', '....': 'H',
    '..': 'I', '.>>>': 'J', '>.>': 'K', '.>..': 'L', '>>': 'M', '>.': 'N', '>>>': 'O', '.>>.': 'P',
    '>>>.': 'Q', '.>.': 'R', '...': 'S', '>': 'T', '..>': 'U', '...>': 'V', '.>>': 'W', '>..>': 'X',
    '>.>>': 'Y', '>>..': 'Z',
    '.>>>>': '1', '..>>>': '2', '...>>': '3', '....>': '4', '.....': '5', '>....': '6', '>>...': '7',
    '>>>..': '8', '>>>>.': '9', '>>>>>': '0',
    '/': ' '
}

def decode_from_morse(encoded_text):
    """
    Decodes a given Morse code string (with '<' and '>' replacements) back into the original text.
    """
    # Replace '<' with '.' and '>' with '-' to convert to standard Morse code
    standard_morse = encoded_text.replace('<', '.').replace('>', '-')
    
    # Split the Morse code into individual codes
    morse_words = standard_morse.split(' / ')  # Split words
    decoded_text = []
    
    for word in morse_words:
        morse_chars = word.split(' ')  # Split characters
        decoded_word = []
        for code in morse_chars:
            if code in MORSE_CODE_DICT:
                decoded_word.append(MORSE_CODE_DICT[code])
            else:
                decoded_word.append('')  # Skip unknown codes
        decoded_text.append(''.join(decoded_word))
    
    return ' '.join(decoded_text)

if __name__ == "__main__":
    # Input from user
    encoded_text = input("Enter the encoded Morse code to decode: ")
    
    # Decode the Morse code
    decoded_text = decode_from_morse(encoded_text)
    
    # Output the decoded text
    print("Decoded Text:")
    print(decoded_text)