#include "p41_compute.h"
int p41_prime(int n)
{
    int i;
    if (n < 2)
        return 0;
    for (i = 2; i * i <= n; i++)
        if (n % i == 0)
            return 0;
    return 1;
}
