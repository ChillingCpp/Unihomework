7.1

đây là đoạn mã sai, hãy sửa nó lại ở câu a
b) kết quả chương trình là gì
int main()
{
    int *x, y = 2; 
    float *z = &y;
    *x = *z + y;
    printf(“%d”, y);
}   

a)
int main()
{
    int *x, y = 2; 
    int *z = &y;
    x = z;
    *x = *z + y;
    printf(“%d”, *x);
}   
b) 4

7.2
void swap1(int x, int y)
{
    int temp = x;
    x = y;
    y = temp;
}
void swap2(int &x, int &y)
{
    int temp = x; 
    x = y;
    y = temp;
}
void swap3(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp; 
}

1) hàm swap1(x, y) chỉ đổi giá trị x, y được copy nội bộ ở trong hàm swap1 mà không thực sự tráo đổi 2 giá trị x và y được truyền vào, vì thế khi sau khi thì khi swap(x, y) thì 2 giá trị x và y vẫn giữ nguyên
2) hàm swap2(x, y) chỉ hỗ trợ trong c++ và có tác dụng tráo đổi 2 giá trị x và y thành y và x. sau khi gọi hàm swap(x, y) thì giá trị x sẽ bằng y và giá trị y sẽ bằng x
3) hàm swap3(x, y) hỗ trợ ở cả 2 ngôn ngữ c và c++, có tác dụng giống như hàm swap2(x, y) nhưng ta phải truyền địa chỉ của x và y vào.

7.3
int main()
{
    double  m[100];
    double *p1, *p2;
    p1 = m;
    p2 = &m[6];
    printf("%lld", p2 - p1);
}
hàm trên trả về khoảng cách giữa 2 phần tử a[0] và a[6] là 6 - 0 = 6, vì là lấy địa chỉ của 2 con trỏ trừ cho nhau và in theo format của long long, không phải là trả về khoảng cách theo byte là 48 ( lí do là double có 8 byte và khoảng cách giữa 2 phần tử là 6 nên khoảng cách theo byte là 6 * 8 = 48)

7.4

int main()
{
    int   x = 1023;
    char* p = (char*) &x;
    printf("%d %d %d %d", p[0], p[1], p[2], p[3]);
}
số 1023 được chuyển đổi thành 32 bit nhị phân như sau : 
00000000 00000000 00000011 11111111

Do đa số máy tính sử dụng cơ chế lưu bộ nhớ bit từ bên phải sang trái ( little endian ) nên thứ tự bit lưu trong bộ nhớ là đảo ngược thứ tự byte của dãy bit trên: 
11111111 00000011 00000000 00000000

vì kiểu dữ liệu int có 4 bytes và kiểu dữ liệu char có 1 byte nên khi int được chuyển đổi sang dạng con trỏ char thì sẽ là mảng gồm 4 phần tử kiểu dữ liệu char
và thứ tự biểu diễn các phần tử của p như sau theo little endian : 
11111111 00000011 00000000 00000000
p[0]     p[1]     p[2]     p[3]

kiểu dữ liệu char tùy theo compiler sẽ được định dưới dạng unsigned ( 0 - 255) hay không unsigned (-128 - 127)

đối với không unsigned thì được biểu diễn dưới dạng 2 complements thì 11111111 = -128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = -1
đối với unsigned thì 11111111 = 255 khi chuyển từ hệ nhị phân sang thập phân

do đó p[0] = -1 hoặc 255, p[1] = 3, p[2] = 0, p[3] = 0;
chương trình trên sẽ in ra như sau trên trình biên dịch GCC (g++ 15.2.0) và Clang (clang++ 19.1.7) windows 11 64 bits UCRT :
 
-1 3 0 0 

