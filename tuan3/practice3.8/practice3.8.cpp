#include <iostream>


int main()
{
    int       n;
    int       mx = 0, mn = 1e9, cnt = 0;
    long long sum = 0;

    int i = 1;
    while (true)
    {
        std::cout << "Number " << i << " = ";
        while (!(std::cin >> n))
        {
            std::cin.clear();
            std::cin.ignore(1e9, '\n');
            std::cout << "Number " << i << " = ";
        }
        if (n == 0)
            break;
        if (n < 0)
            continue;

        mx = std::max(mx, n);
        mn = std::min(mn, n);

        sum += n;
        cnt++;
        i++;
    }

    if (cnt > 0)
    {
        std::cout << "Max = " << mx << '\n';
        std::cout << "Min = " << mn << '\n';
        std::cout << "Average = " << 1.0 * sum / cnt << '\n';
    }

    return 0;
}
