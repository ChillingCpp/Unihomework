#include <stdio.h>
using namespace std;

struct NGAY{
    unsigned short d;
    unsigned short m;
    unsigned short y;
};

void nhap(NGAY &a);
void xuat(NGAY &a);
void xuat(NGAY &a, char f[]);
int ss(NGAY n1, NGAY n2);
bool inc(NGAY &a, int k);
bool dec(NGAY &a, int k);
void compute(NGAY a, NGAY b);


void nhap(NGAY& a)
{
    while (1){
        printf("nhap ngay : ");
        if (scanf("%h", &a.d) != 1 || a.d > 31) continue;
        break;
    }
    while (1){
        printf("nhap thang : ");
        if (scanf("%h", &a.m) != 1 ||  a.m > 12) continue;
        if ((a.d == 29 || a.d == 28) && (a.m !=  2)) continue;
        if ((a.d == 30) && (a.m != 4 || a.m != 6 || a.m != 9 || a.m != 11)) continue;
        if ((a.d == 31) && (a.m != 1 || a.m != 3 || a.m != 5 || a.m != 7 || a.m != 8 || a.m != 10 || a.m != 12)) continue;
        break;
    }
    while (1){
        printf("nhap nam : ");
        if (scanf("%h", &a.y) != 1 || a.y < 0 || a.y > 60000) continue; 
        if (a.d == 29 && !(a.y % 400 == 0 || (a.y % 100 == 0 && a.y % 4 == 0))) continue;
        break;
        
    }
    // gioi han nam [1....60000]
}
void xuat(NGAY &a)
{
    // yyyy-mm-dd
}
void xuat(NGAY& a, char f[]){

}
int ss(NGAY n1, NGAY n2)
{
    // > 0 : ngay 1 > ngay 2
    // = 0 : ngay 1 == ngay 2
    // < 0 : ngay 1 < ngay 2
}
bool inc(NGAY& a, int k) // demo tang 1 ngay trong ham main 
{
    if (k <= 0) return false;
}
bool dec(NGAY& a, int k) // demo giam 1 ngay trong ham main 
{
    if (k >= 0) return false;
}
void compute(NGAY a, NGAY b)
{
    /// in ra khoang cach tinh theo ngay, tinh theo thang, tinh theo nam, dang so thuc
    // lay 365/ 12 ra trung binh
}
int main()
{  
    NGAY ngay;
}
