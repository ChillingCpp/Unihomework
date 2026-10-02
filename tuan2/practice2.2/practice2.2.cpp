#include <iostream>
using namespace std;

int main(){

    int n;
    cin >> n;
    int luck = 0;
    while (n){
        luck = (luck + n % 10) % 10;
        n /= 10;
    }
    cout << "Lucky number = " << luck << '\n';
}