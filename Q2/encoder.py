map = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..' 
}

def converttext(text, map):
    temp = ''
    for ch in text:
        if ch == ' ': temp += 'x'
        elif ch.upper() in map: temp += map[ch.upper()] + 'x'
    if (len(temp) % 2): temp = temp[:len(temp) - 1]
    return temp

def encrypt(text, key):
    temp = []
    key_pairs = ['..', '.-', '.x', '-.', '--', '-x', 'x.', 'x-', 'xx']
    for i in range(0, len(text), 2):
        temp.append(str(key[key_pairs.index(text[i:i+2])]))
    return ''.join(temp)

text = input('Enter Input String:\n')
key = '123456789'
output = encrypt(converttext(text, map), key)
print(f"Encoded Output:\n{output}")
