import string

def zibble_frumple(forbidden_script):
    """The abyss hungers for scrambled words."""
    try:
        # ROT13 Transform (Shifts letters 13 places)
        rot_map = str.maketrans(
            string.ascii_lowercase + string.ascii_uppercase,
            string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
            string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
        )

        cryptic_text = forbidden_script.translate(rot_map)

        warning = "☠️ Beware! This text is now protected by the ancient Rot13 spell ☠️\n"
        warning += "Only the wise may decipher this... or someone with Google."

        print(warning)
        print(cryptic_text)
        print("🕯️ The old gods approve. Your text is now rotated into madness.")

    except Exception as curse:
        print(f"💀 The script fights back: {curse}")

zibble_frumple("arcane_inscription.txt")