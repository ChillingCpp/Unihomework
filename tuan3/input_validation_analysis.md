# Phân tích Input Validation - Tất cả bài tập

## Practice 3.1 - Calculator

| Trường hợp | Ví dụ | Cách xử lý | Trạng thái |
|------------|-------|------------|------------|
| Nhập không phải số nguyên cho a | `abc` | `std::cin >> a` thất bại → clear + nhập lại | ✅ Đã xử lý |
| Nhập không phải số nguyên cho b | `abc` | `std::cin >> b` thất bại → clear + nhập lại | ✅ Đã xử lý |
| Nhập operator không hợp lệ | `@`, `&` | Kiểm tra `op` ∈ {+,-,*,/,%} → nhập lại | ✅ Đã xử lý |
| Chia cho 0 | `7 0 /` | Kiểm tra `b == 0` → in lỗi | ✅ Đã xử lý |
| Modulo cho 0 | `7 0 %` | Kiểm tra `b == 0` → in lỗi | ✅ Đã xử lý |
| Nhập số thực | `3.5` | `std::cin >> int` đọc phần nguyên, phần thực bị bỏ | ⚠️ Chấp nhận |
| Nhập số âm | `-5` | Hợp lệ (số nguyên có dấu) | ✅ Đúng |

## Practice 3.2 - Quadratic Equation

| Trường hợp | Ví dụ | Cách xử lý | Trạng thái |
|------------|-------|------------|------------|
| Nhập không phải số | `abc` | `std::cin >> double` thất bại → clear + nhập lại | ✅ Đã xử lý |
| a = 0, b = 0, c = 0 | `0 0 0` | In "Infinite solutions" | ✅ Đã xử lý |
| a = 0, b = 0, c ≠ 0 | `0 0 5` | In "No solution!" | ✅ Đã xử lý |
| a = 0, b ≠ 0 | `0 2 4` | Giải phương trình bậc 1 | ✅ Đã xử lý |
| Delta < 0 | `1 1 1` | In "No solution!" | ✅ Đã xử lý |
| Delta = 0 | `1 2 1` | In 1 nghiệm | ✅ Đã xử lý |
| Delta > 0 | `2 -5 3` | In 2 nghiệm | ✅ Đã xử lý |
| Nhập số thực | `2.5` | Hợp lệ (hệ số thực) | ✅ Đúng |

## Practice 3.3 - Days in Month

| Trường hợp | Ví dụ | Cách xử lý | Trạng thái |
|------------|-------|------------|------------|
| Nhập không phải số nguyên | `abc` | `std::cin >> month` thất bại → clear + nhập lại | ✅ Đã xử lý |
| Tháng < 1 | `0` | Kiểm tra `month < 1` → nhập lại | ✅ Đã xử lý |
| Tháng > 12 | `13` | Kiểm tra `month > 12` → nhập lại | ✅ Đã xử lý |
| Nhập năm không hợp lệ | `abc` | `std::cin >> year` thất bại → clear + nhập lại | ✅ Đã xử lý |
| Năm nhuận | `2012` | Tính đúng số ngày tháng 2 | ✅ Đã xử lý |
| Năm không nhuận | `2011` | Tính đúng số ngày tháng 2 | ✅ Đã xử lý |
| Nhập số thực | `6.5` | `std::cin >> int` đọc phần nguyên | ⚠️ Chấp nhận |

## Practice 3.4 - N!, ln(2), PI, S

| Trường hợp | Ví dụ | Cách xử lý | Trạng thái |
|------------|-------|------------|------------|
| Nhập không phải số nguyên | `abc` | `std::cin >> N` thất bại → clear + nhập lại | ✅ Đã xử lý |
| N ≤ 0 | `0`, `-5` | Kiểm tra `N <= 0` → nhập lại | ✅ Đã xử lý |
| N quá lớn (overflow) | `100` | `long long` overflow → kết quả sai | ⚠️ Chưa xử lý |
| Nhập số thực | `5.5` | `std::cin >> int` đọc phần nguyên | ⚠️ Chấp nhận |

## Practice 3.5 - 3-digit numbers

| Trường hợp | Ví dụ | Cách xử lý | Trạng thái |
|------------|-------|------------|------------|
| Không có input | - | Chương trình tự động chạy | ✅ Không cần xử lý |

## Practice 3.8 - Max, Min, Average

| Trường hợp | Ví dụ | Cách xử lý | Trạng thái |
|------------|-------|------------|------------|
| Nhập không phải số nguyên | `abc` | `std::cin >> num` thất bại → clear + nhập lại | ✅ Đã xử lý |
| Nhập số âm | `-5` | Kiểm tra `num < 0` → nhập lại | ✅ Đã xử lý |
| Nhập 0 để dừng | `0` | Thoát vòng lặp | ✅ Đã xử lý |
| Không nhập số nào | `0` ngay | In "No valid numbers entered" | ✅ Đã xử lý |
| Nhập số thực | `5.5` | `std::cin >> int` đọc phần nguyên | ⚠️ Chấp nhận |

## Practice 3.9 - Prime Numbers

| Trường hợp | Ví dụ | Cách xử lý | Trạng thái |
|------------|-------|------------|------------|
| Nhập không phải số nguyên | `abc` | `std::cin >> N` thất bại → clear + nhập lại | ✅ Đã xử lý |
| N < 1 | `0`, `-5` | Kiểm tra `N < 1` → nhập lại | ✅ Đã xử lý |
| N = 1 | `1` | In "There are 0 prime numbers" | ✅ Đã xử lý |
| Nhập số thực | `5.5` | `std::cin >> int` đọc phần nguyên | ⚠️ Chấp nhận |

## Practice 3.10 - GCD, LCM

| Trường hợp | Ví dụ | Cách xử lý | Trạng thái |
|------------|-------|------------|------------|
| Nhập không phải số nguyên | `abc` | `std::cin >> a` thất bại → clear + nhập lại | ✅ Đã xử lý |
| a ≤ 0 | `0`, `-5` | Kiểm tra `a <= 0` → nhập lại | ✅ Đã xử lý |
| b ≤ 0 | `0`, `-5` | Kiểm tra `b <= 0` → nhập lại | ✅ Đã xử lý |
| Nhập số thực | `5.5` | `std::cin >> int` đọc phần nguyên | ⚠️ Chấp nhận |

## Practice 3.11 - Bit Representation

| Trường hợp | Ví dụ | Cách xử lý | Trạng thái |
|------------|-------|------------|------------|
| Nhập không phải số nguyên cho N | `abc` | `std::cin >> N` thất bại → clear + nhập lại | ✅ Đã xử lý |
| Nhập không phải số nguyên cho M | `abc` | `std::cin >> M` thất bại → clear + nhập lại | ✅ Đã xử lý |
| M ≤ 0 | `0`, `-3` | Kiểm tra `M <= 0` → nhập lại | ✅ Đã xử lý |
| M > 32 | `33` | In đủ 32 bit (sẽ dấu 0) | ⚠️ Chấp nhận |
| Nhập số thực | `5.5` | `std::cin >> int` đọc phần nguyên | ⚠️ Chấp nhận |

## Practice 3.12 - Phone Number

| Trường hợp | Ví dụ | Cách xử lý | Trạng thái |
|------------|-------|------------|------------|
| Nhập không phải số | `abc` | `std::cin >> phone` thất bại → clear + nhập lại | ✅ Đã xử lý |
| Nhập số âm | `-123` | Kiểm tra `phone < 0` → nhập lại | ✅ Đã xử lý |
| Nhập số > 10 chữ số | `12345678901` | Kiểm tra `phone > 9999999999` → lỗi | ✅ Đã xử lý |
| Nhập số thực | `123.45` | `std::cin >> long long` đọc phần nguyên | ⚠️ Chấp nhận |
| Nhập 0 | `0` | In "Zero" | ✅ Đã xử lý |

## Practice 3.13 - Descending & Symmetric

| Trường hợp | Ví dụ | Cách xử lý | Trạng thái |
|------------|-------|------------|------------|
| Nhập không phải số nguyên | `abc` | `std::cin >> N` thất bại → clear + nhập lại | ✅ Đã xử lý |
| N ≤ 0 | `0`, `-5` | Kiểm tra `N <= 0` → nhập lại | ✅ Đã xử lý |
| Nhập số thực | `5.5` | `std::cin >> int` đọc phần nguyên | ⚠️ Chấp nhận |

---

## Tổng kết

### Đã xử lý đầy đủ:
- ✅ Nhập không phải số (clear + nhập lại)
- ✅ Nhập số âm (nơi yêu cầu số dương)
- ✅ Nhập số 0 (nơi yêu cầu số dương)
- ✅ Nhập tháng không hợp lệ
- ✅ Nhập operator không hợp lệ
- ✅ Chia cho 0
- ✅ Số điện thoại > 10 chữ số
- ✅ M ≤ 0

### Chấp nhận (không cần xử lý đặc biệt):
- ⚠️ Nhập số thực → đọc phần nguyên (hành vi phổ biến)
- ⚠️ N quá lớn → overflow (cần giải thích cho người dùng)
- ⚠️ M > 32 → in đủ bit (hành vi hợp lý)
