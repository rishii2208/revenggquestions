#include <bits/stdc++.h>
using namespace std;

// Function to get the first key
int getKey1() {
    return 42;  // Hardcoded key
}

// Function to get the second key
int getKey2() {
    return 87;  // Hardcoded key
}

// Double XOR Decryption function
string doubleXORDecode(string s) {
    int key1 = getKey1();
    int key2 = getKey2();
    
    for (char &c : s) {
        c ^= key2;  // Reverse XOR (undo second XOR)
        c ^= key1;  // Reverse XOR (undo first XOR)
    }
    return s;
}

int main() {
    string encoded;
    cin >> encoded;

    string decoded = doubleXORDecode(encoded);
    cout << decoded << endl;
}
