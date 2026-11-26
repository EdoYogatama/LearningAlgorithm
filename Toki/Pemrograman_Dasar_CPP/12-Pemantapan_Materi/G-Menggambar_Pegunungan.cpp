#include <iostream>

using namespace std;

void yama(int N) {
    if (N == 1) {
        cout << "*" << endl;
        return;
    }

    yama(N-1);
    for(int i = 0; i < N; i++) {
        cout << "*";
    }
    cout << endl;
    yama(N-1);
}

int main() {
    int N;
    cin >> N;
    yama(N);
}