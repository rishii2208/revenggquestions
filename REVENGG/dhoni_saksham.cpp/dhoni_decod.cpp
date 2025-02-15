#include <iostream>
#include <string>

using namespace std;

string alternateDecipher(const string& encoded_string) {
    string result;
    for (size_t i = 0; i < encoded_string.length(); ++i) {
        if (i % 2 == 0) {
            result += static_cast<char>(encoded_string[i] - 7);
        } else {
            result += static_cast<char>(encoded_string[i] + 7);
        }
    }
    return result;
}

int main() {
    string encoded_string;

    // Take user input for the encoded string
    cout << "Enter an encoded string to decode: ";
    getline(cin, encoded_string);

    // Call the function with the encoded string
    string decoded_string = alternateDecipher(encoded_string);

    // Print the decoded string
    cout << "Decoded String: " << decoded_string << endl;

    return 0;
}
