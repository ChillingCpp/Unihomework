#include "compute.h"
static int leap(int y)
{
    return (y % 4 == 0 && y % 100 != 0) || y % 400 == 0;
}
int dim(int m, int y)
{
    if (m == 2)
        return leap(y) ? 29 : 28;
    if (m == 4 || m == 6 || m == 9 || m == 11)
        return 30;
    return 31;
}
int valid(D d)
{
    if (d.y < 1 || d.m < 1 || d.m > 12)
        return 0;
    if (d.d < 1 || d.d > dim(d.m, d.y))
        return 0;
    return 1;
}
int cmp(D a, D b)
{
    if (a.y != b.y)
        return a.y > b.y ? 1 : -1;
    if (a.m != b.m)
        return a.m > b.m ? 1 : -1;
    if (a.d != b.d)
        return a.d > b.d ? 1 : -1;
    return 0;
}
D next(D d)
{
    d.d++;
    if (d.d > dim(d.m, d.y)) {
        d.d = 1;
        d.m++;
        if (d.m > 12) {
            d.m = 1;
            d.y++;
        }
    }
    return d;
}
D prev(D d)
{
    d.d--;
    if (d.d < 1) {
        d.m--;
        if (d.m < 1) {
            d.m = 12;
            d.y--;
        }
        d.d = dim(d.m, d.y);
    }
    return d;
}
