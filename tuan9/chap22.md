# Chương 22 — Nhập/Xuất (I/O) trong C++

> **Tuần 9 — Tổng quan bài học**
>
> Bài này trình bày các khái niệm nhập/xuất của chương 22 và phần thực hành binary file, nhưng **toàn bộ nội dung và ví dụ chỉ dùng C++ chuẩn**.
>
> Mã nguồn trong tài liệu được biên soạn theo C++17. Có thể biên dịch bằng:
>
> ```bash
> g++ -std=c++17 -Wall -Wextra -pedantic main.cpp -o app
> ```

---

## Mục lục

1. Mục tiêu bài học
2. Mô hình luồng (stream)
3. Trạng thái luồng và xử lý lỗi
4. Nhập/xuất màn hình và định dạng
5. Nhập/xuất tệp văn bản
6. Nhập/xuất tệp nhị phân
7. Truy cập ngẫu nhiên trong tệp
8. String stream
9. Tham số dòng lệnh
10. Sao chép tệp
11. Định hướng Practice 9.1 — lệnh COPY
12. Định hướng Practice 9.2 — cắt ảnh BMP
13. Lỗi thường gặp
14. Bảng tra nhanh
15. Câu hỏi tự kiểm tra
16. Tài liệu tham khảo

---

## 1. Mục tiêu bài học

Sau bài này, cần nắm được:

- Luồng dữ liệu là gì, phân biệt luồng chuẩn, luồng tệp và luồng chuỗi.
- Cách dùng `std::cin`, `std::cout`, `std::cerr`, `std::clog`.
- Cách kiểm tra trạng thái luồng và tránh các vòng lặp `while (!eof())` sai.
- Định dạng dữ liệu bằng `<iomanip>`.
- Mở, đọc, ghi, đóng tệp văn bản bằng `std::ifstream`, `std::ofstream`, `std::fstream`.
- Phân biệt chế độ văn bản và nhị phân; dùng `read`, `write`, `gcount`.
- Đọc/ghi nguyên một struct, mảng hoặc buffer nhị phân.
- Di chuyển vị trí đọc/ghi bằng `seekg`, `seekp`, `tellg`, `tellp`.
- Phân tích và tạo chuỗi bằng `std::istringstream`, `std::ostringstream`, `std::stringstream`.
- Nhận tham số dòng lệnh qua `argc`, `argv`.
- Áp dụng để viết chương trình sao chép tệp và cắt ảnh BMP.

### Sơ đồ tổng quát

```text
                    +-------------------+
   bàn phím  -----> | std::cin          |
                    |                   |
   tệp văn bản ----> | std::ifstream     |----> chương trình
   tệp nhị phân ---> | std::ifstream     |
   chuỗi      -----> | std::istringstream|
                    +-------------------+
                              |
                              | xử lý dữ liệu
                              v
                    +-------------------+
   màn hình  <----- | std::cout         |
   lỗi       <----- | std::cerr/clog    |
   tệp văn bản <---- | std::ofstream     |
   tệp nhị phân <--- | std::ofstream     |
   chuỗi      <----- | std::ostringstream|
                    +-------------------+
```

---

## 2. Mô hình luồng (stream)

### 2.1. Luồng là gì?

**Luồng (stream)** là một dãy byte hoặc ký tự được truyền giữa chương trình và một nguồn/đích.

- Nguồn có thể là bàn phím, tệp, chuỗi trong bộ nhớ, socket, thiết bị...
- Đích có thể là màn hình, tệp, chuỗi, máy in...
- Chương trình không cần biết dữ liệu thực sự đến từ đâu; nó chỉ làm việc với giao diện luồng.

C++ cung cấp ba nhóm thư viện chính:

| Thư viện | Dùng cho | Lớp tiêu biểu |
|---|---|---|
| `<iostream>` | luồng chuẩn (bàn phím, màn hình) | `std::cin`, `std::cout`, `std::cerr`, `std::clog` |
| `<fstream>` | luồng tệp | `std::ifstream`, `std::ofstream`, `std::fstream` |
| `<sstream>` | luồng chuỗi trong bộ nhớ | `std::istringstream`, `std::ostringstream`, `std::stringstream` |

### 2.2. Các luồng chuẩn

| Đối tượng | Ý nghĩa | Ghi chú |
|---|---|---|
| `std::cin` | đầu vào chuẩn | thường là bàn phím |
| `std::cout` | đầu ra chuẩn | thường là màn hình, có buffer |
| `std::cerr` | đầu ra lỗi | flush sau mỗi lần ghi (`unitbuf`) |
| `std::clog` | đầu ra log | có buffer |

`std::cerr` thường được dùng cho thông báo lỗi để chúng xuất hiện ngay cả khi chương trình gặp sự cố. `std::clog` phù hợp hơn cho log thông thường vì có buffer.

### 2.3. Buffer và flush

Dữ liệu ghi vào `std::cout` thường không đến màn hình ngay lập tức. Nó được giữ trong **buffer** và được đẩy ra khi:

- buffer đầy;
- chương trình gọi `std::flush` hoặc `std::endl`;
- chương trình kết thúc bình thường;
- có thao tác nhập từ `std::cin` (do `cin` được "tie" với `cout` theo mặc định).

```cpp
#include <iostream>

int main() {
    std::cout << "Dòng 1\n";          // không flush ngay
    std::cout << "Dòng 2" << std::endl; // '\n' + flush
    std::cout << "Dòng 3" << std::flush; // chỉ flush
}
```

**Lưu ý:**

- `std::endl` = `'\n'` + flush. Trong vòng lặp lớn, dùng `'\n'` để tránh flush không cần thiết.
- `std::flush` không thêm ký tự xuống dòng.
- Khi cần hỏi người dùng, nên flush trước khi chờ nhập:

```cpp
std::cout << "Nhập tuổi: " << std::flush;
int age;
std::cin >> age;
```

Có thể tắt tie để tăng tốc độ khi không cần đồng bộ:

```cpp
std::ios::sync_with_stdio(false);
std::cin.tie(nullptr);
```

Khi đã tắt tie, nếu chương trình vừa in prompt vừa chờ nhập, phải tự flush.

### 2.4. Văn bản và nhị phân

Mọi tệp trên đĩa đều là các byte. Sự khác biệt nằm ở cách chương trình diễn giải các byte:

| Chế độ | Cách xử lý | Ưu điểm | Nhược điểm |
|---|---|---|---|
| Văn bản (text) | byte được hiểu là ký tự; có thể chuyển đổi newline theo hệ điều hành | con người đọc được, dễ trao đổi | chậm hơn, có chuyển đổi ký tự |
| Nhị phân (binary) | byte được đọc/ghi nguyên vẹn | nhanh, tiết kiệm, chính xác | khó đọc bằng mắt, phụ thuộc nền tảng |

Trên Windows, ở chế độ văn bản, ký tự `'\n'` có thể được ghi thành cặp `'\r' '\n'` và ngược lại khi đọc. Chế độ nhị phân (`std::ios::binary`) tắt chuyển đổi này.

> Khi không chắc một tệp là văn bản hay nhị phân, nên xử lý nó ở chế độ nhị phân để không làm hỏng dữ liệu.

### 2.5. Chuyển hướng luồng chuẩn

Ở mức hệ điều hành, `std::cin` và `std::cout` có thể được chuyển hướng từ/đến tệp mà chương trình không cần biết:

```text
app < input.txt > output.txt
```

Đây là tính năng của shell/hệ điều hành, không phải API C++. Chương trình vẫn đọc `std::cin`, ghi `std::cout` như bình thường.

---

## 3. Trạng thái luồng và xử lý lỗi

### 3.1. Các cờ trạng thái

Mỗi luồng có một tập cờ trạng thái:

| Cờ | Ý nghĩa |
|---|---|
| `std::ios::goodbit` | không có lỗi |
| `std::ios::eofbit` | đã chạm cuối tệp |
| `std::ios::failbit` | thao tác thất bại về mặt logic/định dạng |
| `std::ios::badbit` | lỗi nghiêm trọng của luồng (I/O) |

Các phương thức kiểm tra:

```cpp
stream.good();   // không có cờ lỗi nào
stream.eof();    // eofbit được bật
stream.fail();   // failbit hoặc badbit được bật
stream.bad();    // chỉ badbit được bật
stream.rdstate();// trả về tổ hợp cờ hiện tại
stream.clear();  // xóa tất cả cờ lỗi
stream.clear(state); // đặt trạng thái cụ thể
```

`operator bool` của luồng trả về `true` khi `!fail()`:

```cpp
if (std::cin >> x) {
    // đọc thành công
} else {
    // đọc thất bại
}
```

### 3.2. Vì sao không nên dùng `while (!stream.eof())`

Đây là lỗi rất phổ biến:

```cpp
// SAI
while (!in.eof()) {
    std::getline(in, line);
    std::cout << line << '\n';
}
```

Khi dòng cuối được đọc, `eofbit` **chưa** được bật ngay. Vòng lặp chạy thêm một lần, `getline` thất bại, `line` có thể rỗng hoặc giữ giá trị cũ, và chương trình in thêm một dòng rỗng.

Cách đúng:

```cpp
std::string line;
while (std::getline(in, line)) {
    std::cout << line << '\n';
}
```

Hoặc với toán tử nhập:

```cpp
int x;
while (in >> x) {
    // xử lý x
}
```

`getline` và `operator>>` trả về chính luồng, nên có thể dùng trực tiếp trong điều kiện.

### 3.3. Phục hồi sau lỗi nhập

Khi `std::cin >> x` gặp dữ liệu không phải số, `failbit` được bật và dữ liệu sai vẫn nằm trong buffer. Cần:

1. `clear()` để xóa cờ lỗi.
2. Bỏ qua phần dữ liệu sai còn lại, thường đến hết dòng.
3. Thử lại.

```cpp
#include <iostream>
#include <limits>
#include <string>

int main() {
    int x{};
    while (!(std::cin >> x)) {
        std::cin.clear(); // xóa failbit
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Vui lòng nhập một số nguyên: ";
    }
    std::cout << "Bạn nhập: " << x << '\n';
}
```

`std::numeric_limits<std::streamsize>::max()` nằm trong `<limits>`.

### 3.4. Ngoại lệ của luồng

Mặc định, luồng không ném ngoại lệ. Có thể bật:

```cpp
#include <ios>

in.exceptions(std::ios::failbit | std::ios::badbit);
```

Sau đó, lỗi tương ứng sẽ ném `std::ios_base::failure`. Tuy nhiên:

- `eofbit` không nằm trong tập trên, nên cuối tệp bình thường không ném.
- Nếu bật `failbit`, `read` gặp EOF cũng có thể ném; cần xử lý cẩn thận.
- Với người mới, kiểm tra trạng thái bằng `if (!stream)` thường dễ kiểm soát hơn.

---

## 4. Nhập/xuất màn hình và định dạng

### 4.1. Toán tử `>>` và `<<`

```cpp
#include <iostream>
#include <string>

int main() {
    int age{};
    std::string name;

    std::cout << "Tên: ";
    std::cin >> name;       // đọc một từ, dừng ở khoảng trắng
    std::cout << "Tuổi: ";
    std::cin >> age;

    std::cout << name << " (" << age << " tuổi)\n";
}
```

`operator>>`:

- bỏ qua khoảng trắng ở đầu;
- đọc đến khoảng trắng tiếp theo (với `std::string`);
- với số, dừng khi gặp ký tự không hợp lệ.

Vì vậy `std::cin >> name` **không** đọc được tên có khoảng trắng.

### 4.2. Đọc cả dòng bằng `std::getline`

```cpp
#include <iostream>
#include <string>

int main() {
    std::string line;
    std::cout << "Nhập một dòng: ";
    std::getline(std::cin, line);
    std::cout << "Bạn viết: " << line << '\n';
}
```

`std::getline(stream, str)`:

- đọc đến ký tự `'\n'`;
- **lấy** và loại bỏ dấu `'\n'` khỏi luồng;
- không lưu `'\n'` vào `str`;
- trả về `stream`.

### 4.3. Trộn `>>` và `getline`

Sau khi dùng `>>`, ký tự xuống dòng vẫn còn trong buffer. Nếu gọi `getline` ngay, nó sẽ đọc được dòng rỗng.

```cpp
int n;
std::cin >> n;

std::string line;
std::getline(std::cin, line); // có thể nhận dòng rỗng!
```

Cách sửa:

```cpp
std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
std::getline(std::cin, line);
```

Hoặc bỏ qua khoảng trắng trước khi đọc:

```cpp
std::getline(std::cin >> std::ws, line);
```

`std::ws` tiêu thụ mọi khoảng trắng liên tiếp, bao gồm cả newline.

### 4.4. Đọc từng ký tự

```cpp
char c;
while (std::cin.get(c)) {
    // xử lý c
}
```

Các thao tác liên quan:

| Thao tác | Ý nghĩa |
|---|---|
| `get(c)` | đọc một ký tự, không bỏ qua khoảng trắng |
| `get()` | trả về ký tự tiếp theo dưới dạng `int` |
| `peek()` | xem ký tự tiếp theo nhưng không lấy ra |
| `put(c)` | ghi một ký tự |
| `putback(c)` | đẩy một ký tự trở lại luồng |
| `unget()` | lùi lại một ký tự |
| `ignore(n, delim)` | bỏ qua tối đa `n` ký tự hoặc đến `delim` |

### 4.5. Định dạng bằng `<iomanip>`

```cpp
#include <iomanip>
#include <iostream>

int main() {
    std::cout << std::setw(8) << std::left << "Tên"
              << std::setw(6) << std::right << "Tuổi" << '\n';

    std::cout << std::setfill('.')
              << std::setw(8) << "An"
              << std::setfill(' ')
              << std::setw(6) << 20 << '\n';
}
```

Kết quả gần đúng:

```text
Tên     Tuổi
An......    20
```

Các manipulator quan trọng:

| Manipulator | Tác dụng | Ghi nhớ |
|---|---|---|
| `std::setw(n)` | đặt độ rộng tối thiểu cho **mục tiếp theo** | chỉ có tác dụng một lần |
| `std::setfill(c)` | ký tự đệm | có hiệu lực đến khi đổi |
| `std::left` | căn trái | có hiệu lực đến khi đổi |
| `std::right` | căn phải | mặc định |
| `std::internal` | đệm giữa dấu và chữ số | hữu ích cho số có dấu |
| `std::fixed` | số thực dạng cố định | có hiệu lực đến khi đổi |
| `std::scientific` | số thực dạng khoa học | có hiệu lực đến khi đổi |
| `std::setprecision(n)` | số chữ số sau dấu chấm (với `fixed`) | có hiệu lực đến khi đổi |
| `std::showpoint` | luôn hiện dấu chấm thập phân | |
| `std::boolalpha` | in `true`/`false` thay vì `1`/`0` | |
| `std::hex`, `std::dec`, `std::oct` | cơ số cho số nguyên | có hiệu lực đến khi đổi |
| `std::showbase` | hiện tiền tố `0x`, `0` | |
| `std::uppercase` | chữ hex in hoa | |
| `std::quoted(s)` | in/đọc chuỗi có dấu nháy | cần `<iomanip>` |

Ví dụ số thực:

```cpp
double pi = 3.141592653589793;
std::cout << std::fixed << std::setprecision(2) << pi << '\n'; // 3.14
std::cout << std::scientific << pi << '\n';                   // 3.14e+00
```

Ví dụ `std::quoted`:

```cpp
std::string name = "Nguyễn Văn A";
std::cout << std::quoted(name) << '\n'; // "Nguyễn Văn A"

std::string input;
std::cin >> std::quoted(input); // đọc được chuỗi trong dấu nháy, kể cả khoảng trắng
```

### 4.6. `std::format` (C++20, tùy chọn)

Nếu trình biên dịch hỗ trợ C++20, có thể dùng `<format>`:

```cpp
#include <format>
#include <iostream>

int main() {
    std::cout << std::format("x = {:.2f}, y = {:04d}\n", 3.14159, 42);
}
```

Cách này hiện đại và an toàn về kiểu, nhưng không phải trình biên dịch nào cũng hỗ trợ đầy đủ. Trong bài này, `<iomanip>` là lựa chọn tương thích rộng rãi.

---

## 5. Nhập/xuất tệp văn bản

### 5.1. Ba lớp tệp

| Lớp | Mục đích | Chế độ mặc định |
|---|---|---|
| `std::ifstream` | chỉ đọc | `std::ios::in` |
| `std::ofstream` | chỉ ghi | `std::ios::out` (tạo mới/truncate) |
| `std::fstream` | đọc và ghi | `std::ios::in \| std::ios::out` |

### 5.2. Mở tệp

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    std::ifstream in("diem.txt");
    if (!in.is_open()) {
        std::cerr << "Không mở được diem.txt\n";
        return 1;
    }

    std::string line;
    while (std::getline(in, line)) {
        std::cout << line << '\n';
    }
}
```

`std::ifstream` tự đóng tệp khi đối tượng bị hủy (RAII). Không cần gọi `close()` nếu không cần kiểm tra lỗi hoặc mở lại.

Mở bằng phương thức `open()`:

```cpp
std::ifstream in;
in.open("diem.txt");
if (!in) { /* lỗi */ }
```

Khi mở lại cùng một đối tượng, nên gọi `clear()` trước nếu trạng thái cũ đang lỗi:

```cpp
in.clear();
in.open("diem-khac.txt");
```

### 5.3. Các chế độ mở tệp

Các cờ nằm trong `std::ios`:

| Cờ | Ý nghĩa |
|---|---|
| `std::ios::in` | mở để đọc |
| `std::ios::out` | mở để ghi |
| `std::ios::app` | ghi nối vào cuối tệp |
| `std::ios::trunc` | xóa nội dung cũ khi mở |
| `std::ios::ate` | đặt vị trí ở cuối tệp sau khi mở |
| `std::ios::binary` | chế độ nhị phân, không chuyển đổi newline |

Kết hợp bằng `|`:

```cpp
std::ofstream log("app.log", std::ios::app);                 // ghi nối
std::ofstream out("data.bin", std::ios::binary | std::ios::trunc);
std::fstream io("data.bin", std::ios::in | std::ios::out | std::ios::binary);
```

**Phân biệt `app` và `ate`:**

- `app`: mỗi lần ghi đều ghi vào cuối tệp, dù đã seek đi đâu.
- `ate`: đặt vị trí ban đầu ở cuối tệp, nhưng vẫn có thể seek và ghi ở chỗ khác.

**Phân biệt `out` và `trunc`:**

- `ofstream` mặc định có `out`; nếu tệp đã tồn tại, nó thường bị truncate.
- `fstream` với `in | out` **không** tự tạo tệp mới và **không** truncate; tệp phải tồn tại.
- Muốn `fstream` tạo mới/truncate: dùng `in | out | trunc`.

### 5.4. Đọc tệp văn bản

**Đọc từng dòng:**

```cpp
std::string line;
while (std::getline(in, line)) {
    std::cout << line << '\n';
}
```

**Đọc từng từ:**

```cpp
std::string word;
while (in >> word) {
    std::cout << word << '\n';
}
```

**Đọc từng ký tự:**

```cpp
char c;
while (in.get(c)) {
    std::cout << c;
}
```

**Đọc toàn bộ tệp vào `std::string`:**

```cpp
#include <sstream>
#include <string>

std::ostringstream buffer;
buffer << in.rdbuf();
std::string content = buffer.str();
```

Cách khác dùng iterator:

```cpp
#include <iterator>
#include <string>

std::string content(
    (std::istreambuf_iterator<char>(in)),
    std::istreambuf_iterator<char>()
);
```

Chỉ nên đọc toàn bộ khi tệp không quá lớn.

### 5.5. Ghi tệp văn bản

```cpp
#include <fstream>

int main() {
    std::ofstream out("ketqua.txt"); // tạo mới/truncate
    if (!out) {
        return 1;
    }

    out << "Tổng: " << 42 << '\n';
    out << "Trung bình: " << 7.5 << '\n';

    out.close();
    if (!out) {
        return 1; // lỗi khi đóng/ghi
    }
}
```

Ghi nối:

```cpp
std::ofstream out("ketqua.txt", std::ios::app);
out << "Dòng mới\n";
```

### 5.6. Đường dẫn tệp

Có thể dùng `std::string` hoặc `std::filesystem::path`:

```cpp
#include <filesystem>
#include <fstream>

std::filesystem::path p = "data/input.txt";
std::ifstream in(p);
```

- Trên Windows, dấu `/` thường được chấp nhận.
- Nếu dùng dấu `\`, viết `\\` hoặc dùng raw string:

```cpp
std::ifstream in(R"(C:\data\input.txt)");
```

- `std::filesystem::path` giúp nối đường dẫn an toàn:

```cpp
std::filesystem::path dir = "data";
std::filesystem::path file = dir / "input.txt";
```

### 5.7. Thao tác hệ thống tệp với `<filesystem>`

C++17 cung cấp `std::filesystem`:

```cpp
#include <filesystem>
namespace fs = std::filesystem;

fs::path p = "data/input.txt";

if (fs::exists(p)) {
    std::cout << "Kích thước: " << fs::file_size(p) << " byte\n";
}

fs::create_directories("data/backup");
fs::copy_file("data/input.txt", "data/backup/input.txt",
              fs::copy_options::overwrite_existing);
fs::rename("data/old.txt", "data/new.txt");
fs::remove("data/temp.txt");
```

Một số hàm hữu ích:

| Hàm | Công dụng |
|---|---|
| `fs::exists(p)` | kiểm tra tồn tại |
| `fs::is_regular_file(p)` | kiểm tra tệp thường |
| `fs::is_directory(p)` | kiểm tra thư mục |
| `fs::file_size(p)` | kích thước tệp |
| `fs::create_directories(p)` | tạo thư mục (kể cả cha) |
| `fs::remove(p)` | xóa tệp/thư mục rỗng |
| `fs::remove_all(p)` | xóa đệ quy |
| `fs::rename(old, new)` | đổi tên/di chuyển |
| `fs::copy_file(src, dst)` | sao chép tệp |
| `fs::temp_directory_path()` | thư mục tạm của hệ thống |

Khi cần kiểm soát lỗi mà không dùng ngoại lệ, dùng overload có `std::error_code`:

```cpp
std::error_code ec;
if (!fs::exists(p, ec)) {
    // kiểm tra ec
}
```

### 5.8. Tệp tạm

Không có lớp "tệp tạm" riêng trong C++ chuẩn. Có thể tạo tên tạm trong thư mục tạm:

```cpp
#include <filesystem>
#include <fstream>

fs::path temp = fs::temp_directory_path() / "myapp-12345.tmp";
std::ofstream out(temp, std::ios::binary);
// ... ghi ...
out.close();
fs::remove(temp);
```

Trong ứng dụng thật, nên dùng tên ngẫu nhiên/duy nhất để tránh va chạm.

### 5.9. Mã hóa văn bản

- `std::string` lưu **byte**, không tự biết Unicode.
- `std::ifstream` không tự chuyển đổi UTF-8 sang UTF-16 hay ngược lại.
- Nếu tệp là UTF-8, chương trình đọc được các byte; việc hiển thị đúng phụ thuộc terminal/hệ điều hành.
- Đừng giả định `line.size()` là số ký tự nhìn thấy; với UTF-8, một ký tự có thể chiếm nhiều byte.
- Với xử lý Unicode nghiêm túc, dùng thư viện chuyên dụng (ICU, utf8cpp...).

---

## 6. Nhập/xuất tệp nhị phân

### 6.1. Khi nào dùng nhị phân?

Dùng nhị phân khi:

- cần lưu/đọc **nguyên byte** của dữ liệu;
- cần tốc độ và dung lượng;
- dữ liệu là ảnh, âm thanh, tệp nén, mảng số, struct;
- cần truy cập ngẫu nhiên theo bản ghi.

Không nên dùng nhị phân khi:

- cần con người đọc/sửa bằng editor;
- cần trao đổi giữa nhiều nền tảng/kiến trúc khác nhau mà không có định dạng chuẩn;
- dữ liệu chứa con trỏ, `std::string`, lớp có hàm ảo...

### 6.2. Mở tệp nhị phân

```cpp
#include <fstream>

std::ifstream in("data.bin", std::ios::binary);
std::ofstream out("data.bin", std::ios::binary | std::ios::trunc);
std::fstream io("data.bin",
                std::ios::in | std::ios::out | std::ios::binary);
```

Nên chỉ định rõ `std::ios::binary`; nếu không, trên Windows có thể xảy ra chuyển đổi newline và làm hỏng dữ liệu.

### 6.3. `read` và `write`

```cpp
stream.read(char* memory, std::streamsize byteCount);
stream.write(const char* memory, std::streamsize byteCount);
```

- `read` đọc tối đa `byteCount` byte vào vùng nhớ.
- `write` ghi đúng `byteCount` byte từ vùng nhớ.
- Đơn vị là **byte**, không phải số phần tử.
- `read`/`write` là thao tác **không định dạng** (unformatted).
- Nếu `read` không đọc đủ `byteCount`, luồng bật `eofbit` và `failbit`; dùng `gcount()` để biết số byte thực tế.
- Nếu `write` thất bại, luồng thường bật `badbit`.

Ví dụ đọc một số nguyên:

```cpp
#include <cstdint>
#include <fstream>

int main() {
    std::ifstream in("data.bin", std::ios::binary);
    if (!in) {
        return 1;
    }

    std::int32_t x{};
    in.read(reinterpret_cast<char*>(&x), sizeof(x));
    if (!in) {
        return 1;
    }

    // x đã có dữ liệu
}
```

Ghi một số nguyên:

```cpp
std::int32_t x = 1234;
out.write(reinterpret_cast<const char*>(&x), sizeof(x));
```

### 6.4. `gcount()`

Sau một thao tác đọc không định dạng, `gcount()` cho biết **số byte thực tế đã đọc**:

```cpp
char buffer[1024];
in.read(buffer, sizeof(buffer));
std::streamsize n = in.gcount();
```

- Nếu `n == sizeof(buffer)`: đọc đủ.
- Nếu `0 < n < sizeof(buffer)`: chạm cuối tệp hoặc tệp ngắn hơn yêu cầu.
- Nếu `n == 0`: không đọc được byte nào.

`gcount()` chỉ có ý nghĩa ngay sau thao tác đọc không định dạng. Đừng dùng nó sau `>>` hoặc `getline`.

### 6.5. Đọc mảng

```cpp
#include <array>
#include <cstdint>
#include <fstream>

int main() {
    std::ifstream in("numbers.bin", std::ios::binary);
    std::array<std::int32_t, 4> a{};

    in.read(reinterpret_cast<char*>(a.data()),
            static_cast<std::streamsize>(a.size() * sizeof(a[0])));

    if (in.gcount() != static_cast<std::streamsize>(a.size() * sizeof(a[0]))) {
        return 1;
    }
}
```

Ghi mảng:

```cpp
out.write(reinterpret_cast<const char*>(a.data()),
          static_cast<std::streamsize>(a.size() * sizeof(a[0])));
```

### 6.6. Đọc/ghi struct

```cpp
#include <cstdint>
#include <fstream>
#include <type_traits>

struct Fraction {
    std::int32_t num{};
    std::int32_t denom{1};
};

static_assert(std::is_trivially_copyable_v<Fraction>);

void write_fraction(std::ostream& out, const Fraction& f) {
    out.write(reinterpret_cast<const char*>(&f), sizeof(f));
}

void read_fraction(std::istream& in, Fraction& f) {
    in.read(reinterpret_cast<char*>(&f), sizeof(f));
}
```

Điều kiện để ghi/đọc nguyên khối:

- Kiểu phải **trivially copyable**.
- Không chứa con trỏ, tham chiếu, `std::string`, `std::vector`, hàm ảo...
- Chấp nhận rằng bố cục byte phụ thuộc nền tảng.

### 6.7. Padding, endianness và tính khả chuyển

Ghi nguyên `struct` có thể **không portable** vì:

1. **Padding/alignment**: compiler có thể chèn byte trống giữa các thành viên.
2. **Kích thước kiểu**: `int` có thể là 4 byte trên máy này, khác trên máy khác.
3. **Endianness**: little-endian và big-endian lưu thứ tự byte khác nhau.
4. **ABI/compiler**: cách sắp xếp struct có thể khác.
5. **Con trỏ**: địa chỉ trong bộ nhớ không có ý nghĩa khi đọc lại ở tiến trình khác.

Dùng kiểu có kích thước cố định từ `<cstdint>`:

```cpp
#include <cstdint>

struct Fraction {
    std::int32_t num{};
    std::int32_t denom{1};
};
```

Vẫn cần chú ý padding và endianness. Với tệp cần trao đổi rộng rãi, nên **tuần tự hóa từng trường**:

```cpp
#include <array>
#include <cstdint>
#include <istream>
#include <ostream>
#include <stdexcept>

void write_u32_le(std::ostream& out, std::uint32_t v) {
    std::array<unsigned char, 4> b{
        static_cast<unsigned char>(v & 0xFFu),
        static_cast<unsigned char>((v >> 8) & 0xFFu),
        static_cast<unsigned char>((v >> 16) & 0xFFu),
        static_cast<unsigned char>((v >> 24) & 0xFFu)
    };
    out.write(reinterpret_cast<const char*>(b.data()),
              static_cast<std::streamsize>(b.size()));
    if (!out) {
        throw std::runtime_error("Ghi tệp thất bại");
    }
}

std::uint32_t read_u32_le(std::istream& in) {
    std::array<unsigned char, 4> b{};
    in.read(reinterpret_cast<char*>(b.data()),
            static_cast<std::streamsize>(b.size()));
    if (!in) {
        throw std::runtime_error("Đọc tệp thất bại");
    }
    return static_cast<std::uint32_t>(b[0])
         | (static_cast<std::uint32_t>(b[1]) << 8)
         | (static_cast<std::uint32_t>(b[2]) << 16)
         | (static_cast<std::uint32_t>(b[3]) << 24);
}
```

Với số có dấu, chuyển qua kiểu không dấu cùng kích thước khi tuần tự hóa; với số thực, dùng `std::bit_cast` (C++20) hoặc `std::memcpy` sang `std::uint32_t`/`std::uint64_t`.

Có thể kiểm tra endianness ở C++20:

```cpp
#include <bit>

if constexpr (std::endian::native == std::endian::little) {
    // ...
}
```

### 6.8. Đọc bản ghi có kiểm tra

```cpp
struct Record {
    std::int32_t id{};
    double value{};
};

std::ifstream in("records.bin", std::ios::binary);
Record r{};

while (true) {
    in.read(reinterpret_cast<char*>(&r), sizeof(r));
    const auto got = in.gcount();

    if (got == sizeof(r)) {
        // xử lý r
    } else if (got == 0 && in.eof()) {
        break; // hết tệp đúng lúc
    } else {
        // tệp bị cắt giữa bản ghi hoặc có lỗi I/O
        break;
    }
}
```

Lưu ý: nếu `read` đọc được một phần bản ghi, `gcount()` phản ánh số byte thực tế; không nên coi đó là bản ghi hợp lệ.

### 6.9. Ghi đè và ghi nối

```cpp
// Ghi mới/ghi đè
std::ofstream out("data.bin", std::ios::binary | std::ios::trunc);

// Ghi nối
std::ofstream out("data.bin", std::ios::binary | std::ios::app);
```

Với `std::fstream`, muốn ghi đè từ đầu:

```cpp
std::fstream io("data.bin",
                std::ios::in | std::ios::out | std::ios::binary | std::ios::trunc);
```

### 6.10. Bảng quyết định văn bản hay nhị phân

| Tiêu chí | Văn bản | Nhị phân |
|---|---|---|
| Con người đọc được | Có | Không |
| Tốc độ | Chậm hơn | Nhanh hơn |
| Dung lượng | Thường lớn hơn | Thường nhỏ hơn |
| Trao đổi đa nền tảng | Dễ hơn | Khó hơn |
| Truy cập ngẫu nhiên | Hạn chế | Thuận lợi |
| Dữ liệu ảnh/âm thanh | Không phù hợp | Phù hợp |

---

## 7. Truy cập ngẫu nhiên trong tệp

### 7.1. Vị trí đọc/ghi

Mỗi luồng tệp có một **vị trí hiện tại**:

- `tellg()`: vị trí đọc hiện tại.
- `tellp()`: vị trí ghi hiện tại.
- `seekg()`: di chuyển vị trí đọc.
- `seekp()`: di chuyển vị trí ghi.

Kiểu:

```cpp
std::streampos pos = in.tellg();
std::streamoff offset = 100;
```

`tellg()`/`tellp()` trả về `std::streampos`; nếu thất bại, giá trị là `std::streampos(-1)`.

### 7.2. Các gốc tọa độ

| Hằng | Ý nghĩa |
|---|---|
| `std::ios::beg` | từ đầu tệp |
| `std::ios::cur` | từ vị trí hiện tại |
| `std::ios::end` | từ cuối tệp |

Ví dụ:

```cpp
in.seekg(0, std::ios::beg);    // về đầu
in.seekg(4, std::ios::beg);    // byte thứ 4
in.seekg(-8, std::ios::end);   // lùi 8 byte từ cuối
in.seekg(-2, std::ios::cur);   // lùi 2 byte từ hiện tại
```

Offset có thể âm, nhưng kết quả phải nằm trong phạm vi hợp lệ.

### 7.3. Đọc bản ghi thứ `i`

```cpp
constexpr std::streamoff record_size = sizeof(Record);

in.seekg(static_cast<std::streamoff>(i) * record_size, std::ios::beg);
if (!in) {
    return false;
}

Record r{};
in.read(reinterpret_cast<char*>(&r), sizeof(r));
if (in.gcount() != sizeof(r)) {
    return false;
}
```

### 7.4. Lấy kích thước tệp

```cpp
in.seekg(0, std::ios::end);
std::streamoff size = in.tellg();
in.seekg(0, std::ios::beg);
```

Hoặc dùng filesystem:

```cpp
#include <filesystem>

auto size = std::filesystem::file_size("data.bin");
```

### 7.5. `seekg` và trạng thái EOF

`seekg` sẽ xóa `eofbit` trước khi di chuyển. Nếu di chuyển thất bại, `failbit` được bật.

```cpp
in.clear(); // nếu cần xóa failbit trước khi thử lại
in.seekg(0, std::ios::beg);
if (!in) {
    // seek thất bại
}
```

### 7.6. Seek trên tệp văn bản

Với tệp văn bản, không nên tự tính offset byte. Chỉ nên:

- `seekg(0, std::ios::beg)` để về đầu;
- seek đến vị trí đã lấy từ `tellg()` trước đó.

Lý do: text mode có thể chuyển đổi newline, nên số byte vật lý khác số ký tự logic. Muốn tính offset chính xác, dùng `std::ios::binary`.

### 7.7. Cập nhật một bản ghi bằng `fstream`

```cpp
#include <fstream>

std::fstream io("records.bin",
                std::ios::in | std::ios::out | std::ios::binary);
if (!io) {
    return 1;
}

const std::streamoff pos = static_cast<std::streamoff>(index) * sizeof(Record);

Record r{};
io.seekg(pos, std::ios::beg);
io.read(reinterpret_cast<char*>(&r), sizeof(r));
if (!io) {
    return 1;
}

r.value += 1.0;

io.clear(); // xóa eof/fail trước khi chuyển sang ghi
io.seekp(pos, std::ios::beg);
io.write(reinterpret_cast<const char*>(&r), sizeof(r));
if (!io) {
    return 1;
}
```

Với `std::fstream`, sau khi đọc nên seek/flush trước khi ghi và ngược lại. Không nên trộn đọc/ghi liên tiếp mà không di chuyển vị trí.

### 7.8. Ghi đè giữa tệp

```cpp
io.seekp(static_cast<std::streamoff>(index) * sizeof(Record), std::ios::beg);
io.write(reinterpret_cast<const char*>(&r), sizeof(r));
```

Nếu ghi vượt quá cuối tệp, tệp có thể được mở rộng; phần giữa có thể là byte không xác định. Luôn kiểm tra vị trí và kích thước.

---

## 8. String stream

### 8.1. Khái niệm

String stream cho phép dùng cú pháp `<<`/`>>` trên một `std::string` thay vì màn hình/tệp.

| Lớp | Mục đích |
|---|---|
| `std::istringstream` | đọc từ chuỗi |
| `std::ostringstream` | ghi vào chuỗi |
| `std::stringstream` | đọc và ghi |

Cần `<sstream>`.

### 8.2. Định dạng ra chuỗi

```cpp
#include <iomanip>
#include <sstream>
#include <string>

std::ostringstream os;
os << std::fixed << std::setprecision(2) << 3.14159;
std::string s = os.str(); // "3.14"
```

Ứng dụng: tạo thông báo, tạo tên tệp, tạo CSV, log...

```cpp
std::ostringstream name;
name << "part_" << row << "_" << col << ".bmp";
std::string filename = name.str();
```

### 8.3. Phân tích từ chuỗi

```cpp
#include <sstream>
#include <string>

std::string line = "An 20 7.5";

std::istringstream is(line);
std::string name;
int age{};
double score{};

if (is >> name >> age >> score) {
    // thành công
} else {
    // dữ liệu sai định dạng
}
```

Kiểm tra còn dữ liệu thừa:

```cpp
is >> std::ws;
if (!is.eof()) {
    // còn ký tự chưa xử lý
}
```

### 8.4. Tách CSV đơn giản

```cpp
#include <sstream>
#include <string>

std::string line = "An,20,7.5";
std::istringstream row(line);
std::string cell;

while (std::getline(row, cell, ',')) {
    // xử lý cell
}
```

Cách này **không** xử lý dấu phẩy nằm trong dấu nháy. Với CSV đầy đủ, cần bộ phân tích riêng hoặc thư viện.

### 8.5. Tái sử dụng string stream

```cpp
std::stringstream ss;
ss << "12 34";

int a{}, b{};
ss >> a >> b;

ss.clear();      // xóa trạng thái eof/fail
ss.str("56 78"); // thay nội dung

int c{}, d{};
ss >> c >> d;
```

- `str("")` xóa nội dung.
- `clear()` xóa cờ trạng thái.
- Cần cả hai nếu muốn dùng lại hoàn toàn.

### 8.6. Chuyển đổi số an toàn

`std::stoi`, `std::stoll`, `std::stod` tiện nhưng ném ngoại lệ:

```cpp
#include <stdexcept>
#include <string>

try {
    int x = std::stoi("123");
} catch (const std::invalid_argument&) {
    // không phải số
} catch (const std::out_of_range&) {
    // tràn
}
```

`std::from_chars` (C++17) không phụ thuộc locale và không ném ngoại lệ:

```cpp
#include <charconv>
#include <string_view>

std::string_view s = "123";
int x{};
auto [ptr, ec] = std::from_chars(s.data(), s.data() + s.size(), x);

if (ec != std::errc{} || ptr != s.data() + s.size()) {
    // lỗi hoặc còn ký tự thừa
}
```

---

## 9. Tham số dòng lệnh

### 9.1. `argc` và `argv`

```cpp
int main(int argc, char* argv[]) {
    // ...
}
```

- `argc`: số lượng tham số, **bao gồm tên chương trình**.
- `argv[0]`: tên chương trình.
- `argv[1]`...: các tham số.
- `argv[argc]` là con trỏ null.

Ví dụ chạy:

```text
app input.txt output.txt
```

Thì:

```text
argc    = 3
argv[0] = "app"
argv[1] = "input.txt"
argv[2] = "output.txt"
argv[3] = nullptr
```

### 9.2. In danh sách tham số

```cpp
#include <iostream>

int main(int argc, char* argv[]) {
    std::cout << "argc = " << argc << '\n';
    for (int i = 0; i < argc; ++i) {
        std::cout << i << ": " << argv[i] << '\n';
    }
}
```

### 9.3. Phân tích tùy chọn

```cpp
#include <charconv>
#include <iostream>
#include <string_view>

int parse_positive(std::string_view s) {
    int value{};
    auto [ptr, ec] = std::from_chars(s.data(), s.data() + s.size(), value);
    if (ec != std::errc{} || ptr != s.data() + s.size() || value <= 0) {
        return -1;
    }
    return value;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Thiếu tên tệp\n";
        return 2;
    }

    int h = 1;
    int w = 1;

    for (int i = 2; i < argc; ++i) {
        std::string_view arg = argv[i];

        if (arg == "-h" && i + 1 < argc) {
            h = parse_positive(argv[++i]);
        } else if (arg == "-w" && i + 1 < argc) {
            w = parse_positive(argv[++i]);
        } else if (arg == "-?") {
            std::cout << "Dùng: " << argv[0] << " <file> [-h parts] [-w parts]\n";
            return 0;
        } else {
            std::cerr << "Tham số không hợp lệ: " << arg << '\n';
            return 2;
        }

        if (h < 0 || w < 0) {
            std::cerr << "Giá trị phải là số nguyên dương\n";
            return 2;
        }
    }
}
```

### 9.4. Đường dẫn từ `argv`

`argv` là mảng `char*`, nên có thể chuyển thành `std::filesystem::path`:

```cpp
#include <filesystem>

std::filesystem::path input = argv[1];
```

Trên Windows, `main` có thể nhận chuỗi theo code page hiện tại. Với đường dẫn Unicode, cần cơ chế riêng của nền tảng hoặc dùng `std::filesystem::path` cẩn thận; không nên giả định mọi ký tự đều biểu diễn được bằng một byte.

### 9.5. Mã trả về

```cpp
return 0; // thành công
return 1; // lỗi thực thi
return 2; // lỗi cú pháp tham số
```

Mã trả về giúp script/terminal biết chương trình thành công hay thất bại.

---

## 10. Sao chép tệp

### 10.1. Sao chép nhị phân an toàn

```cpp
#include <array>
#include <filesystem>
#include <fstream>
#include <iostream>

bool copy_file(const std::filesystem::path& src,
               const std::filesystem::path& dst) {
    std::ifstream in(src, std::ios::binary);
    if (!in) {
        return false;
    }

    std::ofstream out(dst, std::ios::binary | std::ios::trunc);
    if (!out) {
        return false;
    }

    std::array<char, 64 * 1024> buffer{};

    while (in) {
        in.read(buffer.data(),
                static_cast<std::streamsize>(buffer.size()));

        const std::streamsize n = in.gcount();
        if (n > 0) {
            out.write(buffer.data(), n);
            if (!out) {
                return false;
            }
        }
    }

    if (!in.eof()) {
        return false; // lỗi đọc, không phải EOF bình thường
    }

    out.close();
    return static_cast<bool>(out);
}
```

Giải thích:

- Mở cả hai tệp ở chế độ nhị phân.
- Đọc theo block 64 KB.
- Dùng `gcount()` để biết số byte thực tế, kể cả block cuối không đầy.
- Kiểm tra `in.eof()` sau vòng lặp để phân biệt EOF với lỗi I/O.
- Đóng và kiểm tra trạng thái tệp đích.

### 10.2. Kiểm tra tệp nguồn và đích trùng nhau

```cpp
#include <filesystem>
#include <system_error>

std::error_code ec;
if (std::filesystem::exists(dst, ec) &&
    std::filesystem::equivalent(src, dst, ec)) {
    // không sao chép đè lên chính nó
}
```

Nếu không kiểm tra, mở tệp đích ở chế độ `trunc` có thể xóa nội dung nguồn trước khi đọc.

### 10.3. Dùng `std::filesystem::copy_file`

Nếu không cần tự xử lý buffer:

```cpp
std::filesystem::copy_file(
    src, dst,
    std::filesystem::copy_options::overwrite_existing
);
```

Cách này tiện, nhưng bài thực hành thường yêu cầu tự cài đặt để hiểu luồng nhị phân.

### 10.4. Sao chép nối nhiều tệp

```cpp
bool append_file(std::ofstream& out, const std::filesystem::path& src) {
    std::ifstream in(src, std::ios::binary);
    if (!in) {
        return false;
    }

    std::array<char, 64 * 1024> buffer{};
    while (in) {
        in.read(buffer.data(),
                static_cast<std::streamsize>(buffer.size()));
        const std::streamsize n = in.gcount();
        if (n > 0) {
            out.write(buffer.data(), n);
            if (!out) {
                return false;
            }
        }
    }
    return in.eof();
}
```

Mở đích một lần:

```cpp
std::ofstream out(dst, std::ios::binary | std::ios::trunc);
if (!out) { /* lỗi */ }

if (!append_file(out, file1)) { /* lỗi */ }
if (!append_file(out, file2)) { /* lỗi */ }
```

---

## 11. Định hướng Practice 9.1 — lệnh COPY

### 11.1. Yêu cầu

Viết chương trình `COPY` nhận tham số dòng lệnh:

```text
COPY <source file> <destination file>
COPY <source file> <destination path>/
COPY <file 1> + <file 2> <destination file>
COPY -?
```

- Syntax 1: sao chép tệp nguồn thành tệp đích.
- Syntax 2: sao chép vào thư mục đích, giữ nguyên tên tệp.
- Syntax 3: nối hai tệp thành một tệp đích.
- Syntax 4: hiển thị trợ giúp.
- Ghi chú: dùng chuỗi động (`std::string`, `std::filesystem::path`) và xử lý tệp nhị phân.

### 11.2. Phân tích tham số

```text
argv[1] = source
argv[2] = destination
```

Với nối tệp:

```text
argv[1] = file1
argv[2] = "+"
argv[3] = file2
argv[4] = destination
```

Cần kiểm tra:

- `argc` tối thiểu;
- `argv[2] == "+"` để chọn chế độ nối;
- `-?` để in help;
- các tham số thừa.

### 11.3. Xác định đích

Nếu đích là thư mục:

```cpp
std::filesystem::path dest = argv[2];
if (std::filesystem::is_directory(dest)) {
    dest /= std::filesystem::path(argv[1]).filename();
}
```

Nếu đích kết thúc bằng dấu phân cách nhưng chưa tồn tại, nên báo lỗi thay vì tự đoán.

### 11.4. Luồng xử lý

```text
Bắt đầu
  |
  +-- argc < 2? --> in help, return
  |
  +-- argv[1] == "-?"? --> in help, return
  |
  +-- có "+" ? --> nối file1 + file2
  |       |
  |       +-- mở đích binary/trunc
  |       +-- copy file1
  |       +-- copy file2
  |
  +-- không "+" ? --> copy một tệp
          |
          +-- nếu đích là thư mục: dest = dest / filename(source)
          +-- mở nguồn binary
          +-- mở đích binary/trunc
          +-- copy theo buffer
  |
  +-- kiểm tra lỗi, đóng tệp
  |
Kết thúc
```

### 11.5. Các lỗi cần xử lý

- Không mở được nguồn.
- Không tạo được đích.
- Nguồn và đích trùng nhau.
- Đích là thư mục nhưng không có quyền ghi.
- Nối tệp nhưng thiếu toán hạng.
- Ghi đè ngoài ý muốn.
- Tệp nguồn là thư mục.
- Đường dẫn có khoảng trắng (cần đặt trong dấu nháy khi chạy).
- Tên tệp quá dài hoặc ký tự không hợp lệ.

### 11.6. Gợi ý kiểm thử

```text
COPY a.txt b.txt
COPY a.txt backup/
COPY a.bin + b.bin c.bin
COPY -?
COPY missing.txt out.txt
COPY a.txt a.txt
```

Kiểm tra:

- nội dung tệp đích giống hệt nguồn (so sánh byte);
- kích thước bằng nhau;
- tệp nhị phân không bị hỏng;
- thông báo lỗi rõ ràng;
- mã trả về khác 0 khi lỗi.

---

## 12. Định hướng Practice 9.2 — cắt ảnh BMP

### 12.1. Yêu cầu

Viết chương trình cắt một tệp BMP thành các phần bằng nhau, lưu mỗi phần thành một tệp BMP mới.

Ví dụ:

```text
cutbmp.exe img1.bmp -h 3
cutbmp.exe img1.bmp -h 2 -w 4
```

- `-h 3`: cắt thành 3 phần theo chiều cao.
- `-h 2 -w 4`: cắt thành 2 phần theo chiều cao và 4 phần theo chiều rộng, tổng cộng 8 phần.

### 12.2. Cấu trúc tệp BMP

Một tệp BMP thường gồm:

```text
+----------------------+  offset 0
| BMP file header      |  14 byte
+----------------------+  offset 14
| DIB header           |  40 byte hoặc lớn hơn
+----------------------+  offset 14 + biSize
| Palette (nếu có)     |  tùy bit depth
+----------------------+  bfOffBits
| Pixel data           |  ảnh
+----------------------+
```

#### BMP file header (14 byte)

| Offset | Kích thước | Trường | Ý nghĩa |
|---:|---:|---|---|
| 0 | 2 | `bfType` | phải là `"BM"` |
| 2 | 4 | `bfSize` | kích thước tệp |
| 6 | 2 | `bfReserved1` | dự phòng |
| 8 | 2 | `bfReserved2` | dự phòng |
| 10 | 4 | `bfOffBits` | offset đến pixel data |

#### DIB header tối thiểu (40 byte)

| Offset | Kích thước | Trường | Ý nghĩa |
|---:|---:|---|---|
| 14 | 4 | `biSize` | kích thước DIB header |
| 18 | 4 | `biWidth` | chiều rộng (signed) |
| 22 | 4 | `biHeight` | chiều cao (signed) |
| 26 | 2 | `biPlanes` | thường là 1 |
| 28 | 2 | `biBitCount` | số bit/pixel |
| 30 | 4 | `biCompression` | 0 = BI_RGB |
| 34 | 4 | `biSizeImage` | kích thước pixel data |
| 38 | 4 | `biXPelsPerMeter` | độ phân giải ngang |
| 42 | 4 | `biYPelsPerMeter` | độ phân giải dọc |
| 46 | 4 | `biClrUsed` | số màu dùng |
| 50 | 4 | `biClrImportant` | số màu quan trọng |

Tất cả số nguyên của BMP đều **little-endian**.

### 12.3. Quy tắc hàng và padding

Mỗi hàng pixel được căn lên bội số của 4 byte.

Với ảnh `width` pixel, `bpp` bit/pixel:

```text
rowBytes = (width * bpp + 7) / 8
stride   = ((rowBytes + 3) / 4) * 4
```

Ví dụ ảnh 24-bit, rộng 3 pixel:

```text
rowBytes = 3 * 24 / 8 = 9 byte
stride   = ((9 + 3) / 4) * 4 = 12 byte
```

Vậy mỗi hàng có 3 byte padding.

### 12.4. Chiều cao âm và thứ tự hàng

- `biHeight > 0`: ảnh lưu **bottom-up**, hàng đầu tiên trong tệp là hàng dưới cùng.
- `biHeight < 0`: ảnh lưu **top-down**, hàng đầu tiên là hàng trên cùng.
- `biHeight == 0`: không hợp lệ.

Khi cắt theo tọa độ hiển thị, cần quy đổi:

```text
Nếu bottom-up:
    fileRow = height - 1 - imageRow

Nếu top-down:
    fileRow = imageRow
```

### 12.5. Kiểm tra tệp trước khi cắt

Nên kiểm tra:

- `bfType == "BM"`;
- `biSize >= 40`;
- `biWidth > 0`;
- `biHeight != 0`;
- `biPlanes == 1`;
- `biBitCount` thuộc loại hỗ trợ (24 hoặc 32; có thể thêm 8);
- `biCompression == 0` (BI_RGB);
- `bfOffBits` nằm trong tệp;
- kích thước pixel đủ lớn;
- các phép tính không tràn số.

Với bài tập, nên giới hạn ở ảnh 24-bit hoặc 32-bit không nén để đơn giản.

### 12.6. Chia kích thước

Khi không chia hết, phân phối phần dư cho các phần đầu:

```cpp
#include <vector>

std::vector<int> split_sizes(int total, int parts) {
    std::vector<int> sizes(parts, total / parts);
    const int remainder = total % parts;
    for (int i = 0; i < remainder; ++i) {
        ++sizes[i];
    }
    return sizes;
}
```

Ví dụ `total = 10`, `parts = 3` → `[4, 3, 3]`.

### 12.7. Thuật toán cắt

```text
Đọc header
  |
  +-- kiểm tra hợp lệ
  +-- tính stride, bytesPerPixel
  +-- tính kích thước từng phần theo h và w
  |
Với mỗi phần (rowBand, colBand):
  |
  +-- tạo header mới:
  |     - cùng palette/header
  |     - width = partWidth
  |     - height = ±partHeight
  |     - bfOffBits giữ nguyên nếu palette giữ nguyên
  |     - biSizeImage = newStride * partHeight
  |     - bfSize = bfOffBits + biSizeImage
  |
  +-- với mỗi hàng trong phần:
  |     - seek đến pixel đầu hàng + colStart * bytesPerPixel
  |     - đọc partWidth * bytesPerPixel byte
  |     - ghi vào tệp mới
  |     - ghi padding cho đủ newStride
  |
  +-- đóng tệp
```

### 12.8. Công thức vị trí pixel

```text
pixelOffset = bfOffBits
              + fileRow * stride
              + colStart * bytesPerPixel
```

Trong đó:

```text
stride        = ((width * bpp + 31) / 32) * 4
bytesPerPixel = bpp / 8        // với 24 hoặc 32 bpp
```

Với ảnh 24-bit: mỗi pixel là 3 byte BGR.
Với ảnh 32-bit: mỗi pixel là 4 byte BGRA.

### 12.9. Ghi header mới

Không nên `write` nguyên một struct C++ vì padding có thể khác với định dạng BMP. Thay vào đó:

- đọc toàn bộ vùng từ byte `0` đến `bfOffBits` (header + palette + phần đệm nếu có) vào buffer byte;
- sửa các trường ở offset xác định;
- ghi lại buffer.

Ví dụ sửa chiều rộng/cao:

```cpp
void patch_u32_le(std::vector<unsigned char>& data,
                  std::size_t offset,
                  std::uint32_t value) {
    data[offset + 0] = static_cast<unsigned char>(value & 0xFFu);
    data[offset + 1] = static_cast<unsigned char>((value >> 8) & 0xFFu);
    data[offset + 2] = static_cast<unsigned char>((value >> 16) & 0xFFu);
    data[offset + 3] = static_cast<unsigned char>((value >> 24) & 0xFFu);
}
```

Các offset cần sửa:

```text
bfSize        : 2
biWidth       : 18
biHeight      : 22
biSizeImage   : 34
```

### 12.10. Kiểm tra tràn số

`width * bpp` có thể tràn `int` nếu ảnh rất lớn. Dùng `std::uint64_t` cho tính toán trung gian:

```cpp
const std::uint64_t rowBytes =
    (static_cast<std::uint64_t>(width) * bpp + 7) / 8;
const std::uint64_t stride = ((rowBytes + 3) / 4) * 4;
```

Kiểm tra kết quả vẫn nằm trong giới hạn `std::streamsize` và kích thước tệp.

### 12.11. Đặt tên tệp đầu ra

Ví dụ:

```text
img1_part_r0_c0.bmp
img1_part_r0_c1.bmp
...
```

Dùng `std::ostringstream`:

```cpp
std::ostringstream name;
name << stem << "_part_r" << row << "_c" << col << ".bmp";
```

### 12.12. Gợi ý kiểm thử

- Ảnh nhỏ 1×1, 2×2, 3×3.
- Chiều rộng không chia hết cho 4 (kiểm tra padding).
- `-h 1`, `-w 1`.
- `-h` lớn hơn chiều cao (báo lỗi).
- `-w` lớn hơn chiều rộng (báo lỗi).
- Ảnh 24-bit và 32-bit.
- Ảnh top-down (`height < 0`).
- Tệp không phải BMP.
- Tệp BMP nén (không hỗ trợ).
- Tổng các phần ghép lại đúng ảnh gốc.

---

## 13. Lỗi thường gặp

| Lỗi | Nguyên nhân | Cách tránh |
|---|---|---|
| `while (!eof())` lặp thừa | `eofbit` chỉ bật sau khi đọc thất bại | dùng `while (getline(...))` hoặc `while (stream >> x)` |
| `getline` trả về chuỗi rỗng | còn newline sau `>>` | `ignore(max, '\n')` hoặc `getline(cin >> ws, ...)` |
| Không mở được tệp nhưng chương trình vẫn chạy | không kiểm tra `is_open()`/`!stream` | luôn kiểm tra sau khi mở |
| Tệp nhị phân bị hỏng | mở ở text mode | thêm `std::ios::binary` |
| Đọc thiếu byte | nhầm số phần tử với số byte | dùng `sizeof`, `gcount()` |
| Ghi struct sai | padding/endianness/ABI | serialize từng trường hoặc dùng định dạng chuẩn |
| Ghi con trỏ xuống tệp | địa chỉ chỉ đúng trong tiến trình hiện tại | không ghi con trỏ; ghi dữ liệu trỏ tới |
| `seekg` sai vị trí | text mode hoặc offset sai | dùng binary, kiểm tra `tellg` |
| `fstream` đọc/ghi sai | chưa seek/flush khi chuyển chế độ | `clear()`, `seekg/seekp` đúng |
| `setw` không có tác dụng ở mục sau | `setw` chỉ áp dụng một lần | đặt lại trước mỗi mục |
| `endl` làm chậm | flush mỗi dòng | dùng `'\n'` khi không cần flush |
| Mở đích trước khi kiểm tra nguồn | truncate làm mất nguồn nếu trùng tệp | kiểm tra `equivalent`, mở nguồn trước |
| Đọc toàn bộ tệp quá lớn | tốn RAM | đọc theo buffer |
| `read` trả về false nhưng vẫn còn dữ liệu | EOF/fail sau khi đọc một phần | dùng `gcount()` |
| Đường dẫn `\` bị hiểu sai | escape sequence | dùng `/` hoặc raw string |
| Xóa/đổi tên tệp đang mở | hệ điều hành khóa tệp | đóng tệp trước |
| Tràn số khi tính kích thước ảnh | `int` quá nhỏ | dùng `std::uint64_t` |

---

## 14. Bảng tra nhanh

### 14.1. Thư viện

| Thư viện | Nội dung |
|---|---|
| `<iostream>` | `cin`, `cout`, `cerr`, `clog` |
| `<fstream>` | `ifstream`, `ofstream`, `fstream` |
| `<sstream>` | `istringstream`, `ostringstream`, `stringstream` |
| `<iomanip>` | `setw`, `setprecision`, `setfill`, `quoted`... |
| `<filesystem>` | đường dẫn, kiểm tra, sao chép, xóa, đổi tên |
| `<cstdint>` | `int8_t`...`uint64_t` |
| `<limits>` | `numeric_limits` |
| `<type_traits>` | `is_trivially_copyable` |
| `<charconv>` | `from_chars`, `to_chars` |
| `<bit>` | `std::endian`, `bit_cast` (C++20) |

### 14.2. Trạng thái

```cpp
if (!stream)            // có lỗi
if (stream.eof())       // cuối tệp
if (stream.fail())      // fail hoặc bad
if (stream.bad())       // lỗi nghiêm trọng
stream.clear();         // xóa cờ
stream.ignore(n, c);    // bỏ qua
```

### 14.3. Mở tệp

```cpp
std::ifstream in(path);                              // đọc text
std::ifstream in(path, std::ios::binary);            // đọc binary
std::ofstream out(path);                             // ghi text, truncate
std::ofstream out(path, std::ios::app);              // ghi nối
std::ofstream out(path, std::ios::binary | std::ios::trunc);
std::fstream io(path, std::ios::in | std::ios::out | std::ios::binary);
```

### 14.4. Đọc/ghi

```cpp
std::getline(in, line);          // dòng
in >> word;                      // từ
in.get(c);                       // ký tự
in.read(buf, n);                 // n byte
in.gcount();                     // số byte đọc được
out.write(buf, n);               // n byte
out << value;                    // định dạng
out.flush();                     // đẩy buffer
```

### 14.5. Di chuyển

```cpp
in.seekg(0, std::ios::beg);
in.seekg(offset, std::ios::cur);
in.seekg(-n, std::ios::end);
auto pos = in.tellg();

out.seekp(0, std::ios::beg);
auto pos = out.tellp();
```

### 14.6. Filesystem

```cpp
namespace fs = std::filesystem;

fs::exists(p);
fs::is_directory(p);
fs::file_size(p);
fs::create_directories(p);
fs::remove(p);
fs::rename(old, new);
fs::copy_file(src, dst, fs::copy_options::overwrite_existing);
```

---

## 15. Câu hỏi tự kiểm tra

1. **Phân biệt `std::cin`, `std::ifstream`, `std::istringstream`.**
2. **Vì sao `while (!in.eof())` thường sai?**
3. **`std::endl` khác `'\n'` ở điểm nào?**
4. **Khi nào dùng `std::ios::binary`?**
5. **`read` và `gcount` liên quan thế nào?**
6. **Vì sao không nên ghi nguyên `std::string` xuống tệp nhị phân?**
7. **Padding và endianness ảnh hưởng gì đến tệp nhị phân?**
8. **Khi nào dùng `seekg`, khi nào dùng `seekp`?**
9. **Vì sao không nên seek tùy ý trên tệp văn bản?**
10. **`std::stringstream` dùng để làm gì?**
11. **`argc` và `argv` lưu gì?**
12. **Nêu các bước cắt ảnh BMP theo chiều rộng.**

### Đáp án gợi ý

1. `cin` đọc từ bàn phím/standard input; `ifstream` đọc từ tệp; `istringstream` đọc từ chuỗi trong bộ nhớ.
2. Vì `eofbit` chỉ bật sau khi một thao tác đọc đã thất bại; vòng lặp có thể chạy thêm một lần với dữ liệu cũ/rỗng. Dùng `while (getline(...))` hoặc `while (stream >> x)`.
3. `std::endl` ghi `'\n'` và flush; `'\n'` chỉ ghi newline, không flush.
4. Khi cần đọc/ghi nguyên byte, tránh chuyển đổi newline/encoding, thường cho ảnh, âm thanh, struct, mảng số.
5. `read` đọc tối đa `n` byte; `gcount()` cho biết thực tế đã đọc bao nhiêu byte. Dùng để phát hiện block cuối/đọc thiếu.
6. `std::string` chứa con trỏ, kích thước, capacity...; ghi nguyên object sẽ ghi địa chỉ, không portable và không đọc lại đúng. Ghi nội dung chuỗi (kèm độ dài/encoding) thay vì object.
7. Padding làm kích thước/bố cục khác nhau; endianness làm thứ tự byte khác nhau. Tệp ghi trên máy này có thể không đọc đúng trên máy khác.
8. `seekg` cho luồng đọc; `seekp` cho luồng ghi. Với `fstream`, dùng đúng thao tác trước khi đọc/ghi.
9. Text mode có thể chuyển đổi newline, nên offset byte vật lý không tương ứng vị trí logic; chỉ seek về 0 hoặc vị trí do `tellg` trả về.
10. Dùng chuỗi như luồng để định dạng/parse dữ liệu trong bộ nhớ, ví dụ tạo tên tệp, parse CSV, chuyển số thành chuỗi.
11. `argc` là số tham số gồm tên chương trình; `argv` là mảng chuỗi tham số, `argv[0]` là tên chương trình, `argv[argc] == nullptr`.
12. Đọc/kiểm tra header, tính stride/padding, xác định vùng cột, với mỗi hàng seek đến pixel đầu, đọc `partWidth * bytesPerPixel`, ghi sang tệp mới, thêm padding, cập nhật `biWidth`, `biHeight`, `biSizeImage`, `bfSize`, rồi đóng tệp.

---

## 16. Tài liệu tham khảo

### Nguồn nội dung

- `chap22.pdf` — Chapter 22: Input/Output, nội dung về luồng, tệp, định dạng, block I/O, positioning, string I/O.
- `IP-09-Binary File.pdf` — bài giảng Binary File: tham số dòng lệnh, chế độ nhị phân, `read`/`write`/`seekg`, struct, Practice 9.1 và 9.2.

### C++ reference

- cppreference — `std::basic_ifstream`: <https://en.cppreference.com/w/cpp/io/basic_ifstream>
- cppreference — `std::basic_istream::read`: <https://en.cppreference.com/w/cpp/io/basic_istream/read>
- cppreference — `std::basic_ostream::write`: <https://en.cppreference.com/w/cpp/io/basic_ostream/write>
- cppreference — `std::basic_istream::seekg`: <https://en.cppreference.com/w/cpp/io/basic_istream/seekg>
- cppreference — `std::basic_ostream::seekp`: <https://en.cppreference.com/w/cpp/io/basic_ostream/seekp>
- cppreference — `std::ios_base::openmode`: <https://en.cppreference.com/w/cpp/io/ios_base/openmode>
- cppreference — `std::basic_stringstream`: <https://en.cppreference.com/w/cpp/io/basic_stringstream>
- cppreference — `std::filesystem`: <https://en.cppreference.com/w/cpp/filesystem>
- cppreference — `std::endian`: <https://en.cppreference.com/w/cpp/types/endian>

### Hướng dẫn

- LearnC++ — Basic file I/O: <https://www.learncpp.com/cpp-tutorial/basic-file-io/>
- LearnC++ — Random file I/O: <https://www.learncpp.com/cpp-tutorial/random-file-io/>

### Định dạng BMP

- Microsoft Learn — Bitmap Storage: <https://learn.microsoft.com/en-us/windows/win32/gdi/bitmap-storage>
- Microsoft Learn — BITMAPFILEHEADER: <https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapfileheader>
- Microsoft Learn — BITMAPINFOHEADER: <https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader>

---

> **Ghi chú cuối:** Tài liệu này chỉ dùng thư viện chuẩn C++. Khi làm bài, ưu tiên kiểm tra lỗi mở tệp, đọc/ghi đủ byte, đóng tệp đúng và không giả định bố cục nhị phân giống nhau giữa mọi nền tảng.
