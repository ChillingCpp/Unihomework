#include <bits/stdc++.h>
using namespace std;

int main() {
    int m, y;
    
    cout << "Enter month and year = ";
    while (!(cin >> m) || m < 1 || m > 12) {
        cout << "Invalid month. Please enter a month between 1 and 12.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter month and year = ";
    }
    
    while (!(cin >> y)) {
        cout << "Invalid year. Please enter an integer.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter month and year = ";
    }
    
    int d;
    if (m == 2) {
        bool leap = (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);
        d = leap ? 29 : 28;
    } else if (m == 4 || m == 6 || m == 9 || m == 11) {
        d = 30;
    } else {
        d = 31;
    }
    
    cout << "Month " << m << " in year " << y << " has " << d << " days.\n";
    
    return 0;
}
