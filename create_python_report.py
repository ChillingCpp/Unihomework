from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Create document
doc = Document()

# Set default font
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(13)
style.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

# Set line spacing
pf = style.paragraph_format
pf.line_spacing = 1.5

# Page setup A4
sections = doc.sections
for section in sections:
    section.page_width = Cm(21)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

# Headers and Footer
for section in sections:
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    hp_run = hp.add_run('TÌM HIỂU NGÔN NGỮ LẬP TRÌNH PYTHON')
    hp_run.font.name = 'Times New Roman'
    hp_run.font.size = Pt(12)
    hp_run.bold = True
    hp_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp_run = fp.add_run('Báo cáo môn học — Python')
    fp_run.font.name = 'Times New Roman'
    fp_run.font.size = Pt(11)
    fp_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    
    # Add page number
    fp2 = footer.add_paragraph()
    fp2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = fp2.add_run()
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = 'PAGE'
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'end')
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)

# Helper functions
def add_heading(doc, text, level):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.name = 'Times New Roman'
        run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    return h

def set_justify(p):
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

def add_para(doc, text, indent=False):
    p = doc.add_paragraph()
    set_justify(p)
    if indent:
        p.paragraph_format.first_line_indent = Cm(1.0)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13)
    run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    return p

def add_bullet(doc, text):
    p = doc.add_paragraph(style='List Bullet')
    set_justify(p)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13)
    run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    return p

def add_code_block(doc, code, caption=""):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.left_indent = Cm(0.5)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    
    pPr = p._element.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    for border_name in ['top', 'left', 'bottom', 'right']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '4')
        border.set(qn('w:space'), '4')
        border.set(qn('w:color'), '000000')
        pBdr.append(border)
    pPr.append(pBdr)
    
    run = p.add_run(code)
    run.font.name = 'Consolas'
    run.font.size = Pt(10)
    
    if caption:
        cap = doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap_run = cap.add_run(caption)
        cap_run.font.name = 'Times New Roman'
        cap_run.font.size = Pt(10)
        cap_run.italic = True
        cap_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

def add_table(doc, headers, data, caption=""):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    hdr_cells = table.rows[0].cells
    for i, header in enumerate(headers):
        hdr_cells[i].text = header
        for p in hdr_cells[i].paragraphs:
            for run in p.runs:
                run.font.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(11)
                run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    
    for row_data in data:
        row_cells = table.add_row().cells
        for i, cell_data in enumerate(row_data):
            row_cells[i].text = str(cell_data)
            for p in row_cells[i].paragraphs:
                for run in p.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(11)
                    run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    
    if caption:
        cap = doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap_run = cap.add_run(caption)
        cap_run.font.name = 'Times New Roman'
        cap_run.font.size = Pt(10)
        cap_run.italic = True
        cap_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    
    return table

# ============================================
# COVER PAGE
# ============================================
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
title.paragraph_format.space_after = Pt(30)
title_run = title.add_run('TÌM HIỂU NGÔN NGỮ LẬP TRÌNH PYTHON')
title_run.font.name = 'Times New Roman'
title_run.font.size = Pt(18)
title_run.bold = True
title_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

for _ in range(5):
    doc.add_paragraph()

info = doc.add_paragraph()
info.alignment = WD_ALIGN_PARAGRAPH.CENTER
info.paragraph_format.space_after = Pt(10)
info_run = info.add_run('Giảng viên hướng dẫn: [Tên giảng viên]\nSinh viên thực hiện: [Tên sinh viên]\nMã số sinh viên: [MSV]\nLớp: [Lớp học]')
info_run.font.name = 'Times New Roman'
info_run.font.size = Pt(13)
info_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

doc.add_paragraph()
date = doc.add_paragraph()
date.alignment = WD_ALIGN_PARAGRAPH.CENTER
date_run = date.add_run('[Thành phố], tháng năm 2026')
date_run.font.name = 'Times New Roman'
date_run.font.size = Pt(13)
date_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

doc.add_page_break()

# ============================================
# TABLE OF CONTENTS
# ============================================
toc_title = doc.add_paragraph()
toc_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
toc_run = toc_title.add_run('MỤC LỤC')
toc_run.font.name = 'Times New Roman'
toc_run.font.size = Pt(16)
toc_run.bold = True
toc_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

line = doc.add_paragraph()
line.paragraph_format.space_before = Pt(0)
line.paragraph_format.space_after = Pt(10)
line_run = line.add_run('─' * 50)
line_run.font.name = 'Times New Roman'
line_run.font.size = Pt(10)
line_run.font.color.rgb = RGBColor(128, 128, 128)

def add_toc_entry(doc, text, page, is_chapter=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    if is_chapter:
        p.paragraph_format.left_indent = Cm(0)
    else:
        p.paragraph_format.left_indent = Cm(1.0)
    
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13)
    if is_chapter:
        run.bold = True
    run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    
    dot_run = p.add_run('.' * (50 - len(text)))
    dot_run.font.name = 'Times New Roman'
    dot_run.font.size = Pt(13)
    dot_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    
    page_run = p.add_run(page)
    page_run.font.name = 'Times New Roman'
    page_run.font.size = Pt(13)
    page_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_toc_entry(doc, 'CHƯƠNG 1. TỔNG QUAN VỀ PYTHON', '3', True)
add_toc_entry(doc, '1.1. Python là gì?', '3')
add_toc_entry(doc, '1.2. Lịch sử phát triển', '4')
add_toc_entry(doc, '1.3. Đặc điểm nổi bật', '5')
add_toc_entry(doc, '1.4. Lĩnh vực sử dụng', '6')

add_toc_entry(doc, 'CHƯƠNG 2. NỀN TẢNG NGÔN NGỮ PYTHON', '7', True)
add_toc_entry(doc, '2.1. Cú pháp và indentation', '7')
add_toc_entry(doc, '2.2. Biến và dynamic typing', '8')
add_toc_entry(doc, '2.3. Kiểu dữ liệu cơ bản', '9')
add_toc_entry(doc, '2.4. Cấu trúc điều khiển và function', '10')

add_toc_entry(doc, 'CHƯƠNG 3. ĐẶC TRƯNG THÚ VỊ', '11', True)
add_toc_entry(doc, '3.1. List comprehension và unpacking', '11')
add_toc_entry(doc, '3.2. enumerate(), zip() và lambda', '12')
add_toc_entry(doc, '3.3. Generator và exception handling', '13')
add_toc_entry(doc, '3.4. Context manager và decorator', '14')

add_toc_entry(doc, 'CHƯƠNG 4. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG', '15', True)
add_toc_entry(doc, '4.1-4.5. Class, inheritance và polymorphism', '15')

add_toc_entry(doc, 'CHƯƠNG 5. STANDARD LIBRARY', '16', True)
add_toc_entry(doc, '5.1-5.4. pathlib, collections, json, re', '16')

add_toc_entry(doc, 'CHƯƠNG 6. HỆ SINH THÁI THƯ VIỆN', '17', True)
add_toc_entry(doc, '6.1-6.4. NumPy, Pandas, ML, Web', '17')

add_toc_entry(doc, 'CHƯƠNG 7. ỨNG DỤNG THỰC TẾ', '18', True)
add_toc_entry(doc, '7.1-7.5. Automation, Data, API, AI', '18')

add_toc_entry(doc, 'CHƯƠNG 8. KHÍA CẠNH NÂNG CAO', '19', True)
add_toc_entry(doc, '8.1-8.3. Bytecode, performance, C extension', '19')

add_toc_entry(doc, 'CHƯƠNG 9. ƯU ĐIỂM VÀ HẠN CHẾ', '20', True)
add_toc_entry(doc, 'CHƯƠNG 10. SO SÁNH VỚI NGÔN NGỮ KHÁC', '21', True)
add_toc_entry(doc, 'KẾT LUẬN', '22', True)
add_toc_entry(doc, 'TÀI LIỆU THAM KHẢO', '23', True)

doc.add_page_break()

# ============================================
# CHAPTER 1
# ============================================
add_heading(doc, 'CHƯƠNG 1. TỔNG QUAN VỀ PYTHON', level=1)

add_heading(doc, '1.1. Python là gì?', level=2)
add_para(doc, 'Python là ngôn ngữ lập trình bậc cao, thông dịch, hướng đối tượng và đa mô hình. Tên gọi bắt nguồn từ nhóm hài Monty Python, không liên quan đến loài rắn. Khi ra đời những năm 1990, Python được thiết kế với triết lý mã nguồn dễ đọc, trực quan — khác biệt căn bản so với các ngôn ngữ như C hay Pascal.')
add_para(doc, 'Khác với nhiều ngôn ngữ truyền thống yêu cầu khai báo biến, quản lý bộ nhớ thủ công hay dùng dấu ngoặc nhọn, Python loại bỏ hầu hết ràng buộc đó. Kết quả là người mới học có thể viết chương trình hoạt động sau vài giờ, còn lập trình viên kỳ cựu vẫn tận dụng được sức mạnh cho dự án quy mô lớn.')

add_heading(doc, '1.2. Lịch sử phát triển', level=2)
add_para(doc, 'Python ra đời cuối những năm 1980, do Guido van Rossum — nhà khoa học máy tính người Hà Lan tại CWI (Amsterdam) — phát triển. Phiên bản 0.9.0 ra mắt năm 1991 đã bao gồm OOP, xử lý ngoại lệ, và các hàm map/filter/reduce. Bốn năm sau, Python 1.0 giới thiệu module hệ thống và hàm lambda.')
add_para(doc, 'Python 2.0 (2000) đánh dấu bước ngoặt với list comprehension, garbage collection, và khả năng thu hồi chu kỳ tham chiếu. Năm 2008, Python 3.0 ra mắt với thay đổi không tương thích ngược — khiến cộng đồng chuyển đổi chậm trong nhiều năm. Đến 2020, Python 2 chính thức ngừng hỗ trợ.')

add_heading(doc, '1.3. Đặc điểm nổi bật', level=2)
add_bullet(doc, 'Cú法 dễ đọc: Không dấu ngoặc nhọn, không chấm phẩy, cấu trúc khối lệnh xác định bằng indentation.')
add_bullet(doc, 'Dynamic typing: Biến không cần khai báo kiểu, tự động liên kết với object tại runtime.')
add_bullet(doc, 'High-level language: Trừu tượng hóa chi tiết thấpLevel — không cần lo cấp phát bộ nhớ hay con trỏ.')
add_bullet(doc, 'Interpreted execution: Mã nguồn dịch sang bytecode, PVM thực thi → chạy đa nền tảng.')
add_bullet(doc, 'Garbage collection: Tự động quản lý bộ nhớ qua reference counting và cycle detector.')
add_bullet(doc, 'Đa mô hình: Hỗ trợ OOP, functional, procedural, và event-driven programming.')
add_bullet(doc, 'Hệ sinh thái khổng lồ: Hàng trăm nghìn package trên PyPI cover mọi lĩnh vực.')
add_bullet(doc, 'Cross-platform: Chạy trên Windows, macOS, Linux, embedded systems mà không cần sửa đổi.')

add_heading(doc, '1.4. Lĩnh vực sử dụng', level=2)
add_para(doc, 'Python được ứng dụng rộng rãi. Dưới đây là các lĩnh vực tiêu biểu:')
add_bullet(doc, 'Web Development: Django, Flask, FastAPI xây dựng website phức tạp.')
add_bullet(doc, 'Data Science & Analytics: Pandas, NumPy xử lý dữ liệu lớn.')
add_bullet(doc, 'AI/ML: TensorFlow, PyTorch, scikit-learn huấn luyện mô hình.')
add_bullet(doc, 'Automation & Scripting: Tự động hóa tác vụ lặp, quản lý hệ thống.')
add_bullet(doc, 'Giáo dục: Ngôn ngữ đầu tiên trong hầu hết khóa học lập trình đại học.')

# ============================================
# CHAPTER 2
# ============================================
doc.add_page_break()
add_heading(doc, 'CHƯƠNG 2. NỀN TẢNG NGÔN NGỮ PYTHON', level=1)

add_heading(doc, '2.1. Cú pháp và indentation', level=2)
add_para(doc, 'Điểm khác biệt rõ rệt nhất của Python là cách sử dụng indentation thay cho dấu ngoặc nhọn. Trong C++/Java, bạn dùng {} để phân định khối lệnh; trong Python, indentation thực hiện vai trò đó.')
add_para(doc, 'Quy tắc nghiêm ngặt: các câu lệnh trong cùng khối phải cùng độ thụt lề (thường 4 khoảng trắng). Trộn tab và khoảng trắng, hoặc sai lệch indentation sẽ gây lỗi SyntaxError.')

add_code_block(doc, '''# Python: dùng indentation
if x > 0:
    print("Positive")
    if x > 10:
        print("Big")
else:
    print("Non-positive")

# C++: dùng dấu {}
if (x > 0) {
    printf("Positive");
    if (x > 10) {
        printf("Big");
    }
} else {
    printf("Non-positive");
}''', 'Code 1. So sánh cú pháp Python và C++')

add_para(doc, 'Indentation giúp mã nguồn rõ ràng hơn, tránh "spaghetti code" — tình trạng mã rối ren do thiếu cấu trúc khối.)')

add_heading(doc, '2.2. Biến và dynamic typing', level=2)
add_para(doc, 'Trong Python, biến là tên gọi tham chiếu đến object trong bộ nhớ. Object mới mang kiểu dữ liệu, còn biến thì không. Cùng một biến có thể chứa số nguyên, sau đó là xâu ký tự, rồi danh sách — không có lỗi biên dịch.')

add_code_block(doc, '''x = 10          # x tham chiếu đến object int
print(type(x))  # <class 'int'>

x = "Hello"     # x giờ tham chiếu đến object str
print(type(x))  # <class 'str'>

x = [1, 2, 3]   # x giờ tham chiếu đến object list
print(type(x))  # <class 'list'>''', 'Code 2. Dynamic typing trong Python')

add_para(doc, 'Cơ chế dynamic typing mang lại sự linh hoạt cao, nhưng đòi hỏi cẩn trọng vì lỗi kiểu chỉ phát sinh lúc runtime.')

add_heading(doc, '2.3. Kiểu dữ liệu cơ bản', level=2)
add_para(doc, 'Python có tám kiểu dữ liệu cơ bản:')

add_table(doc,
    ['Kiểu', 'Mô tả', 'Ví dụ'],
    [
        ['int', 'Số nguyên', '42, -7, 0'],
        ['float', 'Số thực', '3.14, -0.5'],
        ['bool', 'Giá trị logic', 'True, False'],
        ['str', 'Chuỗi ký tự', '"Hello"'],
        ['list', 'Danh sách có thứ tự', '[1, 2, 3]'],
        ['tuple', 'Bộ bất biến', '(1, 2, 3)'],
        ['set', 'Tập hợp không trùng', '{1, 2, 3}'],
        ['dict', 'Từ điển khóa-giá trị', '{"a": 1}'],
    ],
    'Bảng 1. Các kiểu dữ liệu cơ bản')

add_para(doc, 'List mutable, tuple immutable. Dict lưu trữ truy xuất nhanh theo khóa. Set loại bỏ trùng lặp.')

add_heading(doc, '2.4. Cấu trúc điều khiển và function', level=2)
add_para(doc, 'Python hỗ trợ đầy đủ if/elif/else, for, while. Khác biệt: for trong Python hoạt động như foreach — lặp qua từng phần tử iterable.')

add_code_block(doc, '''# if/elif/else
age = 20
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

# for loop (foreach)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# break và continue
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)''', 'Code 3. Cấu trúc điều khiển')

add_para(doc, 'Function định nghĩa bằng def, hỗ trợ default argument, keyword argument, *args, **kwargs:')

add_code_block(doc, '''def greet(name, greeting="Hello", times=1):
    for _ in range(times):
        print(f"{greeting}, {name}!")

greet("Alice")           # Hello, Alice!
greet("Bob", "Hi")       # Hi, Bob!

# *args và **kwargs
def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

print(sum_all(1, 2, 3))      # 6
print(print_info(a=1, b=2))''', 'Code 4. Function với parameter')

# ============================================
# CHAPTER 3
# ============================================
doc.add_page_break()
add_heading(doc, 'CHƯƠNG 3. ĐẶC TRƯNG THÚ VỊ', level=1)

add_heading(doc, '3.1. List comprehension và unpacking', level=2)
add_para(doc, 'List comprehension tạo list mới từ iterable bằng cú法 ngắn gọn, đọc như tiếng Anh:')

add_code_block(doc, '''# Tạo list bình phương
squares = [x * x for x in range(10)]

# Có điều kiện
evens = [x for x in range(20) if x % 2 == 0]

# Nested list comprehension
matrix = [[i*j for j in range(1,4)] for i in range(1,4)]''', 'Code 5. List comprehension')

add_para(doc, 'Multiple assignment và unpacking cho phép gán nhiều biến cùng lúc, hoán đổi giá trị không cần biến trung gian:')

add_code_block(doc, '''# Multiple assignment
a, b, c = 10, 20, 30

# Hoán đổi
a, b = b, a

# Unpacking
first, *middle, last = [1, 2, 3, 4, 5]''', 'Code 6. Multiple assignment và unpacking')

add_heading(doc, '3.2. enumerate(), zip() và lambda', level=2)
add_para(doc, 'enumerate() lấy cả chỉ số và giá trị khi lặp:')

add_code_block(doc, '''names = ["An", "Binh", "Cuong"]
for i, name in enumerate(names):
    print(i, name)''', 'Code 7. enumerate()')

add_para(doc, 'zip() ghép các iterable theo cặp:')

add_code_block(doc, '''names = ["An", "Binh"]
scores = [8, 9]
for name, score in zip(names, scores):
    print(name, score)''', 'Code 8. zip()')

add_para(doc, 'Lambda là function ẩn danh, dùng với map(), filter(), sorted():')

add_code_block(doc, '''# Lambda
square = lambda x: x * x

# Map, filter
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, nums))
evens = list(filter(lambda x: x%2==0, nums))

# Sort với key
students = [("An",8), ("Binh",9)]
sorted_s = sorted(students, key=lambda x: x[1])''', 'Code 9. Lambda và higher-order functions')

add_heading(doc, '3.3. Generator và exception handling', level=2)
add_para(doc, 'Generator dùng yield để tạo sequence mà không lưu toàn bộ vào bộ nhớ:')

add_code_block(doc, '''def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num, end=" ")  # 1 2 3 4 5

# Generator expression
squares = (x*x for x in range(10))''', 'Code 10. Generator và yield')

add_para(doc, 'Khác return: yield tạm dừng function, giữ trạng thái; return kết thúc hoàn toàn.')

add_para(doc, 'Exception handling bắt lỗi bằng try-except:')

add_code_block(doc, '''try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: chia cho 0!")
except TypeError:
    print("Error: kiểu không hợp lệ")
else:
    print(f"Result: {result}")
finally:
    print("Operation finished.")''', 'Code 11. Exception handling')

add_heading(doc, '3.4. Context manager và decorator', level=2)
add_para(doc, 'Context manager quản lý tài nguyên tự động qua with:')

add_code_block(doc, '''# File tự động đóng
with open("data.txt", "r") as file:
    content = file.read()

# Context manager tùy chỉnh
from contextlib import contextmanager

@contextmanager
def timer(label):
    import time
    start = time.time()
    yield
    print(f"{label}: {time.time()-start:.4f}s")

with timer("Tính toán"):
    sum(x**2 for x in range(100000))''', 'Code 12. Context manager')

add_para(doc, 'Decorator "bao bọc" function thêm hành vi mới:')

add_code_block(doc, '''def log_call(func):
    def wrapper():
        print("Started")
        func()
        print("Finished")
    return wrapper

@log_call
def hello():
    print("Hello Python")

hello()  # Started → Hello Python → Finished''', 'Code 13. Decorator')

# ============================================
# CHAPTER 4
# ============================================
doc.add_page_break()
add_heading(doc, 'CHƯƠNG 4. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG', level=1)

add_para(doc, 'Python hỗ trợ OOP thông qua class. Khác C++/Java, Python không yêu cầu interface riêng — duck typing cho phép object dùng được nếu có method phù hợp.')

add_code_block(doc, '''class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_sound(animal):
    print(animal.speak())

make_sound(Dog())  # Woof!
make_sound(Cat())  # Meow!

# Duck typing
def introduce(obj):
    print(f"{obj.name}: {obj.speak()}")''', 'Code 14. Class và polymorphism')

add_para(doc, 'Constructor __init__ khởi tạo object. Instance attribute/method gắn với object cụ thể. Python hỗ trợ đa kế thừa nhưng cần thận trọng với MRO.')

# ============================================
# CHAPTER 5
# ============================================
doc.add_page_break()
add_heading(doc, 'CHƯƠNG 5. STANDARD LIBRARY', level=1)

add_para(doc, 'Standard Library là tập module sẵn có, cung cấp công cụ cho hầu hết tác vụ thông thường:')

add_para(doc, 'pathlib thao tác đường dẫn theo hướng object-oriented:')

add_code_block(doc, '''from pathlib import Path
path = Path("data.txt")
path.write_text("Hello")
print(path.read_text())  # Hello
print(path.suffix)       # .txt''', 'Code 15. pathlib')

add_para(doc, 'json deserialize dữ liệu web; re xử lý regular expression; collections cung cấp Counter, defaultdict, deque tiện lợi hơn list/tuple thông thường.')

# ============================================
# CHAPTER 6
# ============================================
doc.add_page_break()
add_heading(doc, 'CHƯƠNG 6. HỆ SINH THÁI THƯ VIỆN', level=1)

add_para(doc, 'PyPI chứa hàng chục nghìn package. Các nhóm tiêu biểu:')

add_table(doc,
    ['Thư viện', 'Lĩnh vực', 'Mô tả'],
    [
        ['NumPy', 'Scientific computing', 'Mảng đa chiều, toán học số'],
        ['Pandas', 'Data analysis', 'DataFrame xử lý dữ liệu'],
        ['Matplotlib', 'Visualization', 'Vẽ biểu đồ, đồ thị'],
        ['Scikit-learn', 'Machine learning', 'Thuật toán ML cổ điển'],
        ['TensorFlow', 'Deep learning', 'Neural network (Google)'],
        ['PyTorch', 'Deep learning', 'Neural network (Meta)'],
        ['Django', 'Web development', 'Full-stack framework'],
        ['Flask', 'Web development', 'Micro framework'],
        ['Requests', 'HTTP', 'Gửi HTTP request'],
    ],
    'Bảng 2. Thư viện Python phổ biến')

add_para(doc, 'Mỗi thư viện giải quyết vấn đề cụ thể. NumPy là nền tảng cho Pandas, Matplotlib; TensorFlow/PyTorch thống trị deep learning. Django/Flask/FastAPI phục vụ web development.')

# ============================================
# CHAPTER 7
# ============================================
doc.add_page_break()
add_heading(doc, 'CHƯƠNG 7. ỨNG DỤNG THỰC TẾ', level=1)

add_para(doc, 'Python xử lý file tự động:')

add_code_block(doc, '''from pathlib import Path
import shutil

folder = Path("photos")
for idx, src in enumerate(folder.glob("*.jpg"), 1):
    dest = folder / f"IMG_{idx:03d}.jpg"
    shutil.move(src, dest)''', 'Code 16. Tự động hóa file')

add_para(doc, 'Xử lý dữ liệu với Pandas:')

add_code_block(doc, '''import pandas as pd
df = pd.read_csv("data.csv")
print(df.describe())
grouped = df.groupby("category").mean()
df.to_csv("cleaned.csv", index=False)''', 'Code 17. Xử lý dữ liệu')

add_para(doc, 'Gọi REST API:')

add_code_block(doc, '''import requests
resp = requests.get("https://api.github.com/users/chillingcpp")
data = resp.json()
print(data["login"], data["public_repos"])''', 'Code 18. Gọi Web API')

add_para(doc, 'Pipeline AI: Python → thư viện dữ liệu (Pandas) → framework ML (Scikit-learn/TensorFlow) → ứng dụng. Python chiếm ưu thế tuyệt đối trong lĩnh vực này.')

# ============================================
# CHAPTER 8
# ============================================
doc.add_page_break()
add_heading(doc, 'CHƯƠNG 8. KHÍA CẠNH NÂNG CAO', level=1)

add_para(doc, 'Python bytecode: source code → AST → bytecode → PVM thực thi. File .pyc lưu bytecode để lần sau không cần parse lại.')

add_para(doc, 'Python mở rộng bằng C/C++: nhiều thư viện performance-critical (NumPy, Pandas) chạy code tính toán trong C, cho Python tốc độ gần bằng native.')

add_para(doc, 'Hiệu năng: Python chậm hơn C++ 10-100 lần trong CPU-bound tasks do dynamic typing và interpretation overhead. Nhưng developer productivity cao hơn nhiều — viết code nhanh, debug dễ, maintain tốt. Phần lớn task không CPU-bound thuần túy mà phụ thuộc I/O, nơi Python vượt trội.')

# ============================================
# CHAPTER 9
# ============================================
add_heading(doc, 'CHƯƠNG 9. ƯU ĐIỂM VÀ HẠN CHẾ', level=1)

add_heading(doc, 'Ưu điểm', level=2)
add_bullet(doc, 'Syntax dễ đọc, dễ học — giảm rào cản gia nhập.')
add_bullet(doc, 'Rapid development —写完 trong giờ thay vì ngày.')
add_bullet(doc, 'Ecosystem phong phú — hàng nghìn package.')
add_bullet(doc, 'Versatility — một ngôn ngữ cho nhiều mục đích.')
add_bullet(doc, 'Cộng đồng lớn — tài liệu, forum đầy đủ.')
add_bullet(doc, 'Cross-platform — chạy mọi hệ điều hành.')

add_heading(doc, 'Hạn chế', level=2)
add_bullet(doc, 'Performance chậm hơn C++ trong CPU-bound tasks.')
add_bullet(doc, 'Memory overhead cao hơn do object model.')
add_bullet(doc, 'Runtime errors — dynamic typing gây lỗi kiểu lúc chạy.')
add_bullet(doc, 'Dependency management phức tạp với dự án lớn.')
add_bullet(doc, 'Không phù hợp real-time systems, embedded low-level.')

# ============================================
# CHAPTER 10
# ============================================
doc.add_page_break()
add_heading(doc, 'CHƯƠNG 10. SO SÁNH VỚI NGÔN NGỮ KHÁC', level=1)

add_table(doc,
    ['Tiêu chí', 'Python', 'C++', 'Java', 'JavaScript'],
    [
        ['Syntax', 'Đơn giản', 'Phức tạp', 'Trung bình', 'Đơn giản'],
        ['Typing', 'Dynamic', 'Static', 'Static', 'Dynamic'],
        ['Performance', 'Trung bình-thấp', 'Cao', 'Trung bình', 'Trung bình'],
        ['ECOSYSTEM', 'Rất lớn', 'Trung bình', 'Lớn', 'Rất lớn'],
        ['Phù hợp', 'Data/AI/Web', 'System/Game', 'Enterprise', 'Web/App'],
        ['Learning curve', 'Thấp', 'Cao', 'Trung bình', 'Thấp-trung bình'],
    ],
    'Bảng 3. So sánh Python với C++, Java, JavaScript')

add_para(doc, 'Python dễ đọc nhất, dynamic typing linh hoạt. C++ nhanh nhất nhưng phức tạp. Java cân bằng giữa performance và productivity. JavaScript thống trị web frontend.')

# ============================================
# KẾT LUẬN
# ============================================
add_heading(doc, 'KẾT LUẬN', level=1)

add_para(doc, 'Python không chỉ là ngôn ngữ lập trình — đó là hệ sinh thái hoàn chỉnh bao gồm ngôn ngữ, standard library, cộng đồng và hàng nghìn thư viện bên thứ ba. Từ năm 1991 đến nay, Python phát triển từ dự án cá nhân thành một trong những ngôn ngữ phổ biến nhất thế giới.')

add_para(doc, 'Những đặc điểm then chốt: cú pháp dễ đọc, dynamic typing linh hoạt, ecosystem phong phú, cross-platform. Python phù hợp automation, data science, AI, web development, education. Sự phổ biến trong giáo dục củng cố vị thế — thế hệ lập trình viên tương lai học Python trước tiên.')

add_para(doc, 'Tuy nhiên, Python không phải giải pháp cho mọi vấn đề. Performance kém C++ trong tính toán nặng, memory overhead cao, dynamic typing có thể gây runtime error. Real-time systems và embedded programming không phải lĩnh vực của Python.')

add_para(doc, 'Dưới góc nhìn sinh viên, Python là ngôn ngữ đáng học nhất hiện nay — mở cánh cửa đến AI, data science, web development. Dù có hạn chế, Python vẫn giữ vững vị thế ngôn ngữ phổ biến bậc nhất, và xu hướng này dự kiến tiếp tục mạnh mẽ.')

# ============================================
# TÀI LIỆU THAM KHẢO
# ============================================
doc.add_page_break()
add_heading(doc, 'TÀI LIỆU THAM KHẢO', level=1)

refs = [
    '[1] Python Software Foundation. Python Documentation. https://docs.python.org/3/',
    '[2] Van Rossum, G. & Drake, F.L. (2009). Python 3 Reference Manual. CreateSpace.',
    '[3] McKinney, W. (2017). Python for Data Analysis. O\'Reilly Media.',
    '[4] Lutz, M. (2013). Learning Python. O\'Reilly Media.',
    '[5] PyPI — The Python Package Index. https://pypi.org/',
]

for ref in refs:
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(-0.5)
    p.paragraph_format.left_indent = Cm(0.5)
    run = p.add_run(ref)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

# Save
doc.save(r'C:\Users\Admin\Desktop\baitap\BaoCao_Python.docx')
print("Done! BaoCao_Python.docx created.")
