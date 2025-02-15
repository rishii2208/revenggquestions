map = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..' 
}

output = input('Enter Output: ')
key = '123456789'

rev_map = {value: key for key, value in map.items()}

def decrypt(text, key):
    temp = ''
    key_pairs = ['..', '.-', '.x', '-.', '--', '-x', 'x.', 'x-', 'xx']
    for i in text:
        temp += key_pairs[int(i) - 1]
    return temp

def deconverttext(morse, rev_map):
    morse = morse.split('x')
    decoded= ''

    for morse_ch in morse:
        if morse_ch == '':
            decoded += ' '
        elif morse_ch in rev_map:
            decoded += rev_map[morse_ch]
    return decoded

print(f"Decoded Input: {deconverttext(decrypt(output, key), rev_map)}")