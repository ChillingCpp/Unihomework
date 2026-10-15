#include "io.h"
int main()
{
    int a[MX][MX];
    int n;
    in(a, n);
    out(md(a, n), ad(a, n), rw(a, n), mg(a, n));
    return 0;
}
