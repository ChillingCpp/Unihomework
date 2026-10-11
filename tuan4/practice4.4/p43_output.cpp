#include <iostream>
#include "p43_output.h"
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
