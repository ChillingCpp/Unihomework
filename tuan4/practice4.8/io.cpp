#include <iostream>

#include "io.h"
#include "compute.h"
static void rd(D &d, int k)
{
    if (k == 1)
        std::cout << "Enter date 1 = ";
    else
        std::cout << "Enter date 2 = ";
    while (1) {
        if (std::cin >> d.d >> d.m >> d.y && valid(d)) {
            std::cin.ignore(1e9, '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        if (k == 1)
            std::cout << "Enter date 1 = ";
        else
            std::cout << "Enter date 2 = ";
    }
}
void in(D &a, D &b)
{
    rd(a, 1);
    rd(b, 2);
}
void out(int k, D a, D b)
{
    if (k > 0)
        std::cout << "d1 is later than d2.\n";
    else
        std::cout << "d1 is not later than d2.\n";
    std::cout << "Tomorrow of d1 = " << a.d << " " << a.m << " " << a.y << "\n";
    std::cout << "Yesterday of d2 = " << b.d << " " << b.m << " " << b.y << "\n";
}
