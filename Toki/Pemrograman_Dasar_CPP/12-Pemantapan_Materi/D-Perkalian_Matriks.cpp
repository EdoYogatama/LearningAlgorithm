#include <iostream>

using namespace std;

int main() {
    int n, m, p;
    cin >> n >> m >> p;
    int matA[n][m], matB[m][p];
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> matA[i][j];
        }
    }

    for(int i = 0; i < m; i++) {
        for(int j = 0; j < p; j++) {
            cin >> matB[i][j];
        }
    }

    int matC[n][p];
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < p; j++) {
            matC[i][j] = 0;
            for(int k = 0; k < m; k++) {
                matC[i][j] += matA[i][k] * matB[k][j];
            }
        }
    }

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < p; j++) {
            if(j > 0) cout << ' ';
            cout << matC[i][j];
        }
        cout << endl;
    }
}