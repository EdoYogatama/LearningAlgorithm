#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> data;
    int N;
    long long res = 0;
    cin >> N;

    for (int i = 0; i < N; i++) {
        int x;
        cin >> x;
        res = res + x;
        data.push_back(x);
    }

    for (int i = 0; i < N; i++) {
        cout << res - data[i] << endl;
    }

}