#include <bits/stdc++.h>
using namespace std;

string decode(string encoded) {
    stringstream ss(encoded);
    string grayCode;
    string decoded = "";

    while (ss >> grayCode) {
        bitset<8> gray(grayCode);
        bitset<8> binary;

        binary[7] = gray[7]; // MSB remains the same
        for (int i = 6; i >= 0; i--) {
            binary[i] = binary[i + 1] ^ gray[i]; // Reverse Gray to Binary conversion
        }
        decoded += char(binary.to_ulong()); // Convert binary to char
    }
    return decoded;
}

int main() {
    string encoded;
    getline(cin, encoded);
    cout << decode(encoded) << endl;
}
