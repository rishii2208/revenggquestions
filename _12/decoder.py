import random

def flibber_wobble_decoder(cursed_text, key):
    """Reverses the cosmic gibberish back to its original form."""
    try:
        # Decrypt the text using the provided XOR key
        decrypted_chars = [chr(ord(c) ^ key) for c in cursed_text]
        original_text = "".join(decrypted_chars)
        return original_text
    except Exception as e:
        print("🌀 The cosmic forces resist decoding: ", e)
        return None

# Example usage
example_text = "l.jed-txt"
key = random.randint(1, 255)  # Same key must be used for encoding & decoding

# Encrypt using the same logic as flibber_wobble
encrypted_chars = [chr(ord(c) ^ key) for c in example_text]
cursed_text = "".join(encrypted_chars)

# Decrypt
decoded_text = flibber_wobble_decoder(cursed_text, key)
print("Decoded text:", decoded_text)