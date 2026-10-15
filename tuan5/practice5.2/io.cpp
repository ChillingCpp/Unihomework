#include <iostream>

#include "io.h"
void in(int a[], int &n)
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
        std::cout << "Element " << i << " = ";
        while (1) {
            if (std::cin >> a[i]) {
                std::cin.ignore(1e9, '\n');
                break;
            }
            std::cin.clear();
            std::cin.ignore(1e9, '\n');
            std::cout << "Element " << i << " = ";
        }
    }
}
int as(int a[], int n)
{
    for (int i = 1; i < n; i++)
        if (a[i] < a[i - 1])
            return 0;
    return 1;
}
int sy(int a[], int n)
{
    for (int i = 0; i < n / 2; i++)
        if (a[i] != a[n - 1 - i])
            return 0;
    return 1;
}
int ap(int a[], int n)
{
    if (n <= 2)
        return 1;
    int d = a[1] - a[0];
    for (int i = 2; i < n; i++)
        if (a[i] - a[i - 1] != d)
            return 0;
    return 1;
}
void out(int x, int y, int z)
{
    if (x)
        std::cout << "Array is ascending.\n";
    else
        std::cout << "Array is not ascending.\n";
    if (y)
        std::cout << "Array is symmetric.\n";
    else
        std::cout << "Array is not symmetric.\n";
    if (z)
        std::cout << "Array is an arithmetic progression.\n";
    else
        std::cout << "Array is not an arithmetic progression.\n";
}
