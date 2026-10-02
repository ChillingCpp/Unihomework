#include <iostream>
using namespace std;

int main(){

    string name;
    int birth;
    getline(cin, name);
    cin >> birth;
    cout << "Hello " << name << ", now you are " << 2026 - birth << " years old.\n";
}