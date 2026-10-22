#include <iostream>
#include <cstring>

static int fr[256];

int main()
{
    char s[1001];
    std::cin.getline(s, 1001);
    for (int i = 0; s[i]; i++)
        if (s[i] != ' ')
            fr[(unsigned char)s[i]]++;
    int mx = 0;
    for (int c = 0; c < 256; c++)
        if (fr[c] > mx)
            mx = fr[c];
    for (int f = mx; f >= 1; f--) {
        int cn = 0;
        char ch[256];
        for (int c = 0; c < 256; c++)
            if (fr[c] == f)
                ch[cn++] = (char)c;
        if (cn > 0) {
            std::cout << f << ":";
            for (int k = 0; k < cn; k++)
                std::cout << ' ' << ch[k];
            std::cout << "\n";
        }
    }
    return 0;
}
