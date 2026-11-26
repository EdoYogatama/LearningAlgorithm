#include <iostream>
#include <string>

using namespace std;

int main() {
    string S, T;
    cin >> S >> T;
    
    while(true) {
        size_t pos = S.find(T);
        if(pos == string::npos) break;

        S.erase(pos, T.length());
    }

    cout << S << endl;
}