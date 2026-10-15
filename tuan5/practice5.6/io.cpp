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
void out(int a[][MX], int m, int n)
{
    int r[MX] = {0};
    int c[MX] = {0};
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            r[i] += a[i][j];
            c[j] += a[i][j];
        }
    int f = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            if (a[i][j] == r[i] - a[i][j] + c[j] - a[i][j]) {
                std::cout << "Element " << i << ", " << j << " = " << a[i][j] << "\n";
                f = 1;
            }
    if (!f)
        std::cout << "No such elements.\n";
}
