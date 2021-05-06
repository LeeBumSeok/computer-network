#include <iostream>

using namespace std;

string bitStuffing(string frame) {
    string sequence;
    int count = 0;

    for(int i = 0; i < frame.length(); i++) {
        sequence += frame[i];
        if(frame[i] == '1') count++;
        else count = 0;

        if(count == 5) {
            sequence += '0';
            count = 0;
        }
    }

    return sequence;
}

int main() {
    string frame;
    cin >> frame;
    
    frame = bitStuffing(frame);

    cout << frame << endl;
}