#include <iostream>
#include <limits>
#include "input.h"
void in(T &t)
{
    std::cout << "Enter triangle points = ";
    while (1) {
        if (std::cin >> t.a.x >> t.a.y >> t.b.x >> t.b.y >> t.c.x >> t.c.y) {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Enter triangle points = ";
    }
}
