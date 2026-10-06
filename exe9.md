# Exercises — Chapter 9 Functions (exe9.pdf)

*(Programming Projects skipped as requested.)*

## Exercise 1

Đề: The following function, which computes the area of a triangle, contains two errors. Locate the errors and show how to fix them. (*Hint:* There are no errors in the formula.)

```c
double triangle_area(double base, height)
double product;
{
  product = base * height;
  return product / 2;
}
```

Đáp án:

```c
double triangle_area(double base, double height)
{
  double product;
  product = base * height;
  return product / 2;
}
```

## Exercise 2 (W)

Đề: Write a function `check(x, y, n)` that returns 1 if both x and y fall between 0 and n-1, inclusive. The function should return 0 otherwise. Assume that x, y, and n are all of type int.

Đáp án:

```c
int check(int x, int y, int n)
{
  return x >= 0 && x <= n - 1 && y >= 0 && y <= n - 1;
}
```

## Exercise 3

Đề: Write a function `gcd(m, n)` that calculates the greatest common divisor of the integers m and n. (Programming Project 2 in Chapter 6 describes Euclid's algorithm for computing the GCD.)

Đáp án:

```c
int gcd(int m, int n)
{
  int r;
  while (n != 0) {
    r = m % n;
    m = n;
    n = r;
  }
  return m;
}
```

## Exercise 4 (W)

Đề: Write a function `day_of_year(month, day, year)` that returns the day of the year (an integer between 1 and 366) specified by the three arguments.

Đáp án:

```c
int day_of_year(int month, int day, int year)
{
  int t[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  int i, s = 0;
  if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
    t[1] = 29;
  for (i = 0; i < month - 1; i++)
    s += t[i];
  return s + day;
}
```

## Exercise 5

Đề: Write a function `num_digits(n)` that returns the number of digits in n (a positive integer). *Hint:* To determine the number of digits in a number n, divide it by 10 repeatedly. When n reaches 0, the number of divisions indicates how many digits n originally had.

Đáp án:

```c
int num_digits(int n)
{
  int c = 0;
  do {
    c++;
    n /= 10;
  } while (n > 0);
  return c;
}
```

## Exercise 6 (W)

Đề: Write a function `digit(n, k)` that returns the k-th digit (from the right) in n (a positive integer). For example, `digit(829, 1)` returns 9, `digit(829, 2)` returns 2, and `digit(829, 3)` returns 8. If k is greater than the number of digits in n, have the function return 0.

Đáp án:

```c
int digit(int n, int k)
{
  int i;
  for (i = 1; i < k; i++)
    n /= 10;
  return n % 10;
}
```

## Exercise 7

Đề: Suppose that the function f has the following definition:

```c
int f(int a, int b) { ... }
```

Which of the following statements are legal? (Assume that i has type int and x has type double.)

```c
(a) i = f(83, 12);
(b) x = f(83, 12);
(c) i = f(3.15, 9.28);
(d) x = f(3.15, 9.28);
(e) f(83, 12);
```

Đáp án:

```text
(a), (b), (c), (d), (e)
```

## Exercise 8 (W)

Đề: Which of the following would be valid prototypes for a function that returns nothing and has one double parameter?

```c
(a) void f(double x);
(b) void f(double);
(c) void f(x);
(d) f(double x);
```

Đáp án:

```text
(a), (b)
```

## Exercise 9 (*)

Đề: What will be the output of the following program?

```c
#include <stdio.h>
void swap(int a, int b);
int main(void)
{
  int i = 1, j = 2;
  swap(i, j);
  printf("i = %d, j = %d\n", i, j);
  return 0;
}
void swap(int a, int b)
{
  int temp = a;
  a = b;
  b = temp;
}
```

Đáp án:

```text
i = 1, j = 2
```

## Exercise 10 (W)

Đề: Write functions that return the following values. (Assume that a and n are parameters, where a is an array of int values and n is the length of the array.)

```text
(a) The largest element in a.
(b) The average of all elements in a.
(c) The number of positive elements in a.
```

Đáp án:

```c
int largest(int a[], int n)
{
  int i, m = a[0];
  for (i = 1; i < n; i++)
    if (a[i] > m)
      m = a[i];
  return m;
}

double average(int a[], int n)
{
  int i, s = 0;
  for (i = 0; i < n; i++)
    s += a[i];
  return (double) s / n;
}

int num_positive(int a[], int n)
{
  int i, c = 0;
  for (i = 0; i < n; i++)
    if (a[i] > 0)
      c++;
  return c;
}
```

## Exercise 11

Đề: Write the following function:

```c
float compute_GPA(char grades[], int n);
```

The grades array will contain letter grades (A, B, C, D, or F, either upper-case or lower-case); n is the length of the array. The function should return the average of the grades (assume that A = 4, B = 3, C = 2, D = 1, and F = 0).

Đáp án:

```c
float compute_GPA(char grades[], int n)
{
  int i, s = 0;
  for (i = 0; i < n; i++) {
    switch (grades[i]) {
    case 'A': case 'a': s += 4; break;
    case 'B': case 'b': s += 3; break;
    case 'C': case 'c': s += 2; break;
    case 'D': case 'd': s += 1; break;
    default: break;
    }
  }
  return (float) s / n;
}
```

## Exercise 12

Đề: Write the following function:

```c
double inner_product(double a[], double b[], int n);
```

The function should return `a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]`.

Đáp án:

```c
double inner_product(double a[], double b[], int n)
{
  int i;
  double s = 0.0;
  for (i = 0; i < n; i++)
    s += a[i] * b[i];
  return s;
}
```

## Exercise 13

Đề: Write the following function, which evaluates a chess position:

```c
int evaluate_position(char board[8][8]);
```

board represents a configuration of pieces on a chessboard, where the letters K, Q, R, B, N, P represent White pieces, and the letters k, q, r, b, n, and p represent Black pieces. `evaluate_position` should sum the values of the White pieces (Q = 9, R = 5, B = 3, N = 3, P = 1). It should also sum the values of the Black pieces (done in a similar way). The function will return the difference between the two numbers. This value will be positive if White has an advantage in material and negative if Black has an advantage.

Đáp án:

```c
int evaluate_position(char board[8][8])
{
  int i, j, w = 0, b = 0;
  for (i = 0; i < 8; i++)
    for (j = 0; j < 8; j++) {
      switch (board[i][j]) {
      case 'Q': w += 9; break;
      case 'R': w += 5; break;
      case 'B': case 'N': w += 3; break;
      case 'P': w += 1; break;
      case 'q': b += 9; break;
      case 'r': b += 5; break;
      case 'b': case 'n': b += 3; break;
      case 'p': b += 1; break;
      default: break;
      }
    }
  return w - b;
}
```

## Exercise 14

Đề: The following function is supposed to return true if any element of the array a has the value 0 and false if all elements are nonzero. Sadly, it contains an error. Find the error and show how to fix it:

```c
bool has_zero(int a[], int n)
{
  int i;
  for (i = 0; i < n; i++)
    if (a[i] == 0)
      return true;
    else
      return false;
}
```

Đáp án:

```c
bool has_zero(int a[], int n)
{
  int i;
  for (i = 0; i < n; i++)
    if (a[i] == 0)
      return true;
  return false;
}
```

## Exercise 15 (W)

Đề: The following (rather confusing) function finds the median of three numbers. Rewrite the function so that it has just one return statement.

```c
double median(double x, double y, double z)
{
  if (x <= y)
    if (y <= z) return y;
    else if (x <= z) return z;
    else return x;
  if (z <= y) return y;
  if (x <= z) return x;
  return z;
}
```

Đáp án:

```c
double median(double x, double y, double z)
{
  double m;
  if (x <= y)
    if (y <= z) m = y;
    else if (x <= z) m = z;
    else m = x;
  else if (z <= y) m = y;
  else if (x <= z) m = x;
  else m = z;
  return m;
}
```

## Exercise 16

Đề: Condense the fact function in the same way we condensed power.

Đáp án:

```c
int fact(int n)
{
  if (n <= 1)
    return 1;
  return n * fact(n - 1);
}
```

## Exercise 17 (W)

Đề: Rewrite the fact function so that it's no longer recursive.

Đáp án:

```c
int fact(int n)
{
  int i, r = 1;
  for (i = 2; i <= n; i++)
    r *= i;
  return r;
}
```

## Exercise 18

Đề: Write a recursive version of the gcd function (see Exercise 3). Here's the strategy to use for computing gcd(m, n): If n is 0, return m. Otherwise, call gcd recursively, passing n as the first argument and m % n as the second.

Đáp án:

```c
int gcd(int m, int n)
{
  if (n == 0)
    return m;
  return gcd(n, m % n);
}
```

## Exercise 19 (W) (*)

Đề: Consider the following "mystery" function:

```c
void pb(int n)
{
  if (n != 0) {
    pb(n / 2);
    putchar('0' + n % 2);
  }
}
```

Trace the execution of the function by hand. Then write a program that calls the function, passing it a number entered by the user. What does the function do?

Đáp án:

Hàm in ra biểu diễn nhị phân của n (n = 0 thì không in gì).

```c
void pb(int n)
{
  if (n != 0) {
    pb(n / 2);
    putchar('0' + n % 2);
  }
}
```
