#include <bits/stdc++.h>
using namespace std;

void printDigit(char c) {
    switch (c) {
        case '0': cout << "Zero "; break;
        case '1': cout << "One "; break;
        case '2': cout << "Two "; break;
        case '3': cout << "Three "; break;
        case '4': cout << "Four "; break;
        case '5': cout << "Five "; break;
        case '6': cout << "Six "; break;
        case '7': cout << "Seven "; break;
        case '8': cout << "Eight "; break;
        case '9': cout << "Nine "; break;
    }
}

int main() {
    while (true) {
        cout << "Phone number: ";
        
        int c, cnt = 0;
        bool bad = false;
        bool tooLong = false;
        
        while ((c = getchar()) != '\n' && c != EOF) {
            if (c >= '0' && c <= '9') {
                cnt++;
                if (cnt > 10) {
                    tooLong = true;
                    break;
                }
                printDigit(c);
            } else if (c == ' ' || c == '\t') {
                continue;
            } else {
                bad = true;
                break;
            }
        }
        
        if (tooLong) {
            cout << "\nInvalid input. Phone number must have at most 10 digits.\n";
            continue;
        }
        
        if (bad) {
            cout << "\nInvalid input. Please enter only digits.\n";
            continue;
        }
        
        if (cnt == 0) {
            cout << "\nInvalid input. Please enter a phone number.\n";
            continue;
        }
        
        cout << '\n';
        break;
    }
    
    return 0;
}
