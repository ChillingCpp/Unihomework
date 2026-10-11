#include "menu.h"
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
