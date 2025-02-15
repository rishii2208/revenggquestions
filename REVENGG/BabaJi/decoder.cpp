#include <iostream>
#include <string>
#include <sstream>

using namespace std;

string decode(const string& input) {
    istringstream stream(input);
    ostringstream decoded;
    int charCode;
    while (stream >> charCode) {
        decoded << static_cast<char>(charCode - 23);
    }
    return decoded.str();
}

int main() {
    string inputText;
    getline(cin, inputText);
    cout << decode(inputText) << endl;
    return 0;
}
