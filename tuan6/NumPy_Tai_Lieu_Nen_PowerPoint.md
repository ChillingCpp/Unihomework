# TÌM HIỂU THƯ VIỆN NUMPY TRONG PYTHON

**Tài liệu nền phục vụ biên soạn bài thuyết trình PowerPoint 20–25 slide**

> **Quy ước kiểm chứng**
> - Toàn bộ code đã chạy thực tế trên **Python 3.14 + NumPy 2.5.4**; kết quả in ra là kết quả thật.
> - **[x]** là nguồn ở mục III.I. **“Nhận định”** là đánh giá tổng quát, không phải số liệu đo.
> - Tài liệu không tạo benchmark tốc độ; chỉ giải thích lợi ích cấu trúc của vector hóa.

---

# PHẦN I — TỔNG QUAN NỘI DUNG

## 1. Mục tiêu học tập

Sau bài thuyết trình, người học có thể:

1. Giải thích NumPy là gì và vai trò của nó trong tính toán khoa học.
2. Mô tả `ndarray` qua `shape`, `ndim`, `size`, `dtype`.
3. Tạo mảng bằng `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`, `np.eye()`.
4. Truy cập dữ liệu bằng indexing, slicing, boolean indexing; biến đổi bằng `reshape()` và `.T`.
5. Phân biệt `*` với `@`, hiểu `axis` trong hàm tổng hợp.
6. Giải thích và áp dụng broadcasting, nhận diện trường hợp thất bại.

## 2. Mạch kiến thức

**Vấn đề → đối tượng → tạo → truy cập → tính toán → mở rộng → ứng dụng.** Cụ thể: giới hạn của list (A) → `ndarray` (A, B) → tạo mảng (C) → lấy dữ liệu (D) → phép toán (E) → broadcasting (F) → ví dụ (G) → kết luận (H).

## 3. Khái niệm phải nắm

- `ndarray`: mảng N chiều, **đồng nhất kiểu**, **kích thước cố định**.
- `ndim = len(shape)`; `size = tích(shape)`.
- Chỉ số bắt đầu từ **0**; slice `start:stop:step` **không gồm `stop`**.
- `*` nhân từng phần tử; `@` nhân ma trận.
- `axis=0` gộp hàng; `axis=1` gộp cột.
- Broadcasting so sánh shape **từ phải sang trái**; tương thích nếu **bằng nhau** hoặc **một bên bằng 1**.

---

# PHẦN II — BẢN ĐỒ CHUYỂN ĐỔI SANG POWERPOINT (24 SLIDE)

> Đây là hướng dẫn biên tập; lời thuyết trình chi tiết ở Phần III.

### Slide 1 — Tiêu đề
- **Mục tiêu:** Giới thiệu chủ đề.
- **Ý chính:** “Tìm hiểu thư viện NumPy trong Python”; phụ đề “Từ `ndarray` đến broadcasting”; tên người trình bày.
- **Hình ảnh:** logo NumPy.
- **Vẽ PowerPoint:** dải màu bo góc, lưới ô vuông mờ.
- **Nguồn:** [1]

### Slide 2 — Nội dung bài thuyết trình
- **Mục tiêu:** Người nghe biết trước 6 chặng.
- **Ý chính:** Giới thiệu; Cấu trúc mảng; Tạo mảng; Truy cập; Phép toán và broadcasting; Ví dụ — Kết luận.
- **Vẽ PowerPoint:** 6 khối bo góc nối bằng mũi tên, đánh số 1–6.
- **Nguồn:** —

### Slide 3 — NumPy là gì?
- **Mục tiêu:** Định nghĩa đúng, ngắn.
- **Ý chính:** **Num**erical **Py**thon; thư viện mã nguồn mở cho tính toán khoa học; cung cấp `ndarray` và kho hàm xử lý mảng; quy ước `import numpy as np`.
- **Code:** `import numpy as np` → `print(np.__version__)` → `2.5.4`.
- **Hình ảnh:** logo NumPy.
- **Vẽ PowerPoint:** ô định nghĩa trung tâm, 3 nhánh: “mảng N chiều”, “hàm toán học”, “nền tảng khoa học”.
- **Nguồn:** [1], [2]

### Slide 4 — NumPy giải quyết vấn đề gì?
- **Mục tiêu:** Cho thấy động cơ sử dụng.
- **Ý chính:** Dữ liệu số lớn; list chứa object và cần vòng lặp Python; NumPy lưu dữ liệu đồng nhất, xử lý bằng code C đã biên dịch; code ngắn, gần ký hiệu toán.
- **Code:** `[1, 2, 3, 4] * 2` vs `np.array([1, 2, 3, 4]) * 2`.
- **Vẽ PowerPoint:** hai làn: “vòng lặp Python” nhiều bước vs “vector hóa” một mũi tên.
- **Nguồn:** [1], [2]

### Slide 5 — `ndarray` — đối tượng trung tâm
- **Mục tiêu:** Nhận diện kiểu dữ liệu cốt lõi.
- **Ý chính:** Mảng N chiều; các phần tử **cùng kiểu**; kích thước **cố định**; dạng lưới chữ nhật, không “răng cưa”; mọi hàm NumPy xoay quanh nó.
- **Vẽ PowerPoint:** lưới 3×4, các ô cùng màu, chú thích “cùng dtype”.
- **Nguồn:** [1], [2]

### Slide 6 — Ưu điểm và giới hạn
- **Mục tiêu:** Cân bằng góc nhìn.
- **Ý chính:** Ưu: vector hóa, ít code, nhiều hàm toán học, nền tảng hệ sinh thái. Giới hạn: dữ liệu phải đồng nhất; không đổi kích thước tại chỗ; không thay thế pandas cho bảng nhiều kiểu; bài toán rất nhỏ có thể không cần.
- **Vẽ PowerPoint:** cân thăng bằng, hai đĩa là hai danh sách.
- **Nguồn:** [1]

### Slide 7 — Ứng dụng thực tế
- **Mục tiêu:** Trả lời “học để làm gì?”.
- **Ý chính:** Khoa học — kỹ thuật; xử lý ảnh; thống kê; học máy; mô phỏng số.
- **Vẽ PowerPoint:** 5 ô icon + nhãn, bố cục 3 trên 2 dưới.
- **Nguồn:** [1]

### Slide 8 — Python list vs NumPy array
- **Mục tiêu:** So sánh bằng bảng và ví dụ gây bất ngờ.
- **Ý chính:** Kiểu dữ liệu; phép `*`; dữ liệu nhiều chiều; hiệu năng.
- **Code:** `[1, 2, 3, 4] * 2` → `[1, 2, 3, 4, 1, 2, 3, 4]`; `np.array([1, 2, 3, 4]) * 2` → `[2 4 6 8]`.
- **Bảng:** Bảng 1.
- **Vẽ PowerPoint:** hai khung code cạnh nhau, mũi tên kết quả đỏ/xanh.
- **Nguồn:** [2], [7]

### Slide 9 — Cấu trúc mảng: 0D, 1D, 2D, nD
- **Mục tiêu:** Hình dung số chiều.
- **Ý chính:** 0D = một giá trị; 1D = dãy; 2D = bảng hàng–cột; 3D = các bảng xếp chồng.
- **Code:** `np.array(7).shape` → `()`; `np.array([1, 2, 3]).shape` → `(3,)`; `np.array([[1, 2, 3], [4, 5, 6]]).shape` → `(2, 3)`; `np.zeros((2, 3, 4)).shape` → `(2, 3, 4)`.
- **Vẽ PowerPoint:** dấu chấm → hàng ô → bảng → 3 bảng xếp chồng.
- **Nguồn:** [2]

### Slide 10 — Bốn thuộc tính quan trọng
- **Mục tiêu:** Đọc “hộ chiếu” của mảng.
- **Ý chính:** `ndim` số chiều; `shape` tuple kích thước; `size` tổng phần tử; `dtype` kiểu dữ liệu.
- **Code:** mảng 2×3 → `2`, `(2, 3)`, `6`, `int64`.
- **Bảng:** Bảng 2.
- **Vẽ PowerPoint:** thẻ “hộ chiếu mảng” 4 dòng.
- **Nguồn:** [2]

### Slide 11 — Tạo mảng (1): `array`, `zeros`, `ones`
- **Mục tiêu:** Ba hàm tạo mảng cơ bản nhất.
- **Ý chính:** `np.array()` từ list; `zeros/ones` nhận shape dạng tuple; mặc định `float64`; có thể chỉ định `dtype`.
- **Code + kết quả:** mục III.C.1–C.2.
- **Vẽ PowerPoint:** ba lưới ô: rỗng, toàn 0, toàn 1.
- **Nguồn:** [2], [5]

### Slide 12 — Tạo mảng (2): `arange`, `linspace`, `eye`
- **Mục tiêu:** Phân biệt dãy theo bước và dãy chia đều.
- **Ý chính:** `arange(start, stop, step)` — không gồm `stop`; `linspace(start, stop, num)` — mặc định gồm điểm cuối; `eye(n)` — ma trận đơn vị.
- **Code + kết quả:** mục III.C.3–C.5.
- **Bảng:** Bảng 3.
- **Vẽ PowerPoint:** trục số với các điểm được đánh dấu.
- **Nguồn:** [2], [5]

### Slide 13 — Indexing và slicing mảng 1D
- **Mục tiêu:** Lấy đúng phần tử và đoạn con.
- **Ý chính:** Chỉ số từ 0; chỉ số âm từ cuối; `start:stop:step`; `stop` bị loại; `[::-1]` đảo ngược.
- **Code:** `c = np.array([0, 10, 20, 30, 40, 50])`; `c[1]` → `10`; `c[-1]` → `50`; `c[1:4]` → `[10 20 30]`; `c[::2]` → `[ 0 20 40]`.
- **Hình ảnh:** `np_indexing.png` của NumPy.
- **Vẽ PowerPoint:** 6 ô, nhãn 0–5 phía trên và -6…-1 phía dưới.
- **Nguồn:** [2]

### Slide 14 — Indexing mảng 2D
- **Mục tiêu:** Phân biệt hàng, cột, khối con.
- **Ý chính:** `a[i, j]` một phần tử; `a[i]` cả hàng; `a[:, j]` cả cột; `a[i1:i2, j1:j2]` khối con.
- **Code:** `b[0, 0]` → `10`; `b[1]` → `[20 21 22 23]`; `b[:, 2]` → `[12 22 32]`; `b[0:2, 1:3]` → `[[11 12] [21 22]]`.
- **Hình ảnh:** `np_matrix_indexing.png`.
- **Vẽ PowerPoint:** bảng 3×4, tô màu hàng/cột được chọn.
- **Nguồn:** [2]

### Slide 15 — Boolean indexing
- **Mục tiêu:** Lọc dữ liệu theo điều kiện.
- **Ý chính:** So sánh tạo mảng boolean cùng shape; dùng làm chỉ số để lấy phần tử `True`; kết quả là mảng 1D; kết hợp bằng `&`, `|` và ngoặc đơn.
- **Code:** `b[b > 21]` → `[22 23 30 31 32 33]`.
- **Vẽ PowerPoint:** lưới gốc → lưới True/False → dãy kết quả.
- **Nguồn:** [2]

### Slide 16 — `reshape()` và `.T`
- **Mục tiêu:** Đổi hình dạng mà không đổi dữ liệu.
- **Ý chính:** Tổng số phần tử phải giữ nguyên; `-1` để tự suy ra một chiều; `.T` hoán vị.
- **Code:** `np.arange(6).reshape(2, 3)`; `.T` → shape `(3, 2)`.
- **Hình ảnh:** `np_reshape.png`.
- **Vẽ PowerPoint:** dãy 6 ô → bảng 2×3 → bảng 3×2 (Morph).
- **Nguồn:** [2]

### Slide 17 — Phép toán theo từng phần tử
- **Mục tiêu:** Thấy NumPy tính theo từng ô.
- **Ý chính:** `+`, `-`, `*`, `/`, `**`, `//`, `%` áp dụng cho từng cặp phần tử; hai mảng cùng shape hoặc broadcast được.
- **Code:** `[1, 2, 3] + [4, 5, 6]` → `[5 7 9]`; `[1, 2, 3] ** 2` → `[1 4 9]`.
- **Vẽ PowerPoint:** hai hàng ô, mũi tên thẳng xuống hàng kết quả.
- **Nguồn:** [2], [4]

### Slide 18 — `*` và `@` khác nhau thế nào?
- **Mục tiêu:** Tránh nhầm lẫn nghiêm trọng.
- **Ý chính:** `*` nhân từng cặp; `@` nhân ma trận theo quy tắc hàng × cột; kết quả khác hoàn toàn.
- **Code:** `A * B` → `[[5 12] [21 32]]`; `A @ B` → `[[19 22] [43 50]]`.
- **Bảng:** Bảng 6.
- **Vẽ PowerPoint:** tô một hàng của `A`, một cột của `B`, nối tới ô kết quả.
- **Nguồn:** [4]

### Slide 19 — Hàm tổng hợp và `axis`
- **Mục tiêu:** Hiểu `axis` bằng hình ảnh.
- **Ý chính:** `np.sum`, `np.mean`, `np.min`, `np.max`; không có `axis` → gộp toàn mảng; `axis=0` → gộp hàng; `axis=1` → gộp cột.
- **Code:** `sum` → `21`; `sum(axis=0)` → `[5 7 9]`; `sum(axis=1)` → `[ 6 15]`; `mean` → `3.5`.
- **Bảng:** Bảng 5.
- **Vẽ PowerPoint:** mũi tên gộp hàng dọc và gộp cột ngang.
- **Nguồn:** [2]

### Slide 20 — Broadcasting: khái niệm và quy tắc
- **Mục tiêu:** Hiểu cơ chế tính giữa shape khác nhau.
- **Ý chính:** “Trải” mảng nhỏ lên mảng lớn mà không sao chép dữ liệu; so sánh từ phải sang trái; bằng nhau hoặc một bên bằng 1; chiều thiếu coi là 1.
- **Vẽ PowerPoint:** hai dãy ô shape đặt lệch phải để thấy phép so sánh từng cặp.
- **Nguồn:** [3]

### Slide 21 — Broadcasting: thành công và thất bại
- **Mục tiêu:** Áp dụng quy tắc vào ví dụ cụ thể.
- **Ý chính:** `(2, 3) + (3,)` hợp lệ; `(2, 3) + (2, 1)` hợp lệ; `(2, 3) + (2,)` lỗi `ValueError`.
- **Code + kết quả:** mục III.F.3–F.4.
- **Hình ảnh:** `broadcasting_2.png`, `broadcasting_3.png`.
- **Vẽ PowerPoint:** ô `(3,)` trượt xuống từng hàng; dấu X đỏ cho trường hợp lỗi.
- **Nguồn:** [3]

### Slide 22 — Ví dụ 1: thống kê điểm
- **Mục tiêu:** Vận dụng hàm thống kê.
- **Ý chính:** Trung bình, cao nhất, thấp nhất, độ lệch chuẩn; đếm điểm đạt ngưỡng; cộng điểm thưởng.
- **Code + kết quả:** mục III.G.1.
- **Vẽ PowerPoint:** biểu đồ cột 5 điểm, đường trung bình.
- **Nguồn:** [2]

### Slide 23 — Ví dụ 2: chuẩn hóa và vector hóa
- **Mục tiêu:** Thấy sức mạnh biểu diễn của phép toán mảng.
- **Ý chính:** Chuẩn hóa z-score bằng một biểu thức; kết quả trung bình 0, độ lệch chuẩn 1; thay vòng lặp bằng phép nhân mảng; lọc theo điều kiện.
- **Code + kết quả:** mục III.G.2 và III.G.4.
- **Vẽ PowerPoint:** hai trục số trước/sau chuẩn hóa.
- **Nguồn:** [2]

### Slide 24 — Kết luận và hướng tìm hiểu tiếp
- **Mục tiêu:** Chốt kiến thức, mở đường.
- **Ý chính:** NumPy = `ndarray` + vector hóa + broadcasting; dùng khi dữ liệu số đồng nhất, kích thước lớn; không thay thế pandas cho bảng nhiều kiểu; học tiếp Matplotlib, pandas, `numpy.linalg`.
- **Vẽ PowerPoint:** bản đồ 3 nhánh “Trực quan hóa — Dữ liệu bảng — Đại số tuyến tính”.
- **Nguồn:** [1], [6]

---

# PHẦN III — NỘI DUNG KIẾN THỨC CHI TIẾT

## A. Giới thiệu NumPy

### A.1. NumPy là gì?

NumPy (**Num**erical **Py**thon) là thư viện mã nguồn mở cho tính toán khoa học trong Python. Tài liệu chính thức gọi đây là “gói nền tảng”, cung cấp đối tượng mảng đa chiều cùng nhiều hàm toán học, logic, biến đổi hình dạng, sắp xếp, nhập/xuất, đại số tuyến tính và thống kê [1].

Cốt lõi là `ndarray` — mảng N chiều chứa các phần tử **cùng kiểu dữ liệu**, với nhiều phép toán được thực hiện trong code đã biên dịch [1]. Quy ước nhập thư viện:

```python
import numpy as np
```

### A.2. NumPy giải quyết vấn đề gì?

Vấn đề thứ nhất là **biểu diễn dữ liệu số nhiều chiều**. List Python chứa các đối tượng rời rạc, có thể khác kiểu; NumPy lưu một khối dữ liệu đồng nhất, kích thước cố định, thường liền mạch trong bộ nhớ. Nhờ đó phép toán chạy bằng vòng lặp C thay vì vòng lặp Python [1].

Vấn đề thứ hai là **độ ngắn gọn**. Thay vì lặp từng cặp phần tử, ta viết một biểu thức:

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(a + b)
```

Kết quả:

```text
[11 22 33 44]
```

Vấn đề thứ ba là **tính toán trên toàn mảng**: `np.sum()`, `np.mean()`, `np.min()`, `np.max()` cho phép thống kê mà không cần tự viết vòng lặp.

### A.3. Vai trò của `ndarray`

`ndarray` là kiểu trung tâm: hàm tạo mảng, hàm toán học, hàm thống kê, phép cắt đều nhận hoặc trả về `ndarray` (hoặc scalar khi kết quả chỉ còn một giá trị). Hiểu `ndarray` là hiểu cách NumPy “nghĩ”: dữ liệu là lưới nhiều chiều, mỗi chiều có kích thước xác định, phép toán áp dụng trên lưới đó.

### A.4. Ưu điểm

- **Vector hóa:** viết phép toán trên cả mảng, không cần vòng lặp hiển ngôn [1].
- **Broadcasting:** tính giữa các mảng khác shape mà không sao chép thủ công [3].
- **Kho hàm phong phú:** toán học, thống kê, đại số tuyến tính, sắp xếp, tìm kiếm, nhập/xuất.
- **Nền tảng hệ sinh thái:** nhiều thư viện khoa học nhận và trả về mảng NumPy [1].
- **Cú pháp gần toán học:** biểu thức mảng đọc như công thức.

### A.5. Giới hạn

- **Đồng nhất kiểu:** dữ liệu bảng có cột chữ, số, ngày tháng không phù hợp trực tiếp; pandas hợp hơn.
- **Kích thước cố định:** thêm/bớt phần tử tạo mảng mới [1].
- **Không có nhãn:** không gắn tên cột, tên hàng.
- **Không phải lúc nào cũng nhanh hơn:** với mảng rất nhỏ, chi phí gọi hàm có thể lớn hơn lợi ích.

Đây là **nhận định tổng quát** dựa trên đặc điểm được mô tả trong [1], không phải kết quả đo.

### A.6. Ứng dụng

NumPy được dùng rộng rãi trong khoa học và kỹ thuật [1]: tính toán khoa học và mô phỏng; xử lý ảnh (ma trận điểm ảnh); thống kê, phân tích dữ liệu; học máy (đặc trưng, trọng số); mô phỏng số trên lưới.

### A.7. So sánh Python list và NumPy array

**Bảng 1 — Python list và NumPy array**

| Tiêu chí | Python list | NumPy array (`ndarray`) |
|---|---|---|
| Kiểu dữ liệu | Hỗn hợp | Đồng nhất, một `dtype` |
| Phép `* 2` | Lặp danh sách | Nhân từng phần tử |
| Nhiều chiều | List lồng nhau, có thể “răng cưa” | Mảng N chiều, kích thước xác định |
| Bộ nhớ | Các object Python rời rạc | Khối dữ liệu đồng nhất, thường liền mạch |
| Hiệu năng | Vòng lặp Python | Vector hóa trong code C đã biên dịch |
| Kích thước | Linh hoạt | Cố định sau khi tạo |

Ví dụ then chốt:

```python
print([1, 2, 3, 4] * 2)
print(np.array([1, 2, 3, 4]) * 2)
```

Kết quả:

```text
[1, 2, 3, 4, 1, 2, 3, 4]
[2 4 6 8]
```

Với list, `*` là **lặp danh sách**; với `ndarray`, `*` là **nhân từng phần tử**.

## B. Cấu trúc mảng NumPy

### B.1. `ndarray`

`ndarray` là mảng N chiều, đồng nhất kiểu, kích thước cố định. Có thể hình dung như lưới: mỗi ô một giá trị, các ô sắp theo trục. Với 2 chiều, trục 0 là hàng, trục 1 là cột; với 3 chiều, thêm trục “độ sâu” như nhiều bảng xếp chồng [2]. Mảng phải “chữ nhật”: mọi hàng cùng số cột.

### B.2. 0 chiều, 1 chiều, 2 chiều, nhiều chiều

- **0-D:** một giá trị, shape `()`.
- **1-D:** một dãy, shape `(n,)`.
- **2-D:** một bảng, shape `(hàng, cột)`.
- **3-D:** chồng bảng, shape `(số_bảng, hàng, cột)`.

```python
import numpy as np

print(np.array(7).shape)
print(np.array([1, 2, 3]).shape)
print(np.array([[1, 2, 3], [4, 5, 6]]).shape)
print(np.zeros((2, 3, 4)).shape)
```

Kết quả:

```text
()
(3,)
(2, 3)
(2, 3, 4)
```

Cú pháp `(3,)` cần dấu phẩy để Python hiểu là tuple một phần tử.

### B.3. `shape`, `ndim`, `size`, `dtype`

**Bảng 2 — Bốn thuộc tính cơ bản**

| Thuộc tính | Ý nghĩa | Ví dụ với mảng 2×3 |
|---|---|---|
| `ndim` | Số chiều | `2` |
| `shape` | Tuple kích thước từng chiều | `(2, 3)` |
| `size` | Tổng số phần tử | `6` |
| `dtype` | Kiểu dữ liệu | `dtype('int64')` |

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
```

Kết quả:

```text
2
(2, 3)
6
int64
```

### B.4. Quan hệ giữa số chiều, hình dạng và số phần tử

`ndim` bằng số phần tử của `shape`; `size` bằng tích các số trong `shape`. Với `(2, 3)`: `ndim = 2`, `size = 6`. Với `(2, 3, 4)`: `ndim = 3`, `size = 24`.

```python
t = np.zeros((2, 3, 4))
print(t.ndim, t.shape, t.size)
```

Kết quả:

```text
3 (2, 3, 4) 24
```

### B.5. Vì sao phải hiểu cấu trúc trước khi tính toán?

Mọi phép toán dựa trên shape. Hai mảng cùng shape cộng trực tiếp; khác shape chỉ tính được nếu broadcasting cho phép. Hàm tổng hợp cần `axis` để biết gộp chiều nào. `reshape()` chỉ thành công khi tổng số phần tử không đổi. Không đọc được `shape` sẽ dẫn tới `ValueError` hoặc kết quả sai khó hiểu.

## C. Tạo mảng

### C.1. `np.array()`

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a)
print(b)
```

Kết quả:

```text
[1 2 3]
[[1 2 3]
 [4 5 6]]
```

NumPy tự suy ra `dtype`. Trộn số nguyên và số thực cho kết quả thực:

```python
print(np.array([1, 2.5, 3]).dtype)
```

```text
float64
```

### C.2. `np.zeros()` và `np.ones()`

```python
print(np.zeros((2, 3)))
print(np.ones(4))
```

Kết quả:

```text
[[0. 0. 0.]
 [0. 0. 0.]]
[1. 1. 1. 1.]
```

Mặc định là `float64`. Muốn số nguyên, chỉ định `dtype`:

```python
print(np.ones(3, dtype=np.int64))
```

```text
[1 1 1]
```

### C.3. `np.arange()`

Tạo dãy theo bước; **`stop` không được bao gồm**.

```python
print(np.arange(0, 10, 2))
print(np.arange(4))
```

```text
[0 2 4 6 8]
[0 1 2 3]
```

### C.4. `np.linspace()`

Tạo `num` điểm chia đều; mặc định **bao gồm** điểm cuối.

```python
print(np.linspace(0, 1, 5))
```

```text
[0.   0.25 0.5  0.75 1.  ]
```

### C.5. `np.eye()`

```python
print(np.eye(3))
```

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

**Bảng 3 — Chọn hàm tạo mảng**

| Hàm | Dùng khi | Điểm cần nhớ |
|---|---|---|
| `np.array(seq)` | Có sẵn dữ liệu trong list/tuple | Tự suy ra `dtype` |
| `np.zeros(shape)` | Cần mảng toàn 0 | Mặc định `float64` |
| `np.ones(shape)` | Cần mảng toàn 1 | Mặc định `float64` |
| `np.arange(start, stop, step)` | Dãy theo bước | Không gồm `stop` |
| `np.linspace(start, stop, num)` | `num` điểm chia đều | Mặc định gồm `stop` |
| `np.eye(n)` | Ma trận đơn vị | Đường chéo chính bằng 1 |

## D. Truy cập và biến đổi dữ liệu

### D.1. Indexing

Chỉ số bắt đầu từ 0; chỉ số âm tính từ cuối.

```python
import numpy as np

c = np.array([0, 10, 20, 30, 40, 50])
print(c[0])
print(c[3])
print(c[-1])
```

```text
0
30
50
```

### D.2. Slicing

Cú pháp `start:stop:step`; `stop` **không** được lấy.

```python
print(c[1:4])
print(c[:3])
print(c[::2])
print(c[::-1])
```

```text
[10 20 30]
[ 0 10 20]
[ 0 20 40]
[50 40 30 20 10  0]
```

Slicing trả về **view**, không phải bản sao: sửa view sẽ sửa mảng gốc; muốn độc lập phải dùng `.copy()` [2].

### D.3. Phần tử, hàng, cột trong mảng 2D

Dùng một cặp ngoặc vuông với dấu phẩy tách chỉ số theo trục: `a[hàng, cột]`.

```python
b = np.array([[10, 11, 12, 13],
              [20, 21, 22, 23],
              [30, 31, 32, 33]])
print(b[0, 0])
print(b[1])
print(b[:, 2])
print(b[0:2, 1:3])
```

```text
10
[20 21 22 23]
[12 22 32]
[[11 12]
 [21 22]]
```

`b[1]` lấy cả hàng 1; `b[:, 2]` lấy cả cột 2; `b[0:2, 1:3]` lấy khối 2×2.

### D.4. Boolean indexing

```python
print(b[b > 21])
print(b > 21)
```

```text
[22 23 30 31 32 33]
[[False False False False]
 [False False  True  True]
 [ True  True  True  True]]
```

Kết quả là mảng **1 chiều** vì các phần tử `True` được nén lại. Kết hợp điều kiện bằng `&`, `|` và ngoặc đơn: `b[(b > 10) & (b < 30)]`.

### D.5. `reshape()`

Đổi hình dạng, giữ nguyên dữ liệu và thứ tự đọc; tổng số phần tử phải bằng nhau.

```python
r = np.arange(6).reshape(2, 3)
print(r)
print(r.shape)
```

```text
[[0 1 2]
 [3 4 5]]
(2, 3)
```

Dùng `-1` để tự suy ra một chiều:

```python
print(np.arange(12).reshape(3, -1).shape)
```

```text
(3, 4)
```

### D.6. Transpose bằng `.T`

```python
print(r.T)
print(r.T.shape)
```

```text
[[0 3]
 [1 4]
 [2 5]]
(3, 2)
```

`.T` hoán vị: hàng thành cột, cột thành hàng.

## E. Phép toán trên mảng

### E.1. Theo từng phần tử

`+`, `-`, `*`, `/`, `**`, `//`, `%` áp dụng cho từng cặp phần tử; kết quả cùng shape (sau broadcasting).

```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** 2)
print(x // 2)
print(x % 2)
```

```text
[5 7 9]
[-3 -3 -3]
[ 4 10 18]
[0.25 0.4  0.5 ]
[1 4 9]
[0 1 1]
[1 0 1]
```

`/` luôn trả về số thực; `//` là chia lấy phần nguyên.

### E.2. Giữa hai mảng

Hai mảng cùng shape tính trực tiếp. Khác shape chỉ tính được nếu broadcasting tương thích (Phần F); nếu không, NumPy báo `ValueError`.

### E.3. `*` và `@`

- `A * B`: nhân **từng phần tử** — `A[i, j] * B[i, j]`.
- `A @ B`: nhân **ma trận** — phần tử `(i, j)` bằng tổng `A[i, k] * B[k, j]` trên mọi `k`.

```python
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
print(A * B)
print(A @ B)
```

```text
[[ 5 12]
 [21 32]]
[[19 22]
 [43 50]]
```

Kiểm tra: phần tử `(0, 0)` của `A @ B` là `1×5 + 2×7 = 19`; của `A * B` là `1×5 = 5`.

**Bảng 6 — So sánh `*` và `@`**

| Toán tử | Ý nghĩa | Điều kiện shape | Ví dụ |
|---|---|---|---|
| `*` | Nhân từng phần tử | Cùng shape hoặc broadcast được | `[[1,2],[3,4]] * [[5,6],[7,8]]` → `[[5,12],[21,32]]` |
| `@` | Nhân ma trận | Số cột `A` bằng số hàng `B` | `[[1,2],[3,4]] @ [[5,6],[7,8]]` → `[[19,22],[43,50]]` |

### E.4. Hàm tổng hợp

`np.sum()`, `np.mean()`, `np.min()`, `np.max()`, `np.std()`, `np.prod()`; gọi dạng hàm hoặc phương thức (`a.sum()`).

```python
m = np.array([[1, 2, 3],
              [4, 5, 6]])
print(np.sum(m))
print(np.mean(m))
print(np.min(m))
print(np.max(m))
```

```text
21
3.5
1
6
```

### E.5. Ý nghĩa của `axis`

`axis` là **chiều bị gộp**:

- `axis=0`: gộp các hàng → kết quả theo cột.
- `axis=1`: gộp các cột → kết quả theo hàng.
- Không truyền: gộp toàn mảng.

```python
print(np.sum(m, axis=0))
print(np.sum(m, axis=1))
print(np.mean(m, axis=0))
print(np.mean(m, axis=1))
```

```text
[5 7 9]
[ 6 15]
[2.5 3.5 4.5]
[2. 5.]
```

**Bảng 5 — `axis` với mảng 2×3**

| Cách gọi | Chiều bị gộp | Shape kết quả | Kết quả |
|---|---|---|---|
| `m.sum()` | Toàn bộ | `()` | `21` |
| `m.sum(axis=0)` | Hàng (trục 0) | `(3,)` | `[5 7 9]` |
| `m.sum(axis=1)` | Cột (trục 1) | `(2,)` | `[ 6 15]` |

## F. Broadcasting

### F.1. Khái niệm

Broadcasting cho phép tính toán trên các mảng **shape khác nhau**: mảng nhỏ được “trải” lên mảng lớn để hai bên tương thích. Cơ chế này vector hóa phép toán (vòng lặp chạy trong C) mà **không tạo bản sao dữ liệu không cần thiết** [3].

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
print(a * 2.0)
```

```text
[2. 4. 6.]
```

Scalar `2.0` được coi như mảng cùng shape, nhưng NumPy không thực sự sao chép ra ba ô [3].

### F.2. Quy tắc

So sánh shape **từ phải sang trái**. Hai chiều tương thích nếu:

1. **bằng nhau**, hoặc
2. **một trong hai bằng 1**.

Mảng ít chiều hơn được coi như có các chiều thiếu bằng **1** ở bên trái. Shape kết quả là shape lớn nhất theo từng chiều [3].

Ví dụ `(2, 3)` với `(3,)`: chiều cuối `3 = 3`; chiều trước `2` với `1` (thiếu) → hợp lệ; kết quả `(2, 3)`.

Nếu không thỏa: `ValueError: operands could not be broadcast together with shapes ...`.

### F.3. Ví dụ thành công

**2D + 1D:**

```python
p = np.array([[1, 2, 3],
              [4, 5, 6]])
q = np.array([10, 20, 30])
print(p + q)
```

```text
[[11 22 33]
 [14 25 36]]
```

`q` shape `(3,)` được coi là `(1, 3)` rồi trải xuống hai hàng: hàng 0 cộng `[10, 20, 30]`, hàng 1 cộng cùng dãy.

**2D + cột:**

```python
col = np.array([[10],
                [20]])
print(p + col)
```

```text
[[11 12 13]
 [24 25 26]]
```

`col` shape `(2, 1)`; chiều cột bằng 1 nên trải sang ba cột: hàng 0 cộng 10, hàng 1 cộng 20.

**2D + scalar:**

```python
print(p * 2)
```

```text
[[ 2  4  6]
 [ 8 10 12]]
```

### F.4. Ví dụ thất bại

```python
try:
    print(p + np.array([10, 20]))
except ValueError as e:
    print(type(e).__name__, e)
```

```text
ValueError operands could not be broadcast together with shapes (2,3) (2,)
```

Chiều cuối là `3` và `2`: không bằng nhau, không bên nào bằng 1 → thất bại ngay.

```python
try:
    print(np.ones((2, 3)) + np.ones((3, 2)))
except ValueError as e:
    print(type(e).__name__, e)
```

```text
ValueError operands could not be broadcast together with shapes (2,3) (3,2)
```

### F.5. Lưu ý bộ nhớ

Broadcasting thường tiết kiệm bộ nhớ, nhưng shape kết quả có thể lớn hơn nhiều so với đầu vào; khi đó mảng trung gian lớn làm chậm chương trình. Tài liệu chính thức cũng lưu ý có trường hợp broadcasting dùng bộ nhớ kém hiệu quả [3]. Với dữ liệu lớn, cân nhắc vòng lặp ngoài hoặc chia nhỏ bài toán.

## G. Ví dụ thực hành

### G.1. Thống kê điểm

**Bài toán:** 5 bài kiểm tra với điểm `8.0, 7.5, 9.0, 6.5, 8.5`. Tính trung bình, cao nhất, thấp nhất, độ lệch chuẩn; đếm số bài đạt từ 8.0; cộng 0.5 điểm thưởng.

```python
import numpy as np

d = np.array([8.0, 7.5, 9.0, 6.5, 8.5])
print("Diem TB:", np.mean(d))
print("Cao nhat:", np.max(d))
print("Thap nhat:", np.min(d))
print("Do lech chuan:", np.std(d))
print("So bai >= 8:", np.sum(d >= 8.0), "/", d.size)
print("Sau thuong:", d + 0.5)
```

```text
Diem TB: 7.9
Cao nhat: 9.0
Thap nhat: 6.5
Do lech chuan: 0.8602325267042626
So bai >= 8: 3 / 5
Sau thuong: [8.5 8.  9.5 7.  9. ]
```

`d >= 8.0` tạo mảng boolean; `np.sum` cộng các `True` để đếm. `d + 0.5` cộng 0.5 vào từng phần tử nhờ broadcasting. Toàn bộ báo cáo thống kê của một lớp có thể tính trong vài dòng.

### G.2. Chuẩn hóa z-score

**Bài toán:** Chuẩn hóa `[2.0, 4.0, 6.0, 8.0]` để kết quả có trung bình 0, độ lệch chuẩn 1.

```python
import numpy as np

x = np.array([2.0, 4.0, 6.0, 8.0])
z = (x - np.mean(x)) / np.std(x)
print(z)
print("mean:", np.mean(z), "std:", np.std(z))
```

```text
[-1.34164079 -0.4472136   0.4472136   1.34164079]
mean: 0.0 std: 1.0
```

`np.mean(x) = 5.0`, `np.std(x) ≈ 2.236`. Biểu thức thực hiện hai lần broadcasting với scalar: trừ 5.0 rồi chia 2.236. Chuẩn hóa là bước bắt buộc trước nhiều thuật toán học máy để các đặc trưng khác đơn vị không lấn át nhau.

### G.3. Dữ liệu dạng ma trận

**Bài toán:** Điểm 3 sinh viên × 4 môn. Tính tổng từng sinh viên và trung bình từng môn.

```python
import numpy as np

scores = np.array([[8, 7, 9, 8],
                   [6, 9, 7, 8],
                   [9, 8, 8, 10]])
print("Tong tung SV:", scores.sum(axis=1))
print("TB tung mon:", scores.mean(axis=0))
print("TB toan bo:", scores.mean())
```

```text
Tong tung SV: [32 30 35]
TB tung mon: [7.66666667 8.         8.         8.66666667]
TB toan bo: 8.083333333333334
```

`axis=1` gộp các cột trong mỗi hàng → tổng từng sinh viên. `axis=0` gộp các hàng trong mỗi cột → trung bình từng môn. Không truyền `axis` → gộp toàn bộ 12 điểm. Đây là mẫu xử lý của bảng điểm, dữ liệu cảm biến, hoặc ma trận “đối tượng × thuộc tính”.

### G.4. Thay vòng lặp bằng phép toán mảng

**Bài toán:** Giá `[100, 250, 80, 320]` (nghìn đồng). Tăng 10% và lọc các mặt hàng sau tăng vẫn trên 200.

```python
import numpy as np

prices = np.array([100, 250, 80, 320])
new_prices = prices * 1.1
print(new_prices)
print(prices > 200)
print(prices[prices > 200])
```

```text
[110. 275.  88. 352.]
[False  True False  True]
[250 320]
```

`prices * 1.1` áp dụng cho từng phần tử; so sánh tạo mảng boolean; boolean indexing lấy phần tử thỏa điều kiện. Viết bằng list sẽ cần vòng lặp và danh sách kết quả mới.

## H. Kết luận và hướng tìm hiểu tiếp

### H.1. Tóm tắt

NumPy là thư viện nền tảng cho tính toán số trong Python. Trung tâm là `ndarray`: mảng N chiều, đồng nhất kiểu, kích thước cố định. Bốn thuộc tính `ndim`, `shape`, `size`, `dtype` mô tả đầy đủ hình dạng dữ liệu. NumPy cung cấp hàm tạo mảng, indexing/slicing, boolean indexing, `reshape`, `.T`, phép toán từng phần tử, nhân ma trận `@`, hàm tổng hợp theo `axis`, và broadcasting.

Ba ý cần nhớ:

1. **Shape quyết định mọi thứ** — đọc `shape` trước khi viết phép toán.
2. **`*` khác `@`** — nhân từng phần tử khác nhân ma trận.
3. **Broadcasting so sánh từ phải sang trái**, với điều kiện bằng nhau hoặc một bên bằng 1.

### H.2. Khi nào nên dùng NumPy?

Khi dữ liệu là số, đồng nhất kiểu, kích thước lớn và cần tính toán hàng loạt: thống kê, biến đổi, đại số tuyến tính, xử lý ảnh, tiền xử lý học máy. Cũng nên dùng khi làm việc với thư viện khoa học khác vì chúng thường nhận và trả về mảng NumPy [1].

### H.3. Khi nào không phải lựa chọn duy nhất?

- **Bảng nhiều kiểu, có nhãn:** pandas phù hợp hơn.
- **Dữ liệu hỗn hợp, kích thước nhỏ:** list Python đủ dùng.
- **GPU hoặc đạo hàm tự động:** PyTorch phù hợp hơn.
- **Xử lý văn bản phức tạp:** công cụ NLP chuyên dụng phù hợp hơn.

Đây là **nhận định tổng quát** về ranh giới công cụ, không phải tuyên bố NumPy “không làm được”.

### H.4. Hướng tìm hiểu tiếp

- **Matplotlib:** trực quan hóa mảng — đường, cột, phân tán.
- **pandas:** dữ liệu bảng có nhãn.
- **`numpy.linalg`:** định thức, nghịch đảo, trị riêng, giải hệ phương trình.
- **Broadcasting nâng cao:** `np.newaxis`, `np.expand_dims`.
- **Đọc/ghi dữ liệu:** `np.loadtxt`, `np.savetxt`, `np.save`, `np.load`.

## I. Tài liệu tham khảo

1. [1] NumPy Developers. *What is NumPy?* NumPy v2.5 Manual. https://numpy.org/doc/stable/user/whatisnumpy.html
2. [2] NumPy Developers. *NumPy: the absolute basics for beginners.* NumPy v2.5 Manual. https://numpy.org/doc/stable/user/absolute_beginners.html
3. [3] NumPy Developers. *Broadcasting.* NumPy v2.5 Manual. https://numpy.org/doc/stable/user/basics.broadcasting.html
4. [4] NumPy Developers. *NumPy quickstart.* NumPy v2.5 Manual. https://numpy.org/doc/stable/user/quickstart.html
5. [5] NumPy Developers. *Array creation routines.* NumPy v2.5 Reference. https://numpy.org/doc/stable/reference/routines.array-creation.html
6. [6] NumPy Developers. *Linear algebra (`numpy.linalg`).* NumPy v2.5 Reference. https://numpy.org/doc/stable/reference/routines.linalg.html
7. [7] Python Software Foundation. *Data Structures — Python Tutorial.* https://docs.python.org/3/tutorial/datastructures.html

---

# PHẦN IV — TÀI NGUYÊN THIẾT KẾ

## 1. Hình ảnh bên ngoài

Các URL dưới đây là đường dẫn ảnh **có thật** trong tài liệu chính thức của NumPy, đối chiếu ngày 23/10/2026. Tài liệu **không khẳng định** đã tải hoặc kiểm tra nội dung hiển thị; người thiết kế cần mở URL và ghi nguồn.

| Mục đích | URL | Slide |
|---|---|---|
| Logo NumPy | https://numpy.org/doc/stable/_static/numpylogo.svg | 1, 3 |
| Indexing 1D | https://numpy.org/doc/stable/_images/np_indexing.png | 13 |
| Indexing ma trận | https://numpy.org/doc/stable/_images/np_matrix_indexing.png | 14 |
| Nhân với scalar | https://numpy.org/doc/stable/_images/np_multiply_broadcasting.png | 20 |
| Broadcasting 2D + 1D | https://numpy.org/doc/stable/_images/broadcasting_2.png | 21 |
| Broadcasting thất bại | https://numpy.org/doc/stable/_images/broadcasting_3.png | 21 |
| Hàm tổng hợp | https://numpy.org/doc/stable/_images/np_aggregation.png | 19 |
| Tổng hợp theo hàng | https://numpy.org/doc/stable/_images/np_matrix_aggregation_row.png | 19 |
| Reshape | https://numpy.org/doc/stable/_images/np_reshape.png | 16 |
| Transpose | https://numpy.org/doc/stable/_images/np_transposing_reshaping.png | 16 |

**Bản quyền:** tài liệu NumPy dùng giấy phép BSD; nên ghi “Nguồn: NumPy Documentation” và giữ liên kết gốc.

## 2. Sơ đồ dựng bằng PowerPoint

### Sơ đồ 1 — “Hộ chiếu mảng” (slide 10)

Hình chữ nhật bo góc lớn, tiêu đề `ndarray`; bốn dòng “thuộc tính — giá trị”: `ndim — 2`, `shape — (2, 3)`, `size — 6`, `dtype — int64`. Dùng **Shapes → Rectangle**, **Text Box**, **Line**.

### Sơ đồ 2 — Lưới chỉ số (slide 13, 14)

Sáu ô vuông liền nhau cho mảng 1D; nhãn 0–5 phía trên, -6…-1 phía dưới. Với 2D: lưới 3×4, nhãn hàng bên trái, nhãn cột phía trên. Tô màu vùng đang giải thích bằng **Shape Fill** bán trong suốt.

### Sơ đồ 3 — Broadcasting (slide 20, 21)

Hai dãy ô `(2, 3)` và `(3,)` đặt lệch phải để thấy phép so sánh từng cặp. Dùng **Down Arrow** từ `(3,)` xuống từng hàng. Trường hợp lỗi: dấu **X** đỏ lớn từ hai **Line** chéo.

### Sơ đồ 4 — Axis (slide 19)

Bảng 2×3; mũi tên dọc gộp hàng ghi `axis=0`; mũi tên ngang gộp cột ghi `axis=1`; kết quả đặt bên cạnh, cùng màu mũi tên.

### Sơ đồ 5 — `*` và `@` (slide 18)

Hai bảng 2×2. Với `@`: tô một hàng của `A` và một cột của `B` cùng màu, nối tới ô kết quả. Với `*`: nối từng cặp ô cùng vị trí bằng mũi tên ngắn.

## 3. Bảng nên có

Bảng 1 (list/array), Bảng 2 (thuộc tính), Bảng 3 (hàm tạo mảng), Bảng 5 (`axis`), Bảng 6 (`*`/`@`). Không đưa quá 2 bảng lên một slide; bảng 4–5 dòng nên dùng cỡ chữ 18–20 pt.

## 4. Nguyên tắc trực quan

- Ưu tiên **lưới ô** cho mảng; màu chỉ để đánh dấu vùng đang nói.
- Mỗi slide một khái niệm mới.
- Code trên slide 4–8 dòng; giải thích dài để lời thuyết trình.
- Kết quả đặt cạnh code, font monospace, nền tối nhạt.
- Luôn vẽ **shape** cạnh mảng khi giảng broadcasting.

---

# PHẦN V — ĐỀ XUẤT ANIMATION VÀ MORPH

Chỉ nên dùng 6–8 hiệu ứng trong toàn bài; animation phục vụ giải thích tiến trình, không trang trí.

### 1. Slide 13 — Indexing 1D
- **Đối tượng:** 6 ô và nhãn chỉ số.
- **Hiệu ứng:** `Appear` từng ô; sau đó `Pulse` ô `c[1]`, rồi `c[-1]`.
- **Mục đích:** Thấy chỉ số gắn với đúng ô, đặc biệt chỉ số âm.

### 2. Slide 14 — Indexing 2D
- **Đối tượng:** lưới 3×4 và hình chữ nhật tô màu.
- **Hiệu ứng:** `Wipe` trái sang cho hàng; `Wipe` trên xuống cho cột; `Appear` khối 2×2 kết quả.
- **Mục đích:** Phân biệt “một hàng”, “một cột”, “một khối con”.

### 3. Slide 15 — Boolean indexing
- **Đối tượng:** lưới gốc, lưới `True/False`, dãy kết quả.
- **Hiệu ứng:** `Appear` lưới gốc → `Fade` lưới boolean → `Fly In` dãy kết quả.
- **Mục đích:** Thấy bước trung gian “mặt nạ” trước khi lọc.

### 4. Slide 16 — Reshape và transpose (Morph)
- **16a:** dãy 6 ô ngang.
- **16b (Morph):** các ô di chuyển thành bảng 2×3.
- **16c (Morph):** bảng 2×3 xoay thành 3×2.
- **Mục đích:** “Cùng dữ liệu, khác hình dạng”; Morph giữ nguyên đối tượng nên theo dõi được từng ô.

### 5. Slide 18 — `*` và `@`
- **Đối tượng:** hai bảng `A`, `B`, bảng kết quả.
- **Hiệu ứng:** với `@`, `Appear` từng số hạng `1×5`, `2×7`; rồi `Pulse` ô `19`.
- **Mục đích:** Giải thích “hàng nhân cột” bằng hành động.

### 6. Slide 19 — Axis
- **Đối tượng:** bảng 2×3 và hai mũi tên gộp.
- **Hiệu ứng:** `Wipe` mũi tên dọc → `Appear` `[5 7 9]`; `Wipe` mũi tên ngang → `Appear` `[6 15]`.
- **Mục đích:** Thấy chiều nào bị “ép” lại.

### 7. Slide 20–21 — Broadcasting (Morph)
- **20a:** hai dãy shape lệch phải.
- **20b (Morph):** dãy `(3,)` trượt xuống, giãn thành `(2, 3)`.
- **21:** từ trạng thái đã giãn, `Appear` kết quả từng hàng.
- **Mục đích:** Cụ thể hóa quy tắc “chiều bằng 1 được trải”.

### 8. Slide 22–23 — Ví dụ
- **Đối tượng:** code và output.
- **Hiệu ứng:** `Appear` từng dòng code; sau đó `Fade` output.
- **Mục đích:** Mô phỏng quá trình viết và chạy code.

### Lưu ý Morph

- Morph cần hai slide có **cùng đối tượng** hoặc hình dạng tương đồng.
- Đặt tên đối tượng trong **Selection Pane** (Home → Select → Selection Pane).
- Thời lượng 0.75–1.5 giây; tránh quá chậm.
- Không dùng Morph cho slide không liên quan bố cục.

---

# PHẦN VI — DANH SÁCH KIỂM TRA CHẤT LƯỢNG

| Tiêu chí | Trạng thái | Ghi chú |
|---|---|---|
| Đúng chủ đề NumPy | Đạt | Toàn bộ xoay quanh NumPy và `ndarray`. |
| Đủ phạm vi A–I | Đạt | A–I đầy đủ. |
| 20–25 slide | Đạt | 24 slide. |
| Mỗi slide một thông điệp | Đạt | Đã tách indexing 1D/2D, `*`/`@`, broadcasting quy tắc/ví dụ. |
| Code chạy được | Đạt | Python 3.14 + NumPy 2.5.4. |
| Output chính xác | Đạt | Output thật của lần chạy kiểm chứng. |
| Có bảng | Đạt | 5 bảng. |
| Có hình ảnh ngoài | Đạt | 10 URL ảnh chính thức (IV.1). |
| Có hình vẽ PowerPoint | Đạt | 5 sơ đồ Shapes/Line/Arrow/Text Box (IV.2). |
| Có animation/Morph | Đạt | 8 đề xuất (Phần V). |
| Nguồn xác thực | Đạt | 7 nguồn, ưu tiên tài liệu chính thức. |
| Không bịa benchmark | Đạt | Không có số liệu tốc độ tự tạo. |
| Không trùng lặp quá mức | Đạt | 4 ví dụ nhắm 4 kỹ năng khác nhau. |
| Độ sâu nhập môn | Đạt | Không đi vào bộ nhớ, strides, C-API. |
| Độ dài 2.000–3.000 từ | Đạt | Phần kiến thức I + III khoảng 2.500 từ, không tính code, bảng, tham khảo; Phần II là bản đồ biên tập. |

## Ghi chú cho người biên tập

- Đoạn **“Diễn giải”**, **“Cách hoạt động”** dùng cho lời thuyết trình, không đưa nguyên văn lên slide.
- Đoạn **“Ý nghĩa thực tế”** rút thành 1 bullet.
- Giữ nguyên tên hàm, cú pháp tiếng Anh; chỉ dịch phần giải thích.
- Muốn còn 20 slide: gộp slide 6–7, 22–23, 24 với tài liệu tham khảo.
- Muốn lên 25 slide: tách slide 20 thành “quy tắc” và “ví dụ shape”, hoặc tách slide 18.
