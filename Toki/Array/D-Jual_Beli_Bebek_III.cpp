#include <iostream>
using namespace std;

int main() {
    int beli[10] = {13, 100, 0, 4, 31, 0, 178, 23, 1, 13};
    int jual[10] = {0, 2, 24, 0, 10, 4, 0, 121, 0, 15};

    int jumlah_bebek = 0;

    for (int i = 0; i < 10; i++) {
        jumlah_bebek = jumlah_bebek + beli[i] - jual[i];
        cout << jumlah_bebek << endl;
    }
}
