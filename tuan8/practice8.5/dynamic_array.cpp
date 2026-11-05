#include "dynamic_array.h"

#include <cstddef>

void initialize(double **p)
{
    if (p == NULL)
        return;

    for (int i = 0; i < 5; ++i) {
        *(p + i) = new double[i + 1];
    }
}

void release(double **p)
{
    if (p == NULL)
        return;

    for (int i = 0; i < 5; ++i) {
        delete[] *(p + i);
        *(p + i) = NULL;
    }
}
