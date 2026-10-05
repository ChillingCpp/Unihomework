#include <iostream>


void printdi(char c, int cnt)
{
    switch (c)
    {
        case '0':
            std::cout << (cnt == 1 ? "Zero " : "zero ");
            break;
        case '1':
            std::cout << (cnt == 1 ? "One " : "one ");
            break;
        case '2':
            std::cout << (cnt == 1 ? "Two " : "two ");
            break;
        case '3':
            std::cout << (cnt == 1 ? "Three " : "three ");
            break;
        case '4':
            std::cout << (cnt == 1 ? "Four " : "four ");
            break;
        case '5':
            std::cout << (cnt == 1 ? "Five " : "five ");
            break;
        case '6':
            std::cout << (cnt == 1 ? "Six " : "six ");
            break;
        case '7':
            std::cout << (cnt == 1 ? "Seven " : "seven ");
            break;
        case '8':
            std::cout << (cnt == 1 ? "Eight " : "eight ");
            break;
        case '9':
            std::cout << (cnt == 1 ? "Nine " : "nine ");
            break;
    }
}

int main()
{
    while (true)
    {
        std::cout << "Phone number: ";

        int c = 0;
        int  cnt     = 0;
        bool bad     = false;
        bool tooLong = false;
        
        while (true)
        {
            c = getchar();
            if (c == '\n' || c == EOF) 
                break;
            if (c >= '0' && c <= '9')
            {
                cnt++;
                if (cnt > 10)
                {
                    tooLong = true;
                    break;
                }
                printdi(c, cnt);
            }
            else if (c == ' ' || c == '\t')
                continue;
            else
            {
                bad = true;
                break;
            }
        }

        if (tooLong || bad || cnt == 0)
        {
            std::cin.ignore(1e9, '\n');
            std::cout << '\n';
            continue;
        }


        std::cout << '\n';
        break;
    }

    return 0;
}
