#include <iostream>

#include "io.h"
#include "compute.h"
static void rd(F &f, int k)
{
    std::cout << "Enter fraction " << k << " = ";
    while (1) {
        if (std::cin >> f.n >> f.d && !(abs(f.d - 0.0) < e)) {
            std::cin.ignore(1e9, '\n');
            return;
        }
        std::cin.clear();
        std::cin.ignore(1e9, '\n');
        std::cout << "Enter fraction " << k << " = ";
    }
}
static void pr(F f)
{
    std::cout << f.n << "/" << f.d;
}
void in(F &f, F &g)
{
    rd(f, 1);
    rd(g, 2);
}
void out(F f, F g)
{
    F s = add(f, g);
    F p = mul(f, g);
    F u = inv(f);
    F v = inv(g);
    F a = red(f);
    F b = red(g);
    pr(f);
    std::cout << " + ";
    pr(g);
    std::cout << " = ";
    pr(s);
    std::cout << "\n";
    pr(f);
    std::cout << " * ";
    pr(g);
    std::cout << " = ";
    pr(p);
    std::cout << "\n";
    std::cout << "Inverse of ";
    pr(f);
    std::cout << " = ";
    pr(u);
    std::cout << "\n";
    std::cout << "Inverse of ";
    pr(g);
    std::cout << " = ";
    pr(v);
    std::cout << "\n";
    pr(f);
    std::cout << " reduced = ";
    pr(a);
    std::cout << "\n";
    pr(g);
    std::cout << " reduced = ";
    pr(b);
    std::cout << "\n";
}
