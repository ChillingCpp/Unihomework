#include <iostream>
#include <limits>
#include "p43_input.h"
void p43_in(double &a, double &b, double &c)
{
    std::cout << "Enter 3 positive real numbers = ";
    while (1) {
        if (std::cin >> a >> b >> c && a > 0 && b > 0 && c > 0) {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Enter 3 positive real numbers = ";
    }
}
