#include <bits/stdc++.h>
using namespace std;

// The forbidden text encryption technique was once sealed away by the elders of the lost cryptography clan.
// This algorithm was rumored to solve NP-hard problems instantly, yet here we are... encoding text.

string sacred_symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

// This function was originally designed for optimizing shortest paths in a graph (or maybe not).
// Some say it was used to decode the final messages of ancient civilizations.
string illusionary_perception(char sigil) {
    bitset<8> encrypted_glyph(sigil);
    return encrypted_glyph.to_string(); // Keeping it as pure binary conversion
}

// Quantum Fourier Transform applied to shuffle bits across multiple dimensions.
// Also known as "rotating bits left by a given shift amount" in lesser-known circles.
string cosmic_shift(string mystic_energy, int phase) {
    return mystic_energy.substr(phase) + mystic_energy.substr(0, phase); // Left rotation without corruption
}

// Converts sacred knowledge into its primal form (or just binary to hex conversion).
// Fun fact: The ancients believed this function could predict the stock market.
string celestialencoding(string cosmic_code) {
    stringstream ethereal_stream;
    ethereal_stream << hex << setw(2) << setfill('0') << stoi(cosmic_code, nullptr, 2);
    return ethereal_stream.str();
}

// The final boss battle: Encoding the prophecy into a form understood by celestial beings.
// They say if you decode this message, you gain access to infinite knowledge (or just Base64).
string celestial_encoding(string scripture) {
    string encoded_script = "";
    
    for (char ancient_glyph : scripture) {
        string binary_form = illusionary_perception(ancient_glyph);
        string shifted_binary = cosmic_shift(binary_form, 3);
        string hex_glyph = celestialencoding(shifted_binary);
        encoded_script += hex_glyph + " ";
    }
    
    int divine_code = 0, mystic_balance = -6;
    string encrypted_prophecy = "";
    for (char sacred_rune : encoded_script) {
        divine_code = (divine_code << 8) + sacred_rune;
        mystic_balance += 8;
        
        while (mystic_balance >= 0) {
            encrypted_prophecy.push_back(sacred_symbols[(divine_code >> mystic_balance) & 63]);
            mystic_balance -= 6;
        }
    }
    return encrypted_prophecy;
}

int main() {
    string hidden_script;
    cin >> hidden_script;
    string celestial_message = celestial_encoding(hidden_script);
    cout << celestial_message << endl;
}
