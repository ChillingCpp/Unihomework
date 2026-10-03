#include <bits/stdc++.h>
using namespace std;

bool isPrime(int n) {
    if (n < 2) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; i * i <= n; i += 2)
        if (n % i == 0) return false;
    return true;
}

int main() {
    int n;
    
    cout << "Enter a positive integer = ";
    while (!(cin >> n) || n < 1) {
        if (cin.fail()) cout << "Invalid input. Please enter an integer.\n";
        else cout << "Invalid input. N must be positive.\n";
        cin.clear();
        cin.ignore(1e9, '\n');
        cout << "Enter a positive integer = ";
    }
    
    int cnt = 0;
    for (int i = 2; i <= n; i++) {
        if (isPrime(i)) {
            cnt++;
            cout << "#" << cnt << " = " << i << '\n';
        }
    }
    cout << "There are " << cnt << " prime numbers.\n";
    
    return 0;
}
