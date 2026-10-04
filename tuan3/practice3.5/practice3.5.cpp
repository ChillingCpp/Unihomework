#include <iostream>
#include <chrono>
#include <thread>

int main()
{
    int cnt = 0;
    for (int n = 100; n <= 999; n++)
    {
        int h = n / 100;
        int t = (n / 10) % 10;
        int o = n % 10;

        if (t == h + o)
        {
            cnt++;
            std::cout << cnt << ": " << n << '\n';
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
        }
    }
    std::cout << "There are " << cnt << " satisfied numbers.\n";
    return 0;
}
