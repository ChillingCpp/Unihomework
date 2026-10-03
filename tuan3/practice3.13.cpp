#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    
    cout << "Enter N = ";
    while (!(cin >> n) || n <= 0) {
        if (cin.fail()) cout << "Invalid input. Please enter an integer.\n";
        else cout << "Invalid input. N must be positive.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter N = ";
    }
    
    bool desc = true;
    int t = n, prev = t % 10;
    t /= 10;
    while (t > 0) {
        int cur = t % 10;
        if (cur >= prev) {
            desc = false;
            break;
        }
        prev = cur;
        t /= 10;
    }
    
    bool sym = true;
    t = n;
    int rev = 0, orig = n;
    while (t > 0) {
        rev = rev * 10 + t % 10;
        t /= 10;
    }
    sym = (orig == rev);
    
    cout << (desc ? "Descending." : "Not descending.") << '\n';
    cout << (sym ? "Symmetric." : "Not symmetric.") << '\n';
    
    return 0;
}
