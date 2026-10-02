#include <iostream>
using namespace std;

int main(){

    int money;
    cin >> money;
    cout << "Note 20000: " << (money / 20000) << '\n';
    money = money - 20000 * (money / 20000);
    cout << "Note 10000: " << (money / 10000) << '\n';
    money = money - 10000 * (money / 10000);
    cout << "Note  5000: " << (money / 5000) << '\n';
    money = money - 5000 * (money / 5000);
    cout << "Note  1000: " << (money / 1000) << '\n';
    money = money - 1000 * (money / 1000);
    cout << "Remain money = " << money << '\n';
}