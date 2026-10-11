#include <iostream>
#include "output.h"
void out(int k, D a, D b)
{
    if (k > 0)
        std::cout << "d1 is later than d2.\n";
    else
        std::cout << "d1 is not later than d2.\n";
    std::cout << "Tomorrow of d1 = " << a.d << " " << a.m << " " << a.y << "\n";
    std::cout << "Yesterday of d2 = " << b.d << " " << b.m << " " << b.y << "\n";
}
