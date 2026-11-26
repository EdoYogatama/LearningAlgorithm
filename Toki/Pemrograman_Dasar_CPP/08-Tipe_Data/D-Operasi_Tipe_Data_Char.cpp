#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "thequickbrownfoxjumpsoverthelazydog";

    for (char c : s) {
        if (c == 'z') {
            c = 'a';
        } else {
            c += 1;
        }
        c = c - ((int) 'a' - (int) 'A');

        cout << c;
    }
    cout << endl;
}
