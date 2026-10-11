#include "p42_compute.h"
int p42_calc(int a, int b, char o, int &e)
{
    e = 0;
    if (o == '+')
        return a + b;
    if (o == '-')
        return a - b;
    if (o == '*')
        return a * b;
    if (b == 0) {
        e = 1;
        return 0;
    }
    if (o == '/')
        return a / b;
    return a % b;
}
