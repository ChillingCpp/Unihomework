#include <iostream>
#include <iomanip>

#include "io.h"
void in(S &s)
{
    std::cout << "Enter literature = ";
    while (1) {
        if (std::cin >> s.l && s.l >= 0 && s.l <= 10) {
            std::cin.ignore(1e9, '\n');
            break;
        }
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Enter literature = ";
    }
    std::cout << "Enter math = ";
    while (1) {
        if (std::cin >> s.m && s.m >= 0 && s.m <= 10) {
            std::cin.ignore(1e9, '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Enter math = ";
    }
}
void out(float g, int k)
{
    std::cout << "GPA = " << std::fixed << std::setprecision(2) << g << "\n";
    std::cout << "Rank = ";
    if (k == 0)
        std::cout << "Excellent\n";
    else if (k == 1)
        std::cout << "Good\n";
    else if (k == 2)
        std::cout << "Fair\n";
    else
        std::cout << "Failed\n";
}
