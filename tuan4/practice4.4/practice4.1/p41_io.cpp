#include <iostream>

#include "p41_io.h"
#include "p41_compute.h"
void p41_in(int &n)
{
    std::cout << "Enter a positive integer = ";
    while (1) {
        if (std::cin >> n && n > 0) {
            std::cin.ignore(1e9, '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Enter a positive integer = ";
    }
}
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
