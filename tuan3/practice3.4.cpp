#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    
    cout << "Enter a positive integer N = ";
    while (!(cin >> n) || n <= 0) {
        if (cin.fail()) cout << "Invalid input. Please enter an integer.\n";
        else cout << "Invalid input. N must be positive.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter a positive integer N = ";
    }
    
    long long f = 1;
    for (int i = 1; i <= n; i++) f *= i;
    cout << "N! = " << f << '\n';
    
    double ln2 = 0;
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 1) ln2 += 1.0 / i;
        else ln2 -= 1.0 / i;
    }
    cout << "ln(2) = " << ln2 << '\n';
    
    double pi = 0;
    for (int i = 0; i <= n; i++) {
        if (i % 2 == 0) pi += 1.0 / (2 * i + 1);
        else pi -= 1.0 / (2 * i + 1);
    }
    cout << "PI = " << pi * 4 << '\n';
    
    long long s = 0;
    for (int i = 1; i * i <= n; i++) s += i * i;
    cout << "S = " << s << '\n';
    
    return 0;
}
