#include <iostream>
#include <string>

using namespace std;

string alternateCipher(const string& input_string) {
    string result;
    for (size_t i = 0; i < input_string.length(); ++i) {
        if (i % 2 == 0) {
            result += static_cast<char>(input_string[i] + 7);
        } else {
            result += static_cast<char>(input_string[i] - 7);
        }
    }
    return result;
}

int main() {
    string user_string;

    // Take user input for the string
    cout << "Enter a string to encode: ";
    getline(cin, user_string);

    // Call the function with the user input
    string encoded_string = alternateCipher(user_string);

    // Print the encoded string
    cout << "Encoded String: " << encoded_string << endl;

    return 0;
}
