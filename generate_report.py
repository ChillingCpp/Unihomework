#!/usr/bin/env python3
"""
Tạo báo cáo học tập: TÌM HIỂU NGÔN NGỮ LẬP TRÌNH PYTHON
Định dạng: Microsoft Word (.docx)
Mục tiêu: 17-19 trang A4, Times New Roman 13, line spacing 1.5, justify
"""

from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
import copy

# ============================================================
# Helper functions for formatting
# ============================================================

DOC_FONT = "Times New Roman"
CODE_FONT = "Consolas"
BODY_SIZE = Pt(13)
HEADING1_SIZE = Pt(18)
HEADING2_SIZE = Pt(15)
HEADING3_SIZE = Pt(14)
LINE_SPACING = 1.5

def set_run_font(run, font_name=DOC_FONT, size=None, bold=False, italic=False):
    run.font.name = font_name
    run.font.size = size or BODY_SIZE
    run.bold = bold
    run.italic = italic
    run.element.rPr.rFonts.set(qn('w:eastAsia'), font_name)

def set_paragraph_alignment(para, alignment):
    para.alignment = alignment
    jf = para.paragraph_format
    jf.line_spacing = LINE_SPACING
    jf.space_after = Pt(6)
    jf.space_before = Pt(4)

def add_heading_custom(doc, text, level=1):
    sizes = {1: HEADING1_SIZE, 2: HEADING2_SIZE, 3: HEADING3_SIZE}
    p = doc.add_paragraph()
    if level == 1:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    set_run_font(run, bold=True, size=sizes.get(level, BODY_SIZE))
    jp = p.paragraph_format
    jp.line_spacing = LINE_SPACING
    jp.space_after = Pt(8)
    jp.space_before = Pt(10)
    return p

def add_body(doc, text, bold=False, indent=False):
    p = doc.add_paragraph()
    set_paragraph_alignment(p, WD_ALIGN_PARAGRAPH.JUSTIFY)
    run = p.add_run(text)
    set_run_font(run, bold=bold)
    if indent:
        p.paragraph_format.first_line_indent = Cm(1.27)
    return p

def add_bullet(doc, text, level=0):
    p = doc.add_paragraph(style='List Bullet')
    set_paragraph_alignment(p, WD_ALIGN_PARAGRAPH.JUSTIFY)
    # Adjust indent based on level
    if level > 0:
        p.paragraph_format.left_indent = Cm(1.27 * (level + 1))
    run = p.add_run(text)
    set_run_font(run)
    return p

def add_code_block(doc, code_text, caption=""):
    """Add a code block in a bordered paragraph with Consolas font."""
    # Add a border frame using a table with single cell
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    
    # Remove table borders and add paragraph border instead
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}></w:tblPr>')
    
    # Clear existing cell content
    cell.paragraphs[0].clear()
    
    # Add code as a paragraph inside the cell
    p = cell.paragraphs[0]
    set_paragraph_alignment(p, WD_ALIGN_PARAGRAPH.LEFT)
    p.paragraph_format.left_indent = Cm(0.5)
    p.paragraph_format.right_indent = Cm(0.5)
    
    # Set cell shading for light gray background
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F5F5F5" w:val="clear"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)
    
    # Add border to the cell
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        '  <w:top w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '  <w:left w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '  <w:right w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '</w:tcBorders>'
    )
    tc_pr.append(tc_borders)
    
    lines = code_text.strip().split('\n')
    for i, line in enumerate(lines):
        run = p.add_run(line + ('\n' if i < len(lines) - 1 else ''))
        set_run_font(run, font_name=CODE_FONT, size=Pt(10))
    
    # Add caption below
    if caption:
        cap_p = doc.add_paragraph()
        set_paragraph_alignment(cap_p, WD_ALIGN_PARAGRAPH.CENTER)
        cap_run = cap_p.add_run(caption)
        set_run_font(cap_run, italic=True, size=Pt(10))
    
    doc.add_paragraph()  # blank line after code
    return table

def add_image_placeholder(doc, number, title):
    """Add an image placeholder box with caption."""
    p = doc.add_paragraph()
    set_paragraph_alignment(p, WD_ALIGN_PARAGRAPH.CENTER)
    
    # Create a small placeholder box
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    cell.width = Inches(4.5)
    
    # Light gray background
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="E8E8E8" w:val="clear"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)
    
    # Border
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        '  <w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
        '  <w:left w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
        '  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
        '  <w:right w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
        '</w:tcBorders>'
    )
    tc_pr.append(tc_borders)
    
    ip = cell.paragraphs[0]
    ip.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ip.paragraph_format.space_before = Pt(20)
    ip.paragraph_format.space_after = Pt(20)
    run = ip.add_run(f"[{title}]\n\n[Điền hình vào đây]")
    set_run_font(run, italic=True, size=Pt(11))
    
    # Caption below
    cap_p = doc.add_paragraph()
    set_paragraph_alignment(cap_p, WD_ALIGN_PARAGRAPH.CENTER)
    cap_run = cap_p.add_run(f"Hình {number}. {title}")
    set_run_font(cap_run, italic=True, size=Pt(10))
    
    doc.add_paragraph()
    return table

def add_table_custom(doc, headers, rows, col_widths=None):
    """Add a formatted table with header styling."""
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = 'Table Grid'
    
    # Header row
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        set_run_font(run, bold=True, size=Pt(11))
        # Dark header background
        shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="4472C4" w:val="clear"/>')
        cell._tc.get_or_add_tcPr().append(shading_elm)
        run.font.color.rgb = RGBColor(255, 255, 255)
    
    # Data rows
    for r_idx, row_data in enumerate(rows):
        for c_idx, val in enumerate(row_data):
            cell = table.cell(r_idx + 1, c_idx)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(str(val))
            set_run_font(run, size=Pt(11))
            # Alternate row colors
            if r_idx % 2 == 0:
                shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="D9E2F3" w:val="clear"/>')
                cell._tc.get_or_add_tcPr().append(shading_elm)
    
    # Set column widths if provided
    if col_widths:
        for i, w in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = w
    
    # Table caption
    cap_p = doc.add_paragraph()
    set_paragraph_alignment(cap_p, WD_ALIGN_PARAGRAPH.CENTER)
    cap_run = cap_p.add_run(table.caption if hasattr(table, 'caption') and table.caption else "")
    set_run_font(cap_run, italic=True, size=Pt(10))
    
    doc.add_paragraph()
    return table

def add_column_section(doc, left_text, right_text):
    """Create a two-column section."""
    # We'll use a 2-column table approach for reliable cross-platform rendering
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Left column
    left_cell = table.cell(0, 0)
    lp = left_cell.paragraphs[0]
    set_paragraph_alignment(lp, WD_ALIGN_PARAGRAPH.JUSTIFY)
    run = lp.add_run(left_text)
    set_run_font(run)
    
    # Right column
    right_cell = table.cell(0, 1)
    rp = right_cell.paragraphs[0]
    set_paragraph_alignment(rp, WD_ALIGN_PARAGRAPH.JUSTIFY)
    run = rp.add_run(right_text)
    set_run_font(run)
    
    # Hide table borders
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}></w:tblPr>')
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        '  <w:top w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        '  <w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        '  <w:bottom w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        '  <w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        '  <w:insideH w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        '  <w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        '</w:tblBorders>'
    )
    tblPr.append(tblBorders)
    
    doc.add_paragraph()
    return table


# ============================================================
# MAIN DOCUMENT CREATION
# ============================================================

def main():
    doc = Document()
    
    # Page setup
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    
    # ---- HEADER ----
    header = section.header
    header_para = header.paragraphs[0]
    header_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    header_run = header_para.add_run("TÌM HIỂU NGÔN NGỮ LẬP TRÌNH PYTHON")
    set_run_font(header_run, size=Pt(10), bold=True)
    
    # ---- FOOTER with page numbers ----
    footer = section.footer
    footer_para = footer.paragraphs[0]
    footer_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer_run = footer_para.add_run("Báo cáo môn học — Python   |   Trang ")
    set_run_font(footer_run, size=Pt(10))
    # Add page number field
    fldChar1 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
    instrText = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> PAGE </w:instrText>')
    fldChar2 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
    footer_para.runs[-1]._r.addnext(fldChar1)
    footer_para.runs[-1]._r.addnext(instrText)
    footer_para.runs[-1]._r.addnext(fldChar2)
    
    # ============================================================
    # COVER PAGE
    # ============================================================
    
    # Blank lines to center content
    for _ in range(4):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
    
    # Title
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_p.add_run("BÁO CÁO HỌC TẬP")
    set_run_font(title_run, size=Pt(16), bold=True)
    
    doc.add_paragraph()
    
    main_title_p = doc.add_paragraph()
    main_title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    main_title_run = main_title_p.add_run("TÌM HIỂU\nNGÔN NGỮ LẬP TRÌNH PYTHON")
    set_run_font(main_title_run, size=HEADING1_SIZE, bold=True)
    
    for _ in range(3):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
    
    # Info
    info_items = [
        ("Môn học:", "Lập trình nâng cao"),
        ("Giảng viên hướng dẫn:", "[Tên giảng viên]"),
        ("Sinh viên thực hiện:", "[Tên sinh viên]"),
        ("Mã sinh viên:", "[Mã số]"),
        ("Ngày nộp:", "Tháng 10 năm 2025"),
    ]
    for label, value in info_items:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r1 = p.add_run(label + "\t")
        set_run_font(r1, bold=True)
        r2 = p.add_run(value)
        set_run_font(r2)
    
    # Page break after cover
    doc.add_page_break()
    
    # ============================================================
    # TABLE OF CONTENTS (Manual)
    # ============================================================
    
    toc_p = doc.add_paragraph()
    toc_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    toc_run = toc_p.add_run("MỤC LỤC")
    set_run_font(toc_run, bold=True, size=HEADING1_SIZE)
    doc.add_paragraph()
    
    toc_entries = [
        ("CHƯƠNG 1. TỔNG QUAN VỀ PYTHON", 1),
        ("1.1. Python là gì?", 2),
        ("1.2. Lịch sử phát triển của Python", 2),
        ("1.3. Những đặc điểm nổi bật của Python", 2),
        ("1.4. Các lĩnh vực sử dụng Python", 2),
        ("CHƯƠNG 2. NỀN TẢNG NGÔN NGỮ PYTHON", 1),
        ("2.1. Cú pháp và indentation", 2),
        ("2.2. Biến và dynamic typing", 2),
        ("2.3. Các kiểu dữ liệu cơ bản", 2),
        ("2.4. Cấu trúc điều khiển", 2),
        ("2.5. Function", 2),
        ("CHƯƠNG 3. NHỮNG ĐẶC TRƯNG THÚ VỊ CỦA PYTHON", 1),
        ("3.1. List comprehension", 2),
        ("3.2. Multiple assignment", 2),
        ("3.3. Unpacking", 2),
        ("3.4. enumerate()", 2),
        ("3.5. zip()", 2),
        ("3.6. Lambda và higher-order functions", 2),
        ("3.7. Generator và yield", 2),
        ("3.8. Exception handling", 2),
        ("3.9. Context manager và with", 2),
        ("3.10. Decorator", 2),
        ("CHƯƠNG 4. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON", 1),
        ("4.1. Class và object", 2),
        ("4.2. Constructor", 2),
        ("4.3. Instance attribute và method", 2),
        ("4.4. Inheritance", 2),
        ("4.5. Polymorphism", 2),
        ("CHƯƠNG 5. PYTHON STANDARD LIBRARY", 1),
        ("CHƯƠNG 6. HỆ SINH THÁI THƯ VIỆN PYTHON", 1),
        ("CHƯƠNG 7. ỨNG DỤNG THỰC TẾ", 1),
        ("CHƯƠNG 8. MỘT SỐ KHÍA CẠNH NÂNG CAO VÀ ĐẶC TRƯNG", 1),
        ("CHƯƠNG 9. ƯU ĐIỂM VÀ HẠN CHẾ", 1),
        ("CHƯƠNG 10. SO SÁNH VỚI MỘT SỐ NGÔN NGỮ", 1),
        ("KẾT LUẬN", 1),
        ("TÀI LIỆU THAM KHẢO", 1),
    ]
    
    for entry, level in toc_entries:
        p = doc.add_paragraph()
        if level == 1:
            p.paragraph_format.left_indent = Cm(0)
            run = p.add_run(entry)
            set_run_font(run, bold=True, size=HEADING2_SIZE)
        else:
            p.paragraph_format.left_indent = Cm(1.5)
            run = p.add_run(entry)
            set_run_font(run, size=BODY_SIZE)
        p.paragraph_format.space_after = Pt(2)
    
    doc.add_page_break()
    
    # ============================================================
    # CHAPTER 1: TỔNG QUAN VỀ PYTHON
    # ============================================================
    
    add_heading_custom(doc, "CHƯƠNG 1. TỔNG QUAN VỀ PYTHON", 1)
    
    # --- 1.1 ---
    add_heading_custom(doc, "1.1. Python là gì?", 2)
    
    add_body(doc, 
        "Python là một ngôn ngữ lập trình đa năng, được thiết kế với triết lý nhấn mạnh vào tính dễ đọc và rõ ràng của mã nguồn. "
        "Được tạo ra bởi Guido van Rossum và lần đầu tiên phát hành vào năm 1991, Python đã trở thành một trong những ngôn ngữ "
        "lập trình phổ biến nhất thế giới nhờ sự linh hoạt, cộng đồng người dùng rộng lớn và hệ sinh thái thư viện phong phú."
    )
    
    add_body(doc,
        "Khác với nhiều ngôn ngữ lập trình chỉ tập trung vào một lĩnh vực cụ thể, Python được thiết kế để phục vụ đa dạng mục đích. "
        "Từ việc viết các kịch bản tự động hóa đơn giản đến xây dựng các hệ thống trí tuệ nhân tạo phức tạp, Python đều có thể đảm nhận. "
        "Điều này xuất phát từ cách Python được thiết kế: nó cung cấp cấu trúc dữ liệu cao cấp mặc định, hỗ trợ lập trình hướng đối tượng, "
        "và cho phép tích hợp dễ dàng với các ngôn ngữ khác như C và C++."
    )
    
    add_body(doc,
        "Về mặt phân loại, Python thuộc nhóm ngôn ngữ thông dịch (interpreted language), nghĩa là mã nguồn được thực thi trực tiếp "
        "bằng một máy ảo thay vì được biên dịch thành mã máy trước khi chạy. Python cũng là ngôn ngữ động (dynamically typed), "
        "không yêu cầu khai báo kiểu dữ liệu rõ ràng cho biến. Những đặc điểm này giúp nhà phát triển viết code nhanh hơn nhưng "
        "đồng thời đòi hỏi kỷ luật kiểm thử nghiêm ngặt hơn."
    )
    
    # Image suggestion 1
    add_body(doc, "[ĐỀ XUẤT HÌNH 1: Sơ đồ tổng quan về các lĩnh vực ứng dụng chính của Python — gồm Automation, Web Development, Data Science, AI/ML, Scientific Computing, Education. Mỗi lĩnh vực là một ô hình chữ nhật nối với trung tâm 'Python'. Màu sắc hài hòa, phong cách infographic.", indent=False)
    
    # --- 1.2 ---
    add_heading_custom(doc, "1.2. Lịch sử phát triển của Python", 2)
    
    add_body(doc,
        "Python được bắt đầu phát triển bởi Guido van Rossum, một nhà khoa học máy tính người Hà Lan, vào cuối thập niên 1980. "
        "Guida muốn tạo ra một ngôn ngữ kịch bản kế thừa tinh hoa của ngôn ngữ ABC — một ngôn ngữ ông từng tham gia thiết kế — "
        "nhưng đồng thời khắc phục những hạn chế của ABC, đặc biệt là khả năng tương tác với hệ điều hành Unix và khả năng xử lý ngoại lệ."
    )
    
    add_body(doc,
        "Phiên bản đầu tiên của Python, 0.9.0, được phát hành vào năm 1991. Phiên bản này đã bao gồm những đặc điểm cốt lõi "
        "vẫn còn tồn tại đến ngày nay: lớp xử lý ngoại lệ (exception handling), lập trình hướng đối tượng, và hàm lambda. "
        "Một quyết định thiết kế quan trọng ngay từ đầu là sử dụng khoảng trắng (whitespace) để xác định khối lệnh thay vì "
        "dùng dấu ngoặc nhọn như trong C hay begin/end như trong Pascal. Đây là một bước đi táo bạo, tạo nên bản sắc riêng "
        "của Python so với phần còn lại của thế giới ngôn ngữ lập trình."
    )
    
    add_body(doc,
        "Sự phát triển của Python trải qua hai nhánh lớn: Python 2 và Python 3. Python 2.0 ra mắt năm 2000, thêm tính năng "
        "garbage collection tự động và hỗ trợ Unicode. Tuy nhiên, Python 3.0 (phát hành năm 2008) được thiết kế với nhiều cải tiến "
        "gây ra sự không tương thích ngược nhằm sửa chữa những thiếu sót cố hữu của ngôn ngữ. Trong nhiều năm, cộng đồng phải mất "
        "thời gian chuyển đổi từ Python 2 sang Python 3. Đến năm 2020, Python 2 chính thức ngừng được hỗ trợ, đánh dấu sự hoàn tất "
        "của quá trình chuyển đổi."
    )
    
    add_body(doc,
        "Hiện nay, Python tiếp tục phát triển với chu kỳ phát hành hai lần mỗi năm. Phiên bản Python 3.12 (phát hành cuối 2023) "
        "mang nhiều cải tiến về hiệu năng và cú pháp mới. Quá trình phát triển của Python được quản lý thông qua Quy trình Cải tiến "
        "Python (Python Enhancement Proposal — PEP), một cơ chế mở cho phép cộng đồng đề xuất và thảo luận về các thay đổi ngôn ngữ."
    )
    
    # --- 1.3 ---
    add_heading_custom(doc, "1.3. Những đặc điểm nổi bật của Python", 2)
    
    add_body(doc,
        "Python sở hữu hàng loạt đặc điểm khiến nó trở thành lựa chọn hàng đầu cho cả người mới bắt đầu và chuyên gia. Dưới đây "
        "là những đặc điểm quan trọng nhất:"
    )
    
    add_bullet(doc, "Cú pháp dễ đọc: Python sử dụng từ khóa tiếng Anh thay vì ký hiệu toán học, giúp mã nguồn gần với văn phong tự nhiên.")
    add_bullet(doc, "Dynamic typing: Kiểu dữ liệu của biến được xác định tại thời điểm chạy, không cần khai báo trước.")
    add_bullet(doc, "High-level language: Python ẩn giấu các chi tiết thấp cấp như quản lý bộ nhớ, cho phép lập trình viên tập trung vào logic.")
    add_bullet(doc, "Interpreted execution: Mã nguồn được dịch và thực thi từng dòng tại runtime, giúp gỡ lỗi và phát triển nhanh hơn.")
    add_bullet(doc, "Garbage collection: Hệ thống thu gom rác tự động giải phóng bộ nhớ cho các đối tượng không còn được tham chiếu.")
    add_bullet(doc, "Object-oriented programming: Hỗ trợ đầy đủ các khái niệm class, inheritance, polymorphism, encapsulation.")
    add_bullet(doc, "Hệ sinh thái thư viện lớn: Standard library phong phú cùng hàng trăm nghìn package trên PyPI.")
    add_bullet(doc, "Cross-platform: Chạy tốt trên Windows, macOS, Linux và nhiều nền tảng khác mà không cần thay đổi mã nguồn.")
    
    add_body(doc,
        "Điều đáng chú ý là những đặc điểm này không tồn tại độc lập mà bổ sung cho nhau. Ví dụ, dynamic typing kết hợp với "
        "high-level abstraction giúp giảm đáng kể boilerplate code — lượng mã nguồn cần viết để thực hiện các thao tác cơ bản. "
        "Trong khi đó, interpreted execution và garbage collection tạo nên một môi trường phát triển mượt mà, nơi lập trình viên "
        "có thể viết code, chạy thử và sửa lỗi ngay lập tức mà không cần qua giai đoạn biên dịch."
    )
    
    # --- 1.4 ---
    add_heading_custom(doc, "1.4. Các lĩnh vực sử dụng Python", 2)
    
    add_body(doc,
        "Python được ứng dụng rộng rãi trong hầu hết các lĩnh vực liên quan đến công nghệ thông tin. Để minh họa tính đa năng "
        "này, chúng ta sẽ xem xét các lĩnh vực chính dưới dạng chia cột."
    )
    
    # Column section
    left_col = (
        "Tự động hóa (Automation): Python là công cụ hàng đầu để viết script tự động hóa các tác vụ lặp đi lặp lại như xử lý file, "
        "quản lý hệ thống, gửi email, scraping dữ liệu web. Thư viện standard library cung cấp đầy đủ module cần thiết như os, shutil, subprocess."
        "\n\n"
        "Phát triển web (Web Development): Với các framework như Django, Flask và FastAPI, Python cho phép xây dựng website từ đơn giản "
        "đến phức tạp. Django được ví như \"framework cho perfectionists with deadlines\" nhờ tính năng toàn diện, trong khi Flask nhẹ nhàng "
        "hơn, phù hợp cho microservice."
    )
    
    right_col = (
        "Khoa học dữ liệu (Data Science): Python thống trị lĩnh vực này nhờ Pandas, NumPy, Scikit-learn và Matplotlib. Bộ công cụ này "
        "cho phép phân tích, trực quan hóa và mô hình hóa dữ liệu với độ chính xác cao."
        "\n\n"
        "Trí tuệ nhân tạo và Machine Learning: TensorFlow, PyTorch, và Scikit-learn là nền tảng cho nghiên cứu và ứng dụng AI. "
        "Python trở thành ngôn ngữ chung giữa academia và industry trong lĩnh vực ML/AI."
    )
    
    add_column_section(doc, left_col, right_col)
    
    left_col2 = (
        "Tính toán khoa học (Scientific Computing): SciPy, NumPy và các công cụ liên quan cho phép giải quyết bài toán tính toán "
        "kỹ thuật, vật lý, sinh học với hiệu suất chấp nhận được nhờ tối ưu hóa ở tầng C/Fortran bên dưới."
        "\n\n"
        "Giáo dục: Python được chọn làm ngôn ngữ dạy lập trình đầu tiên ở nhiều trường đại học và trung học trên thế giới nhờ "
        "cú pháp dễ hiểu và phản hồi tức thì từ interpreter."
    )
    
    right_col2 = (
        "Scripting: Dù không phải là một lĩnh vực riêng biệt, scripting là một trong những công dụng phổ biến nhất của Python. "
        "Nó được dùng để viết các tiện ích nhỏ, automation pipeline, testing tool, và nhiều tác vụ khác trong quy trình phát triển phần mềm."
        "\n\n"
        "Software Development: Python được dùng để xây dựng các ứng dụng desktop, CLI tools, API services, và cả game (với pygame)."
    )
    
    add_column_section(doc, left_col2, right_col2)
    
    # Image suggestion 2
    add_body(doc, "[ĐỀ XUẤT HÌNH 2: Screenshot IDE đang chạy code Python với syntax highlighting, minh họa cú pháp sạch sẽ và dễ đọc của Python.", indent=False)
    
    doc.add_page_break()
    
    # ============================================================
    # CHAPTER 2: NỀN TẢNG NGÔN NGỮ PYTHON
    # ============================================================
    
    add_heading_custom(doc, "CHƯƠNG 2. NỀN TẢNG NGÔN NGỮ PYTHON", 1)
    
    add_body(doc,
        "Chương này cung cấp những kiến thức nền tảng cần thiết để người đọc nắm bắt được cách Python hoạt động. "
        "Nội dung không đi sâu chi tiết mà chỉ giới thiệu những khái niệm cốt lõi, tạo tiền đề cho các chương sau "
        "khi phân tích các đặc trưng thú vị của ngôn ngữ."
    )
    
    # --- 2.1 ---
    add_heading_custom(doc, "2.1. Cú pháp và indentation", 2)
    
    add_body(doc,
        "Một trong những đặc điểm gây ấn tượng mạnh nhất khi tiếp cận Python là cách ngôn ngữ sử dụng indentation (thụt lề) "
        "để xác định cấu trúc khối lệnh. Khác với C++, Java hay JavaScript — vốn dùng dấu ngoặc nhọn {} để bao quanh khối code — "
        "Python yêu cầu các câu lệnh thuộc cùng một khối phải được thụt lề cùng một mức. Quy tắc này không chỉ là vấn đề thẩm mỹ; "
        "nó là một phần của cú pháp ngôn ngữ, được interpreter kiểm tra chặt chẽ."
    )
    
    add_body(doc,
        "Việc sử dụng indentation mang lại lợi ích rõ rệt: mã nguồn có tính nhất quán cao về định dạng, vì mọi developer đều "
        "bắt buộc phải tuân theo cùng một quy tắc thụt lề. Điều này giảm thiểu tranh cãi về style trong các dự án nhóm. "
        "Tuy nhiên,它也 đặt ra yêu cầu về kỷ luật: một sai sót về thụt lề có thể dẫn đến lỗi cú pháp hoặc thậm chí lỗi logic "
        "khó phát hiện nếu không cẩn thận."
    )
    
    add_code_block(doc, 
        "# So sánh Python và C++: cùng một nhiệm vụ — in số từ 1 đến 5\n\n"
        "# Python — dùng indentation\n"
        "for i in range(1, 6):\n"
        "    if i % 2 == 0:\n"
        "        print(i, \"là số chẵn\")\n"
        "    else:\n"
        "        print(i, \"là số lẻ\")\n\n"
        "# C++ — dùng dấu ngoặc nhọn {}\n"
        "for (int i = 1; i <= 5; i++) {\n"
        "    if (i % 2 == 0) {\n"
        "        cout << i << \" la so chan\" << endl;\n"
        "    } else {\n"
        "        cout << i << \" la so le\" << endl;\n"
        "    }\n"
        "}",
        "Code 1. So sánh cú pháp Python và C++"
    )
    
    # --- 2.2 ---
    add_heading_custom(doc, "2.2. Biến và dynamic typing", 2)
    
    add_body(doc,
        "Trong Python, mọi thứ đều là object (đối tượng). Khi bạn gán một giá trị cho một tên biến, thực chất bạn đang tạo một "
        "tham chiếu (reference) từ tên đó đến một đối tượng trong bộ nhớ. Không giống C++ nơi bạn phải khai báo kiểu dữ liệu "
        "trước khi tạo biến (ví dụ: int x = 10), Python xác định kiểu dữ liệu tự động dựa trên giá trị được gán."
    )
    
    add_body(doc,
        "Cơ chế này gọi là dynamic typing — kiểu dữ liệu được xác định tại thời điểm chạy chứ không phải lúc khai báo. Điều "
        "này mang lại sự linh hoạt: một biến có thể chứa giá trị thuộc bất kỳ kiểu nào, và kiểu của nó có thể thay đổi trong "
        "suốt vòng đời. Tất nhiên, sự linh hoạt này đi kèm cái giá: lỗi về kiểu dữ liệu sẽ chỉ xuất hiện khi dòng code đó được "
        "thực thi, thay vì bị compiler bắt từ trước."
    )
    
    add_code_block(doc, 
        "# Dynamic typing trong Python\n"
        "x = 10          # x là int\n"
        "print(type(x))  # <class 'int'>\n\n"
        "x = \"Hello\"     # x giờ là str\n"
        "print(type(x))  # <class 'str'>\n\n"
        "x = [1, 2, 3]   # x giờ là list\n"
        "print(type(x))  # <class 'list'>",
        "Code 2. Minh họa dynamic typing"
    )
    
    add_body(doc,
        "Để hiểu sâu hơn, cần phân biệt ba khái niệm: biến (variable), đối tượng (object), và kiểu (type). Trong Python, "
        "biến thực chất là một nhãn gắn vào một đối tượng. Đối tượng là vùng bộ nhớ chứa dữ liệu cùng với metadata về kiểu. "
        "Kiểu xác định những thao tác nào có thể thực hiện trên đối tượng đó. Khi gán lại biến, ta chỉ thay đổi nhãn tham chiếu, "
        "không tạo ra đối tượng mới (trừ khi giá trị mới thực sự là một đối tượng khác)."
    )
    
    # --- 2.3 ---
    add_heading_custom(doc, "2.3. Các kiểu dữ liệu cơ bản", 2)
    
    add_body(doc,
        "Python cung cấp nhiều kiểu dữ liệu built-in, chia thành hai nhóm chính: immutable (bất biến) và mutable (có thể thay đổi). "
        "Hiểu rõ sự phân biệt này là chìa khóa để sử dụng Python hiệu quả, vì nó ảnh hưởng trực tiếp đến cách dữ liệu được lưu trữ "
        "và truyền giữa các hàm."
    )
    
    # Bảng 1: Các kiểu dữ liệu cơ bản
    table1_caption = "Bảng 1. Các kiểu dữ liệu cơ bản trong Python"
    table1 = add_table_custom(doc,
        headers=["Kiểu", "Thuộc tính", "Ví dụ", "Mutable?"],
        rows=[
            ["int", "Số nguyên", "42, -7, 0", "Không"],
            ["float", "Số thập phân", "3.14, -0.5", "Không"],
            ["bool", "Giá trị đúng/sai", "True, False", "Không"],
            ["str", "Chuỗi ký tự", "\"Hello\", 'Python'", "Không"],
            ["list", "Danh sách có thứ tự", "[1, 2, 3]", "Có"],
            ["tuple", "Bộ không đổi", "(1, 2, 3)", "Không"],
            ["set", "Tập hợp không trùng", "{1, 2, 3}", "Có"],
            ["dict", "Bảng băm key-value", "{\"a\": 1}", "Có"],
        ],
        col_widths=[Cm(2), Cm(3.5), Cm(3), Cm(1.5)]
    )
    
    add_body(doc, "Chú thích: " + table1_caption)
    
    add_body(doc,
        "Trong các kiểu dữ liệu này, list và dict là hai kiểu được sử dụng nhiều nhất. List cho phép lưu trữ dãy các phần tử "
        "có thứ tự và có thể thay đổi, trong khi dict (dictionary) lưu trữ cặp key-value, tương tự map trong C++ hay object "
        "trong JavaScript. Tuple, dù trông giống list, là immutable — một lần tạo ra không thể thay đổi. Điều này khiến tuple "
        "phù hợp cho dữ liệu không nên bị sửa đổi, như tọa độ (x, y) hay kết quả trả về từ hàm nhiều giá trị."
    )
    
    # --- 2.4 ---
    add_heading_custom(doc, "2.4. Cấu trúc điều khiển", 2)
    
    add_body(doc,
        "Python hỗ trợ đầy đủ các cấu trúc điều khiển cơ bản: rẽ nhánh (if/elif/else), lặp có điều kiện (while) và lặp qua "
        "dãy phần tử (for). Điểm khác biệt đáng chú ý là cú pháp của Python rất gọn gàng, không yêu cầu dấu ngoặc đơn xung quanh "
        "điều kiện và không cần từ khóa then hay end."
    )
    
    add_code_block(doc, 
        "# Cấu trúc điều khiển trong Python\n"
        "# Rẽ nhánh\n"
        "age = 20\n"
        "if age >= 18:\n"
        "    print(\"Người lớn\")\n"
        "elif age >= 13:\n"
        "    print(\"Thanh thiếu niên\")\n"
        "else:\n"
        "    print(\"Trẻ em\")\n\n"
        "# Vòng lặp for\n"
        "for i in range(5):\n"
        "    print(i)\n\n"
        "# Vòng lặp while\n"
        "count = 0\n"
        "while count < 3:\n"
        "    print(count)\n"
        "    count += 1",
        "Code 3. Cấu trúc điều khiển cơ bản"
    )
    
    add_body(doc,
        "Hai từ khóa break và continue cũng hoạt động tương tự như trong các ngôn ngữ khác: break thoát khỏi vòng lặp ngay lập tức, "
        "còn continue bỏ qua phần còn lại của vòng lặp hiện tại và chuyển sang iteration tiếp theo. Python còn hỗ trợ vòng lặp for...else, "
        "một tính năng ít gặp ở ngôn ngữ khác — khối else sẽ chạy nếu vòng lặp hoàn tất bình thường (không bị break)."
    )
    
    # --- 2.5 ---
    add_heading_custom(doc, "2.5. Function", 2)
    
    add_body(doc,
        "Function trong Python được định nghĩa bằng từ khóa def. Một function có thể nhận tham số với giá trị mặc định, "
        "accept keyword argument, và trả về nhiều giá trị cùng lúc (thực chất là một tuple). Python cũng xử lý tham số "
        "theo cơ chế pass-by-object-reference, nghĩa là tham số là tham chiếu đến đối tượng chứ không phải bản sao."
    )
    
    add_code_block(doc, 
        "# Định nghĩa function với default argument và keyword argument\n"
        "def greet(name, greeting=\"Xin chao\", formal=False):\n"
        "    if formal:\n"
        "        return f\"Kính chào {name}!\"\n"
        "    return f\"{greeting}, {name}!\"\n\n"
        "# Gọi function\n"
        "print(greet(\"An\"))                        # Xin chao, An!\n"
        "print(greet(\"Binh\", greeting=\"Chao mung\")) # Chao mung, Binh!\n"
        "print(greet(\"Cuong\", formal=True))        # Kinh chao Cuong!\n\n"
        "# Tra ve nhieu gia tri\n"
        "def min_max(data):\n"
        "    return min(data), max(data)\n\n"
        "low, high = min_max([3, 1, 7, 2])\n"
        "print(low, high)  # 1 7",
        "Code 4. Function với parameter và return"
    )
    
    add_body(doc,
        "Một điểm thú vị về function trong Python là function cũng là object — bạn có thể gán function cho biến, truyền "
        "function làm tham số cho function khác, và trả về function từ một function. Tính chất này là nền tảng cho nhiều "
        "kỹ thuật nâng cao như decorator và functional programming, sẽ được bàn kỹ hơn ở Chương 3."
    )
    
    doc.add_page_break()
    
    # ============================================================
    # CHAPTER 3: NHỮNG ĐẶC TRƯNG THÚ VỊ CỦA PYTHON
    # ============================================================
    
    add_heading_custom(doc, "CHƯƠNG 3. NHỮNG ĐẶC TRƯNG THÚ VỊ CỦA PYTHON", 1)
    
    add_body(doc,
        "Nếu Chương 2 giới thiệu những nền tảng cơ bản, thì Chương 3 đi sâu vào những tính năng khiến Python trở nên độc đáo "
        "và khác biệt so với nhiều ngôn ngữ lập trình khác. Đây chính là phần thể hiện rõ nhất triết lý thiết kế của Python: "
        "giúp lập trình viên viết code ngắn gọn, dễ hiểu và expressive."
    )
    
    # --- 3.1 ---
    add_heading_custom(doc, "3.1. List comprehension", 2)
    
    add_body(doc,
        "List comprehension là một trong những tính năng được yêu thích nhất của Python. Nó cho phép tạo list mới từ một iterable "
        "đã có bằng cách áp dụng một biểu thức cho từng phần tử, tất cả trong một dòng code duy nhất. Thay vì viết một vòng lặp "
        "với nhiều dòng code để thêm phần tử vào list, list comprehension gói gọn toàn bộ logic vào một biểu thức ngắn gọn."
    )
    
    add_code_block(doc, 
        "# List comprehension\n"
        "squares = [x * x for x in range(10)]\n"
        "print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]\n\n"
        "# Với điều kiện lọc\n"
        "even_squares = [x * x for x in range(10) if x % 2 == 0]\n"
        "print(even_squares)  # [0, 4, 16, 36, 64]\n\n"
        "# So với cách viết truyền thống:\n"
        "squares_v2 = []\n"
        "for x in range(10):\n"
        "    squares_v2.append(x * x)",
        "Code 5. List comprehension và so sánh"
    )
    
    add_body(doc,
        "Ngoài list comprehension, Python còn cung cấp set comprehension (dùng {}) và dictionary comprehension (dùng {}). "
        "Các phiên bản này hoạt động theo nguyên tắc tương tự, tạo set hoặc dict từ iterable. List comprehension không chỉ "
        "ngắn gọn hơn mà còn thường nhanh hơn vòng lặp truyền thống vì nó được tối ưu ở tầng C bên trong interpreter."
    )
    
    # --- 3.2 ---
    add_heading_custom(doc, "3.2. Multiple assignment", 2)
    
    add_body(doc,
        "Python cho phép gán nhiều biến cùng lúc bằng cách liệt kê các tên biến phía trái dấu bằng và các giá trị tương ứng "
        "phía phải. Cơ chế này hoạt động dựa trên việc Python đóng gói các giá trị phía phải thành một tuple rồi giải nén "
        "vào các biến phía trái."
    )
    
    add_code_block(doc, 
        "# Gán nhiều giá trị\n"
        "a, b = 10, 20\n"
        "print(a, b)  # 10 20\n\n"
        "# Hoa tay hoan vi gia tri ma khong can bien tam\n"
        "a, b = b, a\n"
        "print(a, b)  # 20 10\n\n"
        "# Tra ve nhieu gia tri tu function\n"
        "def divide(a, b):\n"
        "    return a // b, a % b\n\n"
        "quotient, remainder = divide(17, 5)\n"
        "print(quotient, remainder)  # 3 2",
        "Code 6. Multiple assignment"
    )
    
    add_body(doc,
        "Tính năng này không chỉ tiện lợi về mặt cú pháp mà còn phản ánh cách Python xử lý tuple: khi bạn viết (10, 20), "
        "Python tạo một tuple ẩn. Khi gán a, b = 10, 20, Python thực chất đang unpack tuple đó. Sự nhất quán này giúp "
        "developer dễ dàng suy đoán hành vi của ngôn ngữ."
    )
    
    # --- 3.3 ---
    add_heading_custom(doc, "3.3. Unpacking", 2)
    
    add_body(doc,
        "Unpacking mở rộng ý tưởng của multiple assignment. Ký tự * cho phép gom nhiều phần tử còn lại vào một danh sách, "
        "rất hữu ích khi làm việc với iterable có độ dài thay đổi."
    )
    
    add_code_block(doc, 
        "# Unpacking voi *\n"
        "a, *middle, b = [1, 2, 3, 4, 5]\n"
        "print(a)      # 1\n"
        "print(middle) # [2, 3, 4]\n"
        "print(b)      # 5\n\n"
        "# Unpacking dict\n"
        "config = {\"host\": \"localhost\", \"port\": 8080, \"debug\": True}\n"
        "host, port, **rest = config.items()\n"
        "print(host, port)  # host localhost 8080",
        "Code 7. Unpacking với ký tự *"
    )
    
    add_body(doc,
        "Unpacking không chỉ áp dụng cho list mà còn cho tuple, string, dict và bất kỳ iterable nào. Nó là nền tảng cho "
        "nhiều pattern phổ biến trong Python như lấy phần tử đầu và cuối của danh sách, hoặc tách header khỏi body khi xử lý file CSV."
    )
    
    # --- 3.4 ---
    add_heading_custom(doc, "3.4. enumerate()", 2)
    
    add_body(doc,
        "enumerate() là một built-in function nhận vào một iterable và trả về một đối tượng sinh ra các cặp (index, value) "
        "tại mỗi iteration. Thay vì phải tự đếm index bằng một biến đếm riêng, developer có thể dùng enumerate để có cả index "
        "và giá trị simultaneously."
    )
    
    add_code_block(doc, 
        "names = [\"An\", \"Binh\", \"Cuong\"]\n\n"
        "# Khong dung enumerate\n"
        "for i in range(len(names)):\n"
        "    print(i, names[i])\n\n"
        "# Dung enumerate\n"
        "for i, name in enumerate(names):\n"
        "    print(i, name)\n\n"
        "# Bat dau tu index 10\n"
        "for i, name in enumerate(names, start=10):\n"
        "    print(i, name)",
        "Code 8. Sử dụng enumerate()"
    )
    
    add_body(doc,
        "enumerate() không chỉ rút ngắn code mà còn tránh được lỗi IndexError — một lỗi phổ biến khi dùng range(len(...)) "
        "và truy cập index sai. Tham số start cho phép tùy chỉnh chỉ số bắt đầu, mặc định là 0."
    )
    
    # --- 3.5 ---
    add_heading_custom(doc, "3.5. zip()", 2)
    
    add_body(doc,
        "zip() ghép các iterable lại với nhau thành các cặp (tuple) tương ứng. Nếu các iterable có độ dài khác nhau, zip "
        "sẽ dừng tại iterable ngắn nhất. Đây là công cụ lý tưởng khi cần xử lý song song hai hoặc nhiều danh sách có mối "
        "quan hệ với nhau."
    )
    
    add_code_block(doc, 
        "names = [\"An\", \"Binh\", \"Cuong\"]\n"
        "scores = [8, 9, 10]\n\n"
        "for name, score in zip(names, scores):\n"
        "    print(f\"{name}: {score}\")\n"
        "# An: 8\n"
        "# Binh: 9\n"
        "# Cuong: 10\n\n"
        "# Unzip: gan doi tu zip ve dict\n"
        "student_scores = dict(zip(names, scores))\n"
        "print(student_scores)  # {'An': 8, 'Binh': 9, 'Cuong': 10}",
        "Code 9. Sử dụng zip()"
    )
    
    # --- 3.6 ---
    add_heading_custom(doc, "3.6. Lambda và higher-order functions", 2)
    
    add_body(doc,
        "Python hỗ trợ lập trình hàm (functional programming) ở mức độ vừa phải thông qua lambda expression và các higher-order "
        "function như map(), filter(), và reduce(). Lambda cho phép tạo function vô danh (anonymous function) — một function "
        "không cần đặt tên, thường dùng một lần."
    )
    
    add_code_block(doc, 
        "# Lambda expression\n"
        "square = lambda x: x * x\n"
        "print(square(5))  # 25\n\n"
        "# Map: ap dung ham cho tung phan tu\n"
        "numbers = [1, 2, 3, 4, 5]\n"
        "doubled = list(map(lambda x: x * 2, numbers))\n"
        "print(doubled)  # [2, 4, 6, 8, 10]\n\n"
        "# Filter: loc cac phan tu thoa dieu kien\n"
        "evens = list(filter(lambda x: x % 2 == 0, numbers))\n"
        "print(evens)  # [2, 4]\n\n"
        "# Function la object — co the truyen nhu tham so\n"
        "def apply(func, value):\n"
        "    return func(value)\n\n"
        "result = apply(lambda x: x**2, 7)\n"
        "print(result)  # 49",
        "Code 10. Lambda và higher-order functions"
    )
    
    add_body(doc,
        "Mặc dù Python hỗ trợ functional programming, nó không phải là ngôn ngữ functional thuần túy. Lambda trong Python "
        "chỉ giới hạn ở một biểu thức duy nhất (không thể chứa statement), và developer thường prefer list comprehension "
        "hoặc generator expression thay vì map/filter cho readability. Tuy nhiên, việc function là object vẫn là nền tảng "
        "cho decorator và callback pattern."
    )
    
    # --- 3.7 ---
    add_heading_custom(doc, "3.7. Generator và yield", 2)
    
    add_body(doc,
        "Generator là một trong những tính năng mạnh mẽ và ít được khai thác đúng mức nhất của Python. Khác với function "
        "trả về toàn bộ kết quả ngay lập tức qua return, generator sử dụng từ khóa yield để trả về từng giá trị một, tạm dừng "
        "và giữ trạng thái giữa các lần gọi. Kỹ thuật này gọi là lazy evaluation — tính toán trì hoãn, chỉ tính khi thực sự cần."
    )
    
    add_code_block(doc, 
        "# Generator voi yield\n"
        "def count_up_to(n):\n"
        "    i = 1\n"
        "    while i <= n:\n"
        "        yield i\n"
        "        i += 1\n\n"
        "# Su dung generator\n"
        "for num in count_up_to(5):\n"
        "    print(num, end=\" \")\n"
        "# 1 2 3 4 5\n\n"
        "# So sanh: list tra ve tat ca truoc\n"
        "def count_list(n):\n"
        "    result = []\n"
        "    for i in range(1, n + 1):\n"
        "        result.append(i)\n"
        "    return result\n\n"
        "# count_up_to(1000000) khong tao list trong bo nho\n"
        "# count_list(1000000) tao mot list 1 trieu phan tu",
        "Code 11. Generator và yield"
    )
    
    add_body(doc,
        "Sự khác biệt giữa return và yield là then chốt: return kết thúc function hoàn toàn và trả về giá trị, trong khi yield "
        "tạm dừng function, lưu lại toàn bộ trạng thái (biến cục bộ, con trỏ lệnh), và tiếp tục từ điểm dừng khi next() được gọi. "
        "Điều này cho phép xử lý dữ liệu lớn mà không cần tải toàn bộ vào bộ nhớ — một lợi thế quan trọng khi làm việc với file "
        "lớn, stream dữ liệu, hoặc chuỗi vô hạn."
    )
    
    # --- 3.8 ---
    add_heading_custom(doc, "3.8. Exception handling", 2)
    
    add_body(doc,
        "Python xử lý lỗi thông qua cơ chế exception (ngoại lệ). Thay vì kiểm tra mã lỗi sau mỗi thao tác như trong C, Python "
        "dùng try/except để bắt và xử lý lỗi tại chỗ. Cơ chế này giúp code sạch hơn và tập trung vào luồng chính thay vì "
        "xử lý lỗi tràn lan."
    )
    
    add_code_block(doc, 
        "# Exception handling\n"
        "try:\n"
        "    result = 10 / 0\n"
        "except ZeroDivisionError:\n"
        "    print(\"Loi: chia cho 0\")\n"
        "except TypeError as e:\n"
        "    print(f\"Loi loai: {e}\")\n"
        "else:\n"
        "    print(f\"Ket qua: {result}\")  # chay neu khong co loi\n"
        "finally:\n"
        "    print(\"Khoi nay luon chay\")  # bat buoc\n\n"
        "# Raise: phu troi exception\n"
        "def set_age(age):\n"
        "    if age < 0:\n"
        "        raise ValueError(\"Tuoi khong duoc am\")\n"
        "    return age",
        "Code 12. Exception handling"
    )
    
    add_body(doc,
        "Python có hệ thống phân cấp exception khá đầy đủ, với BaseException là gốc và Exception là cha của hầu hết các lỗi "
        "application-level. Developer có thể định nghĩa custom exception bằng cách kế thừa từ Exception. Khối else chạy khi "
        "không có exception nào xảy ra, còn finally luôn chạy — dù có exception hay không — giúp đảm bảo cleanup resource."
    )
    
    # --- 3.9 ---
    add_heading_custom(doc, "3.9. Context manager và with", 2)
    
    add_body(doc,
        "Context manager là một pattern quản lý resource tự động: mở resource, thực hiện thao tác, và đóng resource khi xong. "
        "Từ khóa with đảm bảo rằng cleanup luôn được thực hiện, ngay cả khi có exception xảy ra bên trong khối code."
    )
    
    add_code_block(doc, 
        "# With statement de mo va dong file tu dong\n"
        "with open(\"data.txt\", \"r\") as file:\n"
        "    content = file.read()\n"
        "# File tu dong bi dong o day, khoi co loi hay khong\n\n"
        "# Custom context manager\n"
        "from contextlib import contextmanager\n\n"
        "@contextmanager\n"
        "def timer():\n"
        "    import time\n"
        "    start = time.time()\n"
        "    try:\n"
        "        yield\n"
        "    finally:\n"
        "        print(f\"Thoi gian: {time.time() - start:.2f}s\")\n\n"
        "with timer():\n"
        "    sum(range(1000000))  # Code can do",
        "Code 13. Context manager và with"
    )
    
    add_body(doc,
        "Bên dưới bề mặt, with yêu cầu đối tượng phải có hai phương thức: __enter__ (gọi khi进入 khối) và __exit__ (gọi khi "
        "ra khỏi khối, dù bằng cách bình thường hay exception). Standard library cung cấp nhiều context manager sẵn có: file, "
        "threading.Lock, sqlite3.connection, và nhiều hơn nữa."
    )
    
    # --- 3.10 ---
    add_heading_custom(doc, "3.10. Decorator", 2)
    
    add_body(doc,
        "Decorator là một tính năng nâng cao nhưng rất đặc trưng của Python, cho phép \"bao bọc\" (wrap) một function bằng "
        "một function khác mà không thay đổi code gốc. Về bản chất, decorator là một higher-order function nhận function làm "
        "tham số và trả về một function mới. Cú pháp @ giúp áp dụng decorator một cách tường minh và ngắn gọn."
    )
    
    add_code_block(doc, 
        "# Simple decorator: log moi lan goi ham\n"
        "def log_call(func):\n"
        "    def wrapper():\n"
        "        print(\"Function started\")\n"
        "        func()\n"
        "        print(\"Function finished\")\n"
        "    return wrapper\n\n"
        "@log_call\n"
        "def hello():\n"
        "    print(\"Hello Python\")\n\n"
        "hello()\n"
        "# Output:\n"
        "# Function started\n"
        "# Hello Python\n"
        "# Function finished",
        "Code 14. Decorator đơn giản"
    )
    
    add_body(doc,
        "Decorator được sử dụng rộng rãi trong thực tế: @property để tạo computed attribute, @staticmethod/@classmethod "
        "để định nghĩa các loại method đặc biệt, và trong các framework web như Flask (@app.route) để đăng ký endpoint. "
        "Mặc dù decorator có vẻ trừu tượng ban đầu, bản chất của nó rất đơn giản: đó chỉ là một function nhận function khác "
        "làm tham số và trả về function mới."
    )
    
    doc.add_page_break()
    
    # ============================================================
    # CHAPTER 4: OOP TRONG PYTHON
    # ============================================================
    
    add_heading_custom(doc, "CHƯƠNG 4. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON", 1)
    
    add_body(doc,
        "Python hỗ trợ lập trình hướng đối tượng (OOP) nhưng với cách tiếp cận khác biệt so với C++ hay Java. Trong Python, "
        "class không ép buộc encapsulation nghiêm ngặt — không có public/private/protected modifier. Thay vào đó, Python dựa "
        "vào convention: tên bắt đầu bằng một gạch dưới (_) được coi là protected, hai gạch dưới (__) kích hoạt name mangling."
    )
    
    # --- 4.1-4.5 combined with code ---
    add_heading_custom(doc, "4.1 – 4.5. Class, Object, Constructor, Inheritance và Polymorphism", 2)
    
    add_body(doc,
        "Trong Python, class được định nghĩa bằng từ khóa class. Phương thức khởi tạo __init__() đóng vai trò constructor, "
        "tự động được gọi khi tạo instance. Tất cả method đều có tham số self ngầm định, tham chiếu đến instance hiện tại."
    )
    
    add_code_block(doc, 
        "# Class va Object\n"
        "class Dog:\n"
        "    # Class attribute\n"
        "    species = \"Canis familiaris\"\n\n"
        "    # Constructor\n"
        "    def __init__(self, name, age):\n"
        "        # Instance attributes\n"
        "        self.name = name\n"
        "        self.age = age\n\n"
        "    # Instance method\n"
        "    def bark(self):\n"
        "        return f\"{self.name} ga: Gau gau!\"\n\n"
        "# Tao instance\n"
        "dog1 = Dog(\"Spiky\", 3)\n"
        "print(dog1.bark())  # Spiky ga: Gau gau!\n\n"
        "# Inheritance\n"
        "class Bulldog(Dog):\n"
        "    def bark(self):  # Override — Polymorphism\n"
        "        return f\"{self.name} ga: Gong gong!\"\n\n"
        "bully = Bulldog(\"Rex\", 5)\n"
        "print(bully.bark())  # Rex ga: Gong gong!",
        "Code 15. OOP trong Python"
    )
    
    add_body(doc,
        "Polymorphism trong Python được thể hiện qua duck typing: \"nếu nó đi như vịt và kêu như vịt, thì nó là vịt.\" "
        "Python không yêu cầu class con phải kế thừa từ một interface cụ thể; miễn là nó có cùng method signature, nó có thể "
        "thay thế class khác. Điều này khác với Java nơi interface phải được khai báo rõ ràng."
    )
    
    add_body(doc,
        "Python còn hỗ trợ multiple inheritance — một class có thể kế thừa từ nhiều parent class. Tuy nhiên, điều này cần "
        "thận trọng vì có thể dẫn đến diamond problem (vấn đề hình kim tự tháp). Python giải quyết vấn đề này bằng MRO "
        "(Method Resolution Order), sử dụng thuật toán C3 linearization để xác định thứ tự tìm kiếm method."
    )
    
    # Image suggestion 3
    add_body(doc, "[ĐỀ XUẤT HÌNH 3: Sơ đồ kế thừa class trong Python — Dog (parent) → Bulldog, Labrador (children), với các method và attribute được hiển thị rõ ràng.", indent=False)
    
    doc.add_page_break()
    
    # ============================================================
    # CHAPTER 5: PYTHON STANDARD LIBRARY
    # ============================================================
    
    add_heading_custom(doc, "CHƯƠNG 5. PYTHON STANDARD LIBRARY", 1)
    
    add_body(doc,
        "Standard Library (thư viện chuẩn) của Python là tập hợp các module được đóng gói sẵn cùng interpreter, không cần "
        "cài đặt thêm. Đây là một trong những yếu tố quan trọng nhất khiến Python trở nên hấp dẫn: ngay khi cài đặt Python, "
        "developer đã có hàng trăm module sẵn sàng cho hầu hết các tác vụ phổ biến."
    )
    
    add_body(doc,
        "Dưới đây là giới thiệu về một số module tiêu biểu trong Standard Library, mỗi module được chọn vì tính hữu dụng "
        "cao và phạm vi ứng dụng rộng."
    )
    
    # pathlib
    add_heading_custom(doc, "5.1. pathlib — Làm việc với đường dẫn file", 2)
    
    add_body(doc,
        "pathlib cung cấp một面向对象的 cách xử lý đường dẫn file system, thay thế cho os.path truyền thống. "
        "Class Path cho phép thao tác với file và directory bằng các phương thức rõ ràng, dễ đọc."
    )
    
    add_code_block(doc, 
        "from pathlib import Path\n\n"
        "path = Path(\"data/output.txt\")\n"
        "path.parent.mkdir(parents=True, exist_ok=True)\n"
        "path.write_text(\"Hello Python\")\n"
        "print(path.read_text())\n"
        "print(path.exists())   # True\n"
        "print(path.suffix)     # .txt\n"
        "print(path.stem)       # output",
        "Code 16. pathlib example"
    )
    
    # json
    add_heading_custom(doc, "5.2. json — Xử lý dữ liệu JSON", 2)
    
    add_body(doc,
        "Module json cho phép serialize (encode) và deserialize (decode) dữ liệu JSON — định dạng trao đổi dữ liệu phổ "
        "biết nhất trong web development. Việc chuyển đổi giữa Python dict/list và JSON string chỉ cần một dòng code."
    )
    
    add_code_block(doc, 
        "import json\n\n"
        "data = {\"name\": \"An\", \"age\": 25, \"skills\": [\"Python\", \"SQL\"]}\n"
        "json_str = json.dumps(data, ensure_ascii=False, indent=2)\n"
        "print(json_str)\n\n"
        "# Parse JSON string back to dict\n"
        "parsed = json.loads(json_str)\n"
        "print(parsed[\"name\"])  # An",
        "Code 17. json example"
    )
    
    # datetime
    add_heading_custom(doc, "5.3. datetime — Xử lý ngày giờ", 2)
    
    add_body(doc,
        "Module datetime cung cấp các class để làm việc với ngày, giờ, khoảng thời gian. Đây là module không thể thiếu "
        "trong bất kỳ ứng dụng nào cần xử lý timestamp, tính toán ngày tháng, hay định dạng thời gian."
    )
    
    add_code_block(doc, 
        "from datetime import datetime, timedelta\n\n"
        "now = datetime.now()\n"
        "print(now.strftime(\"%Y-%m-%d %H:%M\"))  # 2025-01-15 14:30\n\n"
        "# Tinh toan khoang thoi gian\n"
        "tomorrow = now + timedelta(days=1)\n"
        "yesterday = now - timedelta(days=1)\n"
        "print((tomorrow - yesterday).days)  # 2",
        "Code 18. datetime example"
    )
    
    # collections
    add_heading_custom(doc, "5.4. collections — Cấu trúc dữ liệu bổ sung", 2)
    
    add_body(doc,
        "Module collections mở rộng các kiểu dữ liệu built-in với Counter (đếm tần suất), defaultdict (dict với giá trị mặc định), "
        "deque (double-ended queue hiệu năng cao), namedtuple (tuple có tên), và OrderedDict. Những cấu trúc này thường được "
        "sử dụng hơn so với workaround thủ công."
    )
    
    add_code_block(doc, 
        "from collections import Counter, defaultdict, deque\n\n"
        "# Counter: dem tan suat\n"
        "words = [\"apple\", \"banana\", \"apple\", \"cherry\", \"banana\", \"apple\"]\n"
        "counts = Counter(words)\n"
        "print(counts.most_common(2))  # [('apple', 3), ('banana', 2)]\n\n"
        "# defaultdict: key khong ton tai tra ve gia tri mac dinh\n"
        "groups = defaultdict(list)\n"
        "for word in words:\n"
        "    groups[len(word)].append(word)\n"
        "print(dict(groups))  # {5: ['apple', 'banana', 'cherry'], 6: ['banana', 'apple']}",
        "Code 19. collections example"
    )
    
    add_body(doc,
        "Bên cạnh các module trên, Standard Library còn bao gồm os (tương tác hệ điều hành), sys (thông tin interpreter), "
        "math/toán học, random/số ngẫu nhiên, re (regular expression), threading/multithreading, logging (ghi log), unittest "
        "(testing), urllib (HTTP request), và rất nhiều module khác. Tổng cộng có hơn 200 module trong Standard Library của Python 3."
    )
    
    doc.add_page_break()
    
    # ============================================================
    # CHAPTER 6: HỆ SINH THÁI THƯ VIỆN PYTHON
    # ============================================================
    
    add_heading_custom(doc, "CHƯƠNG 6. HỆ SINH THÁI THƯ VIỆN PYTHON", 1)
    
    add_body(doc,
        "Nếu Standard Library là xương sống của Python, thì hệ sinh thái thư viện bên ngoài (third-party packages) là cơ bắp "
        "và não bộ. Thông qua Package Index của Python (PyPI — Python Package Index), hơn 500.000 package đã được công bố, "
        "phục vụ hầu hết mọi nhu cầu phát triển phần mềm."
    )
    
    add_body(doc,
        "Thay vì liệt kê hàng chục thư viện, chúng ta sẽ điểm qua các nhóm thư viện tiêu biểu nhất, mỗi nhóm đại diện cho "
        "một lĩnh vực ứng dụng quan trọng của Python."
    )
    
    # --- 6.1 ---
    add_heading_custom(doc, "6.1. NumPy — Tính toán số học", 2)
    
    add_body(doc,
        "NumPy (Numerical Python) là thư viện nền tảng cho tính toán số trong Python. Nó cung cấp đối tượng ndarray — "
        "mảng đa chiều hiệu năng cao — cùng hàng ngàn hàm toán học hoạt động trên mảng. NumPy tối ưu hóa phép toán vector "
        "ở tầng C, cho phép xử lý hàng triệu phép tính trong vài mili giây. Hầu hết các thư viện data science khác đều "
        "dựa trên NumPy."
    )
    
    # --- 6.2 ---
    add_heading_custom(doc, "6.2. Pandas — Phân tích dữ liệu", 2)
    
    add_body(doc,
        "Pandas xây dựng trên NumPy, cung cấp DataFrame — cấu trúc dữ liệu dạng bảng tương tự Excel hay SQL table. "
        "Với Pandas, developer có thể đọc file CSV/Excel, lọc, groupby, merge, pivot, và xử lý missing data với cú pháp "
        "ngắn gọn. Đây là công cụ số một cho data analyst và data scientist."
    )
    
    # --- 6.3 ---
    add_heading_custom(doc, "6.3. Matplotlib — Trực quan hóa dữ liệu", 2)
    
    add_body(doc,
        "Matplotlib là thư viện vẽ biểu đồ mạnh mẽ nhất trong Python. Từ biểu đồ đường, cột, scatter đến heatmap, "
        "contour plot — Matplotlib hỗ trợ hầu hết loại biểu đồ cần thiết cho phân tích dữ liệu. Seaborn, một thư viện "
        "xây dựng trên Matplotlib, cung cấp các biểu đồ thống kê đẹp hơn với ít code hơn."
    )
    
    # --- 6.4 ---
    add_heading_custom(doc, "6.4. Scikit-learn — Machine Learning", 2)
    
    add_body(doc,
        "Scikit-learn cung cấp các thuật toán machine learning kinh điển: regression, classification, clustering, "
        "dimensionality reduction, và model selection. Thư viện này tập trung vào ML truyền thống (không phải deep learning), "
        "với API nhất quán và tài liệu xuất sắc. Đây là điểm khởi đầu tốt nhất cho ai muốn học ML."
    )
    
    # --- 6.5 ---
    add_heading_custom(doc, "6.5. PyTorch / TensorFlow — Deep Learning", 2)
    
    add_body(doc,
        "PyTorch (của Meta) và TensorFlow (của Google) là hai framework deep learning hàng đầu. Chúng cung cấp tensor "
        "computing, automatic differentiation (autograd), và mạng neural sẵn có. PyTorch được ưa chuộng trong research nhờ "
        "dynamic computation graph, trong khi TensorFlow mạnh về production deployment với TensorFlow Serving và TFLite."
    )
    
    # --- 6.6 ---
    add_heading_custom(doc, "6.6. Django / Flask / FastAPI — Web Development", 2)
    
    add_body(doc,
        "Django là full-stack framework \"batteries-included\" với ORM, authentication, admin panel, và nhiều tính năng "
        "built-in. Flask là micro-framework nhẹ nhàng, cho developer tự do chọn công cụ phù hợp. FastAPI (dựa trên Starlette "
        "và Pydantic) là framework hiện đại nhất, hỗ trợ async/await, auto-documentation với Swagger UI, và hiệu năng cao "
        "nhờ Python 3.7+ features."
    )
    
    # --- 6.7 ---
    add_heading_custom(doc, "6.7. Requests / BeautifulSoup — HTTP và Web Scraping", 2)
    
    add_body(doc,
        "Requests là thư viện HTTP được yêu thích nhất trong Python, thay thế urllib với API thân thiện hơn. BeautifulSoup "
        "dùng để parse HTML/XML, kết hợp với Requests tạo thành bộ đôi powerful cho web scraping và data extraction."
    )
    
    # Bảng 2: Thư viện Python
    table2_caption = "Bảng 2. Một số thư viện Python phổ biến và lĩnh vực sử dụng"
    add_table_custom(doc,
        headers=["Thư viện", "Lĩnh vực", "Mô tả ngắn"],
        rows=[
            ["NumPy", "Scientific computing", "Mảng đa chiều và phép toán số"],
            ["Pandas", "Data analysis", "DataFrame phân tích dữ liệu"],
            ["Matplotlib", "Data visualization", "Vẽ biểu đồ 2D"],
            ["Scikit-learn", "Machine learning", "Thuật toán ML truyền thống"],
            ["PyTorch", "Deep learning", "Mạng neural, research"],
            ["TensorFlow", "Deep learning", "Mạng neural, production"],
            ["Django", "Web development", "Full-stack framework"],
            ["Flask", "Web development", "Micro-framework"],
            ["FastAPI", "Web development", "Async API framework"],
            ["Requests", "HTTP", "HTTP client thân thiện"],
        ],
        col_widths=[Cm(2.5), Cm(3), Cm(6)]
    )
    
    add_body(doc, "Chú thích: " + table2_caption)
    
    doc.add_page_break()
    
    # ============================================================
    # CHAPTER 7: ỨNG DỤNG THỰC TẾ
    # ============================================================
    
    add_heading_custom(doc, "CHƯƠNG 7. ỨNG DỤNG THỰC TẾ", 1)
    
    add_body(doc,
        "Chương này trình bày các ví dụ thực tế để minh họa Python được sử dụng như thế nào trong các tình huống cụ thể. "
        "Mỗi ví dụ tập trung vào một khía cạnh ứng dụng khác nhau, từ automation đơn giản đến pipeline ML phức tạp."
    )
    
    # --- 7.1 ---
    add_heading_custom(doc, "7.1. Tự động hóa file", 2)
    
    add_body(doc,
        "Một trong những ứng dụng phổ biến nhất của Python là tự động hóa các tác vụ liên quan đến file system. "
        "Ví dụ dưới đây minh họa cách đọc tất cả file .txt trong một thư mục, đếm số dòng của mỗi file, và ghi kết quả ra file CSV."
    )
    
    add_code_block(doc, 
        "from pathlib import Path\n"
        "import csv\n\n"
        "folder = Path(\"./documents\")\n"
        "results = []\n\n"
        "for txt_file in folder.glob(\"*.txt\"):\n"
        "    line_count = len(txt_file.read_text().splitlines())\n"
        "    results.append({\"file\": txt_file.name, \"lines\": line_count})\n\n"
        "# Ghi ket qua ra CSV\n"
        "with Path(\"report.csv\").open(\"w\", newline=\"\") as f:\n"
        "    writer = csv.DictWriter(f, fieldnames=[\"file\", \"lines\"])\n"
        "    writer.writeheader()\n"
        "    writer.writerows(results)\n"
        "print(f\"Da xu ly {len(results)} file.\")",
        "Code 20. Tự động hóa xử lý file"
    )
    
    # --- 7.2 ---
    add_heading_custom(doc, "7.2. Xử lý dữ liệu", 2)
    
    add_body(doc,
        "Xử lý dữ liệu là lĩnh vực Python tỏa sáng. Ví dụ sau sử dụng Pandas để đọc file CSV, lọc dữ liệu, tính toán "
        "thống kê cơ bản, và xuất kết quả."
    )
    
    add_code_block(doc, 
        "import pandas as pd\n\n"
        "# Doc file CSV\n"
        "df = pd.read_csv(\"sales.csv\")\n\n"
        "# Loc va tinh toan\n"
        "filtered = df[df[\"amount\"] > 1000]\n"
        "summary = filtered.groupby(\"region\")[\"amount\"].agg(\n"
        "    [\"mean\", \"sum\", \"count\"]\n"
        ").round(2)\n\n"
        "print(summary)\n"
        "summary.to_excel(\"summary.xlsx\")",
        "Code 21. Xử lý dữ liệu với Pandas"
    )
    
    # --- 7.3 ---
    add_heading_custom(doc, "7.3. Gọi Web API", 2)
    
    add_body(doc,
        "Python có thể tương tác với REST API một cách dễ dàng nhờ thư viện requests. Ví dụ sau minh họa cách gọi API "
        "lấy thông tin thời tiết và xử lý response JSON."
    )
    
    add_code_block(doc, 
        "import requests\n\n"
        "# Goi REST API\n"
        "response = requests.get(\n"
        "    \"https://api.open-meteo.com/v1/forecast\",\n"
        "    params={\"latitude\": 21.0, \"longitude\": 105.8, \"current_weather\": True}\n"
        ")\n"
        "data = response.json()\n\n"
        "weather = data[\"current_weather\"]\n"
        "print(f\"Nhiet do: {weather['temperature']}°C\")\n"
        "print(f\"Toc gio: {weather['windspeed']} km/h\")",
        "Code 22. Gọi Web API với requests"
    )
    
    # --- 7.4 ---
    add_heading_custom(doc, "7.4. Web development", 2)
    
    add_body(doc,
        "Flask là framework web nhẹ nhàng, phù hợp để minh họa cách Python xử lý HTTP request/response. Ví dụ sau tạo "
        "một API endpoint đơn giản."
    )
    
    add_code_block(doc, 
        "from flask import Flask, jsonify\n\n"
        "app = Flask(__name__)\n\n"
        "@app.route(\"/api/hello/<name>\")\n"
        "def hello(name):\n"
        "    return jsonify({\n"
        "        \"message\": f\"Xin chao, {name}!\",\n"
        "        \"language\": \"Python\"\n"
        "    })\n\n"
        "if __name__ == \"__main__\":\n"
        "    app.run(debug=True)",
        "Code 23. Web API với Flask"
    )
    
    # --- 7.5 ---
    add_heading_custom(doc, "7.5. AI / Machine Learning Pipeline", 2)
    
    add_body(doc,
        "Pipeline ML trong Python thường gồm các bước: thu thập dữ liệu → làm sạch → tiền xử lý → huấn luyện mô hình "
        "→ đánh giá → triển khai. Mỗi bước sử dụng các thư viện chuyên biệt, nhưng tất cả đều nằm trong cùng một ngôn ngữ."
    )
    
    add_code_block(doc, 
        "from sklearn.datasets import load_iris\n"
        "from sklearn.model_selection import train_test_split\n"
        "from sklearn.ensemble import RandomForestClassifier\n"
        "from sklearn.metrics import accuracy_score\n\n"
        "# 1. Load du lieu\n"
        "X, y = load_iris(return_X_y=True)\n\n"
        "# 2. Chia tap train/test\n"
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)\n\n"
        "# 3. Huấn luyen mo hinh\n"
        "model = RandomForestClassifier(n_estimators=100)\n"
        "model.fit(X_train, y_train)\n\n"
        "# 4. Danh gia\n"
        "preds = model.predict(X_test)\n"
        "print(f\"Accuracy: {accuracy_score(y_test, preds):.2%}\")",
        "Code 24. ML Pipeline đơn giản với Scikit-learn"
    )
    
    # Image suggestion 4
    add_body(doc, "[ĐỀ XUẤT HÌNH 4: Sơ đồ pipeline ML: Data Collection → Data Cleaning → Feature Engineering → Model Training → Evaluation → Deployment. Mũi tên nối các bước theo chiều dọc, mỗi bước là một ô màu khác nhau.", indent=False)
    
    doc.add_page_break()
    
    # ============================================================
    # CHAPTER 8: KHÍA CẠNH NÂNG CAO
    # ============================================================
    
    add_heading_custom(doc, "CHƯƠNG 8. MỘT SỐ KHÍA CẠNH NÂNG CAO VÀ ĐẶC TRƯNG", 1)
    
    # --- 8.1 ---
    add_heading_custom(doc, "8.1. Python có thể mở rộng bằng C/C++", 2)
    
    add_body(doc,
        "Một khía cạnh ít được biết đến nhưng cực kỳ quan trọng của Python là khả năng mở rộng bằng C/C++. Qua Python/C API, "
        "developer có thể viết các extension module bằng C, sau đó import vào Python như một module thông thường. Cơ chế này "
        "được sử dụng rộng rãi: nhiều module trong Standard Library (như os, sys, json) thực chất được viết bằng C để đạt "
        "hiệu năng cao."
    )
    
    add_body(doc,
        "Các thư viện nổi tiếng như NumPy, Pandas, và Cython đều dựa trên C extension để đạt tốc độ tính toán gần bằng "
        "code C thuần túy. Ngoài ra, Python 3.11 giới thiệu PEP 659 (Specializing Adaptive Interpreter) giúp tăng tốc "
        "interpreter mà không cần C extension. Gần đây, PyPy — một implementation của Python với JIT compiler — cũng là "
        "một hướng tiếp cận thay thế để cải thiện hiệu năng."
    )
    
    # --- 8.2 ---
    add_heading_custom(doc, "8.2. Python bytecode và Python Virtual Machine", 2)
    
    add_body(doc,
        "Khi Python thực thi một file .py, quá trình diễn ra qua nhiều bước. Đầu tiên, source code được parser phân tích "
        "cú pháp và tạo thành Abstract Syntax Tree (AST). Tiếp theo, AST được compiler chuyển thành bytecode — một dạng "
        "mã trung gian dạng nhị phân, không phải mã máy của CPU mà là mã của Python Virtual Machine (PVM)."
    )
    
    add_body(doc,
        "Bytecode được lưu vào file .pyc (compiled Python) để lần chạy sau không cần compile lại. PVM sau đó đọc và thực "
        "thi từng opcode của bytecode. Cơ chế này tương tự cách Java hoạt động với JVM, và giúp Python có tính cross-platform: "
        "bytecode chạy được trên bất kỳ hệ điều hành nào có Python interpreter cài đặt."
    )
    
    add_code_block(doc, 
        "# Xem bytecode cua mot doan code ngan\n"
        "import dis\n\n"
        "def add(a, b):\n"
        "    return a + b\n\n"
        "dis.dis(add)\n"
        "# Output:\n"
        "#   2           0 LOAD_FAST                0 (a)\n"
        "#               2 LOAD_FAST                1 (b)\n"
        "#               4 BINARY_ADD\n"
        "#               6 RETURN_VALUE",
        "Code 25. Xem bytecode với dis module"
    )
    
    # --- 8.3 ---
    add_heading_custom(doc, "8.3. Hiệu năng của Python", 2)
    
    add_body(doc,
        "Hiệu năng là chủ đề gây nhiều tranh luận khi nói về Python. Cần hiểu rằng Python chậm hơn C/C++ trong các tác vụ "
        "CPU-bound thuần túy (như vòng lặp tính toán nặng) vì overhead của interpreter và cơ chế dynamic typing. Mỗi phép toán "
        "trong Python phải qua nhiều lớp trừu tượng trước khi tới CPU."
    )
    
    add_body(doc,
        "Tuy nhiên, việc so sánh hiệu năng chỉ có ý nghĩa trong ngữ cảnh cụ thể. Phần lớn ứng dụng Python không bị giới hạn "
        "bởi CPU mà bởi I/O (network, disk, database). Trong những trường hợp này, Python hoàn toàn đủ nhanh. Hơn nữa, khi cần "
        "tối ưu, developer có thể: (1) dùng thư viện viết bằng C (NumPy, Pandas); (2) viết phần nóng bằng Cython/C extension; "
        "hoặc (3) dùng multiprocessing để tận dụng multi-core."
    )
    
    add_body(doc,
        "Điều quan trọng cần nhớ là developer productivity — tốc độ viết code và thời gian đưa sản phẩm ra thị trường — "
        "cũng là một dạng \"hiệu năng\". Trong nhiều trường hợp, viết một solution bằng Python trong 2 giờ nhanh hơn nhiều "
        "so với viết cùng solution bằng C++ trong 2 ngày, dù code C++ chạy nhanh hơn 10 lần. Trade-off này phụ thuộc vào "
        "yêu cầu cụ thể của dự án."
    )
    
    doc.add_page_break()
    
    # ============================================================
    # CHAPTER 9: ƯU ĐIỂM VÀ HẠN CHẾ
    # ============================================================
    
    add_heading_custom(doc, "CHƯƠNG 9. ƯU ĐIỂM VÀ HẠN CHẾ", 1)
    
    add_heading_custom(doc, "9.1. Ưu điểm", 2)
    
    add_body(doc,
        "Sau khi đã tìm hiểu về Python từ nhiều góc độ, có thể tổng hợp những ưu điểm nổi bật sau:"
    )
    
    add_bullet(doc, "Cú pháp dễ đọc và dễ viết: Python có cú pháp gần gũi với tiếng Anh, không yêu cầu dấu chấm phẩy hay ngoặc nhọn. Code Python thường ngắn hơn 3–5 lần so với tương đương trong Java hay C++.")
    add_bullet(doc, "Tốc độ phát triển phần mềm nhanh: Nhờ syntax đơn giản và thư viện phong phú, developer có thể xây dựng prototype và sản phẩm nhanh chóng. Thời gian từ ý tưởng đến code chạy thường ngắn hơn đáng kể so với các ngôn ngữ khác.")
    add_bullet(doc, "Hệ sinh thái thư viện khổng lồ: PyPI với hơn 500.000 package bao phủ hầu hết mọi lĩnh vực. Standard library với 200+ module sẵn có.")
    add_bullet(doc, "Đa năng (Versatility): Từ web, data science, AI, automation đến giáo dục — Python có thể làm được nhiều thứ.")
    add_bullet(doc, "Cộng đồng lớn và tích cực: Hàng triệu developer trên toàn thế giới, vô số tutorial, Stack Overflow answers, và tài liệu开源.")
    add_bullet(doc, "Cross-platform: Cùng một codebase chạy trên Windows, macOS, Linux mà không cần sửa đổi.")
    add_bullet(doc, "Phù hợp cho nhiều cấp độ: Từ người mới học lập trình lần đầu đến researcher AI cấp cao đều có thể sử dụng Python hiệu quả.")
    
    add_heading_custom(doc, "9.2. Hạn chế", 2)
    
    add_body(doc,
        "Mặc dù mạnh mẽ, Python không phải là giải pháp cho mọi vấn đề. Nhận diện hạn chế giúp developer đưa ra quyết định "
        "công nghệ sáng suốt:"
    )
    
    add_bullet(doc, "Hiệu năng CPU: Python chậm hơn C/C++/Rust trong các tác vụ tính toán密集型. Mặc dù có thể kết hợp với C extension, nhưng overhead của việc giao tiếp giữa Python và C đôi khi làm giảm lợi thế.")
    add_bullet(doc, "Tiêu thụ bộ nhớ: Do dynamic typing và object model, mỗi giá trị trong Python là một object đầy đủ với metadata, dẫn đến memory footprint lớn hơn so với ngôn ngữ static-typed.")
    add_bullet(doc, "Lỗi runtime type: Dynamic typing có nghĩa là lỗi kiểu dữ liệu chỉ phát hiện khi code chạy. Trong dự án lớn, điều này có thể gây khó khăn cho debugging nếu không có test coverage đầy đủ.")
    add_bullet(doc, "Quản lý dependency: Với nhiều project phụ thuộc vào hàng trăm package, việc quản lý version và tránh conflict là thách thức. Công cụ như venv, pipenv, poetry đã giúp cải thiện nhưng vẫn là vấn đề tồn tại.")
    add_bullet(doc, "Không phù hợp cho real-time/low-level: Python không suitable cho embedded systems, operating system kernel, hay applications yêu cầu deterministic timing (như game engine real-time, robotics control).")
    
    doc.add_page_break()
    
    # ============================================================
    # CHAPTER 10: SO SÁNH VỚI CÁC NGÔN NGỮ KHÁC
    # ============================================================
    
    add_heading_custom(doc, "CHƯƠNG 10. SO SÁNH VỚI MỘT SỐ NGÔN NGỮ", 1)
    
    add_body(doc,
        "Để đánh giá khách quan vị trí của Python, chúng ta so sánh nó với ba ngôn ngữ lập trình phổ biến khác: C++, Java, "
        "và JavaScript/TypeScript. Mỗi ngôn ngữ có thế mạnh riêng, và việc lựa chọn phụ thuộc vào yêu cầu cụ thể của dự án."
    )
    
    # Bảng 3: So sánh
    table3_caption = "Bảng 3. So sánh Python với C++, Java và JavaScript/TypeScript"
    add_table_custom(doc,
        headers=["Tiêu chí", "Python", "C++", "Java", "JavaScript/TS"],
        rows=[
            ["Kiểu dữ liệu", "Dynamic", "Static", "Static", "Dynamic (JS) / Static (TS)"],
            ["Compile/Run", "Interpreted", "Compiled", "JIT Compiled", "Interpreted/JIT"],
            ["Syntax", "Đơn giản, gọn", "Phức tạp", "Chi tiết", "Trung bình"],
            ["Performance", "Trung bình-thấp", "Rất cao", "Cao", "Trung bình"],
            ["Memory", "Tiêu thụ cao", "Kiểm soát tốt", "GC, trung bình", "GC, cao"],
            ["Ecosystem", "Rất lớn (500K+)", "Lớn (std + boost)", "Lớn (JVM)", "Rất lớn (npm)"],
            ["Lĩnh vực chính", "AI, data, web, script", "System, game, HPC", "Enterprise, Android", "Web, full-stack"],
            ["Tốc độ dev", "Rất nhanh", "Chậm", "Trung bình", "Nhanh"],
        ],
        col_widths=[Cm(2), Cm(2.5), Cm(2), Cm(2), Cm(2.5)]
    )
    
    add_body(doc, "Chú thích: " + table3_caption)
    
    add_heading_custom(doc, "10.1. Python vs C++", 2)
    
    add_body(doc,
        "C++ là ngôn ngữ của hệ thống, game engine, và high-performance computing. Nó cho phép kiểm soát hoàn toàn bộ nhớ "
        "và tối ưu hiệu năng. Tuy nhiên, C++ có cú pháp phức tạp, thời gian compile lâu, và dễ gây lỗi segfault nếu quản lý "
        "memory không đúng. Python thay thế C++ khi developer ưu tiên tốc độ phát triển và readability hơn tối ưu hiệu năng "
        "tuyệt đối."
    )
    
    add_heading_custom(doc, "10.2. Python vs Java", 2)
    
    add_body(doc,
        "Java thống trị lĩnh vực enterprise application và Android development nhờ tính ổn định, strong typing, và JVM ecosystem. "
        "Java yêu cầu boilerplate code nhiều hơn Python đáng kể. Python vượt trội hơn trong data science và rapid prototyping, "
        "trong khi Java vẫn là lựa chọn hàng đầu cho hệ thống enterprise lớn với nhiều developer."
    )
    
    add_heading_custom(doc, "10.3. Python vs JavaScript/TypeScript", 2)
    
    add_body(doc,
        "JavaScript là ngôn ngữ của browser và ngày càng phổ biến trên server (Node.js). TypeScript thêm static typing vào JS. "
        "JavaScript thống trị front-end development, trong Python không có đối thủ trực tiếp trong lĩnh vực này. Tuy nhiên, "
        "trên server-side, cả hai đều có framework mạnh (Django/FastAPI vs Express/NestJS). Python có lợi thế về data processing "
        "và AI, trong JavaScript có lợi thế về ecosystem npm và ubiquity trên web."
    )
    
    doc.add_page_break()
    
    # ============================================================
    # KẾT LUẬN
    # ============================================================
    
    add_heading_custom(doc, "KẾT LUẬN", 1)
    
    add_body(doc,
        "Qua quá trình tìm hiểu ngôn ngữ lập trình Python, có thể rút ra những nhận định sau về vị trí và vai trò của Python "
        "trong hệ sinh thái lập trình hiện đại."
    )
    
    add_body(doc,
        "Python là một ngôn ngữ lập trình đa năng, được thiết kế với triết lý nhấn mạnh vào tính readable và developer productivity. "
        "Từ khi ra mắt vào năm 1991, Python đã phát triển từ một ngôn ngữ kịch bản nhỏ thành một trong những ngôn ngữ được sử "
        "dụng rộng rãi nhất thế giới. Sự phát triển này không phải là ngẫu nhiên — nó bắt nguồn từ cách Python được thiết kế: "
        "simple but not simplistic, flexible but not chaotic."
    )
    
    add_body(doc,
        "Những đặc điểm quan trọng nhất của Python có thể tóm tắt ở ba điểm then chốt. Thứ nhất, cú pháp sạch sẽ và indentation "
        "bắt buộc tạo nên một văn hóa code consistency hiếm thấy ở các ngôn ngữ khác. Thứ hai, dynamic typing kết hợp với high-level "
        "abstraction giúp giảm đáng kể cognitive load khi lập trình, cho phép developer tập trung vào solving problem thay vì "
        "worrying about syntax details. Thứ ba, hệ sinh thái thư viện khổng lồ — từ standard library đến PyPI — biến Python thành "
        "một \"glue language\" kết nối các công cụ và service khác nhau một cách liền mạch."
    )
    
    add_body(doc,
        "Python phổ biến vì nó giải quyết được bài toán cân bằng: đủ đơn giản cho người mới bắt đầu, đủ mạnh cho chuyên gia, "
        "đủ đa năng cho nhiều lĩnh vực. Trong kỷ nguyên data và AI, Python trở thành lingua franca — ngôn ngữ chung giữa academia "
        "và industry. Hầu hết paper ML/AI mới đều cung cấp code demo bằng Python, và điều này tạo nên một vòng lặp positive feedback: "
        "càng nhiều research → càng nhiều thư viện → càng nhiều developer → càng nhiều research."
    )
    
    add_body(doc,
        "Python phù hợp nhất với các loại công việc yêu cầu rapid development, data-intensive processing, và cross-domain integration. "
        "Tuy nhiên, Python không phải là công cụ lý tưởng cho mọi tình huống: các ứng dụng real-time, embedded system, hay game "
        "engine 3D vẫn cần đến C++, Rust, hoặc C#. Hiểu rõ giới hạn của Python cũng quan trọng không kém việc biết những gì "
        "Python có thể làm."
    )
    
    add_body(doc,
        "Nhìn vào bức tranh tổng thể, Python không đứng ở vị trí \"ngôn ngữ tốt nhất\" tuyệt đối — không có ngôn ngữ nào làm "
        "được mọi thứ tốt nhất. Thay vào đó, Python chiếm một vị trí độc đáo: nó là ngôn ngữ của sự kết nối và đa năng. "
        "Trong một thế giới công nghệ ngày càng phân mảnh, Python đóng vai trò như sợi chỉ xuyên suốt, kết nối diverse domains "
        "và diverse teams. Và có lẽ, đó chính là lý do khiến Python tiếp tục phát triển và giữ vững vị thế trong nhiều năm "
        "tới."
    )
    
    doc.add_page_break()
    
    # ============================================================
    # TÀI LIỆU THAM KHẢO
    # ============================================================
    
    add_heading_custom(doc, "TÀI LIỆU THAM KHẢO", 1)
    
    references = [
        '1. Python Software Foundation. (2024). Python Documentation. https://docs.python.org/3/',
        '2. Van Rossum, G., & Drake, F. L. (2009). Python 3 Reference Manual. CreateSpace.',
        '3. Python Packaging Authority. (2024). PyPI – The Python Package Index. https://pypi.org/',
        '4. McKinney, W. (2022). Python for Data Analysis (3rd ed.). O\'Reilly Media.',
        '5. Lutz, M. (2013). Programming Python (4th ed.). O\'Reilly Media.',
        '6. Lua, K. (2019). Fluent Python (1st ed.). O\'Reilly Media.',
    ]
    
    for ref in references:
        p = doc.add_paragraph()
        set_paragraph_alignment(p, WD_ALIGN_PARAGRAPH.JUSTIFY)
        p.paragraph_format.left_indent = Cm(1.27)
        p.paragraph_format.first_line_indent = Cm(-1.27)  # Hanging indent
        run = p.add_run(ref)
        set_run_font(run, size=Pt(12))
        p.paragraph_format.space_after = Pt(4)
    
    # ============================================================
    # SAVE
    # ============================================================
    
    output_path = r"C:\Users\Admin\Desktop\baitap\Bao_Cao_Python.docx"
    doc.save(output_path)
    print(f"Document saved to: {output_path}")
    print("Done!")


if __name__ == "__main__":
    main()
