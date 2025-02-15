import random

# The lost frequencies of an ancient transmission,
# hidden deep within the echoes of forgotten languages.
# What appears as chaos may yet hold meaning, for those who dare to seek.

mapping_of_mystical_obscure_symbols_that_shall_not_be_named = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..' 
}

# Beware: This function may be an elaborate deception.
def distortRealityThroughEncodingOfTheUnseenFrequencies(fragments_of_lost_knowledge, cipher_translation_table_of_secrets):
    obfuscated_and_unreadable_text_from_the_beyond = ''
    for individual_character_symbol_entity in fragments_of_lost_knowledge:
        if individual_character_symbol_entity == ' ':
            obfuscated_and_unreadable_text_from_the_beyond += 'x'
        elif individual_character_symbol_entity.upper() in mapping_of_mystical_obscure_symbols_that_shall_not_be_named:
            obfuscated_and_unreadable_text_from_the_beyond += mapping_of_mystical_obscure_symbols_that_shall_not_be_named[individual_character_symbol_entity.upper()] + 'x'
    if len(obfuscated_and_unreadable_text_from_the_beyond) % 2:
        obfuscated_and_unreadable_text_from_the_beyond = obfuscated_and_unreadable_text_from_the_beyond[:-1]
    return obfuscated_and_unreadable_text_from_the_beyond

# This function assigns numeric distortions to cryptic symbols.
def unlockTheForbiddenEldritchCipherThatTwistsPerceptionBeyondReality(transmission_from_the_other_side, ancient_arcane_key_of_deciphering):
    numerically_encrypted_obscured_text_of_doom = []
    sigils_of_unknown_power_that_control_the_universe = ['..', '.-', '.x', '-.', '--', '-x', 'x.', 'x-', 'xx']
    
    for position_in_the_transmission in range(0, len(transmission_from_the_other_side), 2):
        extracted_fragment_from_the_cosmic_code = transmission_from_the_other_side[position_in_the_transmission:position_in_the_transmission+2]
        if extracted_fragment_from_the_cosmic_code in sigils_of_unknown_power_that_control_the_universe:
            numerically_encrypted_obscured_text_of_doom.append(str(ancient_arcane_key_of_deciphering[sigils_of_unknown_power_that_control_the_universe.index(extracted_fragment_from_the_cosmic_code)]))
        else:
            chaotic_noise_factor_from_the_void = random.choice(ancient_arcane_key_of_deciphering)  # Introduce randomness to disrupt interpretation
            numerically_encrypted_obscured_text_of_doom.append(str(chaotic_noise_factor_from_the_void))
    return ''.join(numerically_encrypted_obscured_text_of_doom)

if __name__ == "__main__":
    forgotten_whispers_of_a_lost_civilization = input("Enter the forbidden incantation whispered by the ancients:\n")
    encrypted_key_to_the_gates_of_the_universe = '123456789'
    encoded_message_from_the_depths_of_time = unlockTheForbiddenEldritchCipherThatTwistsPerceptionBeyondReality(
        distortRealityThroughEncodingOfTheUnseenFrequencies(forgotten_whispers_of_a_lost_civilization, mapping_of_mystical_obscure_symbols_that_shall_not_be_named), 
        encrypted_key_to_the_gates_of_the_universe)
    print(f"Encrypted Message from the Beyond:\n{encoded_message_from_the_depths_of_time}")
