# Practice 8.5 — Pointer-to-pointer and dynamic memory

Compile:

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp dynamic_array.cpp -o practice8.5
```

Run:

```powershell
.\practice8.5
```

## a) Memory allocated in `main()`

Given the original code:

```cpp
double *p[10];
initialize(p + 3);
release(p);
```

- `double *p[10];` khai báo mảng 10 con trỏ `double *` trên stack. Kích thước là `10 * sizeof(double *)`: thường **80 byte** trên hệ 64-bit và **40 byte** trên hệ 32-bit.
- `initialize(p + 3);` cấp phát 5 mảng động trên heap với số phần tử lần lượt là `1, 2, 3, 4, 5`. Tổng cộng `15` phần tử `double`, tức `15 * sizeof(double)`: thường **120 byte** nếu `sizeof(double) == 8`.
- `release(p);` không cấp phát byte nào, nhưng trong đề là **không đúng** vì `p[0]`, `p[1]`, `p[2]` chưa được khởi tạo và các vùng nhớ thật nằm ở `p[3]` … `p[7]`. Cần gọi `release(p + 3);` để giải phóng đúng 5 mảng.

## b) Allocation map

```text
p[0]  -> chưa khởi tạo
p[1]  -> chưa khởi tạo
p[2]  -> chưa khởi tạo
p[3]  -> double[1]   (1 phần tử)
p[4]  -> double[2]   (2 phần tử)
p[5]  -> double[3]   (3 phần tử)
p[6]  -> double[4]   (4 phần tử)
p[7]  -> double[5]   (5 phần tử)
p[8]  -> chưa khởi tạo
p[9]  -> chưa khởi tạo
```

`initialize(p + 3)` nhận con trỏ tới `p[3]`, nên bên trong hàm `p[0]` tương ứng với `p[3]` của `main`, `p[1]` tương ứng `p[4]`, …, `p[4]` tương ứng `p[7]`.

## c) `release()`

```cpp
void release(double **p)
{
    if (p == NULL)
        return;

    for (int i = 0; i < 5; ++i) {
        delete[] *(p + i);
        *(p + i) = NULL;
    }
}
```

Phải gọi `release(p + 3)` trong `main`. Mảng `p` được khởi tạo toàn bộ bằng `NULL`, nên `release` an toàn với các vị trí chưa được cấp phát và có thể gọi lại mà không bị double delete.

## Kết quả chạy mẫu

```text
sizeof(double*) = 8 bytes
sizeof(double) = 8 bytes
p[10] uses 80 bytes on the stack
heap doubles = 15
heap bytes = 120
```
