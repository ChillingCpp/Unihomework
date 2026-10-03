#include <bits/stdc++.h>
#include <windows.h>
using namespace std;

int main() {
    int cnt = 0;
    for (int n = 100; n <= 999; n++) {
        int h = n / 100;
        int t = (n / 10) % 10;
        int o = n % 10;
        
        if (t == h + o) {
            cnt++;
            cout << cnt << ": " << n << '\n';
            Sleep(100);
        }
    }
    cout << "There are " << cnt << " satisfied numbers.\n";
    
    return 0;
}
