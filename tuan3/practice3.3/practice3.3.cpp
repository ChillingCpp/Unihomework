#include <iostream>


int main()
{
    int m, y;

    std::cout << "Enter month and year = ";
    std::cin >> m >> y;

    int d = 31;
    if (m == 2)
        d = (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0) ? 29 : 28;
    if (m == 4 || m == 6 || m == 9 || m == 11)
        d = 30;


    std::cout << "Month " << m << " in year " << y << " has " << d << " days.\n";

    return 0;
}
