#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    int bestR = 1;
    int bestC = N;

    for(int r = 1; r < N; r++) {
        if(N%r==0) {
            int c = N / r;
            if(r<=c) {
                if((c-r) < (bestC - bestR)){
                    bestR = r;
                    bestC = c;
                }
            }
        }
    }

    cout << bestR << " " << bestC << endl;
}