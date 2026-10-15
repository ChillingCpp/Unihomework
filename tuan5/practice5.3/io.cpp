#include <iostream>
#include <iomanip>

#include "io.h"
static float gp(S s)
{
    return (s.l * 2 + s.m * 3) / 5;
}
static void rs(char *b, int s, int k)
{
    if (k == 0)
        std::cout << "Enter id = ";
    else
        std::cout << "Enter name = ";
    while (1) {
        std::cin.getline(b, s);
        if (std::cin && b[0])
            return;
        if (!std::cin) {
            std::cin.clear();
            std::cin.ignore(1e9, '\n');
        }
        if (k == 0)
            std::cout << "Enter id = ";
        else
            std::cout << "Enter name = ";
    }
}
static void rf(float &x, int k)
{
    if (k == 0)
        std::cout << "Enter literature = ";
    else
        std::cout << "Enter math = ";
    while (1) {
        if (std::cin >> x && x >= 0 && x <= 10) {
            std::cin.ignore(1e9, '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        if (k == 0)
            std::cout << "Enter literature = ";
        else
            std::cout << "Enter math = ";
    }
}
void in(S a[], int &n)
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
        std::cout << "Student " << i << ":\n";
        rs(a[i].i, 9, 0);
        rs(a[i].n, 50, 1);
        rf(a[i].l, 0);
        rf(a[i].m, 1);
    }
}
void st(S a[], int n)
{
    for (int i = 0; i < n - 1; i++) {
        int k = i;
        for (int j = i + 1; j < n; j++)
            if (gp(a[j]) > gp(a[k]))
                k = j;
        if (k != i) {
            S t = a[i];
            a[i] = a[k];
            a[k] = t;
        }
    }
}
void out(S a[], int n)
{
    int c = 0;
    for (int i = 0; i < n; i++)
        if (gp(a[i]) >= 8.5)
            c++;
    if (!c) {
        std::cout << "No excellent students.\n";
        return;
    }
    for (int i = 0; i < n; i++)
        if (gp(a[i]) >= 8.5)
            std::cout << a[i].i << " " << a[i].n << " " << std::fixed << std::setprecision(2) << gp(a[i]) << "\n";
}
