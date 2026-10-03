#include <bits/stdc++.h>
using namespace std;

int main() {
    double a, b, c;
    
    cout << "Enter coefficients a, b, c = ";
    while (!(cin >> a)) {
        cout << "Invalid input. Please enter a number.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter coefficients a, b, c = ";
    }
    
    while (!(cin >> b)) {
        cout << "Invalid input. Please enter a number.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter coefficients a, b, c = ";
    }
    
    while (!(cin >> c)) {
        cout << "Invalid input. Please enter a number.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter coefficients a, b, c = ";
    }
    
    if (a == 0) {
        if (b == 0) {
            if (c == 0) cout << "Infinite solutions.\n";
            else cout << "No solution!\n";
        } else {
            cout << "Solution 1 = " << -c / b << '\n';
        }
    } else {
        double d = b * b - 4 * a * c;
        if (d > 0) {
            cout << "Solution 1 = " << (-b + sqrt(d)) / (2 * a) << '\n';
            cout << "Solution 2 = " << (-b - sqrt(d)) / (2 * a) << '\n';
        } else if (d == 0) {
            cout << "Solution 1 = " << -b / (2 * a) << '\n';
        } else {
            cout << "No solution!\n";
        }
    }
    
    return 0;
}
