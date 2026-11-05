#include <cstddef>
#include <iostream>

#include "dynamic_array.h"

int main()
{
    double *p[10] = {NULL};
    const int offset = 3;

    initialize(p + offset);

    std::cout << "sizeof(double*) = " << sizeof(double *) << " bytes\n";
    std::cout << "sizeof(double) = " << sizeof(double) << " bytes\n";
    std::cout << "p[10] uses " << sizeof(p) << " bytes on the stack\n";
    std::cout << "heap doubles = " << (1 + 2 + 3 + 4 + 5) << '\n';
    std::cout << "heap bytes = "
              << (1 + 2 + 3 + 4 + 5) * sizeof(double) << '\n';

    release(p + offset);
    return 0;
}
