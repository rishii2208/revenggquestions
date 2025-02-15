import random

def flibber_wobble(lost_words):
    """The cosmic winds whisper secrets to the void."""
    try:
        key = random.randint(1, 255) # A surprise cooking
        print(f"🌌 The stars align with key: {key}")  # Useless for security 😆

        # Encrypt the text using XOR magic
        encrypted_chars = [chr(ord(c) ^ key) for c in lost_words]
        cursed_text = "".join(encrypted_chars)

        gibberish = "👁️ THE VOID SEES ALL 👁️\n"
        gibberish += "Do not attempt to decipher this without the ancient key!"

        print(gibberish)
        print(cursed_text)       

        print("💀 The spell has been cast! Your text is now cosmic gibberish.")

    except Exception as doom:
        print(f"🌀 The chaotic forces resist: {doom}")

flibber_wobble("l.jed-txt")