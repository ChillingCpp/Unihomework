#include <stdio.h>
#include <iostream>

using namespace std;

void bai333(){
    printf("hello world");
}
void bai343();
void bai363(); // tu 0 toi n-1
void bai390(); // neu co nhieu cot thi in ra  het
void bai391(); // ma tran con phai co hang >= 2 va cot >= 2 va khong phai ma tran goc

int main(){

    int a[][50] = {{}};
    int n = sizeof(a) / sizeof(a[0]);

    bai333();
    bai343();
    bai363();
    bai390();
    bai391();
}
