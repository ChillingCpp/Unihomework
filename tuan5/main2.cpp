#include <math.h>
#include <stdio.h>
using namespace std;

long long bai1(long long x) { return x * (x + 1) / 2; }
long long bai2(long long x) { return x * (x + 1) * (2 * x + 1) / 6; }
double bai3(int x) {
  double ans = 0.0;
  for (int i = 1; i <= x; ++i)
    ans += 1.0 / i;
  return ans;
}
double bai4(int x) {
  double ans = 0.0;
  for (int i = 2; i <= x; i += 2)
    ans += 1.0 / i;
  return ans;
}
double bai5(int x) {

  double ans = 0.0;
  for (int i = 1; i <= x; i += 2)
    ans += 1.0 / i;
  return ans;
}

void bai20(int x) {
  for (int i = 1; i * i <= x; ++i) {
    if (i * i == x)
      printf("%d ", i);
    if (x % i == 0) {
      printf("%d ", i);
      printf("%d ", x / i);
    }
  }
}

long long bai21(int x) {
  long long ans = 0;
  for (int i = 1; i * i <= x; ++i) {
    if (i * i == x)
      ans += i;
    else if (x % i == 0)
      ans += i + (x / i);
  }
  return ans;
}

long long bai22(int x) {
  long long ans = 1;
  for (int i = 1; i * i <= x; ++i) {
    if (i * i == x)
      ans *= i;
    else if (x % i == 0)
      ans *= i * (x / i);
  }
  return ans;
}

int bai23(int x) {
  long long ans = 0;
  for (int i = 1; i * i <= x; ++i) {
    if (i * i == x)
      ans++;
    else if (x % i == 0)
      ans += 2;
  }
  return ans;
}

int bai24(int x) {
  long long ans = 0;
  while (x % 2 == 0)
    x /= 2;
  for (int i = 1; i * i <= x; ++i) {
    if (i * i == x)
      ans++;
    else if (x % i == 0)
      ans += 2;
  }
  return ans;
}
long long bai25(int x) {
  long long ans = 0;
  for (int i = 1; i * i <= x; ++i) {
    if (i * i == x && i % 2 == 0)
      ans += i;
    else if (x % i == 0)
      ans += i * (i % 2 == 0) + (x / i) * ((x / i) % 2 == 0);
  }
  return ans;
}

double bai33(long long x) {
  double ans = 0.0;
  for (long long i = 1; i <= x; ++i)
    ans = sqrt(2.0 + ans);
  return ans;
}

double bai34(long long x) {
  double ans = 0.0;
  for (long long i = 1; i <= x; ++i)
    ans = sqrt((double)i + ans);
  return ans;
}

long long bai42(long long x) {
  long long k = 0;
  while ((k + 1) * (k + 2) / 2 < x)
    k++;
  return k;
}

long long bai50(long long x) {
  long long ans = 0;
  while (x > 0) {
    ans = ans * 10 + x % 10;
    x /= 10;
  }
  return ans;
}

int bai57(long long x) {
  long long t = x;
  while (x > 0) {
    if (t % 10 != x % 10)
      return 0;
    t /= 10;
    x /= 10;
  }
  return 1;
}

long long bai74(int d, int m, long long y) {
  int a[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  if (y % 400 == 0 || (y % 4 == 0 && y % 100 != 0))
    a[1] = 29;
  long long ans = d;
  for (int i = 0; i < m - 1; ++i)
    ans += a[i];
  return ans;
}

int main() {
  long long x;
  int n;
  printf("nhap x : ");
  scanf("%lld", &x);
  printf("Tong cong : %lld\n", bai1(x));

  printf("nhap x :");
  scanf("%lld", &x);
  printf("Tong binh phuong : %lld\n", bai2(x));

  printf("nhap n :");
  scanf("%d", &n);
  printf("S3 = %.2f\n", bai3(n));

  printf("nhap n :");
  scanf("%d", &n);
  printf("S4 = %.2f\n", bai4(n));

  printf("nhap n :");
  scanf("%d", &n);
  printf("S5 = %.2f\n", bai5(n));

  printf("nhap n :");
  scanf("%d", &n);
  printf("Uoc so : ");
  bai20(n);
  printf("\n");

  printf("nhap n :");
  scanf("%d", &n);
  printf("Tong uoc so = %lld\n", bai21(n));

  printf("nhap n :");
  scanf("%d", &n);
  printf("Tich uoc so = %lld\n", bai22(n));

  printf("nhap n :");
  scanf("%d", &n);
  printf("So luong uoc so = %d\n", bai23(n));

  printf("nhap n :");
  scanf("%d", &n);
  printf("So luong uoc so le = %d\n", bai24(n));

  printf("nhap n :");
  scanf("%d", &n);
  printf("Tong uoc so chan = %lld\n", bai25(n));

  printf("nhap x :");
  scanf("%lld", &x);
  printf("S33 = %.2f\n", bai33(x));

  printf("nhap x :");
  scanf("%lld", &x);
  printf("S34 = %.2f\n", bai34(x));

  printf("nhap x :");
  scanf("%lld", &x);
  printf("k = %lld\n", bai42(x));

  printf("nhap x :");
  scanf("%lld", &x);
  printf("Dao nguoc = %lld\n", bai50(x));

  printf("nhap x :");
  scanf("%lld", &x);
  printf(bai57(x) ? "YES\n" : "NO\n");

  int d, m, y;
  printf("nhap d m y :");
  scanf("%d %d %d", &d, &m, &y);
  printf("Thu tu ngay = %lld\n", bai74(d, m, y));
}