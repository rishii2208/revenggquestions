# Emoji Cipher Decoder (Text-Based Emojis)

# Mapping of unique text emojis to letters
EMOJI_TO_LETTER = {
    '(ᵔᴥᵔ)': 'A', '(•ω•)': 'B', '(◕‿◕)': 'C', '(≧▽≦)': 'D', '(＾▽＾)': 'E',
    '(¬‿¬)': 'F', '(◠‿◠)': 'G', '(✿◠‿◠)': 'H', '(◕‿◕✿)': 'I', '(◠ω◠)': 'J',
    '(◠△◠)': 'K', '(◠‿◠✿)': 'L', '(◠﹏◠)': 'M', '(◠‿◠)ノ': 'N', '(◠‿◠✿)ノ': 'O',
    '(◠‿◠)♡': 'P', '(◠‿◠✿)♡': 'Q', '(◠‿◠)♫': 'R', '(◠‿◠✿)♫': 'S', '(◠‿◠)☼': 'T',
    '(◠‿◠✿)☼': 'U', '(◠‿◠)☁': 'V', '(◠‿◠✿)☁': 'W', '(◠‿◠)✧': 'X', '(◠‿◠✿)✧': 'Y',
    '(◠‿◠)★': 'Z', '␣': ' '
}

def decode_emoji_cipher(encoded_text):
    """
    Decodes an emoji-encoded message back into plain text using unique text emojis.
    """
    decoded_text = []
    # Split the encoded text into individual emojis
    for emoji in encoded_text.split(' '):
        if emoji in EMOJI_TO_LETTER:
            decoded_text.append(EMOJI_TO_LETTER[emoji])
        else:
            decoded_text.append('')  # Skip unknown emojis
    return ''.join(decoded_text)

if __name__ == "__main__":
    # Input the encoded message
    encoded_message = input("Enter the encoded emoji cipher: ")
    
    # Decode the message
    decoded_message = decode_emoji_cipher(encoded_message)
    
    # Output the decoded text
    print("Decoded Message:")
    print(decoded_message)