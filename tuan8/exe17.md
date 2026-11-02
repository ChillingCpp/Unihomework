# Exercises — Chapter 17 Advanced Uses of Pointers (exe17.pdf)

*(Programming Projects skipped as requested. Các bài tập liên quan đến linked list — bài 6, 7, 8, 11, 12, 13, 14 — được bỏ qua theo yêu cầu.)*

## Exercise 1

Đề: Having to check the return value of `malloc` (or any other memory allocation function) each time we call it can be an annoyance. Write a function named `my_malloc` that serves as a "wrapper" for `malloc`. When we call `my_malloc` and ask it to allocate `n` bytes, it in turn calls `malloc`, tests to make sure that `malloc` doesn't return a null pointer, and then returns the pointer from `malloc`. Have `my_malloc` print an error message and terminate the program if `malloc` returns a null pointer.

Đáp án:

```c
void *my_malloc(size_t n)
{
  void *p = malloc(n);

  if (p == NULL) {
    printf("Error: malloc failed\n");
    exit(EXIT_FAILURE);
  }

  return p;
}
```

## Exercise 2 (W)

Đề: Write a function named `duplicate` that uses dynamic storage allocation to create a copy of a string. For example, the call

```c
p = duplicate(str);
```

would allocate space for a string of the same length as `str`, copy the contents of `str` into the new string, and return a pointer to it. Have `duplicate` return a null pointer if the memory allocation fails.

Đáp án:

```c
char *duplicate(const char *str)
{
  char *p = malloc(strlen(str) + 1);

  if (p != NULL)
    strcpy(p, str);

  return p;
}
```

## Exercise 3

Đề: Write the following function:

```c
int *create_array(int n, int initial_value);
```

The function should return a pointer to a dynamically allocated `int` array with `n` members, each of which is initialized to `initial_value`. The return value should be `NULL` if the array can't be allocated.

Đáp án:

```c
int *create_array(int n, int initial_value)
{
  int *p = malloc(n * sizeof(int));
  int *q;

  if (p == NULL)
    return NULL;

  for (q = p; q < p + n; q++)
    *q = initial_value;

  return p;
}
```

## Exercise 4

Đề: Suppose that the following declarations are in effect:

```c
struct point { int x, y; };
struct rectangle { struct point upper_left, lower_right; };
struct rectangle *p;
```

Assume that we want `p` to point to a `rectangle` structure whose upper left corner is at (10, 25) and whose lower right corner is at (20, 15). Write a series of statements that allocate such a structure and initialize it as indicated.

Đáp án:

```c
p = malloc(sizeof(*p));
p->upper_left.x = 10;
p->upper_left.y = 25;
p->lower_right.x = 20;
p->lower_right.y = 15;
```

## Exercise 5 (W)

Đề: Suppose that `f` and `p` are declared as follows:

```c
struct {
  union {
    char a, b;
    int c;
  } d;
  int e[5];
} f, *p = &f;
```

Which of the following statements are legal?

```c
(a) p->b = ' ';
(b) p->e[3] = 10;
(c) (*p).d.a = '*';
(d) p->d->c = 20;
```

Đáp án:

- Hợp lệ: (b), (c).
- Không hợp lệ: (a), (d).

## Exercise 9

Đề: True or false: If `x` is a structure and `a` is a member of that structure, then `(&x)->a` is the same as `x.a`. Justify your answer.

Đáp án:

Đúng. `&x` là con trỏ đến `x`, nên `(&x)->a` tương đương với `(*&x).a`. Vì `*&x` chính là `x`, biểu thức này bằng `x.a`.

## Exercise 10

Đề: Modify the `print_part` function of Section 16.2 so that its parameter is a pointer to a `part` structure. Use the `->` operator in your answer.

Đáp án:

```c
void print_part(const struct part *p)
{
  printf("Part number: %d\n", p->number);
  printf("Part name: %s\n", p->name);
  printf("Quantity on hand: %d\n", p->on_hand);
}
```

## Exercise 15 (W)

Đề: Show the output of the following program and explain what it does.

```c
#include <stdio.h>

int f1(int (*f)(int));
int f2(int i);

int main(void)
{
  printf("Answer: %d\n", f1(f2));
  return 0;
}

int f1(int (*f)(int))
{
  int n = 0;

  while ((*f)(n)) n++;
  return n;
}

int f2(int i)
{
  return i * i + i - 12;
}
```

Đáp án:

```text
Answer: 3
```

Giải thích: `f1` nhận con trỏ đến hàm `f2` và tăng `n` từ 0 trong khi `f2(n)` khác 0. Ta có `f2(n) = n² + n - 12`; giá trị này bằng 0 tại `n = 3` (và `n = -4`). Vòng lặp dừng ở `n = 3`, nên `f1` trả về 3. Chương trình đếm số giá trị liên tiếp `0, 1, 2` mà `f2` cho kết quả khác 0 trước khi gặp nghiệm đầu tiên.

## Exercise 16

Đề: Write the following function. The call `sum(g, i, j)` should return `g(i) + ... + g(j)`.

```c
int sum(int (*f)(int), int start, int end);
```

Đáp án:

```c
int sum(int (*f)(int), int start, int end)
{
  int total = 0;
  int i;

  for (i = start; i <= end; i++)
    total += f(i);

  return total;
}
```

## Exercise 17 (W)

Đề: Let `a` be an array of 100 integers. Write a call of `qsort` that sorts only the *last 50* elements in `a`. (You don't need to write the comparison function).

Đáp án:

```c
qsort(a + 50, 50, sizeof(int), compare_ints);
```

## Exercise 18

Đề: Modify the `compare_parts` function so that parts are sorted with their numbers in *descending* order.

Đáp án:

```c
int compare_parts(const void *p, const void *q)
{
  return ((const struct part *) q)->number -
         ((const struct part *) p)->number;
}
```

## Exercise 19

Đề: Write a function that, when given a string as its argument, searches the following array of structures for a matching command name, then calls the function associated with that name.

```c
struct {
  char *cmd_name;
  void (*cmd_pointer)(void);
} file_cmd[] = {
  {"new",       new_cmd},
  {"open",      open_cmd},
  {"close",     close_cmd},
  {"close all", close_all_cmd},
  {"save",      save_cmd},
  {"save as",   save_as_cmd},
  {"save all",  save_all_cmd},
  {"print",     print_cmd},
  {"exit",      exit_cmd}
};
```

Đáp án:

```c
void execute_command(const char *command)
{
  int i;

  for (i = 0; i < (int)(sizeof(file_cmd) / sizeof(file_cmd[0])); i++) {
    if (strcmp(command, file_cmd[i].cmd_name) == 0) {
      file_cmd[i].cmd_pointer();
      return;
    }
  }
}
```
