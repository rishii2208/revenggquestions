#include <bits/stdc++.h>
using namespace std;

string base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

// Base64 decoding lookup map
unordered_map<char, int> base64_map;

// Initialize Base64 decoding map
void initBase64Map() {
    for (int i = 0; i < 64; i++) base64_map[base64_chars[i]] = i;
}

// Function to decode Base64
string base64Decode(string s) {
    string decoded = "";
    int val = 0, bits = -8;
    for (char c : s) {
        if (base64_map.find(c) == base64_map.end()) continue;
        val = (val << 6) + base64_map[c];
        bits += 6;
        if (bits >= 0) {
            decoded.push_back(char((val >> bits) & 255));
            bits -= 8;
        }
    }
    return decoded;
}

// Function to rotate bits back (right rotate by 3 positions)
string reverseRotateBits(string binary, int shift) {
    // Rotate right by 'shift' bits
    return binary.substr(binary.size() - shift) + binary.substr(0, binary.size() - shift);
}

// Function to convert hexadecimal to binary
string hexToBinary(string hex) {
    stringstream ss;
    ss << hex << std::hex;
    int num;
    ss >> num;
    bitset<8> bin(num);
    return bin.to_string();
}

// Function to decode the Base64 encoded string with extra steps
string decode(string encoded) {
    // Step 1: Base64 decode
    string base64Decoded = base64Decode(encoded);
    
    string decoded = "";

    // Step 2: Reverse rotate bits (by 3 positions)
    stringstream ss(base64Decoded);
    string hexValue;
    
    while (ss >> hexValue) {
        string binary = hexToBinary(hexValue);
        string rotatedBinary = reverseRotateBits(binary, 3);

        // Step 3: Convert binary to character
        bitset<8> binaryBits(rotatedBinary);
        decoded += char(binaryBits.to_ulong());
    }

    return decoded;
}

int main() {
    initBase64Map();

    string encoded;
    cin >> encoded;

    string decoded = decode(encoded);
    cout << decoded << endl;
}
