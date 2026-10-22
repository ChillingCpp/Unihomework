#include <iostream>
#include <fstream>
#include <cctype>

int main()
{
    std::ifstream fin("INPUT.TXT");
    int wc = 0;
    int nc = 0;
    int c;
    bool iw = false;
    bool inum = false;
    while ((c = fin.get()) != EOF) {
        if (std::isalpha((unsigned char)c)) {
            if (!iw) {
                wc++;
                iw = true;
            }
            inum = false;
        } else if (std::isdigit((unsigned char)c)) {
            if (!inum) {
                nc++;
                inum = true;
            }
            iw = false;
        } else {
            iw = false;
            inum = false;
        }
    }
    fin.close();
    std::cout << "Word count: " << wc << ".\n";
    std::cout << "Number count: " << nc << ".\n";
    return 0;
}
