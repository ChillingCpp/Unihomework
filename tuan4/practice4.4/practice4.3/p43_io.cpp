#include <iostream>

#include "p43_io.h"
void p43_in(double &a, double &b, double &c)
{
    std::cout << "Enter 3 positive real numbers = ";
    while (1) {
        if ((std::cin >> a >> b >> c) && a > 0 && b > 0 && c > 0) {
            std::cin.ignore(1e9, '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Enter 3 positive real numbers = ";
    }
}
void p43_out(int k)
{
    if (k < 0) {
        std::cout << "Cannot form a triangle!\n";
        return;
    }
    std::cout << "Can form a triangle.\n";
    if (k == 4)
        std::cout << "Equilateral triangle.\n";
    else if (k == 3)
        std::cout << "Right-isosceles triangle.\n";
    else if (k == 1)
        std::cout << "Right triangle.\n";
    else if (k == 2)
        std::cout << "Isosceles triangle.\n";
    else
        std::cout << "Normal triangle.\n";
}
