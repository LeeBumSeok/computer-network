#include <iostream>

using namespace std;

string convertBitstream(string bitStream) {
    string result;

    if(bitStream[0] == '0') result += '0';
    else result += '1';

    for(int i = 1; i < bitStream.length(); i++) {
        if(bitStream[i] == bitStream[i - 1]) result += '0';
        else result += '1';
    }

    return result;
}

string bitUnstuffing(string frame) {
    string sequence;
    int count = 0;
    
    for(int i = 0; i < frame.length(); i++) {
        if(count != 5) sequence += frame[i];
        if(frame[i] == '1') count++;
        else count = 0;
    }

    return sequence;
}

int main() {
    string bitStream;
    string result;
    cin >> bitStream;

    bitStream = convertBitstream(bitStream);
    cout << "Convert bit stream result: " << bitStream << endl;

    result = bitUnstuffing(bitStream);
    cout << "Bit-unstuffing result: " << result << endl;
}