#include <iostream>
#include "output.h"
#include "compute.h"
static void pr(F f)
{
    std::cout << f.n << "/" << f.d;
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
