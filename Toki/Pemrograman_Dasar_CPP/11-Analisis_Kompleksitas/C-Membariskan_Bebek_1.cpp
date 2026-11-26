#include <iostream>

using namespace std;

int main() {
    int N = 35;
    // cin >> N;
    int bestR = 1;
    int bestC = N;

    for(int r = 1; r < N; r++) {
        for(int c = r; c < N; c++) {
            if (r * c == N) {
                if ((c - r) < (bestC - bestR)) {
                    bestC = c;
                    bestR = r;
                }
            }
        }
    }

    cout << bestR << " " << bestC << endl;
}