#include <iostream>


bool isPrime(int n)
{
    if (n < 2)
        return false;
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;
    for (int i = 3; i * i <= n; i += 2)
        if (n % i == 0)
            return false;
    return true;
}

int main()
{
    int n;

    std::cout << "Enter a positive integer = ";
    while (!(std::cin >> n) || n < 1)
    {
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Enter a positive integer = ";
    }

    int cnt = 0;
    for (int i = 2; i <= n; i++)
    {
        if (isPrime(i))
        {
            cnt++;
            std::cout << "#" << cnt << " = " << i << '\n';
        }
    }
    std::cout << "There are " << cnt << " prime numbers.\n";

    return 0;
}
