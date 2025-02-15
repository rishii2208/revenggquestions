#include <bits/stdc++.h>
using namespace std;

// Function to get the first XOR key
int getKey1() {
    return 42;  // Hardcoded key
}

// Function to get the second XOR key
int getKey2() {
    return 87;  // Hardcoded key
}

// Function to perform double XOR encryption
string doubleXOREncode(string s) {
    int key1 = getKey1();
    int key2 = getKey2();

    // Apply two successive XOR operations
    for (char &c : s) {
        c ^= key1;  // First XOR operation
        c ^= key2;  // Second XOR operation
    }
    return s; // Return the modified (encoded) string
}

int main() {
    string input;
    cout << "Enter text to encode: ";
    cin >> input; // Read input string (single word, no spaces)

    string encoded = doubleXOREncode(input);
    cout << "Encoded text: " << encoded << endl;
}
