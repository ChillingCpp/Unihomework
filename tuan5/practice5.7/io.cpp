#include <iostream>

#include "io.h"
void in(int a[][MX], int &m, int &n)
{
    std::cout << "Enter M, N = ";
    while (1) {
        if (std::cin >> m >> n && m >= 1 && m <= MX && n >= 1 && n <= MX) {
            std::cin.ignore(1e9, '\n');
            break;
        }
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Enter M, N = ";
    }
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            std::cout << "Element " << i << ", " << j << " = ";
            while (1) {
                if (std::cin >> a[i][j]) {
                    std::cin.ignore(1e9, '\n');
                    break;
                }
                std::cin.clear();
                std::cin.ignore(1e9, '\n');
                std::cout << "Element " << i << ", " << j << " = ";
            }
        }
}
static void pr(int b[][MX], int r, int c)
{
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (j)
                std::cout << " ";
            std::cout << b[i][j];
        }
        std::cout << "\n";
    }
}
void lf(int a[][MX], int m, int n)
{
    int b[MX][MX];
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            b[n - 1 - j][i] = a[i][j];
    std::cout << "Rotate left:\n";
    pr(b, n, m);
}
void rt(int a[][MX], int m, int n)
{
    int b[MX][MX];
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            b[j][m - 1 - i] = a[i][j];
    std::cout << "Rotate right:\n";
    pr(b, n, m);
}
