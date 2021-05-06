#include <iostream>

using namespace std;

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
    string frame;
    cin >> frame;

    frame = bitUnstuffing(frame);

    cout << frame << endl;
}