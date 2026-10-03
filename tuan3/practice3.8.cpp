#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    int mx = 0, mn = 0, cnt = 0;
    double sum = 0;
    
    int i = 1;
    while (true) {
        cout << "Number " << i << " = ";
        while (!(cin >> n)) {
            cout << "Invalid input. Please enter an integer.\n";
            cin.clear();
            cin.ignore(1e9, '\n');
            cout << "Number " << i << " = ";
        }
        
        if (n == 0) break;
        if (n < 0) {
            cout << "Invalid input. Please enter a positive integer.\n";
            continue;
        }
        
        if (cnt == 0) mx = mn = n;
        else {
            mx = max(mx, n);
            mn = min(mn, n);
        }
        sum += n;
        cnt++;
        i++;
    }
    
    if (cnt > 0) {
        cout << "Max = " << mx << '\n';
        cout << "Min = " << mn << '\n';
        cout << "Average = " << sum / cnt << '\n';
    } else {
        cout << "No valid numbers entered.\n";
    }
    
    return 0;
}
