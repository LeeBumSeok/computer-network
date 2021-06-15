#include <iostream>
#include <queue>

using namespace std;

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
    string bitStream;
    queue<string> mlt;
    cin >> bitStream;

    mlt = mlt_3_scheme(bitStream, mlt);

    while(!mlt.empty()) {
        cout << mlt.front();
        mlt.pop();
    }
    cout << endl;

    return 0;
}