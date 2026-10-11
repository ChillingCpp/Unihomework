#include "menu_compute.h"
#include "p41_input.h"
#include "p41_compute.h"
#include "p41_output.h"
#include "p42_input.h"
#include "p42_compute.h"
#include "p42_output.h"
#include "p43_input.h"
#include "p43_compute.h"
#include "p43_output.h"
static void run41()
{
    int n;
    p41_in(n);
    p41_out(n);
}
static void run42()
{
    int a;
    int b;
    char o;
    int e;
    p42_in(a, b, o);
    int r = p42_calc(a, b, o, e);
    p42_out(r, e);
}
static void run43()
{
    double a;
    double b;
    double c;
    p43_in(a, b, c);
    p43_out(p43_kind(a, b, c));
}
int run_sel(int s)
{
    if (s == 1)
        run41();
    else if (s == 2)
        run42();
    else if (s == 3)
        run43();
    else
        return 0;
    return 1;
}
