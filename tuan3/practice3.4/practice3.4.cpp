#include <iostream>


int main()
{
    int n;

    std::cout << "Enter a positive integer N = ";
    std::cin >> n;

    long long f    = 1;
    int       flag = 1;
    double    ln2  = 0;
    double    pi   = (n > 0 ? 1 : 0);
    long long s    = 0;
    for (int i = 1; i <= n; ++i)
    {
        f *= i;
        ln2 += flag * 1.0 / i;
        pi += -flag * 1.0 / (2 * i + 1);
        s += (i * 1ll * i <= n ? i * 1ll * i : 0);
        flag *= -1;
    }

    std::cout << "N! = " << f << '\n';
    std::cout << "ln(2) = " << ln2 << '\n';
    std::cout << "PI = " << pi * 4 << '\n';
    std::cout << "S = " << s << '\n';

    return 0;
}
