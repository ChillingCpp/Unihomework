# Tuần 8 — Advanced Pointer

Hai dạng bài cho mỗi practice:

- **Single-file:** `practice8.1.cpp` … `practice8.5.cpp`.
- **Multi-file project:** thư mục `practice8.1/` … `practice8.5/`, mỗi thư mục có `main.cpp`, header, implementation và `README.md`.

Không dùng `std::vector`; các bài dùng `std::string`, `std::getline`, `std::cout`, `new`/`delete[]`, con trỏ và mảng.

## Compile single-file

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic practice8.1.cpp -o practice8.1
g++ -std=c++17 -Wall -Wextra -pedantic practice8.2.cpp -o practice8.2
g++ -std=c++17 -Wall -Wextra -pedantic practice8.3.cpp -o practice8.3
g++ -std=c++17 -Wall -Wextra -pedantic practice8.4.cpp -o practice8.4
g++ -std=c++17 -Wall -Wextra -pedantic practice8.5.cpp -o practice8.5
```

## Compile multi-file

```powershell
cd practice8.1
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp replace_words.cpp -o practice8.1

cd ../practice8.2
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp big_number.cpp -o practice8.2

cd ../practice8.3
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp paragraph.cpp -o practice8.3

cd ../practice8.4
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp matrix_access.cpp -o practice8.4

cd ../practice8.5
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp dynamic_array.cpp -o practice8.5
```

## Ghi chú xử lý edge case

- **8.1:** từ cần tìm rỗng bị từ chối; không tìm thấy thì giữ nguyên câu; từ thay thế rỗng thì xóa; thay thế không chồng lấn; hỗ trợ chuỗi dài.
- **8.2:** cộng chuỗi số bằng tay, không dùng `int`/`long long`; xử lý số rất lớn, số toàn `9`, số 0 ở đầu; không có chữ số thì giữ nguyên; dấu `-`/dấu chấm được xem là ký tự phân cách (bài chỉ xử lý số nguyên không âm).
- **8.3:** đọc đến dòng kết thúc bằng `.`; giữ xuống dòng; EOF trước dấu chấm sẽ in phần đã đọc và báo lỗi; `std::string` cấp phát động.
- **8.4:** trả lời kiểu địa chỉ của `m[1][3]`, `m[0]`, `m`; truy cập `m[2][4]` bằng `*(*(m + 2) + 4)`.
- **8.5:** giải thích cấp phát `p[10]` và 5 mảng động; sửa `release(p)` thành `release(p + 3)`; `release` xóa đúng 5 mảng và tránh double delete.
