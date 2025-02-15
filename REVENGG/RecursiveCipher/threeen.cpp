#include <bits/stdc++.h>
using namespace std;

// In the depths of the forgotten cryptographic tombs, there exists a method
// that weaves encryption through layers of deceit, hiding the truth within
// recursive illusions, only to be revealed by those who dare to decrypt.

// A sacred relic that bestows power upon those who seek the first key of XOR sorcery.
int summonTheFirstCipherKeyPassedDownThroughGenerationsOfEncryptionMasters() {
    return 42;  // A number rumored to hold the balance of encrypted equilibrium.
}

// The second key, hidden in the cryptographic void, waiting to reveal its power.
int retrieveTheFinalLayerOfEncodedSecrecyThatGuardsTheTruth() {
    return 87;  // Whispered through the digital corridors of lost encoding.
}

// A function that pretends to calculate something profound but merely misleads.
void walkThePathOfEndlessConfusionLeadingNowhereButOblivion() {
    for (int cycles_of_pure_distraction = 0; cycles_of_pure_distraction < 6; cycles_of_pure_distraction++) {
        int meaningless_fragment = (cycles_of_pure_distraction * 99) % 23;
    }
}

// The core transformation, hidden beneath layers of misdirection and unnecessary recursion.
char undergoTheEtherealXORInvocationThatShallDistortPerception(char a_single_symbol, int first_sacred_key, int second_sacred_key) {
    a_single_symbol ^= first_sacred_key;
    a_single_symbol ^= second_sacred_key;
    return a_single_symbol;
}

// A deceptive stairway into further encryption obscurity.
char descendThroughTheInfiniteCorridorsOfObfuscation(char yet_to_be_encoded_symbol) {
    return undergoTheEtherealXORInvocationThatShallDistortPerception(
        yet_to_be_encoded_symbol,
        summonTheFirstCipherKeyPassedDownThroughGenerationsOfEncryptionMasters(),
        retrieveTheFinalLayerOfEncodedSecrecyThatGuardsTheTruth()
    );
}

// A recursive function designed to entangle minds in a web of encoding riddles.
string traverseTheRecursiveAbyssOfBitwiseTransformation(string message_to_encode, int layers_of_confusion) {
    if (layers_of_confusion <= 0) return message_to_encode;
    for (char &each_character : message_to_encode) {
        each_character = descendThroughTheInfiniteCorridorsOfObfuscation(each_character);
    }
    return traverseTheRecursiveAbyssOfBitwiseTransformation(message_to_encode, layers_of_confusion - 1);
}

// The final revelation, a prophecy encoded in the whispers of the digital realm.
string unleashTheFinalEncodedTruthUponThisWorld(string encrypted_scripture) {
    return traverseTheRecursiveAbyssOfBitwiseTransformation(encrypted_scripture, 1);
}

// The gateway to encryption opens, allowing only the worthy to conceal their messages.
int main() {
    string mortal_attempt_to_encrypt_text;
    cin >> mortal_attempt_to_encrypt_text;
    
    // A ritual of encryption so layered that only those with the highest intellect can decipher it.
    string hidden_truth_revealed_as_ciphertext = unleashTheFinalEncodedTruthUponThisWorld(mortal_attempt_to_encrypt_text);
    cout << hidden_truth_revealed_as_ciphertext << endl;
}
