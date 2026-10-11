#include <iostream>

#include "io.h"
void in(T &t)
{
    std::cout << "Enter triangle points = ";
    while (1) {
        if (std::cin >> t.a.x >> t.a.y >> t.b.x >> t.b.y >> t.c.x >> t.c.y) {
            std::cin.ignore(1e9, '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Enter triangle points = ";
    }
}
void out(double p, P c)
{
    std::cout << "Perimeter = " << p << "\n";
    std::cout << "Centroid = (" << c.x << ", " << c.y << ")\n";
}
