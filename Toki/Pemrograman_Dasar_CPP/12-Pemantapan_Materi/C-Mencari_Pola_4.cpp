#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int num = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j <= i; j++) {
            cout << num;
            num++;
            if (num > 9) {
                num = 0;
            }
        }
        cout << endl;
    }
}