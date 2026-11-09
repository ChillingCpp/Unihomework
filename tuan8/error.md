# Kết quả kiểm tra code practice8.1–8.3

## Phạm vi và cách kiểm tra

- Đã đọc lại source hiện tại trong `practice8.1`, `practice8.2`, `practice8.3`.
- Đã compile từng bài bằng `g++ 15.2.0` với `-std=c++17 -Wall -Wextra -pedantic`.
- Đã chạy input mẫu và các edge case; binary/test tạm đặt ngoài các folder bài tập.
- Không sửa file nào trong `practice8.1`–`practice8.5`.
- `add_strings` của practice8.2 là implementation cố ý **chỉ cộng thêm 1** theo đề bài; đây không phải lỗi và không bị yêu cầu viết thành hàm cộng hai số tổng quát.

## Các lỗi đã được sửa / hiện đã ổn

- `practice8.1`: đã nối phần đuôi sau lần khớp cuối; không tìm thấy thì trả lại nguyên câu; match chồng lấn đã đúng; có chặn `find` rỗng. `prev` đã đổi sang `std::string::size_type`, không còn cảnh báo signed/unsigned.
  - `the good, the bad, the ugly` / `the` / `(a very)` → `(a very) good, (a very) bad, (a very) ugly`.
  - `abc abc` / `zzz` / `X` → `abc abc`.
  - `aaaa` / `aa` / `b` → `bb`.
  - `abc` / chuỗi tìm rỗng / `X` → `abc` (không lỗi).
- `practice8.2`: `std::isdigit` đã cast sang `unsigned char`, không còn lỗi UB do byte âm ở vị trí này.
  - `there are 9 cats and 19 dogs.` → `there are 10 cats and 20 dogs.`
  - `9 99 999 0009` → `10 100 1000 0010`.
  - `999` → `1000`; `a1b22c333d` → `a2b23c334d`.
- `practice8.3`: đã thêm kiểm tra `EOF`; input rỗng không còn treo. Logic `pv` hiện cập nhật theo ký tự không phải khoảng trắng, nên đã dừng đúng cả khi đoạn văn có dấu cách.
  - `Hello.` + newline → chỉ đọc `Hello.`.
  - `Hello world.` + newline + dòng khác → chỉ đọc `Hello world.`.
  - `Hello world.  ` + newline (có khoảng trắng sau dấu chấm) → vẫn dừng đúng.
  - `Hello world.` + EOF (không có newline) → đọc hết và kết thúc bình thường.
- `practice8.4` và `practice8.5`: chỉ có file markdown, không có source C++ để kiểm tra.

## Lỗi còn lại

### 1. `practice8.3/paragraph.cpp` — in thêm dòng trống (lỗi thấp)

Vị trí: `paragraph.cpp:19`.

```cpp
std::cout << s << '\n';
```

`s` đã chứa ký tự newline của input (trường hợp bình thường kết thúc bằng `.` + newline), nên output có thêm một dòng trống sau đoạn văn. Với input `Hello.` + newline, output thực tế là:

```text
Hello.

```

Nếu đề chỉ yêu cầu in đoạn văn, nên tránh cộng thêm newline khi `s` đã kết thúc bằng `\n`, ví dụ:

```cpp
std::cout << s;
if (s.empty() || s.back() != '\n')
    std::cout << '\n';
```

Đây chỉ là lỗi định dạng, không ảnh hưởng nội dung đoạn văn.

### 2. `practice8.2/big_number.cpp` — cảnh báo signed/unsigned (lỗi thấp)

Vị trí: `big_number.cpp:27`, `big_number.cpp:33`.

Hai vòng lặp dùng `int i` để so sánh với `sentence.size()` (`std::string::size_type`, không dấu), sinh cảnh báo:

```text
warning: comparison of integer expressions of different signedness:
'int' and 'std::string::size_type' [-Wsign-compare]
```

Với chuỗi thông thường, code vẫn chạy đúng. Về mặt lý thuyết, nếu chuỗi dài hơn `INT_MAX`, `int i` có thể tràn. Nên đổi `i` và `start` sang `std::string::size_type`/`std::size_t` để sạch cảnh báo và nhất quán.

### 3. `practice8.2/big_number.cpp` — `add_strings("")` (edge case, lỗi thấp)

Vị trí: `big_number.cpp:9`.

```cpp
for (int i = t.size() - 1; i >= 0; --i)
```

Nếu `t` rỗng, `t.size() - 1` bị underflow vì `size()` là số không dấu. Đã thử trực tiếp: `add_strings("")` trả về `"1"`, không hợp lý cho input rỗng.

Trong luồng `increase_numbers`, `number` luôn là cụm chữ số không rỗng nên lỗi này **chưa lộ ra** khi chạy chương trình chính. Tuy nhiên `add_strings` đang được khai báo public trong `big_number.h`, nên nên thêm:

```cpp
if (t.empty())
    return t;
```

`add_strings` cũng giả định input chỉ gồm chữ số; `add_strings("12a")` cho `"12b"`. Đây không phải lỗi trong luồng hiện tại vì `increase_numbers` chỉ lấy cụm chữ số, nhưng là giới hạn của hàm public.

## Không phải lỗi

- `add_strings` chỉ cộng 1 là đúng yêu cầu practice8.2, không cần viết hàm cộng hai chuỗi số tổng quát.
- `practice8.3` không báo lỗi khi gặp `EOF` trước dấu chấm: đề chỉ yêu cầu đọc đến `.` + newline rồi in đoạn văn, không yêu cầu thông báo lỗi. Việc dừng ở `EOF` và in phần đã đọc là chấp nhận được.
- `practice8.3` dùng `std::string` nên vẫn đáp ứng yêu cầu “dynamic string”; không cần tự cấp phát bằng `new[]`.

## Kết luận

Không còn lỗi nghiêm trọng trong `practice8.1`–`practice8.3`.

Ưu tiên còn lại:

1. **practice8.3**: bỏ newline thừa khi in — lỗi định dạng thấp.
2. **practice8.2**: đổi chỉ số vòng lặp sang `std::size_t` — chỉ là cảnh báo/portability.
3. **practice8.2**: thêm kiểm tra `t.empty()` trong `add_strings` — edge case của hàm public, không ảnh hưởng luồng chính.

Không có file nào trong các folder `practice8.1`–`practice8.5` bị sửa.
