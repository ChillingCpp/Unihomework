#include <iostream>
#include <limits>
#include "input.h"
void in(S &s)
{
    std::cout << "Enter literature = ";
    while (1) {
        if (std::cin >> s.l && s.l >= 0 && s.l <= 10) {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            break;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Enter literature = ";
    }
    std::cout << "Enter math = ";
    while (1) {
        if (std::cin >> s.m && s.m >= 0 && s.m <= 10) {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Enter math = ";
    }
}
