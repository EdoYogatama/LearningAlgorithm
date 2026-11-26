#include <iostream>

using namespace std;

int main() {
    long long N;
    cin >> N;
    long long bestR = 1;
    long long bestC = N;

    for(long long r = 1; r * r <= N; r++) {
        if(N % r == 0) {
            long long c = N / r;
            if((c - r) < (bestC - bestR)) {
                bestR = r;
                bestC = c;
            }
        }
    }

    cout << bestR << " " << bestC << endl;
}
