#include <iostream>
#include <cstring>

static void trim(char *s)
{
    int n = (int)strlen(s);
    int r = 0;
    int w = 0;
    while (r < n && s[r] == ' ')
        r++;
    while (r < n) {
        if (s[r] != ' ') {
            s[w++] = s[r++];
        } else {
            s[w++] = ' ';
            r++;
            while (r < n && s[r] == ' ')
                r++;
        }
    }
    if (w > 0 && s[w - 1] == ' ')
        w--;
    s[w] = '\0';
}

void run()
{
    char s[1001];
    std::cin.getline(s, 1001);
    trim(s);
    std::cout << s << "\n";
}
