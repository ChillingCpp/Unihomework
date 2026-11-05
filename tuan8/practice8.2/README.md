# Practice 8.2 — Increase all numbers

Compile:

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp big_number.cpp -o practice8.2
```

Run:

```powershell
.\practice8.2
```

Mỗi số được hiểu là một dãy ký tự chữ số liên tiếp (số nguyên không âm). `add_strings` cộng hai chuỗi số có độ dài tùy ý, không chuyển sang `int`/`long long`, nên xử lý được số rất lớn.

Các trường hợp đã xử lý:

- Không có chữ số: giữ nguyên câu.
- Câu rỗng: in dòng trống.
- Số có số 0 ở đầu: kết quả được chuẩn hóa (ví dụ `0009` → `10`).
- Số `0`: tăng thành `1`.
- Số toàn `9`: có nhớ và tăng độ dài (ví dụ `999` → `1000`).
- Chuỗi rất dài: chỉ cấp phát theo độ dài chuỗi, không dùng mảng cố định.
- Lỗi đọc input/EOF: báo lỗi và kết thúc chương trình.
- Dấu `-` và dấu chấm thập phân được xem là ký tự phân cách; chương trình xử lý các cụm chữ số, không phân tích số âm/số thực.
