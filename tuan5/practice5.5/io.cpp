#include <iostream>

#include "io.h"
void in(int a[][MX], int &n)
{
    std::cout << "Enter N = ";
    while (1) {
        if (std::cin >> n && n >= 1 && n <= MX) {
            std::cin.ignore(1e9, '\n');
            break;
        }
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Enter N = ";
    }
    for (int i = 0; i < n; i++)
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
int md(int a[][MX], int n)
{
    int s = 0;
    for (int i = 0; i < n; i++)
        s += a[i][i];
    return s;
}
int ad(int a[][MX], int n)
{
    int s = 0;
    for (int i = 0; i < n; i++)
        s += a[i][n - 1 - i];
    return s;
}
int rw(int a[][MX], int n)
{
    int k = 0;
    int b = 0;
    for (int j = 0; j < n; j++)
        b += a[0][j];
    for (int i = 1; i < n; i++) {
        int s = 0;
        for (int j = 0; j < n; j++)
            s += a[i][j];
        if (s > b) {
            b = s;
            k = i;
        }
    }
    return k;
}
int mg(int a[][MX], int n)
{
    int s = md(a, n);
    if (ad(a, n) != s)
        return 0;
    for (int i = 0; i < n; i++) {
        int r = 0;
        int c = 0;
        for (int j = 0; j < n; j++) {
            r += a[i][j];
            c += a[j][i];
        }
        if (r != s || c != s)
            return 0;
    }
    return 1;
}
void out(int x, int y, int r, int k)
{
    std::cout << "Main diagonal = " << x << ".\n";
    std::cout << "Anti-diagonal = " << y << ".\n";
    std::cout << "Row " << r << " has max sum.\n";
    if (k)
        std::cout << "It is a magic square.\n";
    else
        std::cout << "It is not a magic square.\n";
}
