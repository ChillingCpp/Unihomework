#include "compute.h"
int gcd(int a, int b)
{
    if (a < 0)
        a = -a;
    if (b < 0)
        b = -b;
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}
F red(F f)
{
    int g = gcd(f.n, f.d);
    f.n /= g;
    f.d /= g;
    if (f.d < 0) {
        f.n = -f.n;
        f.d = -f.d;
    }
    return f;
}
F add(F a, F b)
{
    F r;
    r.n = a.n * b.d + b.n * a.d;
    r.d = a.d * b.d;
    return red(r);
}
F mul(F a, F b)
{
    F r;
    r.n = a.n * b.n;
    r.d = a.d * b.d;
    return red(r);
}
F inv(F f)
{
    F r;
    r.n = f.d;
    r.d = f.n;
    return red(r);
}
