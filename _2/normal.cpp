#include <bits/stdc++.h>
using namespace std;

string base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

// Function to convert a character to its 8-bit binary representation
string charToBinary(char c) {
    bitset<8> binary(c);
    return binary.to_string();
}

// Function to rotate bits to the left by a given shift amount
string rotateBits(string binary, int shift) {
    return binary.substr(shift) + binary.substr(0, shift); // Perform left rotation
}

// Convert an 8-bit binary string to a hexadecimal string
string binaryToHex(string binary) {
    stringstream ss;
    ss << hex << setw(2) << setfill('0') << stoi(binary, nullptr, 2); // Convert to hex format
    return ss.str();
}

// Function to encode a string to Base64 with extra processing steps
string base64Encode(string s) {
    string encoded = "";

    // Step 1: Process each character individually
    for (char c : s) {
        string binary = charToBinary(c);      // Convert character to 8-bit binary
        string rotatedBinary = rotateBits(binary, 3); // Rotate bits left by 3 positions
        string hexValue = binaryToHex(rotatedBinary); // Convert binary to hexadecimal
        encoded += hexValue + " "; // Append hex value with space separator
    }

    // Step 2: Base64 Encoding
    int val = 0, bits = -6;
    string base64Encoded = "";
    for (char c : encoded) {
        val = (val << 8) + c; // Shift bits left and add character value
        bits += 8;
        while (bits >= 0) {
            base64Encoded.push_back(base64_chars[(val >> bits) & 63]); // Extract 6-bit values
            bits -= 6;
        }
    }

    return base64Encoded;
}

int main() {
    string input;
    cin >> input; // Read input string (single word, no spaces)

    string encoded = base64Encode(input);
    cout <<  encoded << endl;
}
