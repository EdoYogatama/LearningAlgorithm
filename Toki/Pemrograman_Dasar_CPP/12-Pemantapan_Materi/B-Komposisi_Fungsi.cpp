#include <iostream>
using namespace std;

int main() {
    int a, b, k, x;
    cin >> a >> b >> k >> x;
    int res = 0;
    for(int i = 0; i < k; i++) {
        res = ((a*x) + b);
        if(res < 0) {
            res = res * (-1);
        }
        x = res;
    }

    cout << res;
}