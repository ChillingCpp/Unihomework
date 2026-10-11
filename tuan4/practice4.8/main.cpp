#include "input.h"
#include "compute.h"
#include "output.h"
int main()
{
    D a;
    D b;
    in(a, b);
    out(cmp(a, b), next(a), prev(b));
    return 0;
}
