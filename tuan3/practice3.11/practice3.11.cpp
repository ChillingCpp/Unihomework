#include <iostream>


int main()
{
    int n, m;

    std::cout << "Enter N, M = ";
    std::cin >> n >> m;


    std::cout << "The first " << m << " bit from the right of " << n << ": ";
    for (int i = m - 1; i >= 0; i--)
        std::cout << ((n >> i) & 1);
    std::cout << '\n';

    return 0;
}
