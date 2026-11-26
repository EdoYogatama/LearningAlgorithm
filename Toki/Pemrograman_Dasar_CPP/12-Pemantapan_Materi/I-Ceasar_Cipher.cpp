#include <iostream>
#include <string>

using namespace std;

int main() {
    int k = 3;
    string s = "";
    for(char c: s) {
        int ck = int(c) + k;
        if(ck > int('z')) {
            int diff = ck - int('z');
            ck = int('a') + diff - 1;
        }

        cout << char(ck);
    }

    cout << endl;
}