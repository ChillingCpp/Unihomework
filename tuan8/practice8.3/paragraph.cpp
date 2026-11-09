#include "paragraph.h"

void read_paragraph()
{
    char        pv = 'l';
    int         c  = std::getchar();
    std::string s;
    while (true)
    {
        if (c == EOF)
            break;
        s.push_back(c);
        if (pv == '.' && c == '\n')
            break;
        if (!isspace(c))
            pv = (char) c;
        c = std::getchar();
    }
    std::cout << s << '\n';
}
