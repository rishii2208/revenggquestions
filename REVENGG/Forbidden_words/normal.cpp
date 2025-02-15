#include <bits/stdc++.h>
using namespace std;

// Function to encode a string using Gray code representation
string encode(string s) {
    string encoded = "";

    // Iterate through each character in the string
    for (char c : s) {
        bitset<8> binary(c);                 // Convert character to 8-bit binary
        bitset<8> gray(binary ^ (binary >> 1)); // Convert binary to Gray code
        encoded += gray.to_string() + " ";   // Append Gray code representation with space separation
    }
    return encoded;
}

int main() {
    string s;
    cin >> s;  // Read input string (single word, no spaces)
    cout << encode(s) << endl; // Print Gray code representation of input
}
