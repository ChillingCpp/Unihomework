#include <stdio.h>

struct NGAY{
    unsigned short d;
    unsigned short m;
    unsigned short y;
};

void nhap(NGAY &a);
void xuat(NGAY &a);
void xuat(NGAY &a, const char f[]);
int ss(NGAY n1, NGAY n2);
bool inc(NGAY &a, int k);
bool dec(NGAY &a, int k);
void compute(NGAY a, NGAY b);

static int lp(int y)
{
    return y % 400 == 0 || (y % 4 == 0 && y % 100 != 0);
}

static int vd(NGAY a)
{
    if (a.y < 1 || a.m < 1 || a.m > 12 || a.d < 1)
        return 0;
    int t[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int q = t[a.m - 1];
    if (a.m == 2 && lp(a.y))
        q = 29;
    return a.d <= q;
}

static void clr()
{
    int c;
    while ((c = getchar()) != '\n' && c != EOF)
        ;
}

static int mt(const char *s, const char *t, int n)
{
    int i = 0;
    while (i < n && s[i] && s[i] == t[i])
        i++;
    return i == n;
}

static long ds(NGAY a)
{
    long y = a.y - (a.m <= 2);
    long era = (y >= 0 ? y : y - 399) / 400;
    long yoe = y - era * 400;
    long doy = (153 * (a.m + (a.m > 2 ? -3 : 9)) + 2) / 5 + a.d - 1;
    long doe = yoe * 365 + yoe / 4 - yoe / 100 + doy;
    return era * 146097 + doe - 719468;
}

static void fr(long z, NGAY &a)
{
    z += 719468;
    long era = (z >= 0 ? z : z - 146096) / 146097;
    long doe = z - era * 146097;
    long yoe = (doe - doe / 1460 + doe / 36524 - doe / 146096) / 365;
    long y = yoe + era * 400;
    long doy = doe - (365 * yoe + yoe / 4 - yoe / 100);
    long mp = (5 * doy + 2) / 153;
    long d = doy - (153 * mp + 2) / 5 + 1;
    long m = mp + (mp < 10 ? 3 : -9);
    a.y = (unsigned short)(y + (m <= 2));
    a.m = (unsigned short)m;
    a.d = (unsigned short)d;
}

void nhap(NGAY &a)
{
    while (1) {
        while (1) {
            printf("nhap ngay : ");
            if (scanf("%hu", &a.d) == 1 && a.d >= 1 && a.d <= 31)
                break;
            clr();
        }
        while (1) {
            printf("nhap thang : ");
            if (scanf("%hu", &a.m) == 1 && a.m >= 1 && a.m <= 12)
                break;
            clr();
        }
        while (1) {
            printf("nhap nam : ");
            if (scanf("%hu", &a.y) == 1 && a.y >= 1 && a.y <= 60000)
                break;
            clr();
        }
        if (vd(a))
            return;
    }
}

void xuat(NGAY &a)
{
    printf("%04u-%02u-%02u", (unsigned)a.y, (unsigned)a.m, (unsigned)a.d);
}

void xuat(NGAY &a, const char f[])
{
    char mn[][4] = {"Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
    int i = 0;
    while (f[i]) {
        if (mt(f + i, "yyyy", 4)) {
            printf("%04u", (unsigned)a.y);
            i += 4;
        } else if (mt(f + i, "yy", 2)) {
            printf("%02u", (unsigned)(a.y % 100));
            i += 2;
        } else if (mt(f + i, "MMM", 3)) {
            printf("%s", mn[a.m - 1]);
            i += 3;
        } else if (mt(f + i, "MM", 2)) {
            printf("%02u", (unsigned)a.m);
            i += 2;
        } else if (f[i] == 'M') {
            printf("%u", (unsigned)a.m);
            i++;
        } else if (mt(f + i, "dd", 2)) {
            printf("%02u", (unsigned)a.d);
            i += 2;
        } else if (f[i] == 'd') {
            printf("%u", (unsigned)a.d);
            i++;
        } else {
            putchar(f[i]);
            i++;
        }
    }
}

int ss(NGAY n1, NGAY n2)
{
    if (n1.y != n2.y)
        return n1.y < n2.y ? -1 : 1;
    if (n1.m != n2.m)
        return n1.m < n2.m ? -1 : 1;
    if (n1.d != n2.d)
        return n1.d < n2.d ? -1 : 1;
    return 0;
}

bool inc(NGAY &a, int k)
{
    if (k <= 0)
        return false;
    NGAY t;
    fr(ds(a) + k, t);
    if (t.y < 1 || t.y > 60000)
        return false;
    a = t;
    return true;
}

bool dec(NGAY &a, int k)
{
    if (k >= 0)
        return false;
    NGAY t;
    fr(ds(a) + k, t);
    if (t.y < 1 || t.y > 60000)
        return false;
    a = t;
    return true;
}

void compute(NGAY a, NGAY b)
{
    long u = ds(a);
    long v = ds(b);
    long k = v > u ? v - u : u - v;
    printf("Khoang cach: %ld ngay\n", k);
    printf("              %.2f thang\n", k * 12.0 / 365);
    printf("              %.2f nam\n", k / 365.0);
}

int main()
{
    NGAY a;
    NGAY b;
    NGAY t;
    int k;

    printf("Nhap ngay 1:\n");
    nhap(a);
    printf("Ngay 1: ");
    xuat(a);
    printf("\n");
    printf("yyyy-MM-dd: ");
    xuat(a, "yyyy-MM-dd");
    printf("\n");
    printf("MMM dd yy: ");
    xuat(a, "MMM dd yy");
    printf("\n");

    printf("nhap k : ");
    while (1) {
        if (scanf("%d", &k) == 1 && k > 0)
            break;
        clr();
    }

    t = a;
    if (inc(t, k)) {
        printf("Sau %d ngay: ", k);
        xuat(t);
        printf("\n");
    }

    t = a;
    if (dec(t, -k)) {
        printf("Truoc %d ngay: ", k);
        xuat(t);
        printf("\n");
    }

    printf("Nhap ngay 2:\n");
    nhap(b);
    compute(a, b);

    return 0;
}
