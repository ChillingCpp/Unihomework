#include <iostream>

#include "p42_io.h"
void p42_in(int &a, int &b, char &o)
{
    std::cout << "Enter two integers = ";
    while (1) {
        if (std::cin >> a >> b) {
            std::cin.ignore(1e9, '\n');
            break;
        }
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Enter two integers = ";
    }
    std::cout << "Enter an operator (+, -, *, /, %) = ";
    while (1) {
        if (std::cin >> o && (o == '+' || o == '-' || o == '*' || o == '/' || o == '%')) {
            std::cin.ignore(1e9, '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Enter an operator (+, -, *, /, %) = ";
    }
}
void p42_out(int r, int e)
{
    if (e)
        std::cout << "Error: divided by zero.\n";
    else
        std::cout << "Result = " << r << "\n";
}
