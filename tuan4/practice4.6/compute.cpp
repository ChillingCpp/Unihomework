#include "compute.h"
float gpa(S s)
{
    return (s.l + s.m) /2;
}
int rank(float g)
{
    if (g >= 8.5)
        return 0;
    if (g >= 7)
        return 1;
    if (g >= 5)
        return 2;
    return 3;
}
