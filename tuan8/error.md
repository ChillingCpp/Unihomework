# Kết quả kiểm tra code practice8.1–8.5

## Phạm vi kiểm tra

- Đã đọc source trong `practice8.1`, `practice8.2`, `practice8.3`.
- `practice8.4` và `practice8.5` hiện chỉ có file markdown, không có file `.cpp`/`.h`, nên không có code C++ để kiểm tra.
- Đã compile bằng `g++ 15.2.0` với `-std=c++17 -Wall -Wextra -pedantic` và chạy thử các input mẫu/edge case.
- Không sửa file nào trong 5 folder.

## Tổng hợp lỗi

| Mức | File | Lỗi |
|---|---|---|
| Cao | `practice8.1/replace_words.cpp` | Mất phần đuôi sau lần khớp cuối; không khớp thì trả về chuỗi rỗng |
| Cao | `practice8.1/replace_words.cpp` | Tìm chồng lấn (`p + 1`) gây sai kết quả và có thể append với độ dài âm |
| Trung bình | `practice8.1/replace_words.cpp` | Dùng `int` cho `find()`/`npos`, không an toàn với chuỗi dài |
| Cao | `practice8.2/big_number.cpp` | `std::isdigit(static_cast<char>(...))` có thể là hành vi không xác định với byte UTF-8/ký tự âm |
| Thấp | `practice8.2/big_number.cpp` | Cảnh báo signed/unsigned khi so sánh chỉ số với `std::string::size_type` |
| Nghiêm trọng | `practice8.3/paragraph.cpp` | Gặp EOF sẽ lặp vô hạn |
| Trung bình | `practice8.3/paragraph.cpp` | Dùng `char` cho `getchar()` nên không phân biệt được EOF; thiếu `<cstdio>` |
| Thấp | `practice8.3/paragraph.cpp` | In thêm dòng trống trước và sau đoạn văn |
| Thấp | `practice8.3/paragraph.cpp` | Chỉ dừng khi `.` đứng ngay trước `\n`, không dừng nếu có khoảng trắng sau dấu chấm |

---

## 1. `practice8.1/replace_words.cpp`

### 1.1. Mất phần còn lại sau lần khớp cuối — lỗi cao

Vị trí: `replace_words.cpp:9-16`.

Vòng lặp chỉ nối các đoạn **trước** mỗi lần khớp, nhưng sau khi vòng lặp kết thúc không hề nối đoạn còn lại của `source` từ `prev` đến hết chuỗi.

Hệ quả:

- Không tìm thấy `find`: vòng lặp không chạy, `result` rỗng, hàm trả về chuỗi rỗng thay vì trả lại `source`.
- Có tìm thấy: phần sau lần khớp cuối bị mất.

Ví dụ với input mẫu:

```text
S = the good, the bad, the ugly
F = the
R = (a very)
```

Kết quả thực tế:

```text
(a very) good, (a very) bad, (a very)
```

Kết quả đúng phải còn phần ` ugly`:

```text
(a very) good, (a very) bad, (a very) ugly
```

Ví dụ không khớp:

```text
S = abc abc
F = zzz
R = X
```

Kết quả thực tế: chuỗi rỗng. Kết quả đúng: `abc abc`.

Hướng sửa: sau vòng lặp phải append đoạn `source` từ `prev` đến hết; nếu không có lần khớp nào thì trả lại `source`.

### 1.2. Tìm chồng lấn làm sai kết quả — lỗi cao

Vị trí: `replace_words.cpp:9-13`.

Vòng lặp tìm lần tiếp theo bằng `source.find(find, p + 1)` thay vì tìm từ `prev` (vị trí sau lần khớp trước). Với `find` dài hơn 1 ký tự, lần tìm sau có thể rơi vào bên trong lần khớp trước. Khi đó `p < prev`, biểu thức `p - prev` là số âm nhưng được truyền vào `std::string::append` dưới dạng `size_type`, thành một giá trị rất lớn.

Ví dụ:

```text
S = aaaa
F = aa
R = b
```

Kết quả thực tế:

```text
baabab
```

Trong khi cách thay thế không chồng lấn thông thường phải cho:

```text
bb
```

Đây không chỉ là sai kết quả mà còn là vùng hành vi không xác định/nguy hiểm do độ dài âm khi append.

Hướng sửa: sau mỗi lần khớp, đặt `prev = p + find.size()` và lần tìm tiếp theo phải bắt đầu từ `prev`, không phải `p + 1`.

### 1.3. Dùng `int` cho kết quả `find()` và `npos` — lỗi trung bình

Vị trí: `replace_words.cpp:9-10`.

`std::string::find()` trả về `std::string::size_type` (`size_t`), còn code lưu vào `int` và so sánh với `-1`. Việc `npos` chuyển thành `-1` không được chuẩn C++ bảo đảm; với chuỗi dài hơn `INT_MAX` còn bị tràn. Nên dùng `std::string::size_type` và so sánh với `std::string::npos`.

---

## 2. `practice8.2/big_number.cpp`

### 2.1. `std::isdigit` nhận `char` có thể âm — lỗi cao

Vị trí: `big_number.cpp:29` và `big_number.cpp:33`.

Code đang dùng:

```cpp
std::isdigit(static_cast<char>(sentence[i]))
```

Theo chuẩn C++, đối số của `std::isdigit` phải là giá trị biểu diễn được dưới dạng `unsigned char`, hoặc `EOF`. Nếu `char` là signed và gặp byte UTF-8/tiếng Việt có giá trị > 127, giá trị truyền vào có thể âm, gây hành vi không xác định.

Hướng sửa: dùng `std::isdigit(static_cast<unsigned char>(sentence[i]))`.

### 2.2. Ghi chú: `add_strings` cộng thêm 1 là đúng thiết kế — không phải lỗi

Vị trí: `big_number.cpp:5-20`, khai báo `big_number.h:8`.

Theo yêu cầu bài 8.2, mỗi số chỉ cần tăng thêm `1`. Hàm nhận một chuỗi và luôn cộng `"1"` là implementation chuyên dụng cho đúng đề bài; không cần viết hàm cộng hai số tổng quát. Vì vậy không xem đây là lỗi.

Hàm chỉ được gọi từ `increase_numbers` với cụm chữ số không rỗng, nên việc không kiểm tra chuỗi rỗng/không phải chữ số không phải lỗi trong luồng hiện tại. Nếu sau này dùng lại như một API công khai cho dữ liệu tùy ý thì mới cần bổ sung kiểm tra.

### 2.3. Cảnh báo signed/unsigned — lỗi thấp

Vị trí: `big_number.cpp:27` và `big_number.cpp:33`.

Trình biên dịch cảnh báo:

```text
comparison of integer expressions of different signedness: 'int' and
'std::string::size_type'
```

Nên dùng `std::string::size_type`/`std::size_t` cho chỉ số hoặc ép kiểu có kiểm soát.

---

## 3. `practice8.3/paragraph.cpp`

### 3.1. Gặp EOF sẽ lặp vô hạn — lỗi nghiêm trọng

Vị trí: `paragraph.cpp:5-14`.

Code không kiểm tra giá trị `EOF` của `getchar()`. Khi input kết thúc mà chưa có dãy `.\n`, `getchar()` trả về `EOF`; giá trị này bị chuyển thành `char`, được push vào `std::string`, rồi vòng lặp tiếp tục gọi `getchar()` mãi mãi. Chương trình không thoát và có thể ngốn bộ nhớ.

Đã kiểm tra thực tế: chạy chương trình với input rỗng/đóng stdin, quá trình không kết thúc sau 5 giây.

Hướng sửa: dùng `int c = std::getchar();`, kiểm tra `c == EOF` và thoát vòng lặp; chỉ push `char` sau khi đã loại EOF.

### 3.2. Dùng `char` cho `getchar()` và thiếu `<cstdio>` — lỗi trung bình

Vị trí: `paragraph.cpp:5`, `paragraph.cpp:13`.

`getchar()` trả về `int` để phân biệt được mọi byte với `EOF`. Lưu ngay vào `char` làm mất thông tin EOF. Ngoài ra `getchar()` thuộc `<cstdio>` nhưng file không include trực tiếp; hiện tại biên dịch được nhờ include gián tiếp, không bảo đảm trên mọi compiler.

### 3.3. In thêm dòng trống — lỗi thấp

Vị trí: `paragraph.cpp:15`.

Code in:

```cpp
std::cout << '\n' << s << '\n';
```

Vì `s` đã chứa ký tự `\n` kết thúc input, kết quả có thêm dòng trống trước và sau đoạn văn. Với input `Hello` / `world.`, output thực tế có một dòng trống trước `Hello` và một dòng trống sau `world.`. Nếu đề yêu cầu in đúng đoạn văn, đây là lỗi định dạng.

### 3.4. Chỉ dừng khi dấu chấm đứng ngay trước newline — lỗi thấp

Vị trí: `paragraph.cpp:10`.

Điều kiện:

```cpp
if (pv == '.' && c == '\n')
```

chỉ đúng khi ký tự ngay trước `\n` là `.`. Nếu người dùng nhập `Hello. ` rồi mới xuống dòng (có khoảng trắng sau dấu chấm), chương trình không dừng. Cần làm rõ yêu cầu hoặc bỏ qua khoảng trắng trước khi kiểm tra.

---

## 4. `practice8.4` và `practice8.5`

Hiện tại hai folder chỉ có:

- `practice8.4/practice8.4.md`
- `practice8.5/practice8.5.md`

Không có file source C++ nên không thể kiểm tra code. Nếu cần kiểm tra code hai bài này, cần đặt lại các file `.cpp`/`.h` vào đúng folder.

Ghi chú thêm ở `practice8.5.md` dòng 12: câu “tổng là 200 byte” đang cộng 80 byte trên stack với 120 byte trên heap. Tổng số byte là 200 nếu chỉ hỏi tổng, nhưng nên tách rõ hai vùng nhớ khác nhau để tránh hiểu nhầm.

---

## Kết luận

Các lỗi cần ưu tiên sửa trước:

1. `practice8.1`: mất phần đuôi và sai khi có match chồng lấn.
2. `practice8.3`: lặp vô hạn khi gặp EOF.
3. `practice8.2`: `std::isdigit` với `char` có thể âm.

Các vấn đề còn lại là lỗi biên/portability/định dạng. Riêng `add_strings` cộng thêm 1 là thiết kế đúng theo đề bài 8.2, không phải lỗi.
