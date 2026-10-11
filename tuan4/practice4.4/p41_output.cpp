#include <iostream>
#include "p41_output.h"
#include "p41_compute.h"
void p41_out(int n)
{
    int i;
    int c = 0;
    for (i = 2; i <= n; i++)
        if (p41_prime(i)) {
            c++;
            std::cout << "#" << c << " = " << i << "\n";
        }
    std::cout << "There are " << c << " prime numbers.\n";
}
