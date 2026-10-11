#include <iostream>
#include <limits>
#include "p41_input.h"
void p41_in(int &n)
{
    std::cout << "Enter a positive integer = ";
    while (1) {
        if (std::cin >> n && n > 0) {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Enter a positive integer = ";
    }
}
