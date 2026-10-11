#include "input.h"
#include "compute.h"
#include "output.h"
int main()
{
    S s;
    in(s);
    float g = gpa(s);
    out(g, rank(g));
    return 0;
}
