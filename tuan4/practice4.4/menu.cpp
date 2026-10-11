#include <iostream>

#include "menu.h"
#include "practice4.1/p41_io.h"
#include "practice4.1/p41_compute.h"
#include "practice4.2/p42_io.h"
#include "practice4.2/p42_compute.h"
#include "practice4.3/p43_io.h"
#include "practice4.3/p43_compute.h"
void in_sel(int &s)
{
    while (1) {
        if (std::cin >> s && s >= 1 && s <= 4) {
            std::cin.ignore(1e9, '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Selection (1-4): ";
    }
}
void out_menu()
{
    std::cout << "1. Practice 4.1.\n";
    std::cout << "2. Practice 4.2.\n";
    std::cout << "3. Practice 4.3.\n";
    std::cout << "4. Exit.\n";
    std::cout << "Selection (1-4): ";
}
void run41()
{
    int n;
    p41_in(n);
    p41_out(n);
}
void run42()
{
    int a;
    int b;
    char o;
    int e;
    p42_in(a, b, o);
    int r = p42_calc(a, b, o, e);
    p42_out(r, e);
}
void run43()
{
    double a;
    double b;
    double c;
    p43_in(a, b, c);
    p43_out(p43_kind(a, b, c));
}
int run_sel(int s)
{
    if (s == 1)
        run41();
    else if (s == 2)
        run42();
    else if (s == 3)
        run43();
    else
        return 0;
    return 1;
}
