#include <iostream>

using namespace std;

int absolute(int a) {
    if (a < 0) {
        a *= -1;
    }

    return a;
}

int power(int a, int b) {
    int result = 1;
    for(int i = 0; i < b; i++) {
        result *= a;
    }

    return result;
}

int main() {
    int n, d;
    int minT = 2*power(100,3);
    int maxT = 0;

    cin >> n >> d;
    int x[n], y[n];

    for(int i = 0; i < n; i++) {
        cin >> x[i] >> y[i];
    }

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(j!=i) {
                int t = power(absolute(x[i]-x[j]), d) + power(absolute(y[i]-y[j]), d);
                if(minT > t) {minT = t;}
                if(maxT < t) {maxT = t;}
            }
        }
    }

    cout << minT << ' ' << maxT << endl;
}