#include <iostream>
#include <vector>
using namespace std;

char* Encoding (int num, vector<int>& fibb) {
    int index = fibb.size() - 2; 
    int i = index;
    char* fibb_coded = new char[index + 3]; 
    for (int j = 0; j <= index; ++j)    fibb_coded[j] = '0';
    while (num) {
        fibb_coded[i] = '1';
        num -= fibb[i]; 
        i--; 
        while (i >= 0 && fibb[i] > num) {
            fibb_coded[i] = '0'; 
            i--;
        }
    }
    fibb_coded[index + 1] = '1';
    fibb_coded[index + 2] = '\0'; 
    return fibb_coded;
}

int main() {
    int num;
    cout<<"Enter Input Number: "<<endl;
    cin>>num;
    vector<int>fibb = {1, 2};
    while (fibb.back() <= num)    fibb.push_back(fibb[fibb.size() - 1] + fibb[fibb.size() - 2]);
    string output = Encoding(num, fibb);
    for ( int i = 0; i < output.size(); ++i) {
        if (output[i] == '0')    output[i] = '1';
        else if (output[i] == '1')    output[i] = '0';
    }
    cout<<"Encoded Output:"<<endl<<output<<endl;
    return 0;
}