#include <iostream>
#include <fstream>

int a[100][100];

void run()
{
    std::ifstream fin("MATRIX.TXT");
    int m;
    int n;
    fin >> m >> n;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            fin >> a[i][j];
    fin.close();
    std::ofstream fout("OUTPUT.TXT");
    fout << n << ' ' << m << "\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (j)
                fout << ' ';
            fout << a[j][n - 1 - i];
        }
        fout << "\n";
    }
    fout.close();
}
