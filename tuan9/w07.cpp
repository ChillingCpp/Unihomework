#include <stdio.h>
#include <algorithm>

#define MAXC 50

// P-333: Tinh tong cac so hoan thien trong ma tran cac so nguyen.
void bai333(int a[][MAXC], int n, int m)
{
    long long tong = 0;

    printf("P-333: Tong cac so hoan thien trong ma tran\n");

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int x = a[i][j];

            if (x <= 1)
                continue;

            long long s = 1;
            for (long long d = 2; d * d <= x; ++d) {
                if (x % d == 0) {
                    long long q = x / d;
                    s += d;
                    if (q != d)
                        s += q;
                }
            }

            if (s == x) 
                tong += x;
        }
    }

    printf("  Tong = %lld\n", tong);
}

// P-343: Dem so phan tu cuc tri trong ma tran cac so thuc.
// Cuc tri: lon hon tat ca cac lan can hoac nho hon tat ca cac lan can.
void bai343(float a[][MAXC], int n, int m)
{
    int dem = 0;

    printf("P-343: Cac phan tu cuc tri trong ma tran so thuc\n");
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) {
            int laMax = 1;
            int laMin = 1;
            for (int di = -1; di <= 1; ++di) {
                for (int dj = -1; dj <= 1; ++dj) {
                    if (di == 0 && dj == 0)
                        continue;
                    if (i + di < 0 || i + di >= n || j + dj < 0 || j + dj >= m) 
                        continue;
                    float v = a[i + di][j + dj];
                    if (a[i][j] <= v)
                        laMax = 0;
                    if (a[i][j] >= v)
                        laMin = 0;
                }
            }
            if (laMax || laMin) 
                ++dem;
        }

    printf("  So phan tu cuc tri = %d\n", dem);
}

// P-363: Liet ke cac cot tang dan trong ma tran.
// Chi so cot bat dau tu 0.
void bai363(int a[][MAXC], int n, int m)
{
    int co = 0;

    printf("P-363: Cac cot tang dan tu tren xuong duoi\n");

    for (int j = 0; j < m; ++j) {
        int tang = 1;

        for (int i = 1; i < n; ++i) 
            if (a[i][j] <= a[i - 1][j]) {
                tang = 0;
                break;
            }
        
        if (tang) {
            printf("  Cot %d\n", j);
            co = 1;
        }
    }

    if (!co)
        printf("  Khong co cot nao tang dan\n");
}

// P-390: Liet ke cac cot nhieu chu so nhat trong ma tran cac so nguyen.
// So am khong tinh dau am; so 0 co 1 chu so. Chi so cot bat dau tu 0.
void bai390(int a[][MAXC], int n, int m)
{
    int maxDigit = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            long long t = abs(a[i][j]);
        
            int cnt = 0;
            if (t == 0){ 
                maxDigit = std::max(maxDigit, 1);
                continue;
            }
            while (t > 0) {
                ++cnt;
                t /= 10;
            }
            

            maxDigit = std::max(maxDigit, cnt);
        }
    }

    printf("P-390: Cac cot nhieu chu so nhat (%d chu so)\n", maxDigit);

    for (int j = 0; j < m; ++j) {
        int co = 0;

        for (int i = 0; i < n; ++i) {
            long long t = abs(a[i][j]);
            int cnt = 0;
            if (t == 0) 
                cnt = 1;
            else {
                while (t > 0) {
                    ++cnt;
                    t /= 10;
                }
            }

            if (cnt == maxDigit) {
                co = 1;
                break;
            }
        }

        if (co)
            printf("  Cot %d\n", j);
    }
}

// P-391: Tim ma tran con co tong lon nhat.
// Ma tran con phai co it nhat 2 hang, 2 cot va khong phai ca ma tran ban dau.
// Neu co nhieu ma tran con cung tong lon nhat thi in het. Toa do lap chi so tu 0.
void bai391(int a[][MAXC], int n, int m)
{
    if (n < 2 || m < 2) {
        printf("P-391: Khong co ma tran con thoa man\n");
        return;
    }

    long long pre[50][MAXC + 1];

    for (int i = 0; i <= n; ++i)
        pre[0][i] = 0,
        pre[i][0] = 0;

    for (int i = 1; i <= n; ++i) 
        for (int j = 1; j <= m; ++j) 
            pre[i][j] = (long long) a[i - 1][j - 1]  + pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1];


    int co = 0;
    long long best = -1e18;

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            for (int h = 2; i + h <= n; ++h)
                for (int w = 2; j + w <= m; ++w) {
                    int r2 = i + h - 1;
                    int c2 = j + w - 1;
                    if (h == n && w == m)
                        continue;
                    long long sum = pre[r2 + 1][c2 + 1]  - pre[i][c2 + 1] - pre[r2 + 1][j] + pre[i][j];
                    if (!co || sum > best) {
                        best = sum;
                        co = 1;
                    }
                }


    if (!co) {
        printf("P-391: Khong co ma tran con thoa man\n");
        return;
    }

    printf("P-391: Ma tran con co tong lon nhat la %lld\n", best);

    for (int i = 0; i < n; ++i) 
        for (int j = 0; j < m; ++j) 
            for (int h = 2; i + h <= n; ++h) 
                for (int w = 2; j + w <= m; ++w) {
                    int r2 = i + h - 1;
                    int c2 = j + w - 1;

                    if (h == n && w == m)
                        continue;

                    long long sum = pre[r2 + 1][c2 + 1] - pre[i][c2 + 1] - pre[r2 + 1][j] + pre[i][j];

                    if (sum == best)
                        printf("  Tu [%d][%d] den [%d][%d]\n", i, j, r2, c2);
                }
}

int main(void)
{
    int a[][MAXC] = {{}};
    int n = sizeof(a) / sizeof(a[0]);
    int m = MAXC;

    bai333(a, n, m);
    bai363(a, n, m);
    bai390(a, n, m);
    bai391(a, n, m);


    float b[][MAXC] = {{}};
    n = sizeof(b) / sizeof(b[0]);
    bai343(b, n, m);

    return 0;
}