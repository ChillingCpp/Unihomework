# Practice 8.1 — Find and replace

Compile:

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp replace_words.cpp -o practice8.1
```

Run:

```powershell
.\practice8.1
```

`F` được hiểu là chuỗi cần tìm trong `S` (có thể là một từ hoặc nhiều ký tự). Chương trình thay thế mọi lần xuất hiện **không chồng lấn**, giữ nguyên phần còn lại của câu.

Các trường hợp đã xử lý:

- `F` rỗng: báo lỗi, không thực hiện thay thế.
- `F` không có trong `S`: in lại `S` nguyên vẹn.
- `R` rỗng: xóa các lần xuất hiện của `F`.
- `S` rỗng: in dòng trống.
- `F` dài hơn `S`: không tìm thấy, in lại `S`.
- Chuỗi rất dài: dùng `std::string` nên không giới hạn độ dài cố định.
- Lỗi đọc input/EOF: báo lỗi và kết thúc chương trình.
