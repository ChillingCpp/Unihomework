# Exercises — Chapter 12 Pointers and Arrays (exe12.pdf)

*(Programming Projects skipped as requested.)*

## Exercise 1

Đề: Suppose that the following declarations are in effect:

```c
int a[] = {5, 15, 34, 54, 14, 2, 52, 72};
int *p = &a[1], *q = &a[5];
```

(a) What is the value of `*(p + 3)`?

(b) What is the value of `*(q - 3)`?

(c) What is the value of `q - p`?

(d) Is the condition `p < q` true or false?

(e) Is the condition `*p < *q` true or false?

Đáp án:

| Câu | Kết quả |
|---|---|
| (a) | `14` |
| (b) | `34` |
| (c) | `4` |
| (d) | `true` |
| (e) | `false` |

## Exercise 2 (W)

Đề: Suppose that `high`, `low`, and `middle` are all pointer variables of the same type, and that `low` and `high` point to elements of an array. Why is the following statement illegal, and how could it be fixed?

```c
middle = (low + high) / 2;
```

Đáp án:

Phép cộng hai con trỏ là không hợp lệ trong C vì không có ý nghĩa xác định. Có thể sửa bằng cách dùng hiệu của hai con trỏ rồi cộng một nửa khoảng cách vào `low`:

```c
middle = low + (high - low) / 2;
```

## Exercise 3

Đề: What will be the contents of the `a` array after the following statements are executed?

```c
#define N 10

int a[N] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
int *p = &a[0], *q = &a[N - 1], temp;

while (p < q) {
  temp = *p;
  *p++ = *q;
  *q-- = temp;
}
```

Đáp án:

```c
{10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
```

## Exercise 4 (W)

Đề: Rewrite the `make_empty`, `is_empty`, and `is_full` functions of Section 10.2 to use the pointer variable `top_ptr` instead of the integer variable `top`.

Đáp án:

```c
int *top_ptr = contents;

void make_empty(void)
{
  top_ptr = contents;
}

bool is_empty(void)
{
  return top_ptr == contents;
}

bool is_full(void)
{
  return top_ptr == contents + STACK_SIZE;
}
```

## Exercise 5

Đề: Suppose that `a` is a one-dimensional array and `p` is a pointer variable. Assuming that the assignment `p = a` has just been performed, which of the following expressions are illegal because of mismatched types? Of the remaining expressions, which are true (have a nonzero value)?

```c
(a) p == a[0]
(b) p == &a[0]
(c) *p == a[0]
(d) p[0] == a[0]
```

Đáp án:

- Không hợp lệ: (a).
- Hợp lệ và có giá trị đúng: (b), (c), (d).

## Exercise 6 (W)

Đề: Rewrite the following function to use pointer arithmetic instead of array subscripting. (In other words, eliminate the variable `i` and all uses of the `[]` operator.) Make as few changes as possible.

```c
int sum_array(const int a[], int n)
{
  int i, sum;

  sum = 0;
  for (i = 0; i < n; i++)
    sum += a[i];
  return sum;
}
```

Đáp án:

```c
int sum_array(const int a[], int n)
{
  int sum;
  const int *p;

  sum = 0;
  for (p = a; p < a + n; p++)
    sum += *p;
  return sum;
}
```

## Exercise 7

Đề: Write the following function:

```c
bool search(const int a[], int n, int key);
```

`a` is an array to be searched, `n` is the number of elements in the array, and `key` is the search key. `search` should return `true` if `key` matches some element of `a`, and `false` if it doesn't. Use pointer arithmetic—not subscripting—to visit array elements.

Đáp án:

```c
bool search(const int a[], int n, int key)
{
  const int *p;

  for (p = a; p < a + n; p++)
    if (*p == key)
      return true;

  return false;
}

```

## Exercise 8

Đề: Rewrite the following function to use pointer arithmetic instead of array subscripting. (In other words, eliminate the variable `i` and all uses of the `[]` operator.) Make as few changes as possible.

```c
void store_zeros(int a[], int n)
{
  int i;

  for (i = 0; i < n; i++)
    a[i] = 0;
}
```

Đáp án:

```c
void store_zeros(int a[], int n)
{
  int *p;

  for (p = a; p < a + n; p++)
    *p = 0;
}
```

## Exercise 9

Đề: Write the following function:

```c
double inner_product(const double *a, const double *b, int n);
```

`a` and `b` both point to arrays of length `n`. The function should return `a[0] * b[0] + a[1] * b[1] + ... + a[n-1] * b[n-1]`. Use pointer arithmetic—not subscripting—to visit array elements.

Đáp án:

```c
double inner_product(const double *a, const double *b, int n)
{
  const double *p, *q;
  double sum = 0.0;

  for (p = a, q = b; p < a + n; p++, q++)
    sum += *p * *q;

  return sum;
}
```

## Exercise 10

Đề: Modify the `find_middle` function of Section 11.5 so that it uses pointer arithmetic to calculate the return value.

Đáp án:

```c
int *find_middle(int a[], int n)
{
  return a + n / 2;
}
```

## Exercise 11

Đề: Modify the `find_largest` function so that it uses pointer arithmetic—not subscripting—to visit array elements.

Đáp án:

```c
int find_largest(int a[], int n)
{
  int *p, max;

  max = *a;
  for (p = a + 1; p < a + n; p++)
    if (*p > max)
      max = *p;

  return max;
}
```

## Exercise 12

Đề: Write the following function:

```c
void find_two_largest(const int *a, int n, int *largest,
                      int *second_largest);
```

`a` points to an array of length `n`. The function searches the array for its largest and second-largest elements, storing them in the variables pointed to by `largest` and `second_largest`, respectively. Use pointer arithmetic—not subscripting—to visit array elements.

Đáp án:

```c
void find_two_largest(const int *a, int n, int *largest,
                      int *second_largest)
{
  const int *p;

  if (*a > *(a + 1)) {
    *largest = *a;
    *second_largest = *(a + 1);
  } else {
    *largest = *(a + 1);
    *second_largest = *a;
  }

  for (p = a + 2; p < a + n; p++) {
    if (*p > *largest) {
      *second_largest = *largest;
      *largest = *p;
    } else if (*p > *second_largest) {
      *second_largest = *p;
    }
  }
}
```

## Exercise 13 (W)

Đề: Section 8.2 had a program fragment in which two nested `for` loops initialized the array `ident` for use as an identity matrix. Rewrite this code, using a single pointer to step through the array one element at a time. *Hint:* Since we won't be using row and column index variables, it won't be easy to tell where to store 1. Instead, we can use the fact that the first element of the array should be 1, the next `N` elements should be 0, the next element should be 1, and so forth. Use a variable to keep track of how many consecutive 0s have been stored; when the count reaches `N`, it's time to store 1.

Đáp án:

```c
int *p;
int zeros = N;

for (p = (int *) ident; p < (int *) ident + N * N; p++) {
  if (zeros == N) {
    *p = 1;
    zeros = 0;
  } else {
    *p = 0;
    zeros++;
  }
}
```

## Exercise 14

Đề: Assume that the following array contains a week's worth of hourly temperature readings, with each row containing the readings for one day:

```c
int temperatures[7][24];
```

Write a statement that uses the `search` function (see Exercise 7) to search the entire `temperatures` array for the value 32.

Đáp án:

```c
bool found = search(&temperatures[0][0], 7 * 24, 32);
```

## Exercise 15 (W)

Đề: Write a loop that prints all temperature readings stored in row `i` of the `temperatures` array (see Exercise 14). Use a pointer to visit each element of the row.

Đáp án:

```c
int *p;

for (p = temperatures[i]; p < temperatures[i] + 24; p++)
  printf("%d\n", *p);
```

## Exercise 16

Đề: Write a loop that prints the highest temperature in the `temperatures` array (see Exercise 14) for each day of the week. The loop body should call the `find_largest` function, passing it one row of the array at a time.

Đáp án:

```c
int i;

for (i = 0; i < 7; i++)
  printf("%d\n", find_largest(temperatures[i], 24));
```

## Exercise 17

Đề: Rewrite the following function to use pointer arithmetic instead of array subscripting. (In other words, eliminate the variables `i` and `j` and all uses of the `[]` operator.) Use a single loop instead of nested loops.

```c
int sum_two_dimensional_array(const int a[][LEN], int n)
{
  int i, j, sum = 0;

  for (i = 0; i < n; i++)
    for (j = 0; j < LEN; j++)
      sum += a[i][j];

  return sum;
}
```

Đáp án:

```c
int sum_two_dimensional_array(const int a[][LEN], int n)
{
  const int *p;
  int sum = 0;

  for (p = (const int *) a; p < (const int *) a + n * LEN; p++)
    sum += *p;

  return sum;
}
```

## Exercise 18

Đề: Write the `evaluate_position` function described in Exercise 13 of Chapter 9. Use pointer arithmetic—not subscripting—to visit array elements. Use a single loop instead of nested loops.

Đáp án:

```c
int evaluate_position(char board[8][8])
{
  char *p;
  int white = 0, black = 0;

  for (p = (char *) board; p < (char *) board + 8 * 8; p++) {
    switch (*p) {
      case 'Q': white += 9; break;
      case 'R': white += 5; break;
      case 'B': case 'N': white += 3; break;
      case 'P': white += 1; break;
      case 'q': black += 9; break;
      case 'r': black += 5; break;
      case 'b': case 'n': black += 3; break;
      case 'p': black += 1; break;
      default: break;
    }
  }

  return white - black;
}
```
