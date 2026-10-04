#include <iostream>


int main()
{
    int  a, b;
    char op;

    std::cout << "Enter two integers = ";
    std::cin >> a >> b;
    std::cin.ignore(1e9, '\n');


    std::cout << "Enter an operator (+, -, *, /, %) = ";
    std::cin >> op;
    std::cin.ignore(1e9, '\n');

    switch (op)
    {
        case '+':
            std::cout << "Result = " << a + b << '\n';
            break;
        case '-':
            std::cout << "Result = " << a - b << '\n';
            break;
        case '*':
            std::cout << "Result = " << a * b << '\n';
            break;
        case '/':
            if (b == 0)
                std::cout << "Error: divided by zero.\n";
            else
                std::cout << "Result = " << a / b << '\n';
            break;
        case '%':
            if (b == 0)
                std::cout << "Error: divided by zero.\n";
            else
                std::cout << "Result = " << a % b << '\n';
            break;
    }

    return 0;
}
