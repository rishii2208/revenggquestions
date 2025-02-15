#include <iostream>
#include <cctype>
using namespace std;

// Function to encode the given text using the Trithemius cipher
string encodeTrithemius(string text) {
    string result = ""; // Stores the encoded result

    // Iterate through each character in the input text
    for (int i = 0; i < text.length(); i++) {
        if (isalpha(text[i])) { // Check if the character is an alphabet
            char base = isupper(text[i]) ? 'A' : 'a'; // Determine base ('A' for uppercase, 'a' for lowercase)

            // Apply the Trithemius cipher: Shift character by its index (i) while keeping it within A-Z or a-z range
            char encodedChar = base + (text[i] - base + i) % 26;
            result += encodedChar; // Append the encoded character to the result
        } else {
            result += text[i]; // Keep non-alphabet characters unchanged
        }
    }
    return result; // Return the encoded string
}

int main() {
    string input;
    getline(cin, input); // Read the entire input line (including spaces)
    cout << encodeTrithemius(input) << endl; // Output the encoded string
    return 0;
}
