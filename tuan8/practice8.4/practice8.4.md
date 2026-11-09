8.4
1)
a) m[1][3]

m[1][3] là một phần tử kiểu int. Địa chỉ của nó, &m[1][3], có kiểu:

int *

b) m[0]

m[0] là một mảng một chiều gồm 6 phần tử int, tức kiểu int[6]. Trong biểu thức, mảng này decay thành con trỏ tới phần tử đầu tiên:

int *

Địa chỉ của cả mảng m[0], tức &m[0], có kiểu con trỏ tới mảng 6 int:

int (*)[6]

c) m

m là mảng hai chiều int[4][6]. Trong biểu thức, m decay thành con trỏ tới hàng đầu tiên:

int (*)[6]

Địa chỉ của cả mảng m, tức &m, có kiểu:

int (*)[4][6]

2) Truy cập m[2][4] không dùng []

int value = *(*(m + 2) + 4);
