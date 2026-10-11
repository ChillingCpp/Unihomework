#include <iostream>
#include <limits>
#include "input.h"
#include "compute.h"
static void rd(D &d, int k)
{
    if (k == 1)
        std::cout << "Enter date 1 = ";
    else
        std::cout << "Enter date 2 = ";
    while (1) {
        if (std::cin >> d.d >> d.m >> d.y && valid(d)) {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
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
