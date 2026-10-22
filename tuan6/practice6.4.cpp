#include <iostream>
#include <fstream>

static int isp(int x)
{
    if (x < 2)
        return 0;
    for (int i = 2; i * i <= x; i++)
        if (x % i == 0)
            return 0;
    return 1;
}

int main()
{
    std::ifstream fin("NUMBER.TXT");
    int out[1000];
    int on = 0;
    int x;
    while (fin >> x) {
        if (isp(x))
            out[on++] = x;
    }
    fin.close();
    std::ofstream fout("PRIME.TXT");
    for (int i = 0; i < on; i++) {
        if (i)
            fout << ' ';
        fout << out[i];
    }
    fout << "\n";
    fout.close();
    return 0;
}
