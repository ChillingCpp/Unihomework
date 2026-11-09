#include "paragraph.h"

void read_paragraph()
{
    char        pv = '\n', c = std::getchar();
    std::string s;
    while (true)
    {
        if (c == EOF)
            break;
        s.push_back(c);
        if (pv == '.' && c == '\n')
            break;
        if (!isspace(pv))
            pv = c;
        c = std::getchar();
    }
    std::cout << '\n' << s << '\n';
}
