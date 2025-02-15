#include <iostream>
#include <vector>
#include <string>
using namespace std;

int Decoding(string& encoded, vector<int>& fibb) {
    int index = fibb.size() - 2;
    int num = 0;
    if (encoded.size() < 2 || encoded.back() != '0' || encoded[encoded.size() - 2] != '0')    return -1;
    for (int i = 0; i < encoded.size() - 1; ++i) {
        if (encoded[i] == '0')    num += fibb[i];
        else if (encoded[i] != '1')    return -1;
    }
    return num;
}

int main() {
    string encoded;
    cout<<"Enter Encoded Input: "<<endl;
    cin>>encoded;
    vector<int> fibb = {1, 2};
    while (fibb.size() <= encoded.size() - 2)    fibb.push_back(fibb[fibb.size() - 1] + fibb[fibb.size() - 2]);
    int decoded_number = Decoding(encoded, fibb);
    if (decoded_number != -1)    cout<<"Decoded Output: "<<decoded_number<<endl;
    return 0;
}