import base64

def decode_text(encoded_text):
    print("Decoding the mysterious symbols...")
    try:
        decoded_bytes = base64.b64decode(encoded_text.encode("utf-8"))
        original_text = decoded_bytes.decode("utf-8")
        return original_text
    except Exception as e:
        print("The time vortex rejected the input.")
        return str(e)

# Example usage
test_encoded = "dGJmamFrZmph"  # Encoded version of "Beware of the blue llamas."
print("Decoded output:", decode_text(test_encoded))

