# Braille Decoder

reverse_braille_dict = {
    '⠁': 'a', '⠃': 'b', '⠉': 'c', '⠙': 'd', '⠑': 'e', '⠋': 'f', '⠛': 'g', '⠓': 'h', '⠊': 'i', '⠚': 'j',
    '⠅': 'k', '⠇': 'l', '⠍': 'm', '⠝': 'n', '⠕': 'o', '⠏': 'p', '⠟': 'q', '⠗': 'r', '⠎': 's', '⠞': 't',
    '⠥': 'u', '⠧': 'v', '⠺': 'w', '⠭': 'x', '⠽': 'y', '⠵': 'z', ' ': ' ', 
    '⠠⠁': 'A', '⠠⠃': 'B', '⠠⠉': 'C', '⠠⠙': 'D', '⠠⠑': 'E', '⠠⠋': 'F', '⠠⠛': 'G', '⠠⠓': 'H',
    '⠠⠊': 'I', '⠠⠚': 'J', '⠠⠅': 'K', '⠠⠇': 'L', '⠠⠍': 'M', '⠠⠝': 'N', '⠠⠕': 'O', '⠠⠏': 'P',
    '⠠⠟': 'Q', '⠠⠗': 'R', '⠠⠎': 'S', '⠠⠞': 'T', '⠠⠥': 'U', '⠠⠧': 'V', '⠠⠺': 'W', '⠠⠭': 'X',
    '⠠⠽': 'Y', '⠠⠵': 'Z', '⠖': '!', '⠦': '?', '⠲': '.', '⠂': ','
}

def decode_from_braille(braille_text):
    output = []
    skip_next = False
    for i, char in enumerate(braille_text):
        if skip_next:
            skip_next = False
            continue
        if char == '⠠' and i + 1 < len(braille_text):
            output.append(reverse_braille_dict.get(char + braille_text[i + 1], '?'))
            skip_next = True
        else:
            output.append(reverse_braille_dict.get(char, '?'))
    return ''.join(output)

if __name__ == "__main__":
    braille_input = input("Enter Braille to decode: ")
    decoded_output = decode_from_braille(braille_input)
    print("Decoded Text:", decoded_output)
