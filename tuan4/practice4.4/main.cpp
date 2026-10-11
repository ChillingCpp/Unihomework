#include "menu_input.h"
#include "menu_compute.h"
#include "menu_output.h"
int main()
{
    while (1) {
        out_menu();
        int s;
        in_sel(s);
        if (!run_sel(s))
            break;
    }
    return 0;
}
