#include <iostream>

using namespace std;

void isPrime(int N) {
    if (N == 1) {
        cout << "BUKAN" << endl;
        return;
    }
    for(int i = 2; i * i <= N; i++) {
        if(N%i == 0) {
            cout << "BUKAN" << endl;
            return;
        }
    }

    cout << "YA" << endl;
    return;
}

int main() {
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        int x;
        cin >> x;
        isPrime(x);
    }
}