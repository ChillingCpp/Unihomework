#include "io.h"
#include "compute.h"
int main()
{
    D a;
    D b;
    in(a, b);
    out(cmp(a, b), next(a), prev(b));
    return 0;
}
