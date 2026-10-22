#include <iostream>
#include <fstream>

void run()
{
    std::ifstream fin("OPERATION.TXT");
    std::ofstream fout("RESULT.TXT");
    int a;
    int b;
    char op;
    while (fin >> a >> op >> b) {
        if (op == '+')
            fout << a + b << "\n";
        else if (op == '-')
            fout << a - b << "\n";
        else if (op == '*')
            fout << a * b << "\n";
        else if (op == '/') {
            if (b == 0)
                fout << "Divided by zero\n";
            else
                fout << a / b << "\n";
        }
    }
    fin.close();
    fout.close();
}
