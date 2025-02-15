#include <iostream>
#include <cctype>
using namespace std;

string decodeTrithemius(string text) {
    string result = "";
    for (int i = 0; i < text.length(); i++) {
        if (isalpha(text[i])) {
            char base = isupper(text[i]) ? 'A' : 'a';
            char decodedChar = base + (text[i] - base - i + 26) % 26;
            result += decodedChar;
        } else {
            result += text[i]; // Keep non-alphabet characters unchanged
        }
    }
    return result;
}

int main() {
    string input;
    getline(cin, input); // Allow spaces in input
    cout << decodeTrithemius(input) << endl;
    return 0;
}
