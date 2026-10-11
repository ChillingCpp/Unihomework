#include <cmath>
#include "compute.h"
static double dist(P a, P b)
{
    double dx = a.x - b.x;
    double dy = a.y - b.y;
    return std::hypot(dx, dy);
}
double peri(T t)
{
    return dist(t.a, t.b) + dist(t.b, t.c) + dist(t.c, t.a);
}
P cent(T t)
{
    P p;
    p.x = (t.a.x + t.b.x + t.c.x) / 3;
    p.y = (t.a.y + t.b.y + t.c.y) / 3;
    return p;
}
