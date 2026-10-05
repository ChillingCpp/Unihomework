from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

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

def add_paragraph(doc, text, bold=False, alignment=None):
    p = doc.add_paragraph()
    if alignment:
        p.alignment = alignment
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13)
    run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    if bold:
        run.bold = True
    return p

def add_code_block(doc, code, caption=""):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.left_indent = Cm(0.5)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    
    # Create a border around code
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
    
    # Header row
    hdr_cells = table.rows[0].cells
    for i, header in enumerate(headers):
        hdr_cells[i].text = header
        for p in hdr_cells[i].paragraphs:
            for run in p.runs:
                run.font.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
                run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    
    # Data rows
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

def set_justify(p):
    pf = p.paragraph_format
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# ============================================
# COVER PAGE
# ============================================
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
title_run = title.add_run('TÌM HIỂU NGÔN NGỮ LẬP TRÌNH PYTHON')
title_run.font.name = 'Times New Roman'
title_run.font.size = Pt(18)
title_run.bold = True
title_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

doc.add_paragraph()
doc.add_paragraph()

info = doc.add_paragraph()
info.alignment = WD_ALIGN_PARAGRAPH.CENTER
info_run = info.add_run('Giảng viên hướng dẫn: [Tên giảng viên]\nSinh viên thực hiện: [Tên sinh viên]\nMã số sinh viên: [MSV]\nLớp: [Lớp học]')
info_run.font.name = 'Times New Roman'
info_run.font.size = Pt(13)
info_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

doc.add_paragraph()
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
# Title "MỤC LỤC" - centered, bold, size 16
toc_title = doc.add_paragraph()
toc_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
toc_title.paragraph_format.space_after = Pt(10)
toc_run = toc_title.add_run('MỤC LỤC')
toc_run.font.name = 'Times New Roman'
toc_run.font.size = Pt(16)
toc_run.bold = True
toc_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

# Add horizontal line
line = doc.add_paragraph()
line.paragraph_format.space_before = Pt(0)
line.paragraph_format.space_after = Pt(15)
line_run = line.add_run('─' * 60)
line_run.font.name = 'Times New Roman'
line_run.font.size = Pt(10)
line_run.font.color.rgb = RGBColor(128, 128, 128)

# TOC entries with proper formatting
def add_toc_entry(doc, text, page, is_chapter=False, indent=0):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Cm(indent)
    
    # Add text
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13)
    if is_chapter:
        run.bold = True
    run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    
    # Add dotted line to page number
    dot_run = p.add_run('.' * (55 - len(text)))
    dot_run.font.name = 'Times New Roman'
    dot_run.font.size = Pt(13)
    dot_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    
    # Add page number
    page_run = p.add_run(page)
    page_run.font.name = 'Times New Roman'
    page_run.font.size = Pt(13)
    page_run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

# Chapter entries
add_toc_entry(doc, 'CHƯƠNG 1. TỔNG QUAN VỀ PYTHON', '3', is_chapter=True)
add_toc_entry(doc, '1.1. Python là gì?', '3')
add_toc_entry(doc, '1.2. Lịch sử phát triển của Python', '4')
add_toc_entry(doc, '1.3. Những đặc điểm nổi bật của Python', '5')
add_toc_entry(doc, '1.4. Các lĩnh vực sử dụng Python', '6')

add_toc_entry(doc, 'CHƯƠNG 2. NỀN TẢNG NGÔN NGỮ PYTHON', '8', is_chapter=True)
add_toc_entry(doc, '2.1. Cú pháp và indentation', '8')
add_toc_entry(doc, '2.2. Biến và dynamic typing', '9')
add_toc_entry(doc, '2.3. Các kiểu dữ liệu cơ bản', '10')
add_toc_entry(doc, '2.4. Cấu trúc điều khiển', '11')
add_toc_entry(doc, '2.5. Function', '12')

add_toc_entry(doc, 'CHƯƠNG 3. NHỮNG ĐẶC TRƯNG THÚ VỊ CỦA PYTHON', '13', is_chapter=True)
add_toc_entry(doc, '3.1. List comprehension', '13')
add_toc_entry(doc, '3.2. Multiple assignment', '14')
add_toc_entry(doc, '3.3. Unpacking', '15')
add_toc_entry(doc, '3.4. enumerate()', '15')
add_toc_entry(doc, '3.5. zip()', '16')
add_toc_entry(doc, '3.6. Lambda và higher-order functions', '16')
add_toc_entry(doc, '3.7. Generator và yield', '17')
add_toc_entry(doc, '3.8. Exception handling', '18')
add_toc_entry(doc, '3.9. Context manager và with', '18')
add_toc_entry(doc, '3.10. Decorator', '19')

add_toc_entry(doc, 'CHƯƠNG 4. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON', '20', is_chapter=True)
add_toc_entry(doc, '4.1. Class và object', '20')
add_toc_entry(doc, '4.2. Constructor', '21')
add_toc_entry(doc, '4.3. Instance attribute và method', '21')
add_toc_entry(doc, '4.4. Inheritance', '22')
add_toc_entry(doc, '4.5. Polymorphism', '22')

add_toc_entry(doc, 'CHƯƠNG 5. PYTHON STANDARD LIBRARY', '23', is_chapter=True)
add_toc_entry(doc, '5.1. pathlib và os', '23')
add_toc_entry(doc, '5.2. math, random, datetime', '24')
add_toc_entry(doc, '5.3. json và re', '24')
add_toc_entry(doc, '5.4. collections', '25')

add_toc_entry(doc, 'CHƯƠNG 6. HỆ SINH THÁI THƯ VIỆN PYTHON', '26', is_chapter=True)
add_toc_entry(doc, '6.1. Khoa học dữ liệu và tính toán số', '26')
add_toc_entry(doc, '6.2. Machine Learning và Deep Learning', '27')
add_toc_entry(doc, '6.3. Web Development', '27')
add_toc_entry(doc, '6.4. Network và Web Scraping', '28')

add_toc_entry(doc, 'CHƯƠNG 7. ỨNG DỤNG THỰC TẾ', '29', is_chapter=True)
add_toc_entry(doc, '7.1. Tự động hóa file', '29')
add_toc_entry(doc, '7.2. Xử lý dữ liệu', '30')
add_toc_entry(doc, '7.3. Gọi Web API', '30')
add_toc_entry(doc, '7.4. AI / Machine Learning', '31')

add_toc_entry(doc, 'CHƯƠNG 8. MỘT SỐ KHÍA CẠNH NÂNG CAO VÀ ĐẶC TRƯNG', '32', is_chapter=True)
add_toc_entry(doc, '8.1. Python mở rộng bằng C/C++', '32')
add_toc_entry(doc, '8.2. Python bytecode và Python Virtual Machine', '33')
add_toc_entry(doc, '8.3. Hiệu năng của Python', '33')

add_toc_entry(doc, 'CHƯƠNG 9. ƯU ĐIỂM VÀ HẠN CHẾ', '34', is_chapter=True)

add_toc_entry(doc, 'CHƯƠNG 10. SO SÁNH VỚI MỘT SỐ NGÔN NGỮ', '35', is_chapter=True)

add_toc_entry(doc, 'KẾT LUẬN', '37', is_chapter=True)

add_toc_entry(doc, 'TÀI LIỆU THAM KHẢO', '38', is_chapter=True)

doc.add_page_break()

# ============================================
# CHAPTER 1
# ============================================
add_heading(doc, 'Chương 1. TỔNG QUAN VỀ PYTHON', level=1)

add_heading(doc, '1.1. Python là gì?', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python là một ngôn ngữ lập trình bậc cao, thông dịch, hướng đối tượng và đa mô hình. Tên gọi của ngôn ngữ này bắt nguồn từ nhóm hài nổi tiếng Monty Python của Anh, chứ không liên quan đến loài rắn. Khi được phát minh vào đầu những năm 1990, Python được thiết kế với triết lý rõ ràng: mã nguồn phải dễ đọc, dễ hiểu và mang tính trực quan cao.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Khác với nhiều ngôn ngữ lập trình truyền thống yêu cầu người viết phải khai báo biến, quản lý bộ nhớ thủ công hay sử dụng dấu ngoặc nhọn để phân định khối lệnh, Python loại bỏ hầu hết những ràng buộc đó. Kết quả là người mới học có thể viết được chương trình hoạt động sau vài giờ tiếp cận, trong khi lập trình viên kỳ cựu vẫn tận dụng được sức mạnh của ngôn ngữ này cho các dự án quy mô lớn.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Ngày nay, Python xuất hiện ở khắp nơi: từ các trang web thương mại điện tử lớn, hệ thống phân tích dữ liệu trong ngành tài chính, cho đến những mô hình trí tuệ nhân tạo tiên tiến nhất. Sự phổ biến của Python không chỉ nằm ở cú pháp đẹp mắt, mà còn đến từ một cộng đồng phát triển khổng lồ liên tục tạo ra những công cụ mới mỗi ngày.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

# [ĐỀ XUẤT HÌNH 1]: Sơ đồ minh họa các lĩnh vực ứng dụng của Python (web, data science, AI, automation...). Có thể tìm trên Unsplash hoặc tạo bằng PowerPoint.

add_heading(doc, '1.2. Lịch sử phát triển của Python', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python ra đời vào cuối những năm 1980, khi Guido van Rossum, một nhà khoa học máy tính người Hà Lan, đang làm việc tại Centrum Wiskunde & Informatica (CWI) ở Amsterdam. Ông bắt đầu triển khai Python như một dự án cá nhân nhằm tạo ra một ngôn ngữ kế thừa tinh hoa của ngôn ngữ ABC, đồng thời khắc phục những hạn chế của ABC như khả năng tương tác với hệ điều hành.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Phiên bản đầu tiên, Python 0.9.0, được phát hành vào năm 1991. Phiên bản này đã bao gồm hầu hết các tính năng cốt lõi mà Python sở hữu đến ngày nay: hướng đối tượng, xử lý ngoại lệ, và các hàm tích hợp như map(), filter(), reduce(). Bốn năm sau, Python 1.0 ra mắt với модуль hệ thống module và hàm lambda.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Điểm ngoặt quan trọng trong lịch sử Python xảy ra vào năm 2000, khi Python 2.0 được phát hành. Phiên bản này giới thiệu list comprehension, garbage collection dựa trên cơ chế đếm tham chiếu, và khả năng thu hồi bộ nhớ từ các chu kỳ tham chiếu. Python 2 nhanh chóng trở thành phiên bản được sử dụng rộng rãi trong cộng đồng.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Tuy nhiên, những thay đổi được lên kế hoạch từ rất sớm trong Python 3.0 (phát hành năm 2008) lại gây ra sự chia rẽ. Python 3 không tương thích ngược với Python 2, meaning các chương trình viết cho Python 2 không thể chạy trực tiếp trên Python 3. Sự chuyển đổi này diễn ra chậm chạp trong nhiều năm, nhưng đến năm 2020, Python 2 chính thức bị ngừng hỗ trợ, buộc toàn bộ cộng đồng phải chuyển sang Python 3.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Từ năm 2008 đến nay, Python 3 đã trải qua nhiều phiên bản cải tiến quan trọng như 3.6 (f-string), 3.8 (assignment expression), 3.10 (pattern matching), và 3.12 (cải thiện hiệu năng). Mỗi phiên bản đều mang lại những tính năng mới giúp Python càng trở nên mạnh mẽ và tiện lợi hơn.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, '1.3. Những đặc điểm nổi bật của Python', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python sở hữu nhiều đặc điểm khiến ngôn ngữ này trở nên khác biệt so với các ngôn ngữ lập trình truyền thống. Dưới đây là những đặc trưng quan trọng nhất:')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Cú pháp dễ đọc: Python được thiết kế với triết lý "code readability counts". Không có dấu ngoặc nhọn, không có dấu chấm phẩy cuối dòng, cấu trúc khối lệnh được xác định bằng indentation. Điều này khiến mã nguồn trông giống như văn bản thông thường và dễ hiểu ngay cả với người không chuyên.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Dynamic typing: Trong Python, bạn không cần khai báo kiểu dữ liệu cho biến. Biến tự động liên kết với object tương ứng tại thời điểm gán. Cùng một biến có thể chứa số nguyên, sau đó là xâu ký tự, rồi sau đó là danh sách — tất cả đều diễn ra mà không có lỗi biên dịch.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• High-level language: Python trừu tượng hóa hầu hết các chi tiết thấpLevel của máy tính. Người lập trình không cần lo lắng về cấp phát bộ nhớ, quản lý con trỏ hay các vấn đề liên quan đến bộ nhớ.interpreter đảm bảo mọi thứ hoạt động đúng.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Interpreted execution: Python không được biên dịch thành mã máy trước khi chạy. Thay vào đó, mã nguồn được dịch sang bytecode, sau đó Python Virtual Machine (PVM) thực thi bytecode này. Quá trình này cho phép Python chạy đa nền tảng mà không cần biên dịch lại.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Garbage collection: Python tự động quản lý bộ nhớ thông qua cơ chế tham chiếu đếm (reference counting) và garbage collector phát hiện chu kỳ. Lập trình viên không cần gọi free() hay delete() như trong C/C++.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Hỗ trợ OOP đa hình thái: Python hỗ trợ lập trình hướng đối tượng, nhưng cũng cho phép lập trình chức năng (functional programming), lập trình thủ tục, và lập trình hướng sự kiện. Bạn có thể linh hoạt chọn mô hình phù hợp với bài toán.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Hệ sinh thái thư viện khổng lồ: Python có hàng chục nghìn thư viện chính thức và thứ cấp, cover hầu hết mọi lĩnh vực: từ web development, data science, machine learning, cho đến game development và automation.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Cross-platform: Python chạy được trên Windows, macOS, Linux, và thậm chí trên các thiết bị nhúng. Cùng một mã nguồn có thể chạy ở mọi nơi mà không cần sửa đổi.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, '1.4. Các lĩnh vực sử dụng Python', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python được ứng dụng rộng rãi trong nhiều lĩnh vực khác nhau. Dưới đây là những lĩnh vực tiêu biểu:')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Web Development: Django, Flask, FastAPI cho phép xây dựng các trang web phức tạp với tốc độ nhanh.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Data Science & Analytics: Pandas, NumPy, và Scikit-learn giúp xử lý và phân tích dữ liệu hiệu quả.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Artificial Intelligence & Machine Learning: TensorFlow, PyTorch, và Keras là những framework phổ biến nhất trong lĩnh vực này.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Automation & Scripting: Python là công cụ lý tưởng để tự động hóa các tác vụ lặp đi lặp lại, từ xử lý file đến quản lý hệ thống.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Giáo dục: Nhờ cú pháp đơn giản, Python được chọn làm ngôn ngữ đầu tiên trong hầu hết các khóa học lập trình đại học.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Game Development: Pygame và Panda3D cho phép tạo game 2D và 3D đơn giản.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

# ============================================
# CHAPTER 2
# ============================================
doc.add_page_break()
add_heading(doc, 'Chương 2. NỀN TẢNG NGÔN NGỮ PYTHON', level=1)

add_heading(doc, '2.1. Cú pháp và indentation', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Điểm khác biệt rõ rệt nhất giữa Python và nhiều ngôn ngữ khác là cách Python sử dụng indentation (thụt lề) để xác định cấu trúc khối lệnh. Trong C++ hay Java, bạn dùng dấu ngoặc nhọn {} để bao quanh các câu lệnh trong if, for, function. Còn trong Python, indentation thực hiện vai trò đó.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Quy tắc indentation trong Python khá nghiêm ngặt: các câu lệnh trong cùng một khối phải có cùng độ thụt lề, thường là 4 khoảng trắng (hoặc 1 tab). Nếu bạn trộn lẫn tab và khoảng trắng, hoặc sai lệch indentation, Python sẽ báo lỗi SyntaxError.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

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

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Sự khác biệt này khiến nhiều người mới học Python thấy khó lúc ban đầu, nhưng về lâu dài, indentation giúp mã nguồn trở nên rõ ràng hơn, tránh được tình trạng "spaghetti code" — mã rối ren do thiếu cấu trúc khối lệnh.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, '2.2. Biến và dynamic typing', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Trong Python, biến không phải là "khối bộ nhớ" mang một kiểu cố định như trong C++. Thay vào đó, biến là một tên gọi (name) tham chiếu đến một object trong bộ nhớ. Object mới mang kiểu dữ liệu, còn biến thì không.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''x = 10          # x tham chiếu đến object int(10)
print(type(x))  # <class 'int'>

x = "Hello"     # x giờ tham chiếu đến object str("Hello")
print(type(x))  # <class 'str'>

x = [1, 2, 3]   # x giờ tham chiếu đến object list
print(type(x))  # <class 'list'>''', 'Code 2. Dynamic typing trong Python')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Cơ chế này gọi là dynamic typing: kiểu dữ liệu được xác định tại runtime, không phải compile-time. Điều này mang lại sự linh hoạt cao, nhưng cũng đòi hỏi lập trình viên phải cẩn thận hơn vì lỗi kiểu dữ liệu chỉ phát sinh khi chương trình chạy, không phải khi biên dịch.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, '2.3. Các kiểu dữ liệu cơ bản', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python có tám kiểu dữ liệu cơ bản, chia thành hai nhóm: số học và sequence/mapping.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_table(doc,
    ['Kiểu', 'Mô tả', 'Ví dụ'],
    [
        ['int', 'Số nguyên', '42, -7, 0'],
        ['float', 'Số thực', '3.14, -0.5, 2.0'],
        ['bool', 'Giá trị logic', 'True, False'],
        ['str', 'Chuỗi ký tự', '"Hello", \'Python\''],
        ['list', 'Danh sách có thứ tự', '[1, 2, 3]'],
        ['tuple', 'Bộ bất biến', '(1, 2, 3)'],
        ['set', 'Tập hợp không trùng lặp', '{1, 2, 3}'],
        ['dict', 'Từ điển khóa-giá trị', '{"a": 1, "b": 2}'],
    ],
    'Bảng 1. Các kiểu dữ liệu cơ bản trong Python')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('List và tuple đều là các sequence có thứ tự, nhưng list có thể thay đổi được (mutable), còn tuple thì không (immutable). Dict lưu trữ dữ liệu dưới dạng cặp khóa-giá trị, cho phép truy xuất nhanh chóng theo khóa. Set là tập hợp các phần tử duy nhất, không có thứ tự, thường dùng để loại bỏ trùng lặp.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, '2.4. Cấu trúc điều khiển', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python hỗ trợ đầy đủ các cấu trúc điều khiển cơ bản: if/elif/else, for, while. Khác biệt lớn nhất là for trong Python hoạt động như foreach — nó lặp qua từng phần tử của một iterable, chứ không dựa trên chỉ số như trong C++.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''# if/elif/else
age = 20
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

# for loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# while loop
n = 0
while n < 3:
    print(n)
    n += 1

# break và continue
for i in range(10):
    if i == 3:
        continue  # bỏ qua lần lặp này
    if i == 7:
        break     # thoát vòng lặp
    print(i)''', 'Code 3. Cấu trúc điều khiển trong Python')

add_heading(doc, '2.5. Function', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Function trong Python được định nghĩa bằng từ khóa def. Python hỗ trợ nhiều loại parameter: positional argument, keyword argument, default argument, và variadic argument (*args, **kwargs). Điều này cho phép function rất linh hoạt trong cách gọi.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''def greet(name, greeting="Hello", times=1):
    for _ in range(times):
        print(f"{greeting}, {name}!")

greet("Alice")                  # Hello, Alice!
greet("Bob", "Hi")             # Hi, Bob!
greet("Carol", times=3)        # Carol được chào 3 lần

# *args và **kwargs
def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(sum_all(1, 2, 3, 4))     # 10
print_info(name="An", age=20)  # name: An, age: 20''', 'Code 4. Định nghĩa và gọi function trong Python')

# ============================================
# CHAPTER 3
# ============================================
doc.add_page_break()
add_heading(doc, 'Chương 3. NHỮNG ĐẶC TRƯNG THÚ VỊ CỦA PYTHON', level=1)

add_heading(doc, '3.1. List comprehension', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('List comprehension là một trong những tính năng được yêu thích nhất của Python. Nó cho phép tạo list mới từ một iterable có sẵn bằng một cú pháp ngắn gọn, đọc như tiếng Anh. Đây không chỉ là thủ thuật viết code nhanh — nó còn giúp mã nguồn trở nên súc tích và dễ hiểu hơn nhiều so với vòng lặp thông thường.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''# Cách viết truyền thống
squares = []
for x in range(10):
    squares.append(x * x)

# List comprehension
squares = [x * x for x in range(10)]

# Có điều kiện
evens = [x for x in range(20) if x % 2 == 0]

# Nested list comprehension
matrix = [[i*j for j in range(1,4)] for i in range(1,4)]''', 'Code 5. List comprehension trong Python')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('List comprehension cũng hỗ trợ điều kiện if và thậm chí if-else, cho phép tạo ra các list phức tạp mà không cần nhiều dòng code. Ngoài ra, Python còn có dict comprehension và set comprehension với cú pháp tương tự.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, '3.2. Multiple assignment', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python cho phép gán nhiều biến cùng lúc bằng cách tách chúng bằng dấu phẩy. Tính năng này rất hữu ích khi hoán đổi giá trị giữa các biến — một tác vụ mà trong C++ hay Java đòi hỏi phải dùng biến trung gian.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''# Gán nhiều giá trị
a, b, c = 10, 20, 30

# Hoán đổi giá trị (không cần biến trung gian)
a, b = b, a
print(a, b)  # 20 10

# Gán từ iterable
first, *rest = [1, 2, 3, 4, 5]
print(first)   # 1
print(rest)    # [2, 3, 4, 5]''', 'Code 6. Multiple assignment và unpacking')

add_heading(doc, '3.3. Unpacking', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Unpacking mở rộng từ multiple assignment, cho phép gán các phần tử của iterable (list, tuple, string) vào nhiều biến riêng lẻ. Python 3 còn hỗ trợ starred expression (*) để gộp nhiều phần tử còn lại vào một biến.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''# Unpacking cơ bản
names = ["An", "Binh", "Cuong"]
a, b, c = names
print(a, b, c)  # An Binh Cuong

# Starred expression
first, *middle, last = [1, 2, 3, 4, 5]
print(first)     # 1
print(middle)    # [2, 3, 4]
print(last)      # 5

# Unpacking dict
person = {"name": "An", "age": 20}
for key, value in person.items():
    print(f"{key}: {value}")''', 'Code 7. Unpacking trong Python')

add_heading(doc, '3.4. enumerate()', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Hàm enumerate() là một công cụ hữu ích khi cần lặp qua một iterable và đồng thời lấy cả chỉ số (index) của phần tử. Thay vì phải tự tạo biến đếm riêng, bạn có thể dùng enumerate để nhận cả index và giá trị cùng lúc.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''names = ["An", "Binh", "Cuong"]

# Không dùng enumerate
for i in range(len(names)):
    print(i, names[i])

# Dùng enumerate
for i, name in enumerate(names):
    print(i, name)

# Bắt đầu chỉ số từ 1
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")''', 'Code 8. Sử dụng enumerate()')

add_heading(doc, '3.5. zip()', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Hàm zip() ghép các iterable lại với nhau theo từng cặp phần tử tương ứng. Đây là cách tự nhiên để xử lý nhiều danh sách song song cùng lúc, ví dụ như ghép tên học sinh với điểm số.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''names = ["An", "Binh", "Cuong"]
scores = [8, 9, 10]

# Ghép tên với điểm
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Zip nhiều list
letters = ["A", "B", "C"]
for name, score, letter in zip(names, scores, letters):
    print(f"{name} ({letter}): {score}")

# Zip để tạo dict
keys = ["a", "b", "c"]
vals = [1, 2, 3]
d = dict(zip(keys, vals))
print(d)  # {'a': 1, 'b': 2, 'c': 3}''', 'Code 9. Sử dụng zip()')

add_heading(doc, '3.6. Lambda và higher-order functions', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python hỗ trợ functional programming thông qua hàm lambda, map(), filter(), và sorted(). Lambda cho phép tạo function nhỏ, ẩn danh (anonymous function) chỉ trong một dòng. Mặc dù không phải lúc nào cũng cần thiết, lambda rất hữu ích khi bạn cần truyền một function ngắn gọn làm đối số.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''# Lambda cơ bản
square = lambda x: x * x
print(square(5))  # 25

# Map: áp dụng function cho từng phần tử
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8, 10]

# Filter: lọc các phần tử thỏa điều kiện
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

# Sort với key là lambda
students = [("An", 8), ("Binh", 9), ("Cuong", 7)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)  # [('Binh', 9), ('An', 8), ('Cuong', 7)]''', 'Code 10. Lambda và higher-order functions')

add_heading(doc, '3.7. Generator và yield', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Generator là một tính năng mạnh mẽ cho phép tạo ra một sequence giá trị mà không cần lưu toàn bộ vào bộ nhớ. Thay vì return một list hoàn chỉnh, generator dùng từ khóa yield để "đóng gói" từng giá trị và tạm dừng thực thi. Lần gọi tiếp theo, generator tiếp tục từ điểm dừng trước đó.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Sử dụng generator
for num in count_up_to(5):
    print(num, end=" ")  # 1 2 3 4 5

# Generator expression
squares = (x * x for x in range(10))
print(next(squares))  # 0
print(next(squares))  # 1

# So sánh với list
nums = [1, 2, 3, 4, 5]
sq_list = [x*x for x in nums]    # tạo list trong RAM
sq_gen = (x*x for x in nums)     # tạo generator

print(type(sq_list))  # <class 'list'>
print(type(sq_gen))   # <class 'generator'>''', 'Code 11. Generator và yield trong Python')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Sự khác biệt then chốt giữa return và yield là: return kết thúc hoàn toàn function và trả về một giá trị duy nhất, còn yield tạm dừng function và trả về một giá trị, giữ nguyên trạng thái để tiếp tục lần sau. Generator đặc biệt hữu ích khi xử lý dữ liệu lớn vì chúng tiết kiệm bộ nhớ đáng kể.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, '3.8. Exception handling', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python xử lý lỗi thông qua cơ chế exception. Thay vì kiểm tra lỗi thủ công như trong C (kiểm tra return value), Python cho phép bắt ngoại lệ bằng try-except, giúp mã nguồn sạch hơn và dễ đọc hơn nhiều.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: chia cho 0!")
        return None
    except TypeError:
        print("Error: kiểu dữ liệu không hợp lệ!")
        return None
    else:
        print(f"Result: {result}")
        return result
    finally:
        print("Operation finished.")

divide(10, 2)    # Result: 5.0, Operation finished.
divide(10, 0)    # Error: chia cho 0!, Operation finished.
divide("10", 2)  # Error: kiểu dữ liệu không hợp lệ!, Operation finished.

# Raise exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age''', 'Code 12. Exception handling trong Python')

add_heading(doc, '3.9. Context manager và with', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Context manager là một tính năng cho phép quản lý tài nguyên một cách tự động. Từ khóa with đảm bảo rằng tài nguyên sẽ được giải phóng đúng lúc, bất kể program có bị lỗi hay không. Điều này đặc biệt quan trọng khi làm việc với file, database connection, hay network socket.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''# Không dùng with (kém an toàn)
file = open("data.txt", "r")
content = file.read()
file.close()  # Có thể quên nếu có lỗi giữa chừng

# Dùng with (an toàn hơn)
with open("data.txt", "r") as file:
    content = file.read()
# File tự động đóng sau khi ra khỏi блок

# Context manager tùy chỉnh
from contextlib import contextmanager

@contextmanager
def timer(label):
    import time
    start = time.time()
    yield
    end = time.time()
    print(f"{label}: {end - start:.4f}s")

with timer("Tính toán"):
    sum(x**2 for x in range(1000000))''', 'Code 13. Context manager và with')

add_heading(doc, '3.10. Decorator', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Decorator là một tính năng nâng cao cho phép "bao bọc" (wrap) một function hiện có bằng một function khác, thêm hành vi mới mà không sửa đổi code gốc. Decorator được ký hiệu bằng @ và thường dùng cho logging, timing, authentication, hay caching.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''def log_call(func):
    def wrapper():
        print("Function started")
        func()
        print("Function finished")
    return wrapper

@log_call
def hello():
    print("Hello Python")

hello()
# Output:
# Function started
# Hello Python
# Function finished

# Decorator nhận tham số
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")''', 'Code 14. Decorator trong Python')

# ============================================
# CHAPTER 4
# ============================================
doc.add_page_break()
add_heading(doc, 'Chương 4. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON', level=1)

add_heading(doc, '4.1. Class và object', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python hỗ trợ lập trình hướng đối tượng (OOP) thông qua class. Một class là bản thiết kế (blueprint) để tạo ra object — thực thể cụ thể mang các thuộc tính và phương thức xác định. Khác với C++ hay Java, Python không yêu cầu định nghĩa class theo kiểu interface riêng biệt; mọi class đều kế thừa trực tiếp hoặc gián tiếp từ class object.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, '4.2. Constructor', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Constructor trong Python là phương thức __init__. Phương thức này được gọi tự động khi tạo object mới, thường dùng để khởi tạo các thuộc tính ban đầu. Không giống như các ngôn ngữ khác, Python không có method overload theo nghĩa truyền thống — bạn phải dùng default argument hoặc *args/**kwargs để đạt được hiệu ứng tương tự.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, '4.3. Instance attribute và method', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Instance attribute là biến thuộc về một object cụ thể, được định nghĩa trong __init__ hoặc gán trực tiếp sau khi tạo object. Instance method là function được định nghĩa trong class và nhận self làm đối số đầu tiên — self chính là reference đến object đang gọi method đó.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, '4.4. Inheritance', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Inheritance (kế thừa) cho phép một class con thừa hưởng thuộc tính và phương thức từ class cha. Python hỗ trợ đa kế thừa (multiple inheritance), nghĩa là một class có thể kế thừa từ nhiều class cùng lúc. Tuy nhiên, đa kế thừa cần được sử dụng thận trọng để tránh xung đột method resolution order (MRO).')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, '4.5. Polymorphism', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Polymorphism (đa hình) trong Python xảy ra tự nhiên nhờ duck typing: "nếu nó đi như vịt và gọi như vịt, thì nó là vịt." Bạn không cần định nghĩa interface hay abstract class; miễn là object có method cùng tên, nó có thể được dùng thay thế nhau.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(Dog())  # Woof!
make_animal_speak(Cat())  # Meow!

# Duck typing
def introduce(obj):
    print(f"Name: {obj.name}, Sound: {obj.speak()}")

introduce(Dog())  # Work without explicit interface''', 'Code 15. OOP trong Python')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Nhìn chung, Python hỗ trợ OOP đầy đủ, nhưng cách tiếp cận nhẹ nhàng hơn Java hay C++. Bạn có thể bắt đầu với procedural programming và dần chuyển sang OOP khi cần, mà không bị ép buộc phải thiết kế lớp từ đầu.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

# ============================================
# CHAPTER 5
# ============================================
doc.add_page_break()
add_heading(doc, 'Chương 5. PYTHON STANDARD LIBRARY', level=1)

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Standard Library của Python là tập hợp các module và package được đóng gói sẵn cùng với ngôn ngữ. Nó cung cấp các công cụ hữu ích cho hầu hết mọi tác vụ lập trình thông thường, từ xử lý file, làm việc với date/time, cho đến biểu thức chính quy. Việc có sẵn standard library chất lượng cao là một trong những lý do khiến Python trở nên phổ biến — lập trình viên không cần tìm kiếm thư viện bên ngoài cho những tác vụ cơ bản.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, 'pathlib và os', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('pathlib (Python 3.4+) cung cấp một cách hiện đại để làm việc với đường dẫn file system. Thay vì dùng chuỗi ký tự và các hàm os.path rời rạc, pathlib tạo ra các object Path đại diện cho đường dẫn, cho phép thao tác theo hướng đối tượng.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''from pathlib import Path

path = Path("data.txt")
path.write_text("Hello Python")
print(path.read_text())        # Hello Python
print(path.exists())           # True
print(path.parent)             # .
print(path.stem)               # data
print(path.suffix)             # .txt''', 'Code 16. pathlib cơ bản')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Module os cung cấp các hàm tương tác với hệ điều hành: tạo/xóa thư mục, liệt kê file, lấy thông tin hệ thống. Os thường dùng khi cần thao tác ở mức thấp hơn pathlib.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, 'math, random, datetime', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Module math chứa các hàm toán học cơ bản và nâng cao: căn bậc hai, logarit, lượng giác, hằng số pi/e. Module random sinh số ngẫu nhiên, phục vụ cho mô phỏng, game, hoặc sampling. Module datetime làm việc với ngày giờ, bao gồm timedelta để tính khoảng thời gian.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, 'json và re', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('json module cho phép serialize/deserialize dữ liệu giữa Python object và định dạng JSON — định dạng trao đổi dữ liệu phổ biến nhất trên web hiện nay. Module re cung cấp hỗ trợ cho regular expression, cho phép tìm kiếm và xử lý chuỗi theo mẫu quy tắc.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''import json
import re

# JSON
data = {"name": "An", "age": 20}
json_str = json.dumps(data)        # Serialize
parsed = json.loads(json_str)      # Deserialize

# Regular expression
text = "Contact us at support@example.com"
pattern = r"[\\w.]+@[\\w.]+\\.com"
match = re.search(pattern, text)
print(match.group())  # support@example.com''', 'Code 17. json và re module')

add_heading(doc, 'collections', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Module collections mở rộng các kiểu dữ liệu built-in với Counter (đếm tần suất), defaultdict (dict với giá trị mặc định), namedtuple (tuple có tên), deque (danh sách hai đầu), và OrderedDict. Những lớp này thường hiệu quả hơn và tiện lợi hơn so với việc tự implement.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''from collections import Counter, defaultdict, deque

# Counter: đếm tần suất
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
cnt = Counter(words)
print(cnt.most_common(2))  # [('apple', 3), ('banana', 2)]

# defaultdict: giá trị mặc định
grouped = defaultdict(list)
for name, group in [("An", "A"), ("Binh", "B"), ("Cuong", "A")]:
    grouped[group].append(name)
print(grouped)  # {'A': ['An', 'Cuong'], 'B': ['Binh']}

# Deque: danh sách hai đầu
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.pop()
print(dq)  # deque([0, 1, 2])''', 'Code 18. collections module')

# ============================================
# CHAPTER 6
# ============================================
doc.add_page_break()
add_heading(doc, 'Chương 6. HỆ SINH THÁI THƯ VIỆN PYTHON', level=1)

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Hệ sinh thái thư viện Python là một trong những lợi thế lớn nhất của ngôn ngữ này. Chỉ với một lệnh pip install, bạn có thể tiếp cận hàng chục nghìn package được viết bởi cộng đồng toàn cầu. Mỗi package giải quyết một vấn đề cụ thể, từ xử lý số học đến xây dựng giao diện đồ họa.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, 'Khoa học dữ liệu và tính toán số', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('NumPy là nền tảng của mọi thư viện khoa học trong Python. Nó cung cấp mảng nhiều chiều (ndarray) và các hàm toán học tối ưu cho tính toán số học. Pandas xây dựng trên NumPy, thêm vào đó là DataFrame — cấu trúc dữ liệu bảng giống như trong R hay SQL, cực kỳ hữu ích cho xử lý dữ liệu có cấu trúc.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Matplotlib là thư viện chuẩn để vẽ biểu đồ, đồ thị trong Python. Từ biểu đồ đường, Histogram, đến heatmap — Matplotlib cung cấp hầu hết mọi loại visualization cơ bản. Seaborn, được xây dựng trên Matplotlib, giúp tạo các biểu đồ thống kê đẹp mắt hơn với ít code hơn.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, 'Machine Learning và Deep Learning', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Scikit-learn là thư viện machine learning phổ biến nhất, cung cấp các thuật toán từ cổ điển như hồi quy tuyến tính, SVM, decision tree đến các kỹ thuật tiền xử lý dữ liệu và evaluation. PyTorch và TensorFlow là hai framework deep learning hàng đầu, được Google và Meta (Facebook) phát triển riêng, phục vụ cho việc xây dựng và huấn luyện các mô hình neural network phức tạp.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, 'Web Development', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Django là web framework "full-stack" nặng ký, đi kèm sẵn hệ thống admin, ORM, authentication. Flask là micro-framework nhẹ nhàng hơn, cho phép xây dựng application theo cách tùy ý. FastAPI là sự lựa chọn mới, nổi tiếng với tốc độ cao nhờ async/await và tự động sinh documentation từ type hints.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, 'Network và Web Scraping', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Requests là thư viện HTTP được sử dụng rộng rãi nhất, giúp gửi request GET/POST một cách dễ dàng. BeautifulSoup kết hợp với Requests cho phép trích xuất dữ liệu từ trang web (web scraping) — một kỹ thuật quan trọng trong data collection và competitive intelligence.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_table(doc,
    ['Thư viện', 'Lĩnh vực', 'Mô tả ngắn'],
    [
        ['NumPy', 'Scientific computing', 'Mảng đa chiều và toán học số'],
        ['Pandas', 'Data analysis', 'DataFrame xử lý dữ liệu có cấu trúc'],
        ['Matplotlib', 'Visualization', 'Vẽ biểu đồ, đồ thị'],
        ['Scikit-learn', 'Machine learning', 'Thuật toán ML cổ điển'],
        ['PyTorch', 'Deep learning', 'Neural network (Meta)'],
        ['TensorFlow', 'Deep learning', 'Neural network (Google)'],
        ['Django', 'Web development', 'Full-stack web framework'],
        ['Flask', 'Web development', 'Micro web framework'],
        ['FastAPI', 'Web development', 'High-performance API framework'],
        ['Requests', 'HTTP', 'Gửi HTTP request dễ dàng'],
    ],
    'Bảng 2. Một số thư viện Python phổ biến và lĩnh vực sử dụng')

# ============================================
# CHAPTER 7
# ============================================
doc.add_page_break()
add_heading(doc, 'Chương 7. ỨNG DỤNG THỰC TẾ', level=1)

add_heading(doc, 'Tự động hóa file', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Một trong những ứng dụng đơn giản nhưng mạnh mẽ nhất của Python là tự động hóa các tác vụ file system. Giả sử bạn cần đổi tên hàng trăm file ảnh, di chuyển file theo định dạng, hoặc hợp nhất nhiều file Excel thành một — Python thực hiện những việc này chỉ trong vài chục dòng code.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''from pathlib import Path
import shutil

folder = Path("photos")
jpg_files = folder.glob("*.jpg")

for idx, src in enumerate(jpg_files, start=1):
    dest = folder / f"IMG_{idx:03d}.jpg"
    shutil.move(src, dest)
    print(f"Renamed: {src} -> {dest}")''', 'Code 19. Tự động đổi tên file')

add_heading(doc, 'Xử lý dữ liệu', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python kết hợp với Pandas và NumPy tạo thành bộ công cụ xử lý dữ liệu mạnh mẽ. Từ việc đọc file CSV, xử lý missing values, đến tính toán thống kê cơ bản — tất cả đều có thể làm được chỉ trong vài dòng code.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''import pandas as pd

df = pd.read_csv("data.csv")
print(df.describe())          # Thống kê tóm tắt
print(df.groupby("category").mean())  # Tính trung bình theo nhóm
df.to_csv("cleaned_data.csv", index=False)''', 'Code 20. Xử lý dữ liệu với Pandas')

add_heading(doc, 'Gọi Web API', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python có thể tương tác với hầu hết các REST API hiện nay. Thư viện Requests giúp gửi request và nhận response một cách đơn giản, trong khi json module xử lý dữ liệu trả về.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_code_block(doc, '''import requests

response = requests.get(
    "https://api.github.com/users/ChillingCpp"
)
data = response.json()
print(f"Username: {data['login']}")
print(f"Repos: {data['public_repos']}")''', 'Code 21. Gọi REST API với Requests')

add_heading(doc, 'AI / Machine Learning', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Pipeline machine learning điển hình trong Python bao gồm: thu thập dữ liệu (requests, pandas) → tiền xử lý (numpy, sklearn.preprocessing) → huấn luyện mô hình (sklearn, tensorflow/pytorch) → đánh giá và deploy. Python thống trị hoàn toàn trong lĩnh vực AI hiện nay.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

# ============================================
# CHAPTER 8
# ============================================
doc.add_page_break()
add_heading(doc, 'Chương 8. MỘT SỐ KHÍA CẠNH NÂNG CAO VÀ ĐẶC TRƯNG', level=1)

add_heading(doc, 'Python mở rộng bằng C/C++', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Mặc dù Python là ngôn ngữ thông dịch, nhưng nó cho phép viết extension bằng C/C++ thông qua Python/C API. Nhiều thư viện performance-critical (NumPy, Pandas, TensorFlow) thực chất là wrapper xung quanh code C/C++, cho phép Python tận hưởng tốc độ của mã native trong khi vẫn giữ cú pháp tiện lợi.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, 'Python bytecode và Python Virtual Machine', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Khi chạy một file Python, interpreter đầu tiên đọc và parse source code thành Abstract Syntax Tree (AST). Sau đó, AST được biên dịch thành bytecode — một dạng mã trung gian. Bytecode này được thực thi bởi Python Virtual Machine (PVM), tương tự như cách Java bytecode chạy trên JVM.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Quy trình này giải thích tại sao file .pyc (compiled Python) tồn tại: khi một module được import lần đầu, bytecode được lưu lại để lần sau không cần parse lại. Dù vậy, bytecode vẫn cần PVM để thực thi — khác với mã machine code trực tiếp của C/C++.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, 'Hiệu năng của Python', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python không phải là ngôn ngữ nhanh nhất. Việc dynamic typing và interpretation overhead khiến Python thường chậm hơn C/C++ từ 10 đến 100 lần trong các tác vụ CPU-bound thuần túy. Tuy nhiên, sự chênh lệch này thường bị phóng đại trong thực tế, vì:')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Hầu hết các tác vụ Python không chạy CPU-bound thuần túy: chúng phụ thuộc I/O (file, network, database), nơi Python có thể vượt trội nhờ async/await.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Thư viện native: NumPy, Pandas chạy code tính toán trong C, nên speedup đáng kể.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Developer productivity: Viết code nhanh hơn, debug dễ hơn, maintain tốt hơn — điều này quan trọng hơn nhiều trong thực tế so với micro-optimization.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

# ============================================
# CHAPTER 9
# ============================================
doc.add_page_break()
add_heading(doc, 'Chương 9. ƯU ĐIỂM VÀ HẠN CHẾ', level=1)

add_heading(doc, 'Ưu điểm', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Syntax dễ đọc, dễ học: Giảm rào cản gia nhập với người mới, tăng tốc độ phát triển.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Rapid development:写完 code trong vài giờ thay vì vài ngày so với C++/Java.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Ecosystem phong phú: Hàng trăm nghìn package trên PyPI cover mọi lĩnh vực.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Versatility: Một ngôn ngữ cho nhiều mục đích — từ script nhỏ đến hệ thống lớn.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Cộng đồng lớn: Tài liệu phong phú, stackoverflow, forum, tutorial đầy đủ.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

add_heading(doc, 'Hạn chế', level=2)
p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Performance: Chậm hơn C/C++ trong CPU-bound tasks do dynamic typing và interpretation.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Memory usage: Object model của Python tiêu thụ nhiều bộ nhớ hơn C++ tương đương.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Runtime errors: Dynamic typing có thể gây lỗi kiểu dữ liệu lúc chạy chương trình, khó phát hiện lúc compile.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('• Dependency management: Quản lý package và version có thể phức tạp, đặc biệt với dự án lớn.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('•不适合 real-time systems: Không phù hợp cho embedded systems hay low-level programming cần độ trễ cực thấp.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

# ============================================
# CHAPTER 10
# ============================================
doc.add_page_break()
add_heading(doc, 'Chương 10. SO SÁNH VỚI MỘT SỐ NGÔN NGỮ', level=1)

add_table(doc,
    ['Tiêu chí', 'Python', 'C++', 'Java', 'JavaScript'],
    [
        ['Syntax', 'Đơn giản, readable', 'Phức tạp', 'Trung bình', 'Đơn giản'],
        ['Typing', 'Dynamic', 'Static', 'Static', 'Dynamic'],
        ['Performance', 'Trung bình-thấp', 'Cao', 'Trung bình', 'Trung bình'],
        ['Memory', 'Tự động (GC)', 'Thủ công', 'Tự động (GC)', 'Tự động (GC)'],
        ['ECOSYSTEM', 'Rất lớn (PyPI)', 'Trung bình', 'Lớn (Maven)', 'Rất lớn (NPM)'],
        ['Phù hợp', 'Data/AI/Web', 'System/Game', 'Enterprise', 'Web/App'],
        ['Learning curve', 'Thấp', 'Cao', 'Trung bình', 'Thấp-trung bình'],
    ],
    'Bảng 3. So sánh Python với C++, Java và JavaScript')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Về syntax, Python rõ ràng dễ đọc hơn C++ và Java nhờ loại bỏ dấu ngoặc nhọn và chấm phẩy. Về typing, Python dynamic còn C++/Java static — điều này có nghĩa là lỗi kiểu trong Python thường xuất hiện lúc runtime, nhưng code viết nhanh và linh hoạt hơn. JavaScript cũng dynamic typing nhưng cú pháp khác xa Python.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Về performance, C++ luôn đứng đầu do biên dịch trực tiếp sang machine code. Java có JIT compilation giúp cải thiện đáng kể. Python vẫn chậm nhất, nhưng sự chênh lệch thường không quan trọng nếu task không CPU-bound.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Về lĩnh vực sử dụng, mỗi ngôn ngữ có thế mạnh riêng: Python chiếm ưu thế ở Data/AI, C++ dominate systems programming và game engine, Java thống trị enterprise backend, còn JavaScript thống trị web frontend.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

# ============================================
# KẾT LUẬN
# ============================================
doc.add_page_break()
add_heading(doc, 'KẾT LUẬN', level=1)

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Python không đơn thuần là một ngôn ngữ lập trình — nó là một hệ sinh thái hoàn chỉnh bao gồm ngôn ngữ, standard library, cộng đồng, và hàng nghìn thư viện bên thứ ba. Từ khi ra đời năm 1991, Python đã phát triển từ một dự án cá nhân của Guido van Rossum trở thành một trong những ngôn ngữ được sử dụng phổ biến nhất thế giới.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Những đặc điểm then chốt làm nên sự thành công của Python là: cú法 dễ đọc, dynamic typing linh hoạt, hệ sinh thái thư viện phong phú, và khả năng cross-platform. Python phù hợp với hầu hết mọi loại dự — từ automation script đơn giản, web application, data analysis, machine learning, đến education. Sự phổ biến của Python trong giáo dục cũng là một yếu tố then chốt: thế hệ lập trình viên tương lai được dạy Python trước tiên, tạo nên một vòng lặp củng cố vị trí của ngôn ngữ.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Tuy nhiên, Python không phải là giải pháp cho mọi vấn đề. Performance kém hơn C++/Rust trong các tác vụ tính toán nặng, memory overhead cao hơn, và dynamic typing có thể gây rủi ro runtime error. Đối với real-time systems hay embedded programming, Python thường không phải sự lựa chọn tối ưu.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

p = doc.add_paragraph()
set_justify(p)
run = p.add_run('Dưới góc nhìn của một sinh viên, Python là ngôn ngữ đáng học nhất hiện nay. Không chỉ vì cú法 thân thiện, mà còn vì nó mở ra cánh cửa đến nhiều lĩnh vực hot như AI, data science, và web development. Dù có những hạn chế nhất định, Python vẫn giữ vững vị thế là ngôn ngữ lập trình phổ biến bậc nhất thế giới, và xu hướng này dự kiến sẽ tiếp tục mạnh mẽ trong nhiều năm tới.')
run.font.name = 'Times New Roman'
run.font.size = Pt(13)
run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

# ============================================
# TÀI LIỆU THAM KHẢO
# ============================================
doc.add_page_break()
add_heading(doc, 'TÀI LIỆU THAM KHẢO', level=1)

refs = [
    '[1] Python Software Foundation. Python Documentation. https://docs.python.org/3/',
    '[2] Van Rossum, G., & Drake, F. L. (2009). Python 3 Reference Manual. CreateSpace.',
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

# Save document
doc.save(r'C:\Users\Admin\Desktop\baitap\BaoCao_Python.docx')
print("Document created successfully: BaoCao_Python.docx")
