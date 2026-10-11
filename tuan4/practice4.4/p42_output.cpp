#include <iostream>
#include "p42_output.h"
void p42_out(int r, int e)
{
    if (e)
        std::cout << "Error: divided by zero.\n";
    else
        std::cout << "Result = " << r << "\n";
}
