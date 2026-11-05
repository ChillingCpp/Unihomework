# Practice 8.3 — Arbitrary-length paragraph

Compile:

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp paragraph.cpp -o practice8.3
```

Run:

```powershell
.\practice8.3
```

Chương trình đọc từng dòng bằng `std::getline` và nối vào một `std::string`, nên độ dài đoạn văn không bị giới hạn bởi mảng cố định. Chương trình dừng khi gặp dòng có ký tự cuối (bỏ qua khoảng trắng/tab) là dấu chấm `.`.

Các trường hợp đã xử lý:

- Đoạn văn nhiều dòng: giữ nguyên ký tự xuống dòng giữa các dòng.
- Dòng chỉ có `.`: kết thúc và in `.`.
- Dấu chấm nằm giữa dòng nhưng chưa phải cuối dòng: tiếp tục đọc.
- Dòng kết thúc bằng `.` theo sau bởi khoảng trắng/tab: vẫn nhận là kết thúc.
- EOF trước khi gặp dấu chấm: in phần đã đọc, báo lỗi và trả mã 1.
- Input rỗng: in dòng trống và báo lỗi.
- Đoạn văn rất dài: `std::string` tự cấp phát động.
