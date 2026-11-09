# Exercises — Chapter 22 Input/Output (exercise_exe22.pdf)

*(Programming Projects skipped as requested.)*

> **Quy ước:** Các bài yêu cầu viết hoặc sửa mã xử lý file (bài 3, 10, 12–15) được trả lời bằng **C++17** với `<fstream>` và cơ chế RAII. Đề bài gốc vẫn được giữ nguyên.

## Exercise 1 (Section 22.1)

**Đề:** Indicate whether each of the following files is more likely to contain text data or binary data:

(a) A file of object code produced by a C compiler  
(b) A program listing produced by a C compiler  
(c) An email message sent from one computer to another  
(d) A file containing a graphics image

**Đáp án:**

| Câu | Loại dữ liệu |
|---|---|
| (a) | Binary |
| (b) | Text |
| (c) | Text |
| (d) | Binary |

## Exercise 2 (Section 22.2) (W)

**Đề:** Indicate which mode string is most likely to be passed to `fopen` in each of the following situations:

(a) A database management system opens a file containing records to be updated.  
(b) A mail program opens a file of saved messages so that it can add additional messages to the end.  
(c) A graphics program opens a file containing a picture to be displayed on the screen.  
(d) An operating system command interpreter opens a "shell script" (or "batch file") containing commands to be executed.

**Đáp án:**

| Câu | Mode string |
|---|---|
| (a) | `"r+b"` |
| (b) | `"a"` |
| (c) | `"rb"` |
| (d) | `"r"` |

## Exercise 3

**Đề:** Find the error in the following program fragment and show how to fix it.

```c
FILE *fp;

if (fp = fopen(filename, "r")) {
    read characters until end-of-file
}
fclose(fp);
```

**Đáp án (C++):**

Lỗi: nếu mở file thất bại, `fp` không hợp lệ nhưng `fclose(fp)` vẫn được gọi ở ngoài khối `if`. Trong C++, không cần đóng file thủ công: `std::ifstream` tự đóng khi ra khỏi phạm vi (RAII). Chỉ cần kiểm tra việc mở file trước khi đọc.

```cpp
FILE *fp;

if (fp = fopen(filename, "r")) {
    read characters until end-of-file
    fclose(fp); 
}
```

Nếu vẫn muốn đóng thủ công, đặt `fp.close()` **bên trong** nhánh mở file thành công; không gọi khi mở thất bại.

## Exercise 4 (Section 22.3) (W)

**Đề:** Show how each of the following numbers will look if displayed by `printf` with `%#012.5g` as the conversion specification:

(a) `83.7361`  
(b) `29748.6607`  
(c) `1054932234.0`  
(d) `0.0000235218`

**Đáp án:**

```text
(a) 00000083.736
(b) 00000029749.
(c) 001.0549e+09
(d) 002.3522e-05
```

## Exercise 5

**Đề:** Is there any difference between the `printf` conversion specifications `%.4d` and `%04d`? If so, explain what it is.

**Đáp án:**

Có. `%.4d` dùng **precision** bằng 4: tối thiểu 4 chữ số, dấu âm không tính vào precision. `%04d` dùng **width** bằng 4 với cờ `0`: tổng độ rộng tối thiểu là 4 ký tự, bao gồm cả dấu âm.

Với số không âm có không quá 4 chữ số, hai cách thường cho cùng kết quả. Với số âm thì khác, ví dụ `-42`:

```text
printf("%.4d", -42);   /* -0042 */
printf("%04d", -42);   /* -042  */
```

## Exercise 6 (W)

**Đề:** Write a call of `printf` that prints

```text
1 widget
```

if the `widget` variable (of type `int`) has the value 1, and

```text
n widgets
```

otherwise, where `n` is the value of `widget`. You are not allowed to use the `if` statement or any other statement; the answer must be a single call of `printf`.

**Đáp án:**

```c
printf("%d widget%s\n", widget, widget == 1 ? "" : "s");
```

## Exercise 7

**Đề:** Suppose that we call `scanf` as follows:

```c
n = scanf("%d%f%d", &i, &x, &j);
```

(`i`, `j`, and `n` are `int` variables and `x` is a `float` variable.) Assuming that the input stream contains the characters shown, give the values of `i`, `j`, `n`, and `x` after the call. In addition, indicate which characters were consumed by the call.

(a) `10•20•30□`  
(b) `1.0•2.0•3.0□`  
(c) `0.1•0.2•0.3□`  
(d) `.1•.2•.3□`

Trong các dòng input trên, `•` là dấu cách và `□` là newline.

**Đáp án:**

| Input | `i` | `x` | `j` | `n` | Ký tự đã được đọc |
|---|---:|---:|---:|---:|---|
| (a) | 10 | 20.0 | 30 | 3 | `10 20 30` |
| (b) | 1 | 0.0 | 2 | 3 | `1.0 2` |
| (c) | 0 | 0.1 | 0 | 3 | `0.1 0` |
| (d) | không đổi | không đổi | không đổi | 0 | không có ký tự nào |

Ở (d), `%d` gặp `.` nên matching failure; `i`, `x`, `j` giữ nguyên giá trị cũ (không xác định nếu chưa khởi tạo). Newline ở cuối các dòng (a)–(c) không bị `scanf` đọc.

## Exercise 8 (W)

**Đề:** In previous chapters, we've used the `scanf` format string `" %c"` when we wanted to skip white-space characters and read a nonblank character. Some programmers use `"%1s"` instead. Are the two techniques equivalent? If not, what are the differences?

**Đáp án:**

Không tương đương.

- `" %c"`: bỏ qua whitespace, sau đó đọc đúng một ký tự vào một biến `char`; không thêm ký tự kết thúc `'\0'`.
- `"%1s"`: bỏ qua whitespace, sau đó đọc tối đa một ký tự **không phải** whitespace vào một mảng `char`, rồi thêm `'\0'`; mảng phải có ít nhất 2 phần tử.

Cả hai đọc một ký tự không trắng, nhưng `%1s` lưu dưới dạng chuỗi có kết thúc `'\0'`, còn `%c` chỉ lưu một ký tự đơn.

## Exercise 9 (Section 22.4)

**Đề:** Which one of the following calls is *not* a valid way of reading one character from the standard input stream?

(a) `getch()`  
(b) `getchar()`  
(c) `getc(stdin)`  
(d) `fgetc(stdin)`

**Đáp án:**

`(a) getch()`

## Exercise 10 (W)

**Đề:** The `fcopy.c` program has one minor flaw: it doesn't check for errors as it's writing to the destination file. Errors during writing are rare, but do occasionally occur (the disk might become full, for example). Show how to add the missing error check to the program, assuming that we want it to display a message and terminate immediately if an error occurs.

**Đáp án (C++):**

Thay `getc`/`putc` bằng `std::ifstream::get` và `std::ofstream::put`. Sau mỗi lần ghi, kiểm tra `!dest`; nếu lỗi, báo ra `std::cerr` và kết thúc ngay.

```cpp
#include <cstdlib>
#include <fstream>
#include <iostream>

int main(int argc, char* argv[])
{
    if (argc != 3) {
        std::cerr << "Usage: fcopy <source> <destination>\n";
        return EXIT_FAILURE;
    }

    std::ifstream source(argv[1], std::ios::binary);
    std::ofstream dest(argv[2], std::ios::binary);
    if (!source || !dest) {
        std::cerr << "Cannot open file\n";
        return EXIT_FAILURE;
    }

    char ch;
    while (source.get(ch)) {
        dest.put(ch);
        if (!dest) {
            std::cerr << "Error writing to " << argv[2] << '\n';
            return EXIT_FAILURE;
        }
    }

    if (source.bad()) {
        std::cerr << "Error reading from " << argv[1] << '\n';
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```

Nếu đặt đoạn sao chép trong một hàm khác, dùng `std::exit(EXIT_FAILURE)` sau khi báo lỗi nếu muốn dừng ngay toàn chương trình.

## Exercise 11

**Đề:** The following loop appears in the `fcopy.c` program:

```c
while ((ch = getc(source_fp)) != EOF)
    putc(ch, dest_fp);
```

Suppose that we neglected to put parentheses around `ch = getc(source_fp)`:

```c
while (ch = getc(source_fp) != EOF)
    putc(ch, dest_fp);
```

Would the program compile without an error? If so, what would the program do when it's run?

**Đáp án:**

Có, chương trình vẫn biên dịch được (có thể có cảnh báo).

Do toán tử `!=` có độ ưu tiên cao hơn toán tử `=`, biểu thức được hiểu là:

```c
while (ch = (getc(source_fp) != EOF))
    putc(ch, dest_fp);
```

Vì vậy `ch` chỉ nhận giá trị `0` hoặc `1`. Khi chưa gặp EOF, `ch` bằng `1` và `putc` ghi byte `0x01` vào file đích; khi gặp EOF, vòng lặp dừng. Kết quả là file đích có cùng số byte với file nguồn nhưng mọi byte đều là `0x01`, không phải bản sao nội dung.

## Exercise 12

**Đề:** Find the error in the following function and show how to fix it.

```c
int count_periods(const char *filename)
{
    FILE *fp;
    int n = 0;
    if ((fp = fopen(filename, "r")) != NULL) {
        while (fgetc(fp) != EOF)
            if (fgetc(fp) == '.')
                n++;
        fclose(fp);
    }
    return n;
}
```

**Đáp án (C++):**

Lỗi: mỗi lần lặp gọi `get` hai lần. Ký tự đọc trong điều kiện `while` bị bỏ qua, nên hàm chỉ kiểm tra các ký tự ở vị trí lẻ.

Sửa:

```cpp
int count_periods(const char *filename)
{
    FILE *fp;
    int n = 0;
    if ((fp = fopen(filename, "r")) != NULL) {
        while ((ch = fgetc(fp)) != EOF)
            if (ch == '.')
                n++;
        fclose(fp);
    }
    return n;
}
```

## Exercise 13

**Đề:** Write the following function:

```c
int line_length(const char *filename, int n);
```

The function should return the length of line `n` in the text file whose name is `filename` (assuming that the first line in the file is line 1). If the line doesn't exist, the function should return 0.

**Đáp án (C++):**

```cpp
#include <fstream>
#include <string>

int line_length(const char* filename, int n)
{
    if (filename == nullptr || n < 1)
        return 0;

    std::ifstream fp(filename);
    if (!fp) 
        return 0;

    std::string line;
    int current = 1;

    while (std::getline(fp, line)) {
        if (current == n) {
            if (!line.empty() && line.back() == '\r')
                line.pop_back();
            return (int)line.size();
        }
        ++current;
    }

    return 0;
}
```

`std::getline` bỏ ký tự `'\n'`; nếu file dùng CRLF, hàm bỏ thêm `'\r'` ở cuối dòng. Hàm trả về 0 nếu dòng không tồn tại hoặc dòng rỗng.

## Exercise 14 (Section 22.5) (W)

**Đề:**

(a) Write your own version of the `fgets` function. Make it behave as much like the real `fgets` function as possible; in particular, make sure that it has the proper return value. To avoid conflicts with the standard library, don't name your function `fgets`.

(b) Write your own version of `fputs`, following the same rules as in part (a).

**Đáp án (C++):**

Trong C++, không cần mảng `char` kết thúc bằng `'\0'`; dùng `std::string` và `std::istream`/`std::ostream`. Hai hàm dưới giữ các ý chính của `fgets`/`fputs`: đọc tối đa `n - 1` ký tự, dừng sau newline, trả về `bool` cho biết có đọc/ghi thành công hay không.

```cpp
#include <istream>
#include <ostream>
#include <string>

bool my_fgets(std::istream& in, std::string& s, int n)
{
    s.clear();
    if (n <= 1) {
        return false;
    }

    char ch;
    while (s.size() <  (std::size_t) n-1 && in.get(ch)) {
        s.push_back(ch);
        if (ch == '\n') {
            break;
        }
    }

    if (in.bad()) {
        return false;
    }
    return !s.empty();
}

bool my_fputs(std::ostream& out, const std::string& s)
{
    out.write(s.data(), (std::streamsize) s.size());
    return (bool) out;
}
```

- `my_fgets` giữ newline nếu gặp newline (giống `fgets`), không thêm `'\0'` vì `std::string` tự quản lý kích thước.
- `my_fputs` ghi đúng toàn bộ nội dung chuỗi, không tự thêm newline (giống `fputs`).
- Trả về `false` khi không đọc/ghi được; `true` khi thành công.

## Exercise 15 (Section 22.7) (W)

**Đề:** Write calls of `fseek` that perform the following file-positioning operations on a binary file whose data is arranged in 64-byte "records." Use `fp` as the file pointer in each case.

(a) Move to the beginning of record `n`. (Assume that the first record in the file is record 0.)  
(b) Move to the beginning of the last record in the file.  
(c) Move forward one record.  
(d) Move backward two records.

**Đáp án (C++):**

Giả sử `fp` là `std::ifstream` (hoặc `std::fstream`) đã mở ở chế độ binary:

```cpp
#include <fstream>

std::ifstream fp("data.bin", std::ios::binary);

// (a) đầu record n
fp.seekg((std::streamoff) n * 64, std::ios::beg);

// (b) đầu record cuối
fp.seekg(-64, std::ios::end);

// (c) tiến một record
fp.seekg(64, std::ios::cur);

// (d) lùi hai record
fp.seekg(-128, std::ios::cur);
```

## Exercise 16 (Section 22.8)

**Đề:** Assume that `str` is a string that contains a "sales rank" immediately preceded by the `#` symbol (other characters may precede the `#` and/or follow the sales rank). A sales rank is a series of decimal digits possibly containing commas, such as the following examples:

```text
989
24,675
1,162,620
```

Write a call of `sscanf` that extracts the sales rank (but not the `#` symbol) and stores it in a string variable named `sales_rank`.

**Đáp án:**

```c
char *p = strchr(str, '#');

if (p != NULL)
    sscanf(p, "#%[0-9,]", sales_rank);
```
