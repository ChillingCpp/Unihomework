#include <iostream>
#include <cmath>
using namespace std;

int main(){

    double p, q;
    cin >> p >> q;
    double d = sqrt(pow(q, 2) / 4.0 + pow(p, 6) / 27.0);
    cout << "Solution x = " << (float) cbrt(-q / 2.0  + d)  + cbrt(-q / 2.0 - d) << '\n';
}