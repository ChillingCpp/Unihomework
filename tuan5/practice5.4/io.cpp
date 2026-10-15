#include <iostream>

#include "io.h"
static int lp(int y)
{
    return y % 400 == 0 || (y % 4 == 0 && y % 100 != 0);
}
static int vd(D x)
{
    if (x.y < 1 || x.m < 1 || x.m > 12 || x.d < 1)
        return 0;
    int t[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int q = t[x.m - 1];
    if (x.m == 2 && lp(x.y))
        q = 29;
    return x.d <= q;
}
static int cp(D x, D y)
{
    if (x.y != y.y)
        return x.y - y.y;
    if (x.m != y.m)
        return x.m - y.m;
    return x.d - y.d;
}
void in(D a[], int &n)
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
    for (int i = 0; i < n; i++) {
        std::cout << "Date " << i << " = ";
        while (1) {
            if (std::cin >> a[i].d >> a[i].m >> a[i].y && vd(a[i])) {
                std::cin.ignore(1e9, '\n');
                break;
            }
            std::cin.clear();
            std::cin.ignore(1e9, '\n');
            std::cout << "Date " << i << " = ";
        }
    }
}
void st(D a[], int n)
{
    for (int i = 0; i < n - 1; i++) {
        int k = i;
        for (int j = i + 1; j < n; j++)
            if (cp(a[j], a[k]) > 0)
                k = j;
        if (k != i) {
            D t = a[i];
            a[i] = a[k];
            a[k] = t;
        }
    }
}
void out(D a[], int n)
{
    for (int i = 0; i < n; i++)
        std::cout << a[i].d << " " << a[i].m << " " << a[i].y << "\n";
}
