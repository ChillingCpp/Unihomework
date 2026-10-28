#include <iostream>
#include <fstream>
#include <cstring>
#include <cctype>
#include <iomanip>

struct S {
    char name[100];
    char id[20];
    double gpa;
};

static void cap(char *s)
{
    int n = (int)strlen(s);
    int nw = 1;
    for (int i = 0; i < n; i++) {
        if (isspace(s[i]))
            nw = 1;
        else if (nw) {
            s[i] = (char)std::toupper((unsigned char)s[i]);
            nw = 0;
        } else {
            s[i] = (char)std::tolower((unsigned char)s[i]);
        }
    }
}

void run()
{
    std::ifstream fin("STUDENT.TXT");
    S s[100];
    int sn = 0;
    char line[200];
    while (fin.getline(line, 200)) {
        char *p = std::strchr(line, '|');
        if (!p)
            continue;
        *p = '\0';
        std::strcpy(s[sn].name, line);
        std::strcpy(s[sn].id, p + 1);
        cap(s[sn].name);
        double sum = 0;
        int cnt = 0;
        double v;
        while (fin >> v) {
            sum += v;
            cnt++;
            int c = fin.peek();
            if (c == '\n' || c == EOF)
                break;
        }
        fin.ignore(1000, '\n');
        s[sn].gpa = sum / cnt;
        sn++;
    }
    fin.close();
    for (int i = 0; i < sn - 1; i++)
        for (int j = i + 1; j < sn; j++)
            if (s[j].gpa > s[i].gpa) {
                S t = s[i];
                s[i] = s[j];
                s[j] = t;
            }
    std::ofstream fout("GPA.TXT");
    for (int i = 0; i < sn; i++)
        fout << s[i].id << '|' << s[i].name << '|' << std::fixed << std::setprecision(1) << s[i].gpa << "\n";
    fout.close();
}
