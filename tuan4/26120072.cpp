#include <stdio.h>
#include <iostream>
using namespace std;

void printd(int d){
    switch (d)
    {
    case 1:
        printf("Mot ");
        break;
    case 2:
        printf("Hai ");
        break;
    case 3:
        printf("Ba ");
        break;
    case 4:
        printf("Bon ");
        break;
    case 5:
        printf("Nam ");
        break;
    case 6:
        printf("Sau ");
        break;
    case 7:
        printf("Bay ");
        break;
    case 8:
        printf("Tam ");
        break;
    case 9:
        printf("Chin ");
        break;
    default:
        break;
    }
}

int main(){

    int n;
    scanf("%d", &n);
    bool tram = 0, chuc = 0, donvi=0;
    if (n >= 100 && n <= 999){
        printd(n / 100);
        printf("Tram ");
        n -= (n / 100) * 100;
        tram = 1;
    }
    if (n >= 10 && n <= 99){
        if (n / 10 != 1)
        printd(n /10);
        printf("Muoi ");
        n -= (n / 10) * 10;
        chuc = 1;
    }
    if (n >= 1 && n <= 9){
        if (tram && !chuc)
            printf("le ");
        printd(n);
        donvi = 1;
    }
    if (!tram && !chuc && !donvi) printf("Khong");
    printf("\n");

    int x, y;
    printf("Nhap tien dien thang truoc va thang sau : ");
    scanf("%d%d", &x,&y);

    int ans = 0;
    int kwh = y - x;
    
    (kwh > 0) ? ans += 1484 * min(50, kwh), kwh -= 50 :1;
    (kwh > 0) ? ans += 1533 * min(50, kwh), kwh -= 50:1;
    (kwh > 0) ? ans += 1786 * min(100, kwh), kwh -= 100 :1;
    (kwh > 0) ? ans += 2242 * min(100, kwh), kwh -= 100 :1;
    (kwh > 0) ? ans += 2503 * min(100, kwh), kwh -= 100 :1;
    (kwh > 0) ? ans += 2587 * kwh :1;
    printf("tien dien thang nay : %d", (int) (ans * 1.1f));
}
