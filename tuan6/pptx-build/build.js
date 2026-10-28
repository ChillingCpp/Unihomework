const T = require("./theme");
const {
  C, F, TYPE, deck, tx, bg, header, footer, card, chip,
  codePanel, outPanel, grid, label, arrow, note,
} = T;

const p = deck();

function table(s, head, rows, o) {
  const fs = o.fs || TYPE.table;
  const hfs = o.hfs || Math.min(TYPE.table, fs + 0.5);
  const tRows = [head.map((h) => ({
    text: h,
    options: { bold: true, color: C.white, fill: { color: C.ink }, fontSize: hfs },
  }))];
  rows.forEach((r, i) => {
    tRows.push(r.map((v, j) => ({
      text: v,
      options: {
        color: j === 0 ? C.ink : C.slate,
        bold: j === 0,
        fill: { color: i % 2 ? C.ice : C.white },
        fontSize: fs,
        fontFace: (o.monoFirst && j === 0) ? F.code : F.body,
      },
    })));
  });
  s.addTable(tRows, {
    x: o.x, y: o.y, w: o.w, colW: o.colW, rowH: o.rowH,
    border: { type: "solid", pt: 0.5, color: "DCE8EE" },
    fontFace: F.body, margin: o.margin || 4, valign: "middle", autoPage: false,
  });
}

function bullet(s, x, y, w, text, o = {}) {
  s.addShape(p.ShapeType.ellipse, {
    x, y: y + 0.13, w: 0.13, h: 0.13,
    fill: { color: o.color || C.teal }, line: { color: C.white, width: 0 },
  });
  tx(s, text, {
    x: x + 0.28, y, w, h: o.h || 0.72, fontSize: o.fs || TYPE.body,
    color: o.ink || C.ink, lineSpacingMultiple: 1.08, bold: !!o.bold,
  });
}

/* ---------------------------------------------------------------- 01 title */
{
  const s = p.addSlide();
  bg(s, C.ink);
  for (let r = 0; r < 7; r++) {
    for (let c = 0; c < 8; c++) {
      s.addShape(p.ShapeType.rect, {
        x: 8.15 + c * 0.62, y: 4.55 + r * 0.42, w: 0.56, h: 0.37,
        fill: { color: (r + c) % 5 === 0 ? "0E3E52" : "0A3042" },
        line: { color: "0A3042", width: 0 },
      });
    }
  }
  tx(s, "PYTHON  ·  TÍNH TOÁN KHOA HỌC", {
    x: 0.75, y: 0.95, w: 7.6, h: 0.3, fontSize: 13, bold: true,
    color: C.cyan, charSpacing: 2.2,
  });
  tx(s, "Tìm hiểu thư viện\nNumPy trong Python", {
    x: 0.72, y: 1.45, w: 7.9, h: 2.4, fontSize: TYPE.cover, bold: true,
    color: C.white, lineSpacingMultiple: 0.95, valign: "top",
  });
  s.addShape(p.ShapeType.rect, {
    x: 0.75, y: 3.98, w: 1.15, h: 0.05,
    fill: { color: C.amber }, line: { color: C.amber, width: 0 },
  });
  tx(s, "Từ ndarray đến broadcasting", {
    x: 0.75, y: 4.28, w: 7.2, h: 0.55, fontSize: 26, color: C.cyan,
  });
  tx(s, "Người trình bày: 26120072     ·     Tháng 10 / 2026", {
    x: 0.75, y: 6.35, w: 7.4, h: 0.3, fontSize: 14, color: "9FC0CF",
  });
  card(s, { x: 8.75, y: 1.55, w: 3.95, h: 3.35, fill: C.white, line: "D7E5EC" });
  s.addImage({ path: "assets/numpylogo.png", x: 9.12, y: 2.55, w: 3.2, h: 1.54 });
  tx(s, "Numerical Python  ·  BSD", {
    x: 8.75, y: 4.35, w: 3.95, h: 0.3, fontSize: 11.5,
    color: C.muted, align: "center",
  });
  s.addNotes("Giới thiệu chủ đề: NumPy là thư viện nền tảng cho tính toán số trong Python. Bài đi từ đối tượng ndarray, cách tạo và truy cập dữ liệu, đến phép toán, broadcasting và bốn ví dụ thực hành.");
}

/* ---------------------------------------------------------------- 02 agenda */
{
  const s = p.addSlide(); bg(s);
  header(s, "Nội dung", "Sáu chặng của bài thuyết trình");
  const items = [
    ["01", "Giới thiệu", "NumPy là gì và vì sao nên dùng."],
    ["02", "Cấu trúc mảng", "ndarray, shape, size và dtype."],
    ["03", "Tạo mảng", "array, zeros, ones, arange, linspace, eye."],
    ["04", "Truy cập dữ liệu", "Indexing, slicing, boolean, reshape, .T."],
    ["05", "Tính toán", "Phép toán, axis và broadcasting."],
    ["06", "Thực hành", "Bốn ví dụ, kết luận và hướng học tiếp."],
  ];
  const xs = [0.6, 4.72, 8.84];
  items.forEach((it, i) => {
    const x = xs[i % 3];
    const y = i < 3 ? 1.65 : 3.95;
    card(s, { x, y, w: 3.88, h: 2.08 });
    s.addShape(p.ShapeType.roundRect, {
      x: x + 0.24, y: y + 0.24, w: 0.56, h: 0.56,
      fill: { color: i % 2 ? C.cyan : C.teal }, line: { color: C.white, width: 1.5 }, rectRadius: 0.2,
    });
    tx(s, it[0], {
      x: x + 0.24, y: y + 0.24, w: 0.56, h: 0.56, fontSize: 18, bold: true,
      color: C.white, align: "center", valign: "mid", fontFace: F.code,
    });
    tx(s, it[1], { x: x + 0.92, y: y + 0.27, w: 2.7, h: 0.55, fontSize: TYPE.subhead, bold: true, color: C.ink });
    tx(s, it[2], { x: x + 0.24, y: y + 1.02, w: 3.4, h: 0.86, fontSize: TYPE.body, color: C.slate, lineSpacingMultiple: 1.06 });
  });
  tx(s, "Mạch kiến thức: vấn đề → đối tượng → tạo → truy cập → tính toán → ứng dụng.", {
    x: 0.6, y: 6.28, w: 12.1, h: 0.38, fontSize: TYPE.body, italic: true, color: C.teal,
  });
  footer(s, 2);
  s.addNotes("Sáu chặng tương ứng với sáu phần nội dung. Mạch đi từ động cơ sử dụng, mô hình dữ liệu, thao tác cơ bản, đến tính toán và ví dụ.");
}

/* ---------------------------------------------------------------- 03 what is numpy */
{
  const s = p.addSlide(); bg(s);
  header(s, "01 · Giới thiệu", "NumPy là gì?");
  tx(s, "NumPy (Numerical Python) là thư viện mã nguồn mở cho tính toán khoa học trong Python.", {
    x: 0.6, y: 1.55, w: 6.05, h: 1.1, fontSize: TYPE.lead, color: C.ink, lineSpacingMultiple: 1.08,
  });
  const rows = [
    ["ndarray", "Mảng N chiều, đồng nhất kiểu, kích thước cố định"],
    ["Hàm toán học", "Đại số tuyến tính, thống kê, sắp xếp, tìm kiếm"],
    ["Nền tảng", "Nhiều thư viện khoa học nhận và trả về mảng NumPy"],
  ];
  rows.forEach((r, i) => {
    const y = 2.82 + i * 1.3;
    card(s, { x: 0.6, y, w: 6.05, h: 1.2 });
    s.addShape(p.ShapeType.rect, {
      x: 0.6, y: y + 0.14, w: 0.07, h: 0.92,
      fill: { color: i === 0 ? C.teal : i === 1 ? C.cyan : C.amber },
      line: { color: C.white, width: 0 },
    });
    tx(s, r[0], { x: 0.86, y: y + 0.1, w: 5.4, h: 0.4, fontSize: TYPE.subhead, bold: true, color: C.ink });
    tx(s, r[1], { x: 0.86, y: y + 0.51, w: 5.45, h: 0.6, fontSize: TYPE.body, color: C.slate, lineSpacingMultiple: 1.0 });
  });
  codePanel(s, {
    x: 6.95, y: 1.6, w: 5.78, h: 1.55, fs: 17,
    code: "import numpy as np\n\nprint(np.__version__)",
  });
  outPanel(s, { x: 6.95, y: 3.35, w: 5.78, h: 0.9, text: "2.5.4", fs: 18 });
  card(s, { x: 6.95, y: 4.45, w: 5.78, h: 1.05, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "Quy ước: import numpy as np", {
    x: 7.15, y: 4.45, w: 5.4, h: 1.05, fontSize: TYPE.body, bold: true,
    color: C.teal, valign: "mid",
  });
  tx(s, "Nguồn: NumPy Documentation [1], [2]", {
    x: 6.95, y: 5.7, w: 5.7, h: 0.27, fontSize: TYPE.source, color: C.muted,
  });
  footer(s, 3);
  s.addNotes("Định nghĩa ngắn: NumPy là gói nền tảng cho tính toán khoa học, cung cấp ndarray cùng kho hàm toán học, logic, biến đổi hình dạng, sắp xếp, nhập xuất và đại số tuyến tính. Phiên bản dùng trong tài liệu là 2.5.4.");
}

/* ---------------------------------------------------------------- 04 problem */
{
  const s = p.addSlide(); bg(s);
  header(s, "01 · Giới thiệu", "NumPy giải quyết vấn đề gì?");
  const panel = (x, title, code, out, noteText, col) => {
    card(s, { x, y: 1.6, w: 5.95, h: 3.75 });
    s.addShape(p.ShapeType.rect, {
      x, y: 1.6, w: 5.95, h: 0.08,
      fill: { color: col }, line: { color: col, width: 0 },
    });
    tx(s, title, { x: x + 0.3, y: 1.82, w: 5.3, h: 0.45, fontSize: TYPE.subhead, bold: true, color: C.ink });
    tx(s, code, { x: x + 0.3, y: 2.34, w: 5.35, h: 0.95, fontSize: 17.5, fontFace: F.code, color: C.ink });
    tx(s, "KẾT QUẢ", { x: x + 0.3, y: 3.38, w: 2.0, h: 0.22, fontSize: 10.5, bold: true, color: C.green, charSpacing: 1.1 });
    tx(s, out, { x: x + 0.3, y: 3.62, w: 5.35, h: 0.48, fontSize: 18, fontFace: F.code, color: col });
    tx(s, noteText, { x: x + 0.3, y: 4.28, w: 5.3, h: 0.82, fontSize: TYPE.body, color: C.slate, italic: true });
  };
  panel(0.6, "Cách thủ công", "d = [8.0, 7.5, 9.0,\n     6.5, 8.5]\nprint([x + 0.5 for x in d])",
    "[8.5, 8.0, 9.5, 7.0, 9.0]",
    "Lặp qua từng phần tử — không có phép cộng cho cả danh sách.", C.amber);
  panel(6.78, "Với NumPy", "d = np.array([8.0, 7.5,\n              9.0, 6.5, 8.5])\nprint(d + 0.5)",
    "[8.5 8.  9.5 7.  9. ]",
    "Một phép cộng áp cho toàn mảng — không cần vòng lặp.", C.teal);
  ["Dữ liệu số nhiều chiều", "Code ngắn, gần ký hiệu toán", "Tính toán trên toàn mảng"].forEach((t, i) => {
    const x = 0.6 + i * 4.09;
    card(s, { x, y: 5.45, w: 3.95, h: 1.15, fill: C.ice, line: "CFE5EE", shadow: false });
    tx(s, String(i + 1), {
      x: x + 0.2, y: 5.45, w: 0.45, h: 1.15, fontSize: 26, bold: true,
      color: C.teal, valign: "mid",
    });
    tx(s, t, { x: x + 0.72, y: 5.45, w: 3.05, h: 1.15, fontSize: TYPE.body, color: C.ink, valign: "mid" });
  });
  footer(s, 4);
  s.addNotes("Ba động cơ: biểu diễn dữ liệu số nhiều chiều, viết ngắn hơn nhờ biểu thức mảng, và có sẵn hàm thống kê trên toàn mảng. Ví dụ: cộng 0,5 điểm thưởng cho 5 điểm 8.0, 7.5, 9.0, 6.5, 8.5. Cách thủ công phải lặp từng phần tử bằng comprehension; với NumPy chỉ cần d + 0.5, áp dụng cho cả mảng. Điểm cần nhấn: đây là so sánh cách viết (vòng lặp vs vector hóa), không phải so sánh kiểu list và array. Kết quả NumPy: [8.5 8. 9.5 7. 9.].");
}

/* ---------------------------------------------------------------- 05 ndarray */
{
  const s = p.addSlide(); bg(s);
  header(s, "02 · Cấu trúc mảng", "ndarray — đối tượng trung tâm");
  const items = [
    "Mảng N chiều: 0-D, 1-D, 2-D hoặc nhiều hơn.",
    "Các phần tử cùng một kiểu dữ liệu (dtype).",
    "Kích thước cố định sau khi khởi tạo.",
    "Lưới chữ nhật — mọi hàng cùng số cột.",
    "Mọi hàm NumPy nhận hoặc trả về ndarray.",
  ];
  items.forEach((t, i) => {
    const y = 1.78 + i * 0.92;
    bullet(s, 0.64, y, 5.3, t, { color: i === 4 ? C.amber : C.teal, h: 0.66 });
  });
  tx(s, "Một mảng 3 × 4", { x: 7.0, y: 1.62, w: 5.5, h: 0.42, fontSize: TYPE.subhead, bold: true, color: C.ink });
  tx(s, "trục 1  →", { x: 7.0, y: 2.02, w: 4.25, h: 0.22, fontSize: 14, color: C.muted, align: "right" });
  tx(s, "trục 0", { x: 6.3, y: 2.28, w: 0.55, h: 2.2, fontSize: 13, color: C.muted, align: "center", valign: "mid" });
  grid(s, {
    x: 7.05, y: 2.3, cw: 1.05, ch: 0.7, rows: 3, cols: 4,
    vals: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], fs: 20,
  });
  chip(s, "shape (3, 4)   ·   dtype int64", { x: 7.05, y: 4.55, w: 4.2, h: 0.48, fs: 15.5 });
  tx(s, "Cùng một dtype cho mọi ô — điều kiện để vector hóa.", {
    x: 7.05, y: 5.22, w: 5.5, h: 1.05, fontSize: TYPE.body, italic: true, color: C.slate,
  });
  tx(s, "Nguồn: NumPy Documentation [1], [2]", { x: 7.05, y: 6.48, w: 5.4, h: 0.25, fontSize: TYPE.source, color: C.muted });
  footer(s, 5);
  s.addNotes("ndarray là kiểu trung tâm: mảng N chiều, đồng nhất kiểu, kích thước cố định, dạng lưới chữ nhật. Hiểu ndarray là hiểu cách NumPy nghĩ: dữ liệu là lưới nhiều chiều và phép toán áp lên lưới đó.");
}

/* ---------------------------------------------------------------- 06 pros cons */
{
  const s = p.addSlide(); bg(s);
  header(s, "01 · Giới thiệu", "Ưu điểm và giới hạn");
  const column = (x, title, items, col, symbol) => {
    card(s, { x, y: 1.6, w: 5.95, h: 4.55 });
    s.addShape(p.ShapeType.rect, {
      x, y: 1.6, w: 5.95, h: 0.08,
      fill: { color: col }, line: { color: col, width: 0 },
    });
    tx(s, title, { x: x + 0.3, y: 1.82, w: 5.1, h: 0.45, fontSize: TYPE.subhead, bold: true, color: C.ink });
    items.forEach((t, i) => {
      const yy = 2.55 + i * 0.85;
      tx(s, symbol, { x: x + 0.32, y: yy, w: 0.3, h: 0.35, fontSize: 20, bold: true, color: col });
      tx(s, t, { x: x + 0.68, y: yy - 0.02, w: 4.9, h: 0.78, fontSize: TYPE.body, color: C.slate, lineSpacingMultiple: 1.02 });
    });
  };
  column(0.6, "Ưu điểm", [
    "Vector hóa: tính trên cả mảng, không cần vòng lặp.",
    "Broadcasting: tính giữa các shape khác nhau.",
    "Kho hàm toán học, thống kê, đại số tuyến tính.",
    "Nền tảng của hệ sinh thái khoa học.",
  ], C.teal, "✓");
  column(6.78, "Giới hạn", [
    "Dữ liệu phải đồng nhất kiểu.",
    "Kích thước cố định sau khi tạo.",
    "Không có nhãn cột, nhãn hàng.",
    "Mảng rất nhỏ có thể không cần tối ưu.",
  ], C.coral, "!");
  tx(s, "Nhận định tổng quát, không phải kết quả đo hiệu năng.", {
    x: 0.6, y: 6.32, w: 12.1, h: 0.3, fontSize: 15, italic: true, color: C.muted,
  });
  footer(s, 6);
  s.addNotes("Cân bằng hai mặt: mạnh ở vector hóa, broadcasting và hệ sinh thái; yếu khi dữ liệu không đồng nhất, cần thêm bớt phần tử, hoặc cần nhãn. Với bảng nhiều kiểu, pandas là lựa chọn phù hợp hơn.");
}

/* ---------------------------------------------------------------- 07 applications */
{
  const s = p.addSlide(); bg(s);
  header(s, "01 · Giới thiệu", "Ứng dụng thực tế");
  const items = [
    ["Khoa học & kỹ thuật", "Mô phỏng, xử lý tín hiệu."],
    ["Xử lý ảnh", "Ảnh là ma trận điểm ảnh."],
    ["Thống kê & dữ liệu", "Tính trên mảng lớn."],
    ["Học máy", "Đặc trưng, trọng số, gradient."],
    ["Mô phỏng số", "Lưới không gian, thời gian."],
  ];
  const xs = [0.6, 4.72, 8.84, 2.66, 6.78];
  const ys = [1.6, 1.6, 1.6, 4.02, 4.02];
  items.forEach((it, i) => {
    card(s, { x: xs[i], y: ys[i], w: 3.88, h: 2.3 });
    s.addShape(p.ShapeType.roundRect, {
      x: xs[i] + 0.26, y: ys[i] + 0.2, w: 0.52, h: 0.52,
      fill: { color: i % 2 ? C.ice : "D6EEF5" }, line: { color: "BFDFE9", width: 0.75 }, rectRadius: 0.12,
    });
    tx(s, String(i + 1), {
      x: xs[i] + 0.26, y: ys[i] + 0.2, w: 0.52, h: 0.52, fontSize: 17,
      bold: true, color: C.teal, align: "center", valign: "mid", fontFace: F.code,
    });
    tx(s, it[0], { x: xs[i] + 0.24, y: ys[i] + 0.65, w: 3.38, h: 0.62, fontSize: TYPE.subhead, bold: true, color: C.ink, lineSpacingMultiple: 0.98 });
    tx(s, it[1], { x: xs[i] + 0.24, y: ys[i] + 1.28, w: 3.38, h: 0.66, fontSize: TYPE.body, color: C.slate, lineSpacingMultiple: 1.0 });
  });
  card(s, { x: 0.6, y: 6.44, w: 12.13, h: 0.46, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "Điểm chung: dữ liệu số, đồng nhất kiểu, kích thước lớn.", {
    x: 0.85, y: 6.44, w: 11.6, h: 0.46, fontSize: TYPE.body, bold: true, color: C.teal, valign: "mid",
  });
  footer(s, 7);
  s.addNotes("Năm nhóm ứng dụng tiêu biểu. Điểm chung: dữ liệu là số, đồng nhất kiểu, kích thước lớn và cần tính hàng loạt.");
}

/* ---------------------------------------------------------------- 08 list vs array */
{
  const s = p.addSlide(); bg(s);
  header(s, "01 · Giới thiệu", "Python list và NumPy array");
  table(s,
    ["Tiêu chí", "Python list", "NumPy array"],
    [
      ["Kiểu dữ liệu", "Hỗn hợp", "Đồng nhất, một dtype"],
      ["Phép * 2", "Lặp danh sách", "Nhân từng phần tử"],
      ["Nhiều chiều", "List lồng nhau, có thể “răng cưa”", "Mảng N chiều xác định"],
      ["Bộ nhớ", "Các object rời rạc", "Khối dữ liệu đồng nhất"],
      ["Hiệu năng", "Vòng lặp Python", "Vector hóa trong code C"],
      ["Kích thước", "Linh hoạt", "Cố định sau khi tạo"],
    ],
    { x: 0.6, y: 1.62, w: 6.55, colW: [1.35, 2.25, 2.95], rowH: [0.48, 0.7, 0.55, 0.72, 0.55, 0.55, 0.62], fs: 15.5 }
  );
  codePanel(s, {
    x: 7.35, y: 1.62, w: 5.38, h: 1.8, fs: 16,
    code: "print([1, 2, 3, 4] * 2)\na = np.array([1, 2, 3, 4])\nprint(a * 2)",
  });
  outPanel(s, {
    x: 7.35, y: 3.55, w: 5.38, h: 1.25, fs: 15.5,
    text: "[1, 2, 3, 4, 1, 2, 3, 4]\n[2 4 6 8]",
  });
  card(s, { x: 7.35, y: 4.95, w: 5.38, h: 0.95, fill: "FFF6E7", line: "F0D8B4", shadow: false });
  tx(s, "Cùng một * — hai ngữ nghĩa khác nhau.", {
    x: 7.55, y: 4.95, w: 5.0, h: 0.95, fontSize: TYPE.body, bold: true, color: "9A6412", valign: "mid",
  });
  tx(s, "Chọn cấu trúc theo phép toán, không chỉ theo cách lưu.", {
    x: 0.6, y: 5.98, w: 6.45, h: 0.75, fontSize: TYPE.body, color: C.slate, italic: true,
  });
  tx(s, "Nguồn: NumPy Documentation [2], Python Tutorial [7]", {
    x: 0.6, y: 6.76, w: 6.5, h: 0.24, fontSize: TYPE.source, color: C.muted,
  });
  footer(s, 8);
  s.addNotes("Bảng so sánh sáu tiêu chí. Ví dụ then chốt: list nhân với 2 là lặp danh sách, ndarray nhân với 2 là nhân từng phần tử. Đây là lý do phải phân biệt rõ kiểu dữ liệu khi đọc code.");
}

/* ---------------------------------------------------------------- 09 dimensions */
{
  const s = p.addSlide(); bg(s);
  header(s, "02 · Cấu trúc mảng", "0-D, 1-D, 2-D và nhiều chiều");
  const cards = [
    ["0-D", "Một giá trị", "shape ()"],
    ["1-D", "Một dãy", "shape (3,)"],
    ["2-D", "Một bảng", "shape (2, 3)"],
    ["3-D", "Chồng bảng", "shape (2, 3, 4)"],
  ];
  cards.forEach((c, i) => {
    const x = 0.6 + i * 3.07;
    card(s, { x, y: 1.62, w: 2.92, h: 2.48 });
    tx(s, c[0], { x: x + 0.22, y: 1.76, w: 1.0, h: 0.4, fontSize: TYPE.subhead, bold: true, color: C.teal, fontFace: F.code });
    tx(s, c[1], { x: x + 0.98, y: 1.82, w: 1.75, h: 0.45, fontSize: 17, color: C.muted });
    const gx = x + 0.38, gy = 2.35;
    if (i === 0) {
      s.addShape(p.ShapeType.rect, { x: gx + 0.78, y: gy + 0.2, w: 0.56, h: 0.56, fill: { color: C.cyan }, line: { color: C.white, width: 1 } });
      tx(s, "7", { x: gx + 0.78, y: gy + 0.2, w: 0.56, h: 0.56, fontSize: 18, bold: true, color: C.white, align: "center", valign: "mid", fontFace: F.code });
    } else if (i === 1) {
      for (let k = 0; k < 3; k++) {
        s.addShape(p.ShapeType.rect, { x: gx + 0.45 + k * 0.42, y: gy + 0.2, w: 0.42, h: 0.56, fill: { color: C.ice }, line: { color: "A9CDDB", width: 0.75 } });
        tx(s, String(k + 1), { x: gx + 0.45 + k * 0.42, y: gy + 0.2, w: 0.42, h: 0.56, fontSize: 15, color: C.ink, align: "center", valign: "mid", fontFace: F.code });
      }
    } else if (i === 2) {
      for (let r = 0; r < 2; r++) for (let cc = 0; cc < 3; cc++) {
        s.addShape(p.ShapeType.rect, { x: gx + 0.38 + cc * 0.45, y: gy + 0.08 + r * 0.46, w: 0.45, h: 0.46, fill: { color: C.ice }, line: { color: "A9CDDB", width: 0.75 } });
        tx(s, String(1 + r * 3 + cc), { x: gx + 0.38 + cc * 0.45, y: gy + 0.08 + r * 0.46, w: 0.45, h: 0.46, fontSize: 13, color: C.ink, align: "center", valign: "mid", fontFace: F.code });
      }
    } else {
      for (let d = 0; d < 2; d++) {
        s.addShape(p.ShapeType.rect, { x: gx + 0.55 - d * 0.12, y: gy + 0.03 + d * 0.12, w: 1.1, h: 0.62, fill: { color: d === 1 ? "BFE6F1" : C.ice }, line: { color: "A9CDDB", width: 0.75 } });
      }
      tx(s, "2 lớp · 3 × 4", { x: gx + 0.25, y: gy + 0.9, w: 1.7, h: 0.25, fontSize: 13, color: C.muted, align: "center" });
    }
    tx(s, c[2], { x: x + 0.22, y: 3.58, w: 2.55, h: 0.35, fontSize: 17, fontFace: F.code, color: C.ink, bold: true });
  });
  codePanel(s, {
    x: 0.6, y: 4.3, w: 7.5, h: 1.95, fs: 16,
    code: "print(np.array(7).shape)\nprint(np.array([1, 2, 3]).shape)\na = np.array([[1, 2, 3], [4, 5, 6]])\nprint(a.shape)\nprint(np.zeros((2, 3, 4)).shape)",
  });
  outPanel(s, {
    x: 8.25, y: 4.3, w: 4.48, h: 1.95, fs: 17,
    text: "()\n(3,)\n(2, 3)\n(2, 3, 4)",
  });
  tx(s, "Cú pháp (3,) cần dấu phẩy để Python hiểu là tuple một phần tử.", {
    x: 0.6, y: 6.4, w: 12.1, h: 0.38, fontSize: TYPE.body, italic: true, color: C.muted,
  });
  footer(s, 9);
  s.addNotes("Số chiều là số trục của lưới. 0-D là một giá trị, 1-D là dãy, 2-D là bảng hàng cột, 3-D là chồng các bảng. Cú pháp shape (3,) cần dấu phẩy vì Python coi (3) là số 3 chứ không phải tuple.");
}

/* ---------------------------------------------------------------- 10 properties */
{
  const s = p.addSlide(); bg(s);
  header(s, "02 · Cấu trúc mảng", "Bốn thuộc tính quan trọng");
  card(s, { x: 0.6, y: 1.6, w: 5.5, h: 4.2, fill: C.ink, line: C.ink });
  tx(s, "HỘ CHIẾU MẢNG", { x: 0.9, y: 1.78, w: 4.5, h: 0.28, fontSize: 12, bold: true, color: C.cyan, charSpacing: 1.5 });
  tx(s, "ndarray  ·  (2, 3)", { x: 0.9, y: 2.08, w: 4.7, h: 0.45, fontSize: TYPE.subhead, bold: true, color: C.white, fontFace: F.code });
  const props = [
    ["ndim", "2", "số chiều"],
    ["shape", "(2, 3)", "kích thước từng chiều"],
    ["size", "6", "tổng số phần tử"],
    ["dtype", "int64", "kiểu dữ liệu"],
  ];
  props.forEach((pr, i) => {
    const y = 2.7 + i * 0.7;
    s.addShape(p.ShapeType.rect, { x: 0.9, y: y + 0.6, w: 4.9, h: 0.01, fill: { color: "1D4657" }, line: { color: "1D4657", width: 0 } });
    tx(s, pr[0], { x: 0.9, y, w: 0.95, h: 0.35, fontSize: 18, color: C.cyan, fontFace: F.code });
    tx(s, pr[1], { x: 1.85, y: y - 0.02, w: 1.25, h: 0.4, fontSize: TYPE.body, bold: true, color: C.white, fontFace: F.code });
    tx(s, pr[2], { x: 3.15, y: y + 0.04, w: 2.6, h: 0.38, fontSize: 15.5, color: "8FB0BF", align: "right" });
  });
  codePanel(s, {
    x: 6.35, y: 1.6, w: 6.38, h: 2.15, fs: 16,
    code: "a = np.array([[1, 2, 3], [4, 5, 6]])\nprint(a.ndim)\nprint(a.shape)\nprint(a.size)\nprint(a.dtype)",
  });
  outPanel(s, { x: 6.35, y: 3.88, w: 6.38, h: 1.65, text: "2\n(2, 3)\n6\nint64", fs: 17 });
  ["ndim = len(shape)", "size = tích(shape)"].forEach((t, i) => {
    card(s, { x: 0.6 + i * 6.13, y: 5.95, w: 6.0, h: 0.6, fill: C.ice, line: "CFE5EE", shadow: false });
    tx(s, t, { x: 0.85 + i * 6.13, y: 5.95, w: 5.5, h: 0.6, fontSize: TYPE.body, bold: true, color: C.teal, fontFace: F.code, valign: "mid" });
  });
  tx(s, "Nguồn: NumPy Documentation [2]", { x: 0.6, y: 6.7, w: 5, h: 0.24, fontSize: TYPE.source, color: C.muted });
  footer(s, 10);
  s.addNotes("Bốn thuộc tính mô tả đầy đủ hình dạng dữ liệu: ndim là số chiều, shape là tuple kích thước, size là tổng phần tử, dtype là kiểu. Quan hệ: ndim bằng độ dài shape, size bằng tích các chiều.");
}

/* ---------------------------------------------------------------- 11 create 1 */
{
  const s = p.addSlide(); bg(s);
  header(s, "03 · Tạo mảng", "Ba hàm cơ bản: array, zeros, ones");
  const blocks = [
    {
      title: "np.array()", sub: "Từ list hoặc tuple",
      code: "np.array([1, 2, 3])\nnp.array([[1, 2, 3],\n          [4, 5, 6]])",
      out: "[1 2 3]\n[[1 2 3]\n [4 5 6]]",
    },
    {
      title: "np.zeros()", sub: "Mảng toàn số 0",
      code: "np.zeros((2, 3))",
      out: "[[0. 0. 0.]\n [0. 0. 0.]]",
    },
    {
      title: "np.ones()", sub: "Mảng toàn số 1",
      code: "np.ones(4)\nnp.ones(3, dtype=np.int64)",
      out: "[1. 1. 1. 1.]\n[1 1 1]",
    },
  ];
  blocks.forEach((b, i) => {
    const x = 0.6 + i * 4.09;
    card(s, { x, y: 1.6, w: 3.95, h: 4.85 });
    tx(s, b.title, { x: x + 0.24, y: 1.8, w: 3.45, h: 0.4, fontSize: TYPE.subhead, bold: true, color: C.ink, fontFace: F.code });
    tx(s, b.sub, { x: x + 0.24, y: 2.25, w: 3.45, h: 0.38, fontSize: TYPE.body, color: C.muted });
    codePanel(s, { x: x + 0.2, y: 2.72, w: 3.48, h: 1.55, fs: 16, code: b.code, title: "python" });
    outPanel(s, { x: x + 0.2, y: 4.42, w: 3.48, h: 1.35, fs: 15.5, text: b.out });
    tx(s, i === 0 ? "Tự suy ra dtype từ dữ liệu." : i === 1 ? "Nhận shape dạng tuple." : "Chỉ định dtype khi cần.", {
      x: x + 0.24, y: 5.92, w: 3.45, h: 0.35, fontSize: 15, italic: true, color: C.muted,
    });
  });
  tx(s, "zeros/ones mặc định float64; dùng dtype=np.int64 nếu cần số nguyên.", {
    x: 0.6, y: 6.55, w: 12.1, h: 0.35, fontSize: TYPE.body, italic: true, color: C.muted,
  });
  footer(s, 11);
  s.addNotes("Ba hàm tạo mảng cơ bản nhất. array nhận dữ liệu có sẵn và tự suy ra dtype; zeros và ones nhận shape dạng tuple và mặc định trả về float64. Có thể chỉ định dtype khi cần.");
}

/* ---------------------------------------------------------------- 12 create 2 */
{
  const s = p.addSlide(); bg(s);
  header(s, "03 · Tạo mảng", "Tạo dãy: arange, linspace, eye");
  codePanel(s, {
    x: 0.6, y: 1.6, w: 6.2, h: 2.35, fs: 16,
    code: "np.arange(0, 10, 2)\nnp.arange(4)\n\nnp.linspace(0, 1, 5)\n\nnp.eye(3)",
  });
  outPanel(s, {
    x: 0.6, y: 4.1, w: 6.2, h: 2.05, fs: 15.5,
    text: "[0 2 4 6 8]\n[0 1 2 3]\n[0.   0.25 0.5  0.75 1.  ]\n[[1. 0. 0.]\n [0. 1. 0.]\n [0. 0. 1.]]",
  });
  table(s,
    ["Hàm", "Dùng khi", "Điểm cần nhớ"],
    [
      ["np.arange", "Dãy theo bước", "Không gồm stop"],
      ["np.linspace", "num điểm chia đều", "Mặc định gồm stop"],
      ["np.eye", "Ma trận đơn vị", "Đường chéo bằng 1"],
    ],
    { x: 7.05, y: 1.6, w: 5.68, colW: [1.65, 1.95, 2.08], rowH: [0.48, 0.55, 0.55, 0.55], fs: 15.5, monoFirst: true }
  );
  card(s, { x: 7.05, y: 3.95, w: 5.68, h: 2.2, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "Phân biệt nhanh", { x: 7.28, y: 4.08, w: 5.2, h: 0.4, fontSize: TYPE.subhead, bold: true, color: C.ink });
  tx(s, "•  arange: theo bước, không lấy stop.\n•  linspace: số điểm, mặc định lấy stop.\n•  eye(n): ma trận đơn vị n × n.", {
    x: 7.28, y: 4.55, w: 5.2, h: 1.4, fontSize: TYPE.body, color: C.slate, lineSpacingMultiple: 1.08,
  });
  tx(s, "Nguồn: NumPy Documentation [2], [5]", { x: 0.6, y: 6.35, w: 5.5, h: 0.24, fontSize: TYPE.source, color: C.muted });
  footer(s, 12);
  s.addNotes("arange tạo dãy theo bước và không gồm stop; linspace tạo num điểm chia đều và mặc định gồm điểm cuối; eye tạo ma trận đơn vị. Chọn hàm theo cách mô tả dữ liệu: bước nhảy hay số điểm.");
}

/* ---------------------------------------------------------------- 13 indexing 1d */
{
  const s = p.addSlide(); bg(s);
  header(s, "04 · Truy cập dữ liệu", "Indexing và slicing mảng 1-D");
  const vals = [0, 10, 20, 30, 40, 50];
  const cw = 0.85, ch = 0.85, gx = 0.8, gy = 2.55;
  vals.forEach((v, i) => {
    const on = i === 1 || i === 5;
    s.addShape(p.ShapeType.rect, {
      x: gx + i * cw, y: gy, w: cw, h: ch,
      fill: { color: on ? C.cyan : C.ice }, line: { color: "A9CDDB", width: 0.75 },
    });
    tx(s, String(v), { x: gx + i * cw, y: gy, w: cw, h: ch, fontSize: 20, bold: on, color: on ? C.white : C.ink, align: "center", valign: "mid", fontFace: F.code });
    tx(s, String(i), { x: gx + i * cw, y: gy - 0.36, w: cw, h: 0.26, fontSize: 15, color: C.teal, align: "center", fontFace: F.code });
    tx(s, String(i - 6), { x: gx + i * cw, y: gy + ch + 0.1, w: cw, h: 0.26, fontSize: 15, color: C.coral, align: "center", fontFace: F.code });
  });
  label(s, "chỉ số dương", { x: gx, y: 2.0, w: 3.7, h: 0.25, align: "left", fontSize: 14 });
  label(s, "chỉ số âm", { x: gx, y: 3.65, w: 3.7, h: 0.25, align: "left", fontSize: 14 });
  tx(s, "start:stop:step — không lấy stop", {
    x: 0.8, y: 4.15, w: 5.4, h: 0.4, fontSize: TYPE.body, bold: true, color: C.ink,
  });
  tx(s, "Slicing trả về view, không phải bản sao. Dùng .copy() nếu cần dữ liệu độc lập.", {
    x: 0.8, y: 4.78, w: 5.4, h: 1.35, fontSize: TYPE.body, color: C.slate, lineSpacingMultiple: 1.1,
  });
  codePanel(s, {
    x: 6.3, y: 1.6, w: 6.43, h: 2.9, fs: 16,
    code: "c = np.array([0, 10, 20, 30, 40, 50])\nprint(c[1])      # 10\nprint(c[-1])     # 50\nprint(c[1:4])    # [10 20 30]\nprint(c[::2])    # [ 0 20 40]\nprint(c[::-1])   # [50 40 30 20 10  0]",
  });
  outPanel(s, {
    x: 6.3, y: 4.65, w: 6.43, h: 1.9, fs: 16,
    text: "10\n50\n[10 20 30]\n[ 0 20 40]\n[50 40 30 20 10  0]",
  });
  footer(s, 13);
  s.addNotes("Chỉ số bắt đầu từ 0, chỉ số âm tính từ cuối. Slice start:stop:step không lấy stop, c[::2] lấy cách một, c[::-1] đảo ngược. Lưu ý slicing trả về view nên sửa view sẽ ảnh hưởng mảng gốc.");
}

/* ---------------------------------------------------------------- 14 indexing 2d */
{
  const s = p.addSlide(); bg(s);
  header(s, "04 · Truy cập dữ liệu", "Indexing mảng 2-D: hàng, cột, khối con");
  const base = [[10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33]];
  const panels = [
    ["a[1]", "cả hàng", { "1,0": C.cyan, "1,1": C.cyan, "1,2": C.cyan, "1,3": C.cyan }],
    ["a[:, 2]", "cả cột", { "0,2": C.teal, "1,2": C.teal, "2,2": C.teal }],
    ["a[0:2, 1:3]", "khối con", { "0,1": C.coral, "0,2": C.coral, "1,1": C.coral, "1,2": C.coral }],
  ];
  panels.forEach((pn, i) => {
    const x = 0.65 + i * 2.0;
    tx(s, pn[0], { x: x - 0.12, y: 1.55, w: 1.95, h: 0.28, fontSize: 16, bold: true, color: C.slate, align: "center", fontFace: F.code });
    grid(s, { x, y: 1.92, cw: 0.44, ch: 0.42, rows: 3, cols: 4, vals: base, fs: 13.5, hi: pn[2] });
    tx(s, pn[1], { x: x - 0.02, y: 3.28, w: 1.75, h: 0.24, fontSize: 13.5, color: C.muted, align: "center" });
  });
  card(s, { x: 0.6, y: 3.68, w: 5.6, h: 2.75, fill: C.white, line: C.border, shadow: false });
  tx(s, "Cách đọc kết quả", { x: 0.85, y: 3.82, w: 5.0, h: 0.4, fontSize: TYPE.subhead, bold: true, color: C.ink });
  [
    [C.cyan, "b[1]", "hàng → 1-D, (4,)"],
    [C.teal, "b[:, 2]", "cột → 1-D, (3,)"],
    [C.coral, "b[0:2, 1:3]", "khối → 2-D, (2, 2)"],
  ].forEach((r, i) => {
    const y = 4.38 + i * 0.6;
    s.addShape(p.ShapeType.rect, { x: 0.85, y: y + 0.08, w: 0.08, h: 0.26, fill: { color: r[0] }, line: { color: r[0], width: 0 } });
    tx(s, r[1], { x: 1.05, y: y, w: 1.45, h: 0.3, fontSize: 16, fontFace: F.code, bold: true, color: C.slate });
    tx(s, r[2], { x: 2.55, y: y, w: 3.35, h: 0.3, fontSize: TYPE.body, color: C.slate });
  });
  codePanel(s, {
    x: 6.5, y: 1.6, w: 6.23, h: 2.7, fs: 15.5,
    code: "b = np.array([[10, 11, 12, 13],\n              [20, 21, 22, 23],\n              [30, 31, 32, 33]])\nprint(b[1])        # [20 21 22 23]\nprint(b[:, 2])     # [12 22 32]\nprint(b[0:2, 1:3]) # [[11 12] [21 22]]",
  });
  outPanel(s, {
    x: 6.5, y: 4.45, w: 6.23, h: 1.55, fs: 15.5,
    text: "[20 21 22 23]\n[12 22 32]\n[[11 12]\n [21 22]]",
  });
  tx(s, "a[hàng, cột]; dấu : lấy cả trục.", {
    x: 0.6, y: 6.58, w: 12.1, h: 0.35, fontSize: TYPE.body, italic: true, color: C.muted,
  });
  footer(s, 14);
  s.addNotes("Với mảng hai chiều, dùng a[hàng, cột]. b[1] lấy cả hàng, b[:, 2] lấy cả cột, b[0:2, 1:3] lấy khối con. Ba hình nhỏ bên trái tô màu đúng vùng được chọn.");
}

/* ---------------------------------------------------------------- 15 boolean */
{
  const s = p.addSlide(); bg(s);
  header(s, "04 · Truy cập dữ liệu", "Boolean indexing: lọc theo điều kiện");
  const base = [[10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33]];
  const mask = base.map((r) => r.map((v) => (v > 21 ? "T" : "F")));
  const mh = {};
  mask.forEach((r, i) => r.forEach((v, j) => { if (v === "T") mh[i + "," + j] = C.green; }));
  tx(s, "b", { x: 0.7, y: 1.56, w: 2.0, h: 0.3, fontSize: TYPE.body, bold: true, color: C.slate, fontFace: F.code });
  tx(s, "b > 21", { x: 3.05, y: 1.56, w: 2.0, h: 0.3, fontSize: TYPE.body, bold: true, color: C.slate, fontFace: F.code });
  tx(s, "b[b > 21]", { x: 5.45, y: 1.56, w: 1.9, h: 0.3, fontSize: TYPE.body, bold: true, color: C.slate, fontFace: F.code });
  grid(s, { x: 0.7, y: 1.95, cw: 0.52, ch: 0.38, rows: 3, cols: 4, vals: base, fs: 14 });
  grid(s, { x: 3.05, y: 1.95, cw: 0.52, ch: 0.38, rows: 3, cols: 4, vals: mask, fs: 14, fill: "F1F7F9", line: "B9D7E4", hi: mh });
  const res = [22, 23, 30, 31, 32, 33];
  res.forEach((v, i) => {
    const y = 1.95 + i * 0.38;
    s.addShape(p.ShapeType.rect, { x: 5.45, y, w: 1.55, h: 0.38, fill: { color: C.ice }, line: { color: "A9CDDB", width: 0.75 } });
    tx(s, String(v), { x: 5.45, y, w: 1.55, h: 0.38, fontSize: 15, bold: true, color: C.green, align: "center", valign: "mid", fontFace: F.code });
  });
  tx(s, "T = True · F = False", { x: 3.05, y: 3.16, w: 2.2, h: 0.24, fontSize: 13, color: C.muted });
  card(s, { x: 7.0, y: 1.95, w: 5.7, h: 1.80, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "Cách hoạt động", { x: 7.22, y: 2.08, w: 5.2, h: 0.4, fontSize: TYPE.subhead, bold: true, color: C.ink });
  tx(s, "So sánh tạo mask cùng shape; chỉ các ô True được giữ lại.", {
    x: 7.22, y: 2.58, w: 5.25, h: 0.95, fontSize: TYPE.body, color: C.slate, lineSpacingMultiple: 1.08,
  });
  codePanel(s, {
    x: 0.6, y: 4.35, w: 6.2, h: 1.50, fs: 16.5,
    code: "print(b[b > 21])\nprint(b > 21)",
  });
  outPanel(s, {
    x: 6.95, y: 4.35, w: 5.78, h: 1.65, fs: 14.5,
    text: "[22 23 30 31 32 33]\n[[False False False False]\n [False False  True  True]\n [ True  True  True  True]]",
  });
  tx(s, "Kết quả nén thành 1-D; kết hợp điều kiện bằng &, | và ngoặc đơn.", {
    x: 0.6, y: 6.20, w: 12.1, h: 0.38, fontSize: TYPE.body, italic: true, color: C.muted,
  });
  footer(s, 15);
  s.addNotes("So sánh một mảng với một giá trị tạo ra mảng boolean cùng shape. Dùng mảng boolean làm chỉ số sẽ lấy các phần tử True và nén thành mảng một chiều. Kết hợp điều kiện bằng & và |, nhớ đặt ngoặc đơn.");
}

/* ---------------------------------------------------------------- 16 reshape */
{
  const s = p.addSlide(); bg(s);
  header(s, "04 · Truy cập dữ liệu", "reshape() và .T: cùng dữ liệu, khác hình dạng");
  const seq = [0, 1, 2, 3, 4, 5];
  tx(s, "1-D  ·  shape (6,)", { x: 0.7, y: 1.55, w: 3.2, h: 0.3, fontSize: 17, bold: true, color: C.slate });
  seq.forEach((v, i) => {
    s.addShape(p.ShapeType.rect, { x: 0.7 + i * 0.55, y: 1.95, w: 0.55, h: 0.55, fill: { color: C.ice }, line: { color: "A9CDDB", width: 0.75 } });
    tx(s, String(v), { x: 0.7 + i * 0.55, y: 1.95, w: 0.55, h: 0.55, fontSize: 17, color: C.ink, align: "center", valign: "mid", fontFace: F.code });
  });
  arrow(s, 4.15, 2.23, 4.55, 2.23, { color: C.teal, w: 1.75 });
  tx(s, "reshape(2, 3)", { x: 3.9, y: 1.55, w: 1.8, h: 0.3, fontSize: 14, color: C.teal, align: "center", fontFace: F.code });
  for (let r = 0; r < 2; r++) for (let c = 0; c < 3; c++) {
    s.addShape(p.ShapeType.rect, { x: 4.6 + c * 0.55, y: 1.95 + r * 0.55, w: 0.55, h: 0.55, fill: { color: "D6EEF5" }, line: { color: "A9CDDB", width: 0.75 } });
    tx(s, String(r * 3 + c), { x: 4.6 + c * 0.55, y: 1.95 + r * 0.55, w: 0.55, h: 0.55, fontSize: 17, color: C.ink, align: "center", valign: "mid", fontFace: F.code });
  }
  tx(s, "shape (2, 3)", { x: 4.6, y: 3.15, w: 1.8, h: 0.28, fontSize: 14, color: C.muted, fontFace: F.code });
  arrow(s, 6.4, 2.23, 6.8, 2.23, { color: C.amber, w: 1.75 });
  tx(s, ".T", { x: 6.45, y: 1.55, w: 0.6, h: 0.3, fontSize: 18, bold: true, color: C.amber, align: "center", fontFace: F.code });
  for (let r = 0; r < 3; r++) for (let c = 0; c < 2; c++) {
    s.addShape(p.ShapeType.rect, { x: 6.95 + c * 0.55, y: 1.95 + r * 0.5, w: 0.55, h: 0.5, fill: { color: "FBEFD9" }, line: { color: "E5C28C", width: 0.75 } });
    tx(s, String(c * 3 + r), { x: 6.95 + c * 0.55, y: 1.95 + r * 0.5, w: 0.55, h: 0.5, fontSize: 17, color: C.ink, align: "center", valign: "mid", fontFace: F.code });
  }
  tx(s, "shape (3, 2)", { x: 6.95, y: 3.58, w: 1.6, h: 0.28, fontSize: 14, color: C.muted, fontFace: F.code });
  card(s, { x: 9.55, y: 1.7, w: 3.18, h: 2.25, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "Mẹo -1", { x: 9.78, y: 1.85, w: 2.75, h: 0.4, fontSize: TYPE.subhead, bold: true, color: C.teal });
  tx(s, "reshape(3, -1) tự suy ra chiều còn lại: (3, 4).", {
    x: 9.78, y: 2.32, w: 2.72, h: 1.3, fontSize: TYPE.body, color: C.slate, lineSpacingMultiple: 1.08,
  });
  codePanel(s, {
    x: 0.6, y: 3.95, w: 6.4, h: 2.38, fs: 16,
    code: "r = np.arange(6).reshape(2, 3)\nprint(r)\nprint(r.T)\nprint(np.arange(12).reshape(3, -1).shape)",
  });
  outPanel(s, {
    x: 7.2, y: 3.95, w: 5.53, h: 2.38, fs: 15,
    text: "[[0 1 2]\n [3 4 5]]\n\n[[0 3]\n [1 4]\n [2 5]]\n\n(3, 4)",
  });
  tx(s, "Tổng phần tử giữ nguyên: 6 = 2 × 3 = 3 × 2. .T hoán vị hàng/cột.", {
    x: 0.6, y: 6.44, w: 12.1, h: 0.35, fontSize: TYPE.body, italic: true, color: C.muted,
  });
  footer(s, 16);
  s.addNotes("reshape đổi hình dạng nhưng giữ nguyên dữ liệu và thứ tự đọc; tổng số phần tử phải bằng nhau. Dùng -1 để tự suy ra một chiều. .T hoán vị hàng và cột, không đổi dữ liệu.");
}

/* ---------------------------------------------------------------- 17 element-wise */
{
  const s = p.addSlide(); bg(s);
  header(s, "05 · Tính toán", "Phép toán theo từng phần tử");
  const row = (vals, y, hi) => vals.forEach((v, i) => {
    s.addShape(p.ShapeType.rect, { x: 1.2 + i * 0.62, y, w: 0.62, h: 0.6, fill: { color: hi || C.ice }, line: { color: "A9CDDB", width: 0.75 } });
    tx(s, String(v), { x: 1.2 + i * 0.62, y, w: 0.62, h: 0.6, fontSize: 18, color: hi ? C.white : C.ink, align: "center", valign: "mid", fontFace: F.code });
  });
  tx(s, "x", { x: 0.75, y: 2.02, w: 0.3, h: 0.35, fontSize: TYPE.body, bold: true, color: C.muted, fontFace: F.code });
  tx(s, "y", { x: 0.75, y: 3.08, w: 0.3, h: 0.35, fontSize: TYPE.body, bold: true, color: C.muted, fontFace: F.code });
  tx(s, "x + y", { x: 0.15, y: 4.55, w: 1.0, h: 0.4, fontSize: 17, bold: true, color: C.teal, fontFace: F.code, align: "right" });
  row([1, 2, 3], 1.95);
  row([4, 5, 6], 3.0);
  row([5, 7, 9], 4.42, C.teal);
  tx(s, "+", { x: 1.2, y: 2.62, w: 0.4, h: 0.32, fontSize: 24, bold: true, color: C.teal, align: "center" });
  arrow(s, 2.25, 3.68, 2.25, 4.28, { color: C.teal, w: 1.75 });
  tx(s, "Mỗi toán tử áp cho từng cặp phần tử.", {
    x: 0.7, y: 5.35, w: 3.45, h: 0.9, fontSize: TYPE.body, color: C.slate, lineSpacingMultiple: 1.08,
  });
  codePanel(s, {
    x: 4.55, y: 1.6, w: 8.18, h: 3.0, fs: 16,
    code: "x = np.array([1, 2, 3])\ny = np.array([4, 5, 6])\nprint(x + y)   # [5 7 9]\nprint(x - y)   # [-3 -3 -3]\nprint(x * y)   # [ 4 10 18]\nprint(x / y)   # [0.25 0.4  0.5 ]\nprint(x ** 2)  # [1 4 9]\nprint(x // 2)  # [0 1 1]",
  });
  outPanel(s, {
    x: 4.55, y: 4.8, w: 8.18, h: 1.35, fs: 15.5,
    text: "[5 7 9]   [-3 -3 -3]   [ 4 10 18]\n[0.25 0.4 0.5]   [1 4 9]   [0 1 1]",
  });
  tx(s, "/ luôn trả về số thực; // là chia lấy phần nguyên.", {
    x: 4.55, y: 6.32, w: 8.2, h: 0.35, fontSize: TYPE.body, italic: true, color: C.muted,
  });
  footer(s, 17);
  s.addNotes("Các toán tử +, -, *, /, **, //, % áp dụng cho từng cặp phần tử và trả về mảng cùng shape. Lưu ý / luôn trả về số thực, còn // là chia lấy phần nguyên.");
}

/* ---------------------------------------------------------------- 18 star vs at */
{
  const s = p.addSlide(); bg(s);
  header(s, "05 · Tính toán", "Toán tử * và @ khác nhau thế nào?");
  const drawMat = (x, y, vals, hi, labelText) => {
    label(s, labelText, { x, y: y - 0.3, w: 1.12, h: 0.24, fontSize: 15, bold: true, color: C.slate, fontFace: F.code, align: "center" });
    grid(s, { x, y, cw: 0.56, ch: 0.5, rows: 2, cols: 2, vals, fs: 17, hi: hi || {} });
  };
  drawMat(0.6, 2.0, [[1, 2], [3, 4]], { "0,0": C.amber }, "A");
  tx(s, "*", { x: 1.78, y: 2.45, w: 0.3, h: 0.35, fontSize: 22, bold: true, color: C.teal, align: "center" });
  drawMat(2.1, 2.0, [[5, 6], [7, 8]], { "0,0": C.amber }, "B");
  tx(s, "=", { x: 3.22, y: 2.45, w: 0.3, h: 0.35, fontSize: 22, color: C.muted, align: "center" });
  drawMat(3.58, 2.0, [[5, 12], [21, 32]], { "0,0": C.amber }, "A * B");
  tx(s, "từng cặp ô cùng vị trí", { x: 0.6, y: 3.22, w: 4.2, h: 0.28, fontSize: 15, color: C.muted, italic: true });

  drawMat(0.6, 4.5, [[1, 2], [3, 4]], { "0,0": C.cyan, "0,1": C.cyan }, "A");
  tx(s, "@", { x: 1.78, y: 4.95, w: 0.3, h: 0.35, fontSize: 22, bold: true, color: C.amber, align: "center" });
  drawMat(2.1, 4.5, [[5, 6], [7, 8]], { "0,0": C.cyan, "1,0": C.cyan }, "B");
  tx(s, "=", { x: 3.22, y: 4.95, w: 0.3, h: 0.35, fontSize: 22, color: C.muted, align: "center" });
  drawMat(3.58, 4.5, [[19, 22], [43, 50]], { "0,0": C.amber }, "A @ B");
  tx(s, "hàng × cột: 1×5 + 2×7 = 19", { x: 0.6, y: 5.72, w: 4.4, h: 0.28, fontSize: 15, color: C.muted, italic: true });
  tx(s, "Dùng đúng toán tử: * từng phần tử, @ hàng × cột.", {
    x: 0.6, y: 6.2, w: 4.4, h: 0.7, fontSize: TYPE.body, bold: true, color: C.ink, lineSpacingMultiple: 1.05,
  });
  codePanel(s, {
    x: 5.15, y: 1.6, w: 7.58, h: 2.1, fs: 16,
    code: "A = np.array([[1, 2], [3, 4]])\nB = np.array([[5, 6], [7, 8]])\nprint(A * B)   # [[ 5 12] [21 32]]\nprint(A @ B)   # [[19 22] [43 50]]",
  });
  outPanel(s, {
    x: 5.15, y: 3.85, w: 7.58, h: 1.25, fs: 16,
    text: "A * B: [[ 5 12] [21 32]]\nA @ B: [[19 22] [43 50]]",
  });
  table(s,
    ["Toán tử", "Ý nghĩa", "Điều kiện shape"],
    [
      ["*", "Nhân từng phần tử", "Cùng shape hoặc broadcast được"],
      ["@", "Nhân ma trận", "Số cột A = số hàng B"],
    ],
    { x: 5.15, y: 5.35, w: 7.58, colW: [0.95, 2.3, 4.33], rowH: [0.38, 0.42, 0.42], fs: 16, monoFirst: true }
  );
  footer(s, 18);
  s.addNotes("Đây là lỗi rất dễ mắc: * là nhân từng phần tử, @ là nhân ma trận theo quy tắc hàng nhân cột. Với A@B, phần tử (0,0) bằng 1×5 + 2×7 = 19, còn A*B cho 1×5 = 5.");
}

/* ---------------------------------------------------------------- 19 axis */
{
  const s = p.addSlide(); bg(s);
  header(s, "05 · Tính toán", "Hàm tổng hợp và ý nghĩa của axis");
  const vals = [[1, 2, 3], [4, 5, 6]];
  const gx = 1.45, gy = 2.28, cw = 0.85, ch = 0.68;
  grid(s, { x: gx, y: gy, cw, ch, rows: 2, cols: 3, vals, fs: 20 });
  label(s, "m", { x: 0.92, y: 1.91, w: 0.45, h: 0.25, fontSize: 16, bold: true, color: C.slate, fontFace: F.code });
  arrow(s, gx - 0.32, gy + 0.08, gx - 0.32, gy + 1.08, { color: C.teal, w: 1.5, begin: true, end: true });
  tx(s, "axis = 0", { x: 0.35, y: gy + 1.18, w: 1.0, h: 0.24, fontSize: 14, bold: true, color: C.teal, align: "center", fontFace: F.code });
  arrow(s, gx + 0.05, gy - 0.27, gx + 1.80, gy - 0.27, { color: C.amber, w: 1.5, begin: true, end: true });
  tx(s, "axis = 1", { x: gx + 1.85, y: gy - 0.39, w: 0.95, h: 0.24, fontSize: 14, bold: true, color: "B7771B", fontFace: F.code });
  tx(s, "[5 7 9]", { x: gx - 0.20, y: gy + 1.50, w: 2.35, h: 0.35, fontSize: 20, bold: true, color: C.teal, fontFace: F.code });
  tx(s, "[ 6 15]", { x: gx + cw * 3 + 0.18, y: gy + 0.32, w: 1.30, h: 0.35, fontSize: 20, bold: true, color: "B7771B", fontFace: F.code });
  label(s, "gộp hàng → theo cột", { x: gx - 0.15, y: gy + 1.92, w: 2.55, h: 0.24, fontSize: 14 });
  label(s, "gộp cột\n→ theo hàng", { x: gx + cw * 3 + 0.16, y: gy + 0.75, w: 1.35, h: 0.48, fontSize: 13.5 });
  codePanel(s, {
    x: 5.75, y: 1.6, w: 6.98, h: 2.55, fs: 15.5,
    code: "print(np.sum(m))           # 21\nprint(np.sum(m, axis=0))   # [5 7 9]\nprint(np.sum(m, axis=1))   # [ 6 15]\nprint(np.mean(m))          # 3.5\nprint(np.min(m), np.max(m)) # 1 6",
  });
  outPanel(s, { x: 5.75, y: 4.25, w: 6.98, h: 0.9, fs: 17, text: "21 · [5 7 9] · [ 6 15] · 3.5 · 1 6" });
  table(s,
    ["Cách gọi", "Chiều bị gộp", "Kết quả"],
    [
      ["m.sum()", "toàn bộ", "21"],
      ["m.sum(axis=0)", "hàng (trục 0)", "[5 7 9] · (3,)"],
      ["m.sum(axis=1)", "cột (trục 1)", "[ 6 15] · (2,)"],
    ],
    { x: 0.6, y: 5.20, w: 7.20, colW: [1.85, 1.85, 3.50], rowH: [0.38, 0.40, 0.42, 0.42], fs: 15, monoFirst: true }
  );
  tx(s, "axis là chiều bị gộp: axis=0 gộp hàng, axis=1 gộp cột.", {
    x: 8.05, y: 5.30, w: 4.65, h: 1.05, fontSize: TYPE.body, italic: true, color: C.muted,
  });
  footer(s, 19);
  s.addNotes("axis là chiều bị gộp, không phải chiều giữ lại. Với mảng 2×3, axis=0 gộp các hàng nên kết quả theo cột; axis=1 gộp các cột nên kết quả theo hàng. Không truyền axis thì gộp toàn mảng.");
}

/* ---------------------------------------------------------------- 20 broadcasting rules */
{
  const s = p.addSlide(); bg(s);
  header(s, "05 · Tính toán", "Broadcasting: tính giữa các shape khác nhau");
  tx(s, "Broadcasting cho phép mảng nhỏ được “trải” lên mảng lớn. Vòng lặp chạy trong C, không sao chép dữ liệu.", {
    x: 0.6, y: 1.6, w: 5.75, h: 1.3, fontSize: TYPE.body, color: C.ink, lineSpacingMultiple: 1.1,
  });
  const rules = [
    ["1", "So sánh shape từ phải sang trái."],
    ["2", "Mỗi cặp chiều bằng nhau, hoặc một bên bằng 1."],
    ["3", "Mảng ít chiều hơn được thêm chiều 1 ở bên trái."],
  ];
  rules.forEach((r, i) => {
    const y = 3.05 + i * 1.0;
    s.addShape(p.ShapeType.roundRect, { x: 0.6, y, w: 0.52, h: 0.52, fill: { color: C.teal }, line: { color: C.white, width: 1 }, rectRadius: 0.15 });
    tx(s, r[0], { x: 0.6, y, w: 0.52, h: 0.52, fontSize: TYPE.body, bold: true, color: C.white, align: "center", valign: "mid" });
    tx(s, r[1], { x: 1.28, y: y - 0.03, w: 4.9, h: 0.85, fontSize: TYPE.body, color: C.slate, lineSpacingMultiple: 1.05 });
  });
  tx(s, "Scalar trải nhưng không sao chép thật.", { x: 0.6, y: 6.05, w: 5.75, h: 0.35, fontSize: 18, italic: true, color: C.muted });
  card(s, { x: 6.55, y: 1.6, w: 6.18, h: 3.7, fill: C.ink, line: C.ink });
  tx(s, "SO SÁNH TỪ PHẢI SANG TRÁI", { x: 6.82, y: 1.78, w: 5.6, h: 0.25, fontSize: 12, bold: true, color: C.cyan, charSpacing: 1.3 });
  tx(s, "(2, 3)", { x: 6.82, y: 2.12, w: 2.7, h: 0.5, fontSize: 28, bold: true, color: C.white, fontFace: F.code, align: "right" });
  tx(s, "(   3,)", { x: 6.82, y: 2.72, w: 2.7, h: 0.5, fontSize: 28, bold: true, color: C.cyan, fontFace: F.code, align: "right" });
  s.addShape(p.ShapeType.rect, { x: 6.82, y: 3.33, w: 2.7, h: 0.01, fill: { color: "2A5668" }, line: { color: "2A5668", width: 0 } });
  tx(s, "(2, 3)", { x: 6.82, y: 3.45, w: 2.7, h: 0.5, fontSize: 28, bold: true, color: C.amber, fontFace: F.code, align: "right" });
  tx(s, "3 = 3", { x: 9.7, y: 2.18, w: 1.5, h: 0.32, fontSize: 18, color: "8AD9C0", fontFace: F.code });
  tx(s, "2 vs 1 → 2", { x: 9.7, y: 3.05, w: 2.5, h: 0.32, fontSize: 18, color: "8AD9C0", fontFace: F.code });
  arrow(s, 9.55, 2.38, 9.55, 3.5, { color: C.cyan, w: 1, end: false, dash: "dash" });
  tx(s, "KẾT QUẢ", { x: 6.82, y: 3.98, w: 2.7, h: 0.24, fontSize: 12, bold: true, color: C.cyan, charSpacing: 1.2, align: "right" });
  tx(s, "(2, 3)", { x: 6.82, y: 4.24, w: 2.7, h: 0.5, fontSize: 28, bold: true, color: C.amber, fontFace: F.code, align: "right" });
  tx(s, "shape của mảng lớn được giữ nguyên", { x: 6.82, y: 4.78, w: 5.55, h: 0.40, fontSize: TYPE.body, color: "B8D2DD" });
  card(s, { x: 6.55, y: 5.5, w: 6.18, h: 1.0, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "a * 2.0  →  [2. 4. 6.]", { x: 6.78, y: 5.5, w: 3.35, h: 1.0, fontSize: 18, bold: true, color: C.ink, fontFace: F.code, valign: "mid" });
  tx(s, "scalar trải như (3,)", { x: 10.20, y: 5.58, w: 2.30, h: 0.75, fontSize: 15.5, color: C.muted });
  tx(s, "Nguồn: NumPy Documentation — Broadcasting [3]", { x: 0.6, y: 6.65, w: 5.7, h: 0.24, fontSize: TYPE.source, color: C.muted });
  footer(s, 20);
  s.addNotes("Quy tắc cốt lõi: so sánh shape từ phải sang trái; mỗi cặp chiều bằng nhau hoặc một bên bằng 1 thì tương thích; mảng ít chiều hơn được coi là có chiều thiếu bằng 1 ở bên trái. Scalar được trải nhưng không thực sự sao chép.");
}

/* ---------------------------------------------------------------- 21 broadcasting examples */
{
  const s = p.addSlide(); bg(s);
  header(s, "05 · Tính toán", "Broadcasting: thành công và thất bại");
  const okCard = (x, title, sub, result) => {
    card(s, { x, y: 1.6, w: 3.88, h: 2.85 });
    tx(s, title, { x: x + 0.24, y: 1.76, w: 3.42, h: 0.4, fontSize: 21, bold: true, color: C.ink, fontFace: F.code });
    tx(s, sub, { x: x + 0.24, y: 2.22, w: 3.42, h: 0.55, fontSize: 18, color: C.muted, lineSpacingMultiple: 1.02 });
    tx(s, result, { x: x + 0.24, y: 2.9, w: 3.42, h: 0.75, fontSize: TYPE.body, color: C.green, fontFace: F.code, lineSpacingMultiple: 1.0 });
    tx(s, "✓ hợp lệ", { x: x + 0.24, y: 3.8, w: 1.6, h: 0.28, fontSize: 17, bold: true, color: C.green });
  };
  okCard(0.6, "(2, 3) + (3,)", "(3,) coi là (1, 3), trải xuống 2 hàng", "[[11 22 33]\n [14 25 36]]");
  okCard(4.72, "(2, 3) + (2, 1)", "(2, 1) trải sang 3 cột, mỗi hàng cộng một số", "[[11 12 13]\n [24 25 26]]");
  card(s, { x: 8.84, y: 1.6, w: 3.89, h: 2.85, fill: "FBEDEA", line: "EBC3BB" });
  tx(s, "(2, 3) + (2,)", { x: 9.08, y: 1.76, w: 3.42, h: 0.4, fontSize: 21, bold: true, color: C.ink, fontFace: F.code });
  tx(s, "Chiều cuối 3 ≠ 2, không bên nào bằng 1.", { x: 9.08, y: 2.22, w: 3.42, h: 0.55, fontSize: 18, color: C.muted, lineSpacingMultiple: 1.02 });
  tx(s, "ValueError", { x: 9.08, y: 2.9, w: 3.42, h: 0.35, fontSize: TYPE.body, bold: true, color: C.coral, fontFace: F.code });
  tx(s, "shapes (2,3) (2,)\nkhông broadcast được", { x: 9.08, y: 3.28, w: 3.42, h: 0.5, fontSize: 14, color: C.coral, fontFace: F.code, lineSpacingMultiple: 1.0 });
  tx(s, "✕ thất bại", { x: 9.08, y: 3.8, w: 1.6, h: 0.28, fontSize: 17, bold: true, color: C.coral });
  codePanel(s, {
    x: 0.6, y: 4.7, w: 7.6, h: 1.7, fs: 15.5,
    code: "p = np.array([[1, 2, 3], [4, 5, 6]])\nprint(p + np.array([10, 20, 30]))\nprint(p + np.array([[10], [20]]))\nprint(p + np.array([10, 20]))   # ValueError",
  });
  outPanel(s, {
    x: 8.4, y: 4.7, w: 4.33, h: 1.7, fs: 13,
    text: "[[11 22 33]\n [14 25 36]]\n[[11 12 13]\n [24 25 26]]\nValueError: (2,3) vs (2,)",
  });
  tx(s, "Chiều cuối không khớp và không bên nào bằng 1 → ValueError.", {
    x: 0.6, y: 6.55, w: 12.1, h: 0.35, fontSize: TYPE.body, italic: true, color: C.muted,
  });
  footer(s, 21);
  s.addNotes("Hai trường hợp thành công: (2,3)+(3,) và (2,3)+(2,1). Trường hợp thất bại: (2,3)+(2,) vì chiều cuối 3 khác 2 và không bên nào bằng 1. NumPy báo ValueError thay vì tự suy diễn.");
}

/* ---------------------------------------------------------------- 22 example stats */
{
  const s = p.addSlide(); bg(s);
  header(s, "06 · Thực hành", "Ví dụ 1 — Thống kê điểm kiểm tra");
  tx(s, "5 bài: 8.0, 7.5, 9.0, 6.5, 8.5. Tính trung bình, min, max, độ lệch chuẩn, đếm điểm đạt và cộng thưởng.", {
    x: 0.6, y: 1.55, w: 12.1, h: 0.7, fontSize: TYPE.body, color: C.slate, lineSpacingMultiple: 1.04,
  });
  codePanel(s, {
    x: 0.6, y: 2.32, w: 6.1, h: 2.55, fs: 15,
    code: 'd = np.array([8.0, 7.5, 9.0, 6.5, 8.5])\nprint("TB:", np.mean(d))\nprint("Max:", np.max(d))\nprint("Min:", np.min(d))\nprint("Std:", np.std(d))\nprint(">=8:", np.sum(d >= 8), "/", d.size)',
  });
  outPanel(s, {
    x: 0.6, y: 5.02, w: 6.1, h: 1.4, fs: 13.5,
    text: "TB: 7.9   Max: 9.0\nMin: 6.5   Std: 0.8602\n>=8: 3 / 5\nSau thưởng: [8.5 8. 9.5 7. 9.]",
  });
  const stats = [["7.9", "Trung bình"], ["9.0", "Cao nhất"], ["6.5", "Thấp nhất"], ["0.860", "Độ lệch chuẩn"]];
  stats.forEach((st, i) => {
    const x = 6.95 + (i % 2) * 2.92;
    const y = 2.32 + Math.floor(i / 2) * 1.18;
    card(s, { x, y, w: 2.82, h: 1.05 });
    tx(s, st[0], { x: x + 0.16, y: y + 0.08, w: 1.45, h: 0.55, fontSize: 28, bold: true, color: C.teal, fontFace: F.code });
    tx(s, st[1], { x: x + 1.5, y: y + 0.18, w: 1.2, h: 0.7, fontSize: 14.5, color: C.muted, lineSpacingMultiple: 1.0 });
  });
  tx(s, "3/5 bài đạt ≥ 8.0 · TB 7.9", { x: 6.95, y: 4.82, w: 5.7, h: 0.3, fontSize: 16, bold: true, color: C.slate });
  const bx = 7.1, by = 5.25, bw = 5.5, bh = 1.3, maxV = 10;
  const scores = [8.0, 7.5, 9.0, 6.5, 8.5];
  scores.forEach((v, i) => {
    const h = (v / maxV) * bh;
    const x = bx + i * 1.02;
    s.addShape(p.ShapeType.rect, { x, y: by + bh - h, w: 0.58, h, fill: { color: i === 1 ? C.cyan : C.teal }, line: { color: C.white, width: 0.5 } });
    tx(s, v.toFixed(1), { x: x - 0.08, y: by + bh - h - 0.25, w: 0.74, h: 0.22, fontSize: 12.5, color: C.ink, align: "center", fontFace: F.code });
  });
  const meanY = by + bh - (7.9 / maxV) * bh;
  s.addShape(p.ShapeType.line, {
    x: bx - 0.05, y: meanY, w: 5.2, h: 0,
    line: { color: C.amber, width: 1.25, dashType: "dash" },
  });
  tx(s, "TB 7.9", { x: bx + 4.55, y: meanY - 0.25, w: 0.8, h: 0.22, fontSize: 12.5, bold: true, color: "B7771B", fontFace: F.code });
  footer(s, 22);
  s.addNotes("Ví dụ thống kê: mean 7.9, max 9.0, min 6.5, std khoảng 0.860. d >= 8.0 tạo mảng boolean, np.sum cộng các True để đếm 3/5. d + 0.5 cộng điểm thưởng nhờ broadcasting.");
}

/* ---------------------------------------------------------------- 23 example zscore */
{
  const s = p.addSlide(); bg(s);
  header(s, "06 · Thực hành", "Ví dụ 2 — Chuẩn hóa và thay vòng lặp");
  const col = (x, title, code, out, take) => {
    card(s, { x, y: 1.6, w: 5.95, h: 4.55 });
    tx(s, title, { x: x + 0.26, y: 1.76, w: 5.4, h: 0.4, fontSize: TYPE.subhead, bold: true, color: C.ink });
    codePanel(s, { x: x + 0.22, y: 2.25, w: 5.5, h: 1.62, fs: 15.5, code });
    outPanel(s, { x: x + 0.22, y: 4.02, w: 5.5, h: 1.1, fs: 13.5, text: out });
    tx(s, take, { x: x + 0.26, y: 5.3, w: 5.4, h: 0.75, fontSize: TYPE.body, italic: true, color: C.muted, lineSpacingMultiple: 1.05 });
  };
  col(0.6, "Chuẩn hóa z-score",
    "x = np.array([2.0, 4.0, 6.0, 8.0])\nz = (x - np.mean(x)) / np.std(x)\nprint(z)\nprint(np.mean(z), np.std(z))",
    "[-1.3416 -0.4472 0.4472 1.3416]\nmean: 0.0  std: 1.0",
    "Broadcasting với scalar: trừ 5.0, chia 2.236. Kết quả mean 0, std 1.");
  col(6.78, "Vector hóa và lọc dữ liệu",
    "prices = np.array([100, 250, 80, 320])\nnew = prices * 1.1\nprint(new)\nprint(prices[prices > 200])",
    "[110. 275.  88. 352.]\n[False  True False  True]\n[250 320]",
    "Một biểu thức thay vòng lặp: nhân, tạo mặt nạ, lọc.");
  card(s, { x: 0.6, y: 6.3, w: 12.13, h: 0.55, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "Biểu thức mảng thay vòng lặp — ngắn hơn, ít lỗi chỉ số.", {
    x: 0.85, y: 6.3, w: 11.6, h: 0.55, fontSize: TYPE.body, bold: true, color: C.teal, valign: "mid",
  });
  footer(s, 23);
  s.addNotes("Hai ví dụ cho thấy sức mạnh biểu diễn: chuẩn hóa z-score bằng một biểu thức, và thay vòng lặp bằng phép nhân mảng kết hợp mặt nạ boolean. Kết quả z có mean 0 và std 1.");
}

/* ---------------------------------------------------------------- 24 conclusion */
{
  const s = p.addSlide(); bg(s, C.ink);
  header(s, "Kết luận", "Ba điều cần nhớ về NumPy", { dark: true });
  const items = [
    ["01", "Shape quyết định mọi thứ", "Đọc shape trước khi viết phép toán."],
    ["02", "* khác @", "* nhân từng phần tử; @ nhân ma trận hàng × cột."],
    ["03", "Broadcasting so sánh từ phải sang trái", "Bằng nhau hoặc một bên bằng 1; chiều thiếu là 1."],
  ];
  items.forEach((it, i) => {
    const y = 1.7 + i * 1.32;
    tx(s, it[0], { x: 0.62, y: y + 0.02, w: 0.8, h: 0.5, fontSize: 26, bold: true, color: C.amber, fontFace: F.code });
    tx(s, it[1], { x: 1.45, y, w: 10.9, h: 0.42, fontSize: TYPE.subhead, bold: true, color: C.white });
    tx(s, it[2], { x: 1.45, y: y + 0.45, w: 10.9, h: 0.4, fontSize: TYPE.body, color: "A9C6D3", lineSpacingMultiple: 1.02 });
  });
  card(s, { x: 0.6, y: 6.05, w: 12.13, h: 0.62, fill: "0F3A4C", line: "1D566B", shadow: false });
  tx(s, "Ngoài NumPy: pandas cho bảng nhiều kiểu; PyTorch cho GPU/autograd.", {
    x: 0.85, y: 6.05, w: 11.6, h: 0.62, fontSize: 18, bold: true, color: C.cyan, valign: "mid",
  });
  footer(s, 24, true);
  s.addNotes("Ba điều cần nhớ: shape quyết định mọi thứ, * khác @, và broadcasting so sánh từ phải sang trái. Kết thúc bằng ranh giới công cụ: pandas cho bảng nhiều kiểu, PyTorch cho GPU và autograd.");
}

/* ---------------------------------------------------------------- 25 references */
{
  const s = p.addSlide(); bg(s);
  header(s, "Tài liệu tham khảo", "Nguồn và hướng tìm hiểu tiếp");
  tx(s, "Hướng tìm hiểu tiếp", { x: 0.6, y: 1.55, w: 4.9, h: 0.4, fontSize: TYPE.subhead, bold: true, color: C.ink });
  const next = [
    ["Matplotlib", "Trực quan hóa mảng."],
    ["pandas", "Bảng dữ liệu có nhãn."],
    ["numpy.linalg", "Đại số tuyến tính."],
    ["Broadcasting", "np.newaxis, expand_dims."],
    ["Đọc / ghi", "loadtxt, savetxt, save, load."],
  ];
  next.forEach((n, i) => {
    const y = 2.08 + i * 0.8;
    card(s, { x: 0.6, y, w: 4.9, h: 0.68 });
    tx(s, n[0], { x: 0.8, y: y + 0.08, w: 1.8, h: 0.28, fontSize: 18, bold: true, color: C.teal, fontFace: F.code });
    tx(s, n[1], { x: 2.7, y: y + 0.08, w: 2.55, h: 0.52, fontSize: 16, color: C.slate, lineSpacingMultiple: 1.0 });
  });
  tx(s, "Tài liệu tham khảo", { x: 5.85, y: 1.55, w: 6.8, h: 0.4, fontSize: TYPE.subhead, bold: true, color: C.ink });
  tx(s, "Truy cập: 25/10/2026", { x: 5.85, y: 1.96, w: 3.2, h: 0.24, fontSize: 12.5, color: C.muted, italic: true });
  const refs = [
    "[1] NumPy Developers. What is NumPy? NumPy v2.5 Manual. https://numpy.org/doc/stable/user/whatisnumpy.html",
    "[2] NumPy Developers. NumPy: the absolute basics for beginners. https://numpy.org/doc/stable/user/absolute_beginners.html",
    "[3] NumPy Developers. Broadcasting. https://numpy.org/doc/stable/user/basics.broadcasting.html",
    "[4] NumPy Developers. NumPy quickstart. https://numpy.org/doc/stable/user/quickstart.html",
    "[5] NumPy Developers. Array creation routines. https://numpy.org/doc/stable/reference/routines.array-creation.html",
    "[6] NumPy Developers. Linear algebra (numpy.linalg). https://numpy.org/doc/stable/reference/routines.linalg.html",
    "[7] Python Software Foundation. Data Structures — Python Tutorial. https://docs.python.org/3/tutorial/datastructures.html",
  ];
  s.addText(refs.map((r) => ({ text: r, options: { breakLine: true } })), {
    x: 5.85, y: 2.32, w: 6.88, h: 3.95, fontFace: F.body, fontSize: 13.2, color: C.slate,
    margin: 0, valign: "top", lineSpacingMultiple: 1.04, paraSpaceAfter: 4,
  });
  tx(s, "Logo: NumPy Documentation (giấy phép BSD). Các sơ đồ khác được vẽ bằng hình khối PowerPoint. Code và output kiểm chứng trên Python 3.14 + NumPy 2.5.4.", {
    x: 0.6, y: 6.38, w: 12.1, h: 0.45, fontSize: 11.5, italic: true, color: C.muted,
  });
  footer(s, 25);
  s.addNotes("Bảy nguồn chính thức: What is NumPy, absolute beginners, broadcasting, quickstart, array creation, numpy.linalg và Python datastructures. Hướng tiếp: Matplotlib, pandas, numpy.linalg, broadcasting nâng cao và đọc ghi dữ liệu.");
}

p.writeFile({ fileName: "presentation.pptx" }).then(() => console.log("saved presentation.pptx"));
