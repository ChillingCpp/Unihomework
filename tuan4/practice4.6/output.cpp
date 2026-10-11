#include <iostream>
#include <iomanip>
#include "output.h"
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
