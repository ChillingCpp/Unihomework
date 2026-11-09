#include "paragraph.h"

void read_paragraph()
{
    char        pv = '\n', c = getchar();
    std::string s;
    while (true)
    {
        s.push_back(c);
        if (pv == '.' && c == '\n')
            break;
        pv = c;
        c  = getchar();
    }
    std::cout << '\n' << s << '\n';
}
