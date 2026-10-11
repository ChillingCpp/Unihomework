#include <iostream>
#include <limits>
#include "p42_input.h"
void p42_in(int &a, int &b, char &o)
{
    std::cout << "Enter two integers = ";
    while (1) {
        if (std::cin >> a >> b) {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            break;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Enter two integers = ";
    }
    std::cout << "Enter an operator (+, -, *, /, %) = ";
    while (1) {
        if (std::cin >> o && (o == '+' || o == '-' || o == '*' || o == '/' || o == '%')) {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Enter an operator (+, -, *, /, %) = ";
    }
}
