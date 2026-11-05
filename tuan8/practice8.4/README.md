# Practice 8.4 — Address types of a static 2-D array

Compile:

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp matrix_access.cpp -o practice8.4
```

Run:

```powershell
.\practice8.4
```

Given:

```cpp
int m[4][6];
```

## a) Address types

- `m[1][3]` là một `int`. Địa chỉ `&m[1][3]` có kiểu `int *`.
- `m[0]` là mảng `int[6]`; trong biểu thức nó decay thành `int *`. Địa chỉ `&m[0]` có kiểu `int (*)[6]` (con trỏ tới mảng 6 `int`).
- `m` là mảng `int[4][6]`; trong biểu thức nó decay thành `int (*)[6]`. Địa chỉ `&m` có kiểu `int (*)[4][6]` (con trỏ tới mảng 4×6 `int`).

## b) Access `m[2][4]` without `[]`

```cpp
int value = *(*(m + 2) + 4);
```

Hoặc dùng hàm trong project:

```cpp
int value = matrix_value(m, 2, 4);
```

`m + 2` trỏ tới hàng thứ 2; `*(m + 2)` là mảng hàng đó và decay thành `int *`; cộng 4 rồi dereference để lấy phần tử cột 4.
