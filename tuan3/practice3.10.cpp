#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b) {
    while (b) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int main() {
    int a, b;
    
    cout << "Enter 2 positive integers = ";
    while (!(cin >> a) || a <= 0) {
        if (cin.fail()) cout << "Invalid input. Please enter an integer.\n";
        else cout << "Invalid input. a must be positive.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter 2 positive integers = ";
    }
    
    while (!(cin >> b) || b <= 0) {
        if (cin.fail()) cout << "Invalid input. Please enter an integer.\n";
        else cout << "Invalid input. b must be positive.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter 2 positive integers = ";
    }
    
    int g = gcd(a, b);
    cout << "GCD = " << g << '\n';
    cout << "LCM = " << 1LL * a * b / g << '\n';
    
    return 0;
}
