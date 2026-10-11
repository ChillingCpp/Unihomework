#include <iostream>
#include <limits>
#include "menu_input.h"
void in_sel(int &s)
{
    while (1) {
        if (std::cin >> s && s >= 1 && s <= 4) {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Selection (1-4): ";
    }
}
