import string

def rot13_decoder(encrypted_text):
    """Deciphers the ancient Rot13 spell and restores the original text."""
    try:
        # ROT13 Transform (Reverses by applying the same shift)
        rot_map = str.maketrans(
            string.ascii_lowercase + string.ascii_uppercase,
            string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
            string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
        )

        original_text = encrypted_text.translate(rot_map)
        return original_text

    except Exception as curse:
        print(f"💀 The script resists decoding: {curse}")
        return None


encoded_text = "nepnar_vafpevcgvba.gkg"
decoded_text = rot13_decoder(encoded_text)
print("Decoded text:", decoded_text)