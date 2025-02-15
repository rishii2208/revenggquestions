#include <iostream>
#include <string>
using namespace std;

string rot13_decode(const string& text) {
    string decoded = "";
    for (char ch : text) {
        if (isalpha(ch)) {
            char base = isupper(ch) ? 'A' : 'a';
            decoded += char((ch - base + 13) % 26 + base);
        } else {
            decoded += ch;
        }
    }
    return decoded;
}

int main() {
    string input;
    cout << "Enter text to decode: ";
    getline(cin, input);
    cout << "Decoded text: " << rot13_decode(input) << endl;
    return 0;
}
