#include <iostream>
#include <limits>
#include "input.h"
static void rd(F &f, int k)
{
    if (k == 1)
        std::cout << "Enter fraction 1 = ";
    else
        std::cout << "Enter fraction 2 = ";
    while (1) {
        if (std::cin >> f.n >> f.d && f.d != 0) {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        if (k == 1)
            std::cout << "Enter fraction 1 = ";
        else
            std::cout << "Enter fraction 2 = ";
    }
}
void in(F &f, F &g)
{
    rd(f, 1);
    rd(g, 2);
}
