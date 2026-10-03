#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    char op;
    
    cout << "Enter two integers = ";
    while (!(cin >> a)) {
        cout << "Invalid input. Please enter an integer.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter two integers = ";
    }
    
    while (!(cin >> b)) {
        cout << "Invalid input. Please enter an integer.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter two integers = ";
    }
    
    cout << "Enter an operator (+, -, *, /, %) = ";
    while (!(cin >> op) || (op != '+' && op != '-' && op != '*' && op != '/' && op != '%')) {
        cout << "Invalid operator. Please enter one of +, -, *, /, %.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter an operator (+, -, *, /, %) = ";
    }
    
    switch (op) {
        case '+': cout << "Result = " << a + b << '\n'; break;
        case '-': cout << "Result = " << a - b << '\n'; break;
        case '*': cout << "Result = " << a * b << '\n'; break;
        case '/':
            if (b == 0) cout << "Error: divided by zero.\n";
            else cout << "Result = " << a / b << '\n';
            break;
        case '%':
            if (b == 0) cout << "Error: divided by zero.\n";
            else cout << "Result = " << a % b << '\n';
            break;
    }
    
    return 0;
}
