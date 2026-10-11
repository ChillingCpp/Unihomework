# Tóm tắt IP-04: Function, Struct và Project nhiều file

## 1. Function

- Hàm là khối lệnh có tên, gọi được từ bất cứ đâu với đối số khác nhau. Sinh ra để gom code lặp lại: viết một lần, dùng mọi nơi, sửa một chỗ.
- Cấu trúc gồm prototype (khai báo: tên, tham số, kiểu trả về) và body (định nghĩa).
- Truyền tham số trị (by-value): hàm chỉ nhận bản sao, đối số thật không đổi; dùng được biến, hằng, biểu thức.
- Truyền tham chiếu (by-reference, C++ với `&`): hàm nhận đúng đối số thật nên đổi được nó; chỉ dùng được biến. Dùng để trả nhiều giá trị (hàm nhập, hàm tính ghi kết quả qua tham chiếu).
- Hàm có scope toàn cục. Biến toàn cục khai báo ngoài mọi hàm, dùng khắp nơi; biến cục bộ chỉ sống trong block của nó.

## 2. Tổ chức project nhiều file

- Chương trình như cuốn sách: `main()` là phần tóm tắt, các file `.cpp` là các chương (input, compute, output).
- File header `.h` nối các file nguồn: chỉ chứa khai báo (prototype), file `.cpp` chứa định nghĩa. Muốn `A.cpp` thấy code của `B.cpp` thì `#include "B.h"`.
- Quy trình build: compile (source -> assembly) + assemble (assembly -> machine) + link (machine -> exe). Build bằng wildcard `*.cpp`.
- Cây phân rã chương trình: chia theo mức trừu tượng và khả năng tái dùng (ví dụ `input_num`, `factorial` dùng lại cho nhiều nhánh). Mỗi hàm nên ngắn, dưới ~30 lệnh.

## 3. Struct

- Gom nhiều dữ liệu liên quan thành một kiểu dữ liệu hợp nhất (ví dụ sinh viên: id, name, literature, math).
- Khai báo dạng `struct` hoặc `typedef struct {...} Name`; trong C++ dùng tên trực tiếp, C phải viết `struct Name`.
- Khởi tạo theo thứ tự khai báo, hoặc theo tên member kiểu C99 (`.name = ...`). Truy xuất member bằng dấu `.`.
- Truyền struct trị thì chép toàn bộ (kể cả member mảng), không đổi được bản gốc; truyền tham chiếu thì đổi được.
- Gán struct chép toàn bộ member sang struct cùng kiểu.
