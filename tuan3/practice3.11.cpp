#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    
    cout << "Enter N, M = ";
    while (!(cin >> n)) {
        cout << "Invalid input. Please enter an integer for N.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter N, M = ";
    }
    
    while (!(cin >> m) || m <= 0) {
        if (cin.fail()) cout << "Invalid input. Please enter an integer for M.\n";
        else cout << "Invalid input. M must be positive.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter M = ";
    }
    
    cout << "The first " << m << " bit from the right of " << n << ": ";
    for (int i = m - 1; i >= 0; i--) cout << ((n >> i) & 1);
    cout << '\n';
    
    return 0;
}
