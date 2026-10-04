#include <iostream>
#include <cmath>

int main()
{
    double a, b, c;

    std::cout << "Enter coefficients a, b, c = ";
    std::cin >> a >> b >> c;
    std::cin.ignore(1e9, '\n');

    double eps = 1e-9;
    if (abs(a) < eps)
    {
        if (abs(b) < eps)
        {
            if (abs(c) < eps)
                std::cout << "Infinite solutions.\n";
            else
                std::cout << "No solution!\n";
        }
        else
            std::cout << "Solution 1 = " << -c / b << '\n';
    }
    else
    {
        double d = b * b - 4 * a * c;
        if (d > 0.0 && d > eps)
        {
            std::cout << "Solution 1 = " << (-b + std::sqrt(d)) / (2 * a) << '\n';
            std::cout << "Solution 2 = " << (-b - std::sqrt(d)) / (2 * a) << '\n';
        }
        else if (d > 0.0)
            std::cout << "Solution 1 = " << -b / (2 * a) << '\n';

        else
            std::cout << "No solution!\n";
    }

    return 0;
}
