#include <iostream>
#include <string>
#include <sstream>

using namespace std;

string encode(const string& input) {
    ostringstream encoded;
    for (char ch : input) {
        encoded << static_cast<int>(ch + 23) << " ";
    }
    return encoded.str();
}

int main() {
    string inputText;
    getline(cin, inputText);
    cout << encode(inputText) << endl;
    return 0;
}
