#include <cmath>
#include <utility>
#include "p43_compute.h"
bool eq(double a, double b)
{
    return std::abs(a - b) < e;
}
int p43_kind(double a, double b, double c)
{
    double d;
    if (a + b <= c || a + c <= b || b + c <= a)
        return -1;
    if (a > b) 
        std::swap(a, b);
    if (b > c) 
        std::swap(b, c);
    if (a > b) 
        std::swap(a, b);
    
    d = std::abs(a * a + b * b - c * c);
    
    if (eq(a, b) && eq(b, c))
        return 4;
    if (d < e && (eq(a, b) || eq(b, c)))
        return 3;
    if (d < e)
        return 1;
    if (eq(a, b) || eq(b, c))
        return 2;
    return 0;
}
