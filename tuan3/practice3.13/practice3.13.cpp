#include <iostream>


int main()
{
    int n;

    std::cout << "Enter N = ";
    while (!(std::cin >> n) || n <= 0)
    {
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Enter N = ";
    }

    bool desc = true;
    int  t = n, prev = t % 10;
    t /= 10;
    while (t > 0)
    {
        int cur = t % 10;
        if (cur >= prev)
        {
            desc = false;
            break;
        }
        prev = cur;
        t /= 10;
    }

    bool sym = true;
    t        = n;
    int rev = 0, orig = n;
    while (t > 0)
    {
        rev = rev * 10 + t % 10;
        t /= 10;
    }
    sym = (orig == rev);

    std::cout << (desc ? "Descending." : "Not descending.") << '\n';
    std::cout << (sym ? "Symmetric." : "Not symmetric.") << '\n';

    return 0;
}
