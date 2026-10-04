#include <iostream>
#include <numeric>

int main()
{
    int a, b;

    std::cout << "Enter 2 positive integers = ";
    while (!(std::cin >> a >> b) || b <= 0 || a <= 0)
    {
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Enter 2 positive integers = ";
    }

    int g = std::gcd(a, b);
    std::cout << "GCD = " << g << '\n';
    std::cout << "LCM = " << 1LL * a * b / g << '\n';

    return 0;
}
