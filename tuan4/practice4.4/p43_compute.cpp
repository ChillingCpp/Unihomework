#include <cmath>
#include "p43_compute.h"
int p43_kind(double a, double b, double c)
{
    double t;
    double e = 1e-9;
    double d;
    if (a + b <= c || a + c <= b || b + c <= a)
        return -1;
    if (a > b) {
        t = a;
        a = b;
        b = t;
    }
    if (b > c) {
        t = b;
        b = c;
        c = t;
    }
    if (a > b) {
        t = a;
        a = b;
        b = t;
    }
    d = a * a + b * b - c * c;
    if (d < 0)
        d = -d;
    if (a == b && b == c)
        return 4;
    if (d < e && (a == b || b == c))
        return 3;
    if (d < e)
        return 1;
    if (a == b || b == c)
        return 2;
    return 0;
}
