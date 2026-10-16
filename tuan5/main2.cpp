#include <stdio.h>
#include <functional>
using namespace std;

long long bai1(long long x)
{
    return x * (x+ 1)/2;
}
long long bai2(long long x)
{
    return x * (x  + 1) * (2* x+ 1) / 6;
}
double bai3(int x)
{
    double ans = 0.0;
    for (int i= 1 ; i <= x; ++i)
        ans += 1.0 / i;
    return ans;
}
double bai4(int x)
{
    double ans = 0.0;
    for (int i= 2 ; i <= x; i+=2)
        ans += 1.0 / i;
    return ans;
}
double bai5(int x)
{

    double ans = 0.0;
    for (int i= 1 ; i <= x; i+=2)
        ans += 1.0 / i;
    return ans;
}

void bai20(int x)
{
    for (int i= 1; i * i <= x; ++i){
        if (i * i == x) printf("%d ", &i);
        if(x % i == 0) { printf("%d ", &i); printf("%d ", x / i);}
    }
}

int bai21(int x)
{
    long long ans =0;
    for (int i= 1; i * i <= x; ++i){
        if (i * i == x) ans += i;
        else if(x % i == 0) ans += i + (x /  i);
    }
    return ans;
}

long long bai22(int x)
{
    long long ans =1;
    for (int i= 1; i * i <= x; ++i){
        if (i * i == x) ans *= i;
        else if(x % i == 0) ans *= i * (x /  i);
    }
    return ans;
}

int bai23(int x)
{
    long long ans =0;
    for (int i= 1; i * i <= x; ++i){
        if (i * i == x) ans++;
        else if(x % i == 0) ans+= 2;
    }
    return ans;
}

int bai24(int x)
{
    long long ans =0;
    while (x % 2 == 0) x /= 2;
    for (int i= 1; i * i <= x; ++i){
        if (i * i == x) ans++;
        else if(x % i == 0) ans+= 2;
    }
    return ans;
}
int bai25(int x)
{
    long long ans =0;
    for (int i= 1; i * i <= x; ++i){
        if (i * i == x && i % 2 ==0 ) ans += i;
        else if(x % i == 0) ans += i * (i % 2 == 0) + (x /  i) * ((x / i) % 2== 0);
    }
    return ans;
}
int main()
{
    long long x;
    printf("nhap n : ");
    scanf("%d", &x);
    printf("Tong : ", bai1(x));
    

}