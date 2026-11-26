#include <iostream>

using namespace std;

int main() {
    int n;
    int mostMin = 1000000;
    int mostMax = -1000000;
    cin >> n;
    int data[n];

    for(int i = 0; i < n; i++) {
        cin >> data[i];
        if(mostMax < data[i]) {
            mostMax = data[i];
        }

        if(mostMin > data[i]) {
            mostMin = data[i];
        }
    }

    cout << mostMax << " " << mostMin << endl;
}