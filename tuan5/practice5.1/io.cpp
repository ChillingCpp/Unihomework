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
static int pm(int x)
{
    if (x < 2)
        return 0;
    for (int i = 2; i <= x / i; i++)
        if (x % i == 0)
            return 0;
    return 1;
}
int ng(int a[], int n)
{
    int c = 0;
    for (int i = 0; i < n; i++)
        if (a[i] < 0)
            c++;
    return c;
}
int pr(int a[], int n)
{
    int c = 0;
    for (int i = 0; i < n; i++)
        if (pm(a[i]))
            c++;
    return c;
}
void out(int x, int y)
{
    std::cout << "Negative numbers: " << x << ".\n";
    std::cout << "Prime numbers: " << y << ".\n";
}
