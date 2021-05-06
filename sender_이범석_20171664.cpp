#include <iostream>
#include <queue>

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

queue<string> mlt_3_scheme(string bitStream, queue<string> mlt) {
    string lastSign;

    for(int i = 0; i < bitStream.length() - 1; i++) {
        if(i == 0) {
            if(bitStream[0] == '0') mlt.push("0");
            else {
                mlt.push("+");
                lastSign = "+";
            }
        }
        if(bitStream[i + 1] == '0') mlt.push(mlt.back());
        else {
            if(mlt.back() == "0") {
                if(lastSign == "+") {
                    mlt.push("-");
                    lastSign = "-";
                }
                else {
                    mlt.push("+");
                    lastSign = "+";
                }
            }
            else mlt.push("0");
        }
    }

    return mlt;
}

int main() {
    string frame;
    string stuffingBit;
    queue<string> mlt3;

    cin >> frame;
    stuffingBit = bitStuffing(frame);
    mlt3 = mlt_3_scheme(stuffingBit, mlt3);

    cout << "bit-stuffing result: " << stuffingBit << endl;
    cout << "mlt-3 result: ";
    while(!mlt3.empty()) {
        cout << mlt3.front();
        mlt3.pop();
    }
    cout << endl;
}