const T = require("./theme");
const { C, F, deck, tx, bg, header, footer, card, chip, codePanel, outPanel, grid, label, arrow } = T;

const p = deck();

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
    x: 0.75, y: 0.95, w: 7.6, h: 0.25, fontSize: 10.5, bold: true,
    color: C.cyan, charSpacing: 2.4,
  });
  tx(s, "Tìm hiểu thư viện\nNumPy trong Python", {
    x: 0.72, y: 1.45, w: 7.7, h: 2.35, fontSize: 44, bold: true,
    color: C.white, lineSpacingMultiple: 0.95, valign: "top",
  });
  s.addShape(p.ShapeType.rect, {
    x: 0.75, y: 3.95, w: 1.15, h: 0.05,
    fill: { color: C.amber }, line: { color: C.amber, width: 0 },
  });
  tx(s, "Từ ndarray đến broadcasting", {
    x: 0.75, y: 4.25, w: 7.0, h: 0.5, fontSize: 21, color: C.cyan,
  });
  tx(s, "Người trình bày: 26120072     ·     Tháng 10 / 2026", {
    x: 0.75, y: 6.35, w: 7.2, h: 0.3, fontSize: 12, color: "9FC0CF",
  });
  card(s, { x: 8.75, y: 1.55, w: 3.95, h: 3.35, fill: C.white, line: "D7E5EC" });
  s.addImage({ path: "assets/numpylogo.png", x: 9.12, y: 2.55, w: 3.2, h: 1.54 });
  tx(s, "Numerical Python  ·  BSD", {
    x: 8.75, y: 4.35, w: 3.95, h: 0.25, fontSize: 9.5, color: C.muted, align: "center",
  });
  s.addNotes("Giới thiệu chủ đề: NumPy là thư viện nền tảng cho tính toán số trong Python. Bài đi từ đối tượng ndarray, cách tạo và truy cập dữ liệu, đến phép toán, broadcasting và bốn ví dụ thực hành.");
}

/* ---------------------------------------------------------------- 02 agenda */
{
  const s = p.addSlide(); bg(s);
  header(s, "Nội dung", "Sáu chặng của bài thuyết trình");
  const items = [
    ["01", "Giới thiệu", "NumPy là gì, vì sao nên dùng và dùng ở đâu."],
    ["02", "Cấu trúc mảng", "ndarray, số chiều, shape, size và dtype."],
    ["03", "Tạo mảng", "array, zeros, ones, arange, linspace, eye."],
    ["04", "Truy cập dữ liệu", "Indexing, slicing, boolean, reshape, .T."],
    ["05", "Tính toán", "Phép toán từng phần tử, axis và broadcasting."],
    ["06", "Thực hành", "Bốn ví dụ, kết luận và hướng tìm hiểu tiếp."],
  ];
  const xs = [0.6, 4.72, 8.84];
  items.forEach((it, i) => {
    const x = xs[i % 3];
    const y = i < 3 ? 1.62 : 3.92;
    card(s, { x, y, w: 3.88, h: 2.02 });
    s.addShape(p.ShapeType.roundRect, {
      x: x + 0.24, y: y + 0.24, w: 0.52, h: 0.52,
      fill: { color: i % 2 ? C.cyan : C.teal }, line: { color: "FFFFFF", width: 1.5 }, rectRadius: 0.2,
    });
    tx(s, it[0], {
      x: x + 0.24, y: y + 0.24, w: 0.52, h: 0.52, fontSize: 14, bold: true,
      color: C.white, align: "center", valign: "mid", fontFace: F.code,
    });
    tx(s, it[1], { x: x + 0.9, y: y + 0.3, w: 2.7, h: 0.42, fontSize: 16, bold: true, color: C.ink });
    tx(s, it[2], { x: x + 0.24, y: y + 1.0, w: 3.4, h: 0.8, fontSize: 11.5, color: C.slate, lineSpacingMultiple: 1.15 });
  });
  tx(s, "Mạch kiến thức: vấn đề → đối tượng → tạo → truy cập → tính toán → mở rộng → ứng dụng.", {
    x: 0.6, y: 6.18, w: 12.1, h: 0.35, fontSize: 12, italic: true, color: C.teal,
  });
  footer(s, 2);
  s.addNotes("Sáu chặng tương ứng với sáu phần nội dung. Mạch đi từ động cơ sử dụng, mô hình dữ liệu, thao tác cơ bản, đến tính toán và ví dụ.");
}

/* ---------------------------------------------------------------- 03 what is numpy */
{
  const s = p.addSlide(); bg(s);
  header(s, "01 · Giới thiệu", "NumPy là gì?");
  tx(s, "NumPy (Numerical Python) là thư viện mã nguồn mở cho tính toán khoa học trong Python.", {
    x: 0.6, y: 1.55, w: 6.1, h: 0.95, fontSize: 17, color: C.ink, lineSpacingMultiple: 1.2,
  });
  const rows = [
    ["ndarray", "Mảng N chiều, đồng nhất kiểu, kích thước cố định"],
    ["Hàm toán học", "Đại số tuyến tính, thống kê, sắp xếp, tìm kiếm"],
    ["Nền tảng", "Nhiều thư viện khoa học nhận và trả về mảng NumPy"],
  ];
  rows.forEach((r, i) => {
    const y = 2.72 + i * 1.05;
    card(s, { x: 0.6, y, w: 6.05, h: 0.9 });
    s.addShape(p.ShapeType.rect, {
      x: 0.6, y: y + 0.12, w: 0.06, h: 0.66,
      fill: { color: i === 0 ? C.teal : i === 1 ? C.cyan : C.amber },
      line: { color: C.white, width: 0 },
    });
    tx(s, r[0], { x: 0.85, y: y + 0.13, w: 1.75, h: 0.28, fontSize: 12, bold: true, color: C.ink, fontFace: F.code });
    tx(s, r[1], { x: 2.55, y: y + 0.12, w: 3.95, h: 0.62, fontSize: 10.5, color: C.slate, lineSpacingMultiple: 1.08 });
  });
  codePanel(s, {
    x: 7.0, y: 1.6, w: 5.7, h: 1.45, fs: 12,
    code: "import numpy as np\n\nprint(np.__version__)",
  });
  outPanel(s, { x: 7.0, y: 3.2, w: 5.7, h: 0.85, text: "2.5.4", fs: 13 });
  tx(s, "Quy ước: import numpy as np", {
    x: 7.0, y: 4.25, w: 5.7, h: 0.3, fontSize: 11.5, color: C.muted, italic: true,
  });
  tx(s, "Nguồn: NumPy Documentation [1], [2]", {
    x: 7.0, y: 4.6, w: 5.7, h: 0.25, fontSize: 8.5, color: C.muted,
  });
  footer(s, 3);
  s.addNotes("Định nghĩa ngắn: NumPy là gói nền tảng cho tính toán khoa học, cung cấp ndarray cùng kho hàm toán học, logic, biến đổi hình dạng, sắp xếp, nhập xuất và đại số tuyến tính. Phiên bản dùng trong tài liệu là 2.5.4.");
}

/* ---------------------------------------------------------------- 04 problem */
{
  const s = p.addSlide(); bg(s);
  header(s, "01 · Giới thiệu", "NumPy giải quyết vấn đề gì?");
  const mk = (x, title, code, out, col, note) => {
    card(s, { x, y: 1.6, w: 5.95, h: 3.05 });
    s.addShape(p.ShapeType.roundRect, {
      x: x + 0.25, y: 1.85, w: 1.72, h: 0.36,
      fill: { color: col }, line: { color: col, width: 0 }, rectRadius: 0.4,
    });
    tx(s, title, { x: x + 0.25, y: 1.85, w: 1.72, h: 0.36, fontSize: 9.5, bold: true, color: C.white, align: "center", valign: "mid" });
    tx(s, code, { x: x + 0.25, y: 2.45, w: 5.45, h: 0.6, fontSize: 12, fontFace: F.code, color: C.ink });
    tx(s, "→", { x: x + 0.25, y: 3.15, w: 0.4, h: 0.3, fontSize: 13, color: C.muted });
    tx(s, out, { x: x + 0.75, y: 3.1, w: 4.9, h: 0.6, fontSize: 12, fontFace: F.code, color: col === C.teal ? C.teal : C.amber });
    tx(s, note, { x: x + 0.25, y: 3.95, w: 5.45, h: 0.45, fontSize: 11, color: C.slate, italic: true });
  };
  mk(0.6, "PYTHON LIST", "[1, 2, 3, 4] * 2", "[1, 2, 3, 4, 1, 2, 3, 4]", C.amber, "Lặp danh sách — không phải phép nhân.");
  mk(6.78, "NUMPY ARRAY", "np.array([1, 2, 3, 4]) * 2", "[2 4 6 8]", C.teal, "Nhân từng phần tử — đúng kỳ vọng toán học.");
  ["Dữ liệu số nhiều chiều", "Code ngắn, gần ký hiệu toán", "Tính toán trên toàn mảng"].forEach((t, i) => {
    const x = 0.6 + i * 4.09;
    card(s, { x, y: 5.0, w: 3.95, h: 0.85, fill: C.ice, line: "CFE5EE", shadow: false });
    tx(s, String(i + 1), {
      x: x + 0.2, y: 5.0, w: 0.4, h: 0.85, fontSize: 18, bold: true, color: C.teal, valign: "mid",
    });
    tx(s, t, { x: x + 0.65, y: 5.0, w: 3.1, h: 0.85, fontSize: 11.5, color: C.ink, valign: "mid" });
  });
  footer(s, 4);
  s.addNotes("Ba động cơ: biểu diễn dữ liệu số nhiều chiều, viết ngắn hơn nhờ biểu thức mảng, và có sẵn hàm thống kê trên toàn mảng. Ví dụ then chốt: cùng dấu * nhưng list lặp còn ndarray nhân từng phần tử.");
}

/* ---------------------------------------------------------------- 05 ndarray */
{
  const s = p.addSlide(); bg(s);
  header(s, "02 · Cấu trúc mảng", "ndarray — đối tượng trung tâm");
  const items = [
    "Mảng N chiều: 0-D, 1-D, 2-D hoặc nhiều hơn.",
    "Các phần tử cùng một kiểu dữ liệu (dtype).",
    "Kích thước cố định sau khi khởi tạo.",
    "Lưới chữ nhật — mọi hàng cùng số cột, không “răng cưa”.",
    "Mọi hàm NumPy đều nhận hoặc trả về ndarray.",
  ];
  items.forEach((t, i) => {
    const y = 1.65 + i * 0.86;
    s.addShape(p.ShapeType.ellipse, {
      x: 0.62, y: y + 0.12, w: 0.14, h: 0.14,
      fill: { color: i === 4 ? C.amber : C.teal }, line: { color: C.white, width: 0 },
    });
    tx(s, t, { x: 0.95, y, w: 5.35, h: 0.62, fontSize: 13.5, color: C.ink, lineSpacingMultiple: 1.12 });
  });
  tx(s, "Một mảng 3 × 4", { x: 7.05, y: 1.55, w: 4.8, h: 0.3, fontSize: 12, bold: true, color: C.ink });
  grid(s, {
    x: 7.35, y: 2.1, cw: 0.95, ch: 0.62, rows: 3, cols: 4,
    vals: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], fs: 13,
  });
  tx(s, "trục 1  →", { x: 7.35, y: 1.83, w: 3.8, h: 0.22, fontSize: 9.5, color: C.muted, align: "right" });
  tx(s, "trục 0", { x: 6.52, y: 2.1, w: 0.7, h: 1.86, fontSize: 8.5, color: C.muted, align: "center", valign: "mid" });
  chip(s, "shape (3, 4)   ·   dtype int64", { x: 7.35, y: 4.25, w: 3.8, h: 0.42, fs: 11 });
  tx(s, "Cùng một dtype cho mọi ô — đây là điều kiện để vector hóa.", {
    x: 7.05, y: 4.95, w: 5.5, h: 0.5, fontSize: 11.5, italic: true, color: C.slate,
  });
  tx(s, "Nguồn: NumPy Documentation [1], [2]", { x: 7.05, y: 5.55, w: 5.4, h: 0.25, fontSize: 8.5, color: C.muted });
  footer(s, 5);
  s.addNotes("ndarray là kiểu trung tâm: mảng N chiều, đồng nhất kiểu, kích thước cố định, dạng lưới chữ nhật. Hiểu ndarray là hiểu cách NumPy nghĩ: dữ liệu là lưới nhiều chiều và phép toán áp lên lưới đó.");
}

/* ---------------------------------------------------------------- 06 pros cons */
{
  const s = p.addSlide(); bg(s);
  header(s, "01 · Giới thiệu", "Ưu điểm và giới hạn");
  const colCard = (x, title, items, col, symbol) => {
    card(s, { x, y: 1.6, w: 5.95, h: 4.25 });
    s.addShape(p.ShapeType.rect, {
      x, y: 1.6, w: 5.95, h: 0.08,
      fill: { color: col }, line: { color: col, width: 0 },
    });
    tx(s, title, { x: x + 0.3, y: 1.85, w: 4.5, h: 0.4, fontSize: 17, bold: true, color: C.ink });
    items.forEach((t, i) => {
      const yy = 2.42 + i * 0.66;
      tx(s, symbol, { x: x + 0.32, y: yy, w: 0.3, h: 0.3, fontSize: 13, bold: true, color: col });
      tx(s, t, { x: x + 0.68, y: yy - 0.02, w: 4.95, h: 0.52, fontSize: 11.5, color: C.slate, lineSpacingMultiple: 1.05 });
    });
  };
  colCard(0.6, "Ưu điểm", [
    "Vector hóa — viết phép toán trên cả mảng, không cần vòng lặp hiển ngôn.",
    "Broadcasting — tính giữa các shape khác nhau mà không sao chép thủ công.",
    "Kho hàm phong phú: toán học, thống kê, đại số tuyến tính, sắp xếp.",
    "Nền tảng hệ sinh thái khoa học; cú pháp gần với công thức toán.",
  ], C.teal, "✓");
  colCard(6.78, "Giới hạn", [
    "Dữ liệu phải đồng nhất kiểu — bảng có cột chữ, số, ngày không phù hợp trực tiếp.",
    "Kích thước cố định — thêm hoặc bớt phần tử phải tạo mảng mới.",
    "Không có nhãn cột, nhãn hàng như DataFrame.",
    "Với mảng rất nhỏ, chi phí gọi hàm có thể lớn hơn lợi ích.",
  ], C.coral, "!");
  tx(s, "Đây là nhận định tổng quát dựa trên đặc điểm thư viện, không phải kết quả đo hiệu năng.", {
    x: 0.6, y: 6.05, w: 12.1, h: 0.3, fontSize: 10, italic: true, color: C.muted,
  });
  footer(s, 6);
  s.addNotes("Cân bằng hai mặt: mạnh ở vector hóa, broadcasting và hệ sinh thái; yếu khi dữ liệu không đồng nhất, cần thêm bớt phần tử, hoặc cần nhãn. Với bảng nhiều kiểu, pandas là lựa chọn phù hợp hơn.");
}

/* ---------------------------------------------------------------- 07 applications */
{
  const s = p.addSlide(); bg(s);
  header(s, "01 · Giới thiệu", "Ứng dụng thực tế");
  const items = [
    ["Khoa học & kỹ thuật", "Tính toán số, mô phỏng, xử lý tín hiệu."],
    ["Xử lý ảnh", "Ảnh là ma trận điểm ảnh; phép toán áp lên toàn ảnh."],
    ["Thống kê & dữ liệu", "Trung bình, độ lệch chuẩn, tương quan trên mảng lớn."],
    ["Học máy", "Đặc trưng, trọng số và gradient là các mảng số."],
    ["Mô phỏng số", "Tính trên lưới không gian, thời gian rời rạc."],
  ];
  const xs = [0.6, 4.72, 8.84, 2.66, 6.78];
  const ys = [1.7, 1.7, 1.7, 3.95, 3.95];
  items.forEach((it, i) => {
    card(s, { x: xs[i], y: ys[i], w: 3.88, h: 1.95 });
    s.addShape(p.ShapeType.roundRect, {
      x: xs[i] + 0.26, y: ys[i] + 0.25, w: 0.46, h: 0.46,
      fill: { color: i % 2 ? C.ice : "D6EEF5" }, line: { color: "BFDFE9", width: 0.75 }, rectRadius: 0.12,
    });
    tx(s, String(i + 1), {
      x: xs[i] + 0.26, y: ys[i] + 0.25, w: 0.46, h: 0.46, fontSize: 13,
      bold: true, color: C.teal, align: "center", valign: "mid", fontFace: F.code,
    });
    tx(s, it[0], { x: xs[i] + 0.86, y: ys[i] + 0.28, w: 2.8, h: 0.42, fontSize: 14, bold: true, color: C.ink });
    tx(s, it[1], { x: xs[i] + 0.26, y: ys[i] + 0.92, w: 3.4, h: 0.8, fontSize: 11, color: C.slate, lineSpacingMultiple: 1.12 });
  });
  card(s, { x: 0.6, y: 5.98, w: 12.13, h: 0.48, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "Điểm chung: dữ liệu số, đồng nhất kiểu, kích thước lớn — nơi NumPy phát huy lợi thế.", {
    x: 0.85, y: 5.98, w: 11.6, h: 0.48, fontSize: 10.5, bold: true, color: C.teal, valign: "mid",
  });
  tx(s, "Nguồn: NumPy Documentation [1]", { x: 0.6, y: 6.55, w: 5, h: 0.25, fontSize: 8.5, color: C.muted });
  footer(s, 7);
  s.addNotes("Năm nhóm ứng dụng tiêu biểu. Điểm chung: dữ liệu là số, đồng nhất kiểu, kích thước lớn và cần tính hàng loạt.");
}

/* ---------------------------------------------------------------- 08 list vs array */
{
  const s = p.addSlide(); bg(s);
  header(s, "01 · Giới thiệu", "Python list và NumPy array");
  const head = ["Tiêu chí", "Python list", "NumPy array"];
  const rows = [
    ["Kiểu dữ liệu", "Hỗn hợp", "Đồng nhất, một dtype"],
    ["Phép * 2", "Lặp danh sách", "Nhân từng phần tử"],
    ["Nhiều chiều", "List lồng nhau, có thể “răng cưa”", "Mảng N chiều xác định"],
    ["Bộ nhớ", "Các object Python rời rạc", "Khối dữ liệu đồng nhất"],
    ["Hiệu năng", "Vòng lặp Python", "Vector hóa trong code C"],
    ["Kích thước", "Linh hoạt", "Cố định sau khi tạo"],
  ];
  const tRows = [head.map((h) => ({
    text: h, options: { bold: true, color: C.white, fill: { color: C.ink }, fontSize: 10.5 },
  }))];
  rows.forEach((r, i) => {
    tRows.push(r.map((v, j) => ({
      text: v,
      options: {
        color: j === 2 ? C.ink : C.slate,
        bold: j === 0 || (j === 2 && i === 1),
        fill: { color: i % 2 ? C.ice : C.white },
        fontSize: 10,
      },
    })));
  });
  s.addTable(tRows, {
    x: 0.6, y: 1.6, w: 6.3, colW: [1.35, 2.35, 2.6],
    rowH: [0.4, 0.5, 0.5, 0.62, 0.5, 0.5, 0.5],
    border: { type: "solid", pt: 0.5, color: "DCE8EE" },
    fontFace: F.body, margin: 5, valign: "middle", autoPage: false,
  });
  codePanel(s, {
    x: 7.15, y: 1.6, w: 5.55, h: 1.65, fs: 11,
    code: "print([1, 2, 3, 4] * 2)\nprint(np.array([1, 2, 3, 4]) * 2)",
  });
  outPanel(s, {
    x: 7.15, y: 3.4, w: 5.55, h: 1.35, fs: 10.5,
    text: "[1, 2, 3, 4, 1, 2, 3, 4]\n[2 4 6 8]",
  });
  card(s, { x: 7.15, y: 4.95, w: 5.55, h: 0.9, fill: "FFF6E7", line: "F0D8B4", shadow: false });
  tx(s, "Cùng một toán tử * — hai ngữ nghĩa hoàn toàn khác.", {
    x: 7.33, y: 4.95, w: 5.2, h: 0.9, fontSize: 11.5, bold: true, color: "9A6412", valign: "mid",
  });
  card(s, { x: 0.6, y: 5.5, w: 6.3, h: 1.0, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "Chọn cấu trúc dữ liệu theo phép toán cần làm, không chỉ theo cách lưu: list linh hoạt, ndarray tối ưu cho tính toán số.", {
    x: 0.82, y: 5.5, w: 5.9, h: 1.0, fontSize: 9.8, color: C.slate, valign: "mid", lineSpacingMultiple: 1.12,
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
    card(s, { x, y: 1.6, w: 2.92, h: 2.65 });
    tx(s, c[0], { x: x + 0.22, y: 1.75, w: 1.0, h: 0.32, fontSize: 15, bold: true, color: C.teal, fontFace: F.code });
    tx(s, c[1], { x: x + 0.95, y: 1.78, w: 1.8, h: 0.28, fontSize: 10, color: C.muted });
    const gx = x + 0.35, gy = 2.35;
    if (i === 0) {
      s.addShape(p.ShapeType.rect, { x: gx + 0.75, y: gy + 0.25, w: 0.42, h: 0.42, fill: { color: C.cyan }, line: { color: C.white, width: 1 } });
      tx(s, "7", { x: gx + 0.75, y: gy + 0.25, w: 0.42, h: 0.42, fontSize: 12, bold: true, color: C.white, align: "center", valign: "mid", fontFace: F.code });
    } else if (i === 1) {
      for (let k = 0; k < 3; k++) {
        s.addShape(p.ShapeType.rect, { x: gx + 0.35 + k * 0.34, y: gy + 0.25, w: 0.34, h: 0.42, fill: { color: C.ice }, line: { color: "A9CDDB", width: 0.75 } });
        tx(s, String(k + 1), { x: gx + 0.35 + k * 0.34, y: gy + 0.25, w: 0.34, h: 0.42, fontSize: 10, color: C.ink, align: "center", valign: "mid", fontFace: F.code });
      }
    } else if (i === 2) {
      for (let r = 0; r < 2; r++) for (let cc = 0; cc < 3; cc++) {
        s.addShape(p.ShapeType.rect, { x: gx + 0.25 + cc * 0.36, y: gy + 0.12 + r * 0.38, w: 0.36, h: 0.38, fill: { color: C.ice }, line: { color: "A9CDDB", width: 0.75 } });
        tx(s, String(1 + r * 3 + cc), { x: gx + 0.25 + cc * 0.36, y: gy + 0.12 + r * 0.38, w: 0.36, h: 0.38, fontSize: 9, color: C.ink, align: "center", valign: "mid", fontFace: F.code });
      }
    } else {
      for (let d = 0; d < 2; d++) {
        s.addShape(p.ShapeType.rect, { x: gx + 0.55 - d * 0.12, y: gy + 0.05 + d * 0.1, w: 0.95, h: 0.55, fill: { color: d === 1 ? "BFE6F1" : C.ice }, line: { color: "A9CDDB", width: 0.75 } });
      }
      tx(s, "2 lớp · 3 × 4", { x: gx + 0.25, y: gy + 0.8, w: 1.5, h: 0.22, fontSize: 8.5, color: C.muted, align: "center" });
    }
    tx(s, c[2], { x: x + 0.22, y: 3.55, w: 2.5, h: 0.3, fontSize: 11, fontFace: F.code, color: C.ink, bold: true });
  });
  codePanel(s, {
    x: 0.6, y: 4.5, w: 7.55, h: 1.95, fs: 10.5,
    code: "print(np.array(7).shape)\nprint(np.array([1, 2, 3]).shape)\nprint(np.array([[1, 2, 3], [4, 5, 6]]).shape)\nprint(np.zeros((2, 3, 4)).shape)",
  });
  outPanel(s, {
    x: 8.35, y: 4.5, w: 4.35, h: 1.95, fs: 10.5,
    text: "()\n(3,)\n(2, 3)\n(2, 3, 4)",
  });
  tx(s, "Cú pháp (3,) cần dấu phẩy để Python hiểu là tuple một phần tử.", {
    x: 0.6, y: 6.55, w: 11.9, h: 0.25, fontSize: 9.5, italic: true, color: C.muted,
  });
  footer(s, 9);
  s.addNotes("Số chiều là số trục của lưới. 0-D là một giá trị, 1-D là dãy, 2-D là bảng hàng cột, 3-D là chồng các bảng. Cú pháp shape (3,) cần dấu phẩy vì Python coi (3) là số 3 chứ không phải tuple.");
}

/* ---------------------------------------------------------------- 10 properties */
{
  const s = p.addSlide(); bg(s);
  header(s, "02 · Cấu trúc mảng", "Bốn thuộc tính quan trọng");
  card(s, { x: 0.6, y: 1.6, w: 4.75, h: 3.45, fill: C.ink, line: C.ink });
  tx(s, "HỘ CHIẾU MẢNG", { x: 0.9, y: 1.8, w: 4.1, h: 0.25, fontSize: 9, bold: true, color: C.cyan, charSpacing: 1.8 });
  tx(s, "ndarray  ·  (2, 3)", { x: 0.9, y: 2.08, w: 4.2, h: 0.35, fontSize: 15, bold: true, color: C.white, fontFace: F.code });
  const props = [
    ["ndim", "2", "số chiều"],
    ["shape", "(2, 3)", "kích thước từng chiều"],
    ["size", "6", "tổng số phần tử"],
    ["dtype", "int64", "kiểu dữ liệu"],
  ];
  props.forEach((pr, i) => {
    const y = 2.6 + i * 0.57;
    s.addShape(p.ShapeType.rect, { x: 0.9, y: y + 0.48, w: 4.1, h: 0.01, fill: { color: "1D4657" }, line: { color: "1D4657", width: 0 } });
    tx(s, pr[0], { x: 0.9, y, w: 0.8, h: 0.3, fontSize: 11, color: C.cyan, fontFace: F.code });
    tx(s, pr[1], { x: 1.75, y: y - 0.02, w: 1.45, h: 0.32, fontSize: 13, bold: true, color: C.white, fontFace: F.code });
    tx(s, pr[2], { x: 3.2, y: y + 0.03, w: 1.8, h: 0.26, fontSize: 8.5, color: "8FB0BF", align: "right" });
  });
  codePanel(s, {
    x: 5.7, y: 1.6, w: 7.0, h: 1.85, fs: 11,
    code: "a = np.array([[1, 2, 3],\n              [4, 5, 6]])\nprint(a.ndim)\nprint(a.shape)\nprint(a.size)\nprint(a.dtype)",
  });
  outPanel(s, { x: 5.7, y: 3.6, w: 7.0, h: 1.45, text: "2\n(2, 3)\n6\nint64", fs: 11 });
  ["ndim = len(shape)", "size = tích(shape)"].forEach((t, i) => {
    card(s, { x: 0.6 + i * 6.13, y: 5.35, w: 6.0, h: 0.85, fill: C.ice, line: "CFE5EE", shadow: false });
    tx(s, t, { x: 0.85 + i * 6.13, y: 5.35, w: 5.5, h: 0.85, fontSize: 13, bold: true, color: C.teal, fontFace: F.code, valign: "mid" });
  });
  footer(s, 10);
  s.addNotes("Bốn thuộc tính mô tả đầy đủ hình dạng dữ liệu: ndim là số chiều, shape là tuple kích thước, size là tổng phần tử, dtype là kiểu. Quan hệ: ndim bằng độ dài shape, size bằng tích các chiều.");
}

/* ---------------------------------------------------------------- 11 create 1 */
{
  const s = p.addSlide(); bg(s);
  header(s, "03 · Tạo mảng", "Ba hàm cơ bản: array, zeros, ones");
  const blocks = [
    {
      title: "np.array()", sub: "Từ list hoặc tuple có sẵn",
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
    card(s, { x, y: 1.6, w: 3.95, h: 4.05 });
    tx(s, b.title, { x: x + 0.24, y: 1.78, w: 3.4, h: 0.32, fontSize: 14, bold: true, color: C.ink, fontFace: F.code });
    tx(s, b.sub, { x: x + 0.24, y: 2.1, w: 3.4, h: 0.25, fontSize: 9.5, color: C.muted });
    codePanel(s, { x: x + 0.2, y: 2.45, w: 3.55, h: 1.55, fs: 9.5, code: b.code, title: "python" });
    outPanel(s, { x: x + 0.2, y: 4.12, w: 3.55, h: 1.25, fs: 9.5, text: b.out });
  });
  tx(s, "zeros và ones mặc định là float64; chỉ định dtype=np.int64 nếu cần số nguyên.", {
    x: 0.6, y: 5.85, w: 12.1, h: 0.3, fontSize: 10.5, italic: true, color: C.muted,
  });
  footer(s, 11);
  s.addNotes("Ba hàm tạo mảng cơ bản nhất. array nhận dữ liệu có sẵn và tự suy ra dtype; zeros và ones nhận shape dạng tuple và mặc định trả về float64. Có thể chỉ định dtype khi cần.");
}

/* ---------------------------------------------------------------- 12 create 2 */
{
  const s = p.addSlide(); bg(s);
  header(s, "03 · Tạo mảng", "Dãy theo bước và chia đều: arange, linspace, eye");
  codePanel(s, {
    x: 0.6, y: 1.6, w: 6.2, h: 2.35, fs: 10.5,
    code: "np.arange(0, 10, 2)\nnp.arange(4)\n\nnp.linspace(0, 1, 5)\n\nnp.eye(3)",
  });
  outPanel(s, {
    x: 0.6, y: 4.1, w: 6.2, h: 1.75, fs: 10,
    text: "[0 2 4 6 8]\n[0 1 2 3]\n\n[0.   0.25 0.5  0.75 1.  ]\n\n[[1. 0. 0.]\n [0. 1. 0.]\n [0. 0. 1.]]",
  });
  const head = ["Hàm", "Dùng khi", "Điểm cần nhớ"];
  const rows = [
    ["np.arange", "Dãy theo bước", "Không gồm stop"],
    ["np.linspace", "num điểm chia đều", "Mặc định gồm stop"],
    ["np.eye", "Ma trận đơn vị", "Đường chéo chính bằng 1"],
  ];
  const tRows = [head.map((h) => ({ text: h, options: { bold: true, color: C.white, fill: { color: C.ink }, fontSize: 10.5 } }))];
  rows.forEach((r, i) => tRows.push(r.map((v, j) => ({
    text: v,
    options: { color: j === 0 ? C.ink : C.slate, bold: j === 0, fill: { color: i % 2 ? C.ice : C.white }, fontSize: 10, fontFace: j === 0 ? F.code : F.body },
  }))));
  s.addTable(tRows, {
    x: 7.05, y: 1.6, w: 5.65, colW: [1.55, 2.0, 2.1], rowH: [0.45, 0.62, 0.62, 0.62],
    border: { type: "solid", pt: 0.5, color: "DCE8EE" }, fontFace: F.body, margin: 5, valign: "middle", autoPage: false,
  });
  card(s, { x: 7.05, y: 4.02, w: 5.65, h: 1.88, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "Phân biệt nhanh", { x: 7.3, y: 4.15, w: 5.0, h: 0.28, fontSize: 11.5, bold: true, color: C.ink });
  tx(s, "•  arange quan tâm “bước nhảy”, không lấy stop.\n•  linspace quan tâm “số điểm”, mặc định lấy cả hai đầu.\n•  eye(n) tạo ma trận vuông n × n, đường chéo bằng 1.", {
    x: 7.3, y: 4.48, w: 5.15, h: 1.35, fontSize: 9.8, color: C.slate, lineSpacingMultiple: 1.15,
  });
  footer(s, 12);
  s.addNotes("arange tạo dãy theo bước và không gồm stop; linspace tạo num điểm chia đều và mặc định gồm điểm cuối; eye tạo ma trận đơn vị. Chọn hàm theo cách mô tả dữ liệu: bước nhảy hay số điểm.");
}

/* ---------------------------------------------------------------- 13 indexing 1d */
{
  const s = p.addSlide(); bg(s);
  header(s, "04 · Truy cập dữ liệu", "Indexing và slicing mảng 1-D");
  const vals = [0, 10, 20, 30, 40, 50];
  const cw = 0.62, ch = 0.62, gx = 0.75, gy = 2.35;
  vals.forEach((v, i) => {
    const on = i === 1 || i === 5;
    s.addShape(p.ShapeType.rect, {
      x: gx + i * cw, y: gy, w: cw, h: ch,
      fill: { color: on ? C.cyan : C.ice }, line: { color: "A9CDDB", width: 0.75 },
    });
    tx(s, String(v), { x: gx + i * cw, y: gy, w: cw, h: ch, fontSize: 12, bold: on, color: on ? C.white : C.ink, align: "center", valign: "mid", fontFace: F.code });
    tx(s, String(i), { x: gx + i * cw, y: gy - 0.3, w: cw, h: 0.22, fontSize: 9, color: C.teal, align: "center", fontFace: F.code });
    tx(s, String(i - 6), { x: gx + i * cw, y: gy + ch + 0.1, w: cw, h: 0.22, fontSize: 9, color: C.coral, align: "center", fontFace: F.code });
  });
  label(s, "chỉ số dương", { x: gx, y: gy - 0.58, w: 3.7, h: 0.22, align: "left", fontSize: 8.5 });
  label(s, "chỉ số âm", { x: gx, y: gy + ch + 0.36, w: 3.7, h: 0.22, align: "left", fontSize: 8.5 });
  tx(s, "c[1] = 10   ·   c[-1] = 50", { x: 0.7, y: 4.05, w: 4.0, h: 0.28, fontSize: 11, bold: true, color: C.ink, fontFace: F.code });
  codePanel(s, {
    x: 4.95, y: 1.6, w: 7.75, h: 2.55, fs: 10,
    code: "c = np.array([0, 10, 20, 30, 40, 50])\nprint(c[0])      # 0\nprint(c[3])      # 30\nprint(c[-1])     # 50\nprint(c[1:4])    # [10 20 30]\nprint(c[::2])    # [ 0 20 40]\nprint(c[::-1])   # [50 40 30 20 10  0]",
  });
  outPanel(s, {
    x: 4.95, y: 4.3, w: 7.75, h: 1.4, fs: 9.5,
    text: "0\n30\n50\n[10 20 30]   [ 0 20 40]   [50 40 30 20 10  0]",
  });
  tx(s, "Slicing trả về view, không phải bản sao: sửa view sẽ sửa mảng gốc. Dùng .copy() nếu cần dữ liệu độc lập.", {
    x: 0.6, y: 5.95, w: 12.1, h: 0.45, fontSize: 10.5, italic: true, color: C.muted,
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
    ["a[1] — cả hàng", { "1,0": C.cyan, "1,1": C.cyan, "1,2": C.cyan, "1,3": C.cyan }],
    ["a[:, 2] — cả cột", { "0,2": C.teal, "1,2": C.teal, "2,2": C.teal }],
    ["a[0:2, 1:3] — khối con", { "0,1": C.coral, "0,2": C.coral, "1,1": C.coral, "1,2": C.coral }],
  ];
  panels.forEach((pn, i) => {
    const x = 0.6 + i * 1.98;
    label(s, pn[0], { x: x - 0.05, y: 1.55, w: 1.95, h: 0.24, fontSize: 8.5, bold: true, color: C.slate, align: "center" });
    grid(s, { x, y: 2.0, cw: 0.4, ch: 0.34, rows: 3, cols: 4, vals: base, fs: 8.5, hi: pn[1] });
    for (let c = 0; c < 4; c++) tx(s, String(c), { x: x + c * 0.4, y: 1.78, w: 0.4, h: 0.2, fontSize: 8.5, color: C.muted, align: "center", fontFace: F.code });
    for (let r = 0; r < 3; r++) tx(s, String(r), { x: x - 0.24, y: 2.0 + r * 0.34, w: 0.2, h: 0.34, fontSize: 8.5, color: C.muted, align: "center", valign: "mid", fontFace: F.code });
  });
  codePanel(s, {
    x: 6.45, y: 1.6, w: 6.25, h: 2.4, fs: 10,
    code: "b = np.array([[10, 11, 12, 13],\n              [20, 21, 22, 23],\n              [30, 31, 32, 33]])\nprint(b[0, 0])       # 10\nprint(b[1])         # [20 21 22 23]\nprint(b[:, 2])      # [12 22 32]\nprint(b[0:2, 1:3])  # [[11 12] [21 22]]",
  });
  outPanel(s, {
    x: 6.45, y: 4.15, w: 6.25, h: 1.6, fs: 9.5,
    text: "10\n[20 21 22 23]\n[12 22 32]\n[[11 12]\n [21 22]]",
  });
  card(s, { x: 0.7, y: 3.35, w: 5.45, h: 1.95, fill: C.white, line: C.border, shadow: false });
  tx(s, "Cách đọc kết quả", { x: 0.95, y: 3.5, w: 4.9, h: 0.26, fontSize: 11, bold: true, color: C.ink });
  [
    [C.cyan, "b[1]", "một hàng → mảng 1-D, shape (4,)"],
    [C.teal, "b[:, 2]", "một cột → mảng 1-D, shape (3,)"],
    [C.coral, "b[0:2, 1:3]", "khối con → mảng 2-D, shape (2, 2)"],
  ].forEach((r, i) => {
    const y = 3.88 + i * 0.42;
    s.addShape(p.ShapeType.rect, { x: 0.95, y: y + 0.05, w: 0.08, h: 0.2, fill: { color: r[0] }, line: { color: r[0], width: 0 } });
    tx(s, r[1], { x: 1.15, y: y - 0.01, w: 1.0, h: 0.28, fontSize: 9, fontFace: F.code, bold: true, color: C.slate });
    tx(s, r[2], { x: 2.2, y: y - 0.01, w: 3.75, h: 0.28, fontSize: 9, color: C.slate });
  });
  tx(s, "Một cặp ngoặc vuông với dấu phẩy: a[hàng, cột]. Bỏ chỉ số hàng hoặc cột bằng dấu : để lấy cả trục.", {
    x: 0.6, y: 5.95, w: 12.1, h: 0.45, fontSize: 10.5, italic: true, color: C.muted,
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
  mask.forEach((r, i) => r.forEach((v, j) => { if (v === "T") mh[i + "," + j] = "2D8C6F"; }));
  const hh = {};
  [[1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]].forEach(([r, c]) => { hh[r + "," + c] = "2D8C6F"; });
  label(s, "b", { x: 0.7, y: 1.52, w: 1.6, h: 0.22, fontSize: 9, bold: true, color: C.slate, fontFace: F.code });
  label(s, "b > 21", { x: 2.55, y: 1.52, w: 1.7, h: 0.22, fontSize: 9, bold: true, color: C.slate, fontFace: F.code });
  label(s, "b[b > 21]", { x: 4.45, y: 1.52, w: 1.4, h: 0.22, fontSize: 9, bold: true, color: C.slate, fontFace: F.code });
  grid(s, { x: 0.7, y: 1.85, cw: 0.45, ch: 0.37, rows: 3, cols: 4, vals: base, fs: 8.5 });
  grid(s, { x: 2.6, y: 1.85, cw: 0.45, ch: 0.37, rows: 3, cols: 4, vals: mask, fs: 8.5, fill: "F1F7F9", line: "B9D7E4", hi: mh });
  const res = [22, 23, 30, 31, 32, 33];
  res.forEach((v, i) => {
    const y = 1.85 + i * 0.37;
    s.addShape(p.ShapeType.rect, { x: 4.55, y, w: 0.9, h: 0.37, fill: { color: C.ice }, line: { color: "A9CDDB", width: 0.75 } });
    tx(s, String(v), { x: 4.55, y, w: 0.9, h: 0.37, fontSize: 9, bold: true, color: C.green, align: "center", valign: "mid", fontFace: F.code });
  });
  tx(s, "6 phần tử True\nđược nén thành mảng 1-D", {
    x: 0.7, y: 3.55, w: 3.4, h: 0.6, fontSize: 9.5, color: C.muted, lineSpacingMultiple: 1.1,
  });
  codePanel(s, {
    x: 6.55, y: 1.6, w: 6.15, h: 0.95, fs: 10,
    code: "print(b[b > 21])\nprint(b > 21)",
  });
  outPanel(s, {
    x: 6.55, y: 2.7, w: 6.15, h: 2.35, fs: 9.2,
    text: "[22 23 30 31 32 33]\n\n[[False False False False]\n [False False  True  True]\n [ True  True  True  True]]\n\nMảng kết quả 1-D vì các phần tử\nTrue được nén lại.",
  });
  card(s, { x: 0.7, y: 4.15, w: 5.5, h: 1.45, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "Cách đọc", { x: 0.92, y: 4.28, w: 5.0, h: 0.24, fontSize: 10.5, bold: true, color: C.teal });
  tx(s, "1  So sánh b > 21 → mảng boolean cùng shape.\n2  Dùng mảng boolean làm chỉ số → lấy phần tử True.\n3  Kết quả nén thành mảng 1-D, giữ thứ tự đọc.", {
    x: 0.92, y: 4.57, w: 5.05, h: 0.95, fontSize: 9.4, color: C.slate, lineSpacingMultiple: 1.18,
  });
  tx(s, "Kết hợp điều kiện bằng &, | và ngoặc đơn, ví dụ b[(b > 10) & (b < 30)].", {
    x: 0.6, y: 6.02, w: 12.1, h: 0.4, fontSize: 10.5, italic: true, color: C.muted,
  });
  footer(s, 15);
  s.addNotes("So sánh một mảng với một giá trị tạo ra mảng boolean cùng shape. Dùng mảng boolean làm chỉ số sẽ lấy các phần tử True và nén thành mảng một chiều. Kết hợp điều kiện bằng & và |, nhớ đặt ngoặc đơn.");
}

/* ---------------------------------------------------------------- 16 reshape */
{
  const s = p.addSlide(); bg(s);
  header(s, "04 · Truy cập dữ liệu", "reshape() và .T: cùng dữ liệu, khác hình dạng");
  const seq = [0, 1, 2, 3, 4, 5];
  label(s, "1-D  ·  shape (6,)", { x: 0.7, y: 1.55, w: 3.2, h: 0.22, fontSize: 10, bold: true, color: C.slate });
  seq.forEach((v, i) => {
    s.addShape(p.ShapeType.rect, { x: 0.7 + i * 0.52, y: 1.85, w: 0.52, h: 0.52, fill: { color: C.ice }, line: { color: "A9CDDB", width: 0.75 } });
    tx(s, String(v), { x: 0.7 + i * 0.52, y: 1.85, w: 0.52, h: 0.52, fontSize: 11, color: C.ink, align: "center", valign: "mid", fontFace: F.code });
  });
  arrow(s, 3.95, 2.1, 4.55, 2.1, { color: C.teal, w: 1.75 });
  label(s, "reshape(2, 3)", { x: 3.85, y: 1.55, w: 1.5, h: 0.22, fontSize: 9, color: C.teal, align: "center", fontFace: F.code });
  for (let r = 0; r < 2; r++) for (let c = 0; c < 3; c++) {
    s.addShape(p.ShapeType.rect, { x: 4.7 + c * 0.55, y: 1.85 + r * 0.55, w: 0.55, h: 0.55, fill: { color: "D6EEF5" }, line: { color: "A9CDDB", width: 0.75 } });
    tx(s, String(r * 3 + c), { x: 4.7 + c * 0.55, y: 1.85 + r * 0.55, w: 0.55, h: 0.55, fontSize: 11, color: C.ink, align: "center", valign: "mid", fontFace: F.code });
  }
  label(s, "shape (2, 3)", { x: 4.7, y: 3.02, w: 1.7, h: 0.22, fontSize: 9, color: C.muted, fontFace: F.code });
  arrow(s, 6.5, 2.1, 7.1, 2.1, { color: C.amber, w: 1.75 });
  label(s, ".T", { x: 6.55, y: 1.55, w: 0.6, h: 0.22, fontSize: 11, bold: true, color: C.amber, align: "center", fontFace: F.code });
  for (let r = 0; r < 3; r++) for (let c = 0; c < 2; c++) {
    s.addShape(p.ShapeType.rect, { x: 7.25 + c * 0.55, y: 1.85 + r * 0.5, w: 0.55, h: 0.5, fill: { color: "FBEFD9" }, line: { color: "E5C28C", width: 0.75 } });
    tx(s, String(c * 3 + r), { x: 7.25 + c * 0.55, y: 1.85 + r * 0.5, w: 0.55, h: 0.5, fontSize: 11, color: C.ink, align: "center", valign: "mid", fontFace: F.code });
  }
  label(s, "shape (3, 2)", { x: 7.25, y: 3.42, w: 1.5, h: 0.22, fontSize: 9, color: C.muted, fontFace: F.code });
  card(s, { x: 9.55, y: 1.7, w: 3.15, h: 1.6, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "Mẹo -1", { x: 9.75, y: 1.85, w: 2.7, h: 0.25, fontSize: 11, bold: true, color: C.teal });
  tx(s, "reshape(3, -1) để NumPy tự suy ra chiều còn lại: kết quả (3, 4).", {
    x: 9.75, y: 2.15, w: 2.75, h: 0.95, fontSize: 9.5, color: C.slate, lineSpacingMultiple: 1.15,
  });
  codePanel(s, {
    x: 0.6, y: 3.95, w: 6.3, h: 1.9, fs: 10,
    code: "r = np.arange(6).reshape(2, 3)\nprint(r)\nprint(r.T)\nprint(np.arange(12).reshape(3, -1).shape)",
  });
  outPanel(s, {
    x: 7.1, y: 3.95, w: 5.6, h: 1.9, fs: 9.5,
    text: "[[0 1 2]\n [3 4 5]]\n\n[[0 3]\n [1 4]\n [2 5]]\n\n(3, 4)",
  });
  tx(s, "Tổng số phần tử phải giữ nguyên: 6 = 2 × 3; 6 = 3 × 2. .T hoán vị hàng thành cột.", {
    x: 0.6, y: 6.05, w: 12.1, h: 0.3, fontSize: 10, italic: true, color: C.muted,
  });
  footer(s, 16);
  s.addNotes("reshape đổi hình dạng nhưng giữ nguyên dữ liệu và thứ tự đọc; tổng số phần tử phải bằng nhau. Dùng -1 để tự suy ra một chiều. .T hoán vị hàng và cột, không đổi dữ liệu.");
}

/* ---------------------------------------------------------------- 17 element-wise */
{
  const s = p.addSlide(); bg(s);
  header(s, "05 · Tính toán", "Phép toán theo từng phần tử");
  const row = (vals, y, col, hi) => vals.forEach((v, i) => {
    s.addShape(p.ShapeType.rect, { x: 1.0 + i * 0.62, y, w: 0.62, h: 0.52, fill: { color: hi || C.ice }, line: { color: "A9CDDB", width: 0.75 } });
    tx(s, String(v), { x: 1.0 + i * 0.62, y, w: 0.62, h: 0.52, fontSize: 12, color: hi ? C.white : C.ink, align: "center", valign: "mid", fontFace: F.code });
  });
  row([1, 2, 3], 1.85, C.ink);
  row([4, 5, 6], 3.05, C.ink);
  row([5, 7, 9], 4.35, C.ink, C.teal);
  tx(s, "+", { x: 1.0, y: 2.52, w: 0.4, h: 0.3, fontSize: 18, bold: true, color: C.teal, align: "center" });
  arrow(s, 2.1, 3.65, 2.1, 4.2, { color: C.teal, w: 1.75 });
  label(s, "x", { x: 0.7, y: 1.95, w: 0.25, h: 0.3, fontSize: 11, bold: true, color: C.muted, fontFace: F.code });
  label(s, "y", { x: 0.7, y: 3.15, w: 0.25, h: 0.3, fontSize: 11, bold: true, color: C.muted, fontFace: F.code });
  codePanel(s, {
    x: 4.55, y: 1.6, w: 8.15, h: 2.85, fs: 9.8,
    code: "x = np.array([1, 2, 3])\ny = np.array([4, 5, 6])\nprint(x + y)   # [5 7 9]\nprint(x - y)   # [-3 -3 -3]\nprint(x * y)   # [ 4 10 18]\nprint(x / y)   # [0.25 0.4  0.5 ]\nprint(x ** 2)  # [1 4 9]\nprint(x // 2)  # [0 1 1]\nprint(x % 2)   # [1 0 1]",
  });
  outPanel(s, {
    x: 4.55, y: 4.6, w: 8.15, h: 1.15, fs: 9.5,
    text: "[5 7 9]   [-3 -3 -3]   [ 4 10 18]   [0.25 0.4  0.5 ]\n[1 4 9]   [0 1 1]   [1 0 1]",
  });
  tx(s, "Mỗi toán tử áp cho từng cặp phần tử; kết quả cùng shape (sau broadcasting). / luôn trả về số thực, // là chia lấy phần nguyên.", {
    x: 0.6, y: 6.0, w: 12.1, h: 0.45, fontSize: 10.5, italic: true, color: C.muted,
  });
  footer(s, 17);
  s.addNotes("Các toán tử +, -, *, /, **, //, % áp dụng cho từng cặp phần tử và trả về mảng cùng shape. Lưu ý / luôn trả về số thực, còn // là chia lấy phần nguyên.");
}

/* ---------------------------------------------------------------- 18 star vs at */
{
  const s = p.addSlide(); bg(s);
  header(s, "05 · Tính toán", "Toán tử * và @ khác nhau thế nào?");
  const drawMat = (x, y, vals, hi, labelText) => {
    label(s, labelText, { x, y: y - 0.28, w: 1.3, h: 0.22, fontSize: 9, bold: true, color: C.slate, fontFace: F.code, align: "center" });
    grid(s, { x, y, cw: 0.48, ch: 0.42, rows: 2, cols: 2, vals, fs: 10.5, hi: hi || {} });
  };
  drawMat(0.7, 2.05, [[1, 2], [3, 4]], { "0,0": C.amber }, "A");
  tx(s, "*", { x: 1.78, y: 2.5, w: 0.3, h: 0.3, fontSize: 16, bold: true, color: C.teal, align: "center" });
  drawMat(2.15, 2.05, [[5, 6], [7, 8]], { "0,0": C.amber }, "B");
  tx(s, "=", { x: 3.22, y: 2.5, w: 0.3, h: 0.3, fontSize: 16, color: C.muted, align: "center" });
  drawMat(3.62, 2.05, [[5, 12], [21, 32]], { "0,0": C.amber }, "A * B");
  tx(s, "từng cặp ô cùng vị trí", { x: 0.7, y: 3.28, w: 3.4, h: 0.22, fontSize: 8.5, color: C.muted, italic: true });

  drawMat(0.7, 4.55, [[1, 2], [3, 4]], { "0,0": C.cyan, "0,1": C.cyan }, "A");
  tx(s, "@", { x: 1.78, y: 5.0, w: 0.3, h: 0.3, fontSize: 16, bold: true, color: C.amber, align: "center" });
  drawMat(2.15, 4.55, [[5, 6], [7, 8]], { "0,0": C.cyan, "1,0": C.cyan }, "B");
  tx(s, "=", { x: 3.22, y: 5.0, w: 0.3, h: 0.3, fontSize: 16, color: C.muted, align: "center" });
  drawMat(3.62, 4.55, [[19, 22], [43, 50]], { "0,0": C.amber }, "A @ B");
  tx(s, "hàng × cột: 1×5 + 2×7 = 19", { x: 0.7, y: 5.8, w: 3.5, h: 0.24, fontSize: 8.5, color: C.muted, italic: true });

  codePanel(s, {
    x: 4.95, y: 1.6, w: 7.75, h: 1.75, fs: 10.5,
    code: "A = np.array([[1, 2], [3, 4]])\nB = np.array([[5, 6], [7, 8]])\nprint(A * B)\nprint(A @ B)",
  });
  outPanel(s, {
    x: 4.95, y: 3.5, w: 7.75, h: 1.45, fs: 10.5,
    text: "[[ 5 12]\n [21 32]]\n[[19 22]\n [43 50]]",
  });
  const head = ["Toán tử", "Ý nghĩa", "Điều kiện shape"];
  const rows = [
    ["*", "Nhân từng phần tử", "Cùng shape hoặc broadcast được"],
    ["@", "Nhân ma trận", "Số cột của A = số hàng của B"],
  ];
  const tRows = [head.map((h) => ({ text: h, options: { bold: true, color: C.white, fill: { color: C.ink }, fontSize: 8.8 } }))];
  rows.forEach((r, i) => tRows.push(r.map((v, j) => ({
    text: v,
    options: { color: j === 0 ? C.ink : C.slate, bold: j === 0, fill: { color: i % 2 ? C.ice : C.white }, fontSize: 8.8, fontFace: j === 0 ? F.code : F.body },
  }))));
  s.addTable(tRows, {
    x: 4.95, y: 5.12, w: 7.75, colW: [0.9, 2.6, 4.25], rowH: [0.32, 0.34, 0.34],
    border: { type: "solid", pt: 0.5, color: "DCE8EE" }, fontFace: F.body, margin: 4, valign: "middle", autoPage: false,
  });
  footer(s, 18);
  s.addNotes("Đây là lỗi rất dễ mắc: * là nhân từng phần tử, @ là nhân ma trận theo quy tắc hàng nhân cột. Với A@B, phần tử (0,0) bằng 1×5 + 2×7 = 19, còn A*B cho 1×5 = 5.");
}

/* ---------------------------------------------------------------- 19 axis */
{
  const s = p.addSlide(); bg(s);
  header(s, "05 · Tính toán", "Hàm tổng hợp và ý nghĩa của axis");
  const vals = [[1, 2, 3], [4, 5, 6]];
  const gx = 1.15, gy = 2.15, cw = 0.62, ch = 0.5;
  grid(s, { x: gx, y: gy, cw, ch, rows: 2, cols: 3, vals, fs: 12 });
  label(s, "m", { x: 0.7, y: gy - 0.3, w: 0.4, h: 0.22, fontSize: 10, bold: true, color: C.slate, fontFace: F.code });
  arrow(s, gx - 0.28, gy + 0.1, gx - 0.28, gy + 1.05, { color: C.teal, w: 1.5, begin: true, end: true });
  tx(s, "axis = 0", { x: 0.45, y: gy + 1.18, w: 0.95, h: 0.24, fontSize: 8, bold: true, color: C.teal, align: "center", fontFace: F.code });
  arrow(s, gx + 0.1, gy - 0.25, gx + 1.95, gy - 0.25, { color: C.amber, w: 1.5, begin: true, end: true });
  tx(s, "axis = 1", { x: gx + 2.02, y: gy - 0.36, w: 0.8, h: 0.22, fontSize: 8, bold: true, color: "B7771B", fontFace: F.code });
  tx(s, "[5 7 9]", { x: gx - 0.1, y: gy + 1.45, w: 2.2, h: 0.3, fontSize: 13, bold: true, color: C.teal, fontFace: F.code });
  tx(s, "[ 6 15]", { x: gx + cw * 3 + 0.25, y: gy + 0.35, w: 1.4, h: 0.3, fontSize: 13, bold: true, color: "B7771B", fontFace: F.code });
  label(s, "kết quả theo cột", { x: gx - 0.1, y: gy + 1.75, w: 2.3, h: 0.22, fontSize: 8.5 });
  label(s, "kết quả theo hàng", { x: gx + cw * 3 + 0.25, y: gy + 0.68, w: 1.55, h: 0.22, fontSize: 8.5 });

  codePanel(s, {
    x: 5.65, y: 1.6, w: 7.05, h: 2.35, fs: 9.8,
    code: "print(np.sum(m))           # 21\nprint(np.sum(m, axis=0))   # [5 7 9]\nprint(np.sum(m, axis=1))   # [ 6 15]\nprint(np.mean(m))          # 3.5\nprint(np.min(m), np.max(m))  # 1 6",
  });
  outPanel(s, { x: 5.65, y: 4.1, w: 7.05, h: 1.0, fs: 10, text: "21   ·   [5 7 9]   ·   [ 6 15]   ·   3.5   ·   1 6" });

  const head = ["Cách gọi", "Chiều bị gộp", "Shape kết quả", "Kết quả"];
  const rows = [
    ["m.sum()", "toàn bộ", "()", "21"],
    ["m.sum(axis=0)", "hàng (trục 0)", "(3,)", "[5 7 9]"],
    ["m.sum(axis=1)", "cột (trục 1)", "(2,)", "[ 6 15]"],
  ];
  const tRows = [head.map((h) => ({ text: h, options: { bold: true, color: C.white, fill: { color: C.ink }, fontSize: 9 } }))];
  rows.forEach((r, i) => tRows.push(r.map((v, j) => ({
    text: v,
    options: { color: j === 0 ? C.ink : C.slate, bold: j === 0, fill: { color: i % 2 ? C.ice : C.white }, fontSize: 9, fontFace: j === 0 || j === 3 ? F.code : F.body },
  }))));
  s.addTable(tRows, {
    x: 0.6, y: 5.2, w: 7.0, colW: [1.55, 1.55, 1.3, 2.6], rowH: [0.36, 0.38, 0.38, 0.38],
    border: { type: "solid", pt: 0.5, color: "DCE8EE" }, fontFace: F.body, margin: 4, valign: "middle", autoPage: false,
  });
  tx(s, "axis là chiều bị gộp: axis=0 gộp các hàng, axis=1 gộp các cột.", {
    x: 7.95, y: 5.45, w: 4.8, h: 0.6, fontSize: 10, italic: true, color: C.muted,
  });
  footer(s, 19);
  s.addNotes("axis là chiều bị gộp, không phải chiều giữ lại. Với mảng 2×3, axis=0 gộp các hàng nên kết quả theo cột; axis=1 gộp các cột nên kết quả theo hàng. Không truyền axis thì gộp toàn mảng.");
}

/* ---------------------------------------------------------------- 20 broadcasting rules */
{
  const s = p.addSlide(); bg(s);
  header(s, "05 · Tính toán", "Broadcasting: tính giữa các shape khác nhau");
  tx(s, "Broadcasting cho phép mảng nhỏ được “trải” lên mảng lớn để hai bên tương thích — vòng lặp chạy trong C, không sao chép dữ liệu không cần thiết.", {
    x: 0.6, y: 1.55, w: 5.7, h: 1.0, fontSize: 13.5, color: C.ink, lineSpacingMultiple: 1.2,
  });
  const rules = [
    ["1", "So sánh shape từ phải sang trái."],
    ["2", "Mỗi cặp chiều tương thích nếu bằng nhau, hoặc một bên bằng 1."],
    ["3", "Mảng ít chiều hơn được coi là có các chiều thiếu bằng 1 ở bên trái."],
  ];
  rules.forEach((r, i) => {
    const y = 2.8 + i * 1.12;
    s.addShape(p.ShapeType.roundRect, { x: 0.6, y, w: 0.5, h: 0.5, fill: { color: C.teal }, line: { color: C.white, width: 1 }, rectRadius: 0.15 });
    tx(s, r[0], { x: 0.6, y, w: 0.5, h: 0.5, fontSize: 13, bold: true, color: C.white, align: "center", valign: "mid" });
    tx(s, r[1], { x: 1.25, y: y - 0.05, w: 4.9, h: 0.85, fontSize: 11.5, color: C.slate, lineSpacingMultiple: 1.15 });
  });
  card(s, { x: 6.6, y: 1.6, w: 6.1, h: 3.55, fill: C.ink, line: C.ink });
  tx(s, "SO SÁNH TỪ PHẢI SANG TRÁI", { x: 6.85, y: 1.78, w: 5.6, h: 0.22, fontSize: 8.5, bold: true, color: C.cyan, charSpacing: 1.5 });
  tx(s, "(2, 3)", { x: 6.85, y: 2.15, w: 2.6, h: 0.42, fontSize: 21, bold: true, color: C.white, fontFace: F.code, align: "right" });
  tx(s, "(   3,)", { x: 6.85, y: 2.72, w: 2.6, h: 0.42, fontSize: 21, bold: true, color: C.cyan, fontFace: F.code, align: "right" });
  s.addShape(p.ShapeType.rect, { x: 6.85, y: 3.28, w: 2.6, h: 0.01, fill: { color: "2A5668" }, line: { color: "2A5668", width: 0 } });
  tx(s, "(2, 3)", { x: 6.85, y: 3.4, w: 2.6, h: 0.42, fontSize: 21, bold: true, color: C.amber, fontFace: F.code, align: "right" });
  tx(s, "3 = 3", { x: 9.75, y: 2.18, w: 1.2, h: 0.3, fontSize: 9.5, color: "8AD9C0", fontFace: F.code });
  tx(s, "2 vs 1 (thiếu) → 2", { x: 9.75, y: 3.45, w: 2.4, h: 0.3, fontSize: 9.5, color: "8AD9C0", fontFace: F.code });
  arrow(s, 9.55, 2.38, 9.55, 3.5, { color: C.cyan, w: 1, end: false, dash: "dash" });
  tx(s, "KẾT QUẢ", { x: 6.85, y: 4.45, w: 2.6, h: 0.2, fontSize: 8.5, bold: true, color: C.cyan, charSpacing: 1.2, align: "right" });
  tx(s, "(2, 3)", { x: 6.85, y: 4.7, w: 2.6, h: 0.4, fontSize: 19, bold: true, color: C.amber, fontFace: F.code, align: "right" });
  tx(s, "shape của mảng lớn\nđược giữ nguyên", { x: 9.55, y: 4.62, w: 2.9, h: 0.55, fontSize: 8.5, color: "B8D2DD", lineSpacingMultiple: 1.1 });

  card(s, { x: 6.6, y: 5.35, w: 6.1, h: 0.85, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "a * 2.0  →  [2. 4. 6.]", { x: 6.85, y: 5.35, w: 3.2, h: 0.85, fontSize: 12, bold: true, color: C.ink, fontFace: F.code, valign: "mid" });
  tx(s, "scalar trải như shape (3,),\nkhông sao chép thật", { x: 9.9, y: 5.42, w: 2.65, h: 0.72, fontSize: 8.5, color: C.muted, lineSpacingMultiple: 1.1 });
  tx(s, "Nguồn: NumPy Documentation — Broadcasting [3]", { x: 0.6, y: 6.3, w: 5.6, h: 0.25, fontSize: 8.5, color: C.muted });
  footer(s, 20);
  s.addNotes("Quy tắc cốt lõi: so sánh shape từ phải sang trái; mỗi cặp chiều bằng nhau hoặc một bên bằng 1 thì tương thích; mảng ít chiều hơn được coi là có chiều thiếu bằng 1 ở bên trái. Scalar được trải nhưng không thực sự sao chép.");
}

/* ---------------------------------------------------------------- 21 broadcasting examples */
{
  const s = p.addSlide(); bg(s);
  header(s, "05 · Tính toán", "Broadcasting: thành công và thất bại");
  const okCard = (x, title, sub, result) => {
    card(s, { x, y: 1.6, w: 3.88, h: 2.5 });
    tx(s, title, { x: x + 0.24, y: 1.78, w: 3.4, h: 0.35, fontSize: 14, bold: true, color: C.ink, fontFace: F.code });
    tx(s, sub, { x: x + 0.24, y: 2.16, w: 3.4, h: 0.5, fontSize: 9.5, color: C.muted, lineSpacingMultiple: 1.1 });
    tx(s, result, { x: x + 0.24, y: 2.78, w: 3.4, h: 1.1, fontSize: 12, color: C.green, fontFace: F.code, lineSpacingMultiple: 1.15 });
    tx(s, "✓ hợp lệ", { x: x + 0.24, y: 3.66, w: 1.5, h: 0.24, fontSize: 9, bold: true, color: C.green });
  };
  okCard(0.6, "(2, 3) + (3,)", "(3,) coi là (1, 3),\ntrải xuống 2 hàng", "[[11 22 33]\n [14 25 36]]");
  okCard(4.72, "(2, 3) + (2, 1)", "(2, 1) trải sang 3 cột,\nmỗi hàng cộng một số", "[[11 12 13]\n [24 25 26]]");
  card(s, { x: 8.84, y: 1.6, w: 3.89, h: 2.5, fill: "FBEDEA", line: "EBC3BB" });
  tx(s, "(2, 3) + (2,)", { x: 9.08, y: 1.78, w: 3.4, h: 0.35, fontSize: 14, bold: true, color: C.ink, fontFace: F.code });
  tx(s, "Chiều cuối 3 ≠ 2,\nkhông bên nào bằng 1", { x: 9.08, y: 2.16, w: 3.4, h: 0.5, fontSize: 9.5, color: C.muted, lineSpacingMultiple: 1.1 });
  tx(s, "ValueError", { x: 9.08, y: 2.82, w: 3.4, h: 0.35, fontSize: 14, bold: true, color: C.coral, fontFace: F.code });
  tx(s, "operands could not be\nbroadcast together with\nshapes (2,3) (2,)", { x: 9.08, y: 3.16, w: 3.4, h: 0.62, fontSize: 8.2, color: C.coral, fontFace: F.code, lineSpacingMultiple: 1.0 });
  tx(s, "✕ thất bại", { x: 9.08, y: 3.82, w: 1.5, h: 0.2, fontSize: 9, bold: true, color: C.coral });

  codePanel(s, {
    x: 0.6, y: 4.3, w: 7.6, h: 2.0, fs: 8.8,
    code: "p = np.array([[1, 2, 3], [4, 5, 6]])\nprint(p + np.array([10, 20, 30]))\nprint(p + np.array([[10], [20]]))\n\ntry:\n    print(p + np.array([10, 20]))\nexcept ValueError as e:\n    print(type(e).__name__, e)",
  });
  outPanel(s, {
    x: 8.4, y: 4.3, w: 4.33, h: 2.0, fs: 8.2,
    text: "[[11 22 33]\n [14 25 36]]\n[[11 12 13]\n [24 25 26]]\nValueError operands could not\nbe broadcast together with\nshapes (2,3) (2,)",
  });
  tx(s, "Khi chiều cuối không khớp và không bên nào bằng 1, NumPy báo lỗi ngay — không tự “đoán” ý người viết.", {
    x: 0.6, y: 6.45, w: 12.1, h: 0.3, fontSize: 9.5, italic: true, color: C.muted,
  });
  footer(s, 21);
  s.addNotes("Hai trường hợp thành công: (2,3)+(3,) và (2,3)+(2,1). Trường hợp thất bại: (2,3)+(2,) vì chiều cuối 3 khác 2 và không bên nào bằng 1. NumPy báo ValueError thay vì tự suy diễn.");
}

/* ---------------------------------------------------------------- 22 example stats */
{
  const s = p.addSlide(); bg(s);
  header(s, "06 · Thực hành", "Ví dụ 1 — Thống kê điểm kiểm tra");
  tx(s, "5 bài kiểm tra: 8.0, 7.5, 9.0, 6.5, 8.5. Tính trung bình, cao nhất, thấp nhất, độ lệch chuẩn; đếm bài đạt từ 8.0; cộng 0.5 điểm thưởng.", {
    x: 0.6, y: 1.52, w: 12.1, h: 0.5, fontSize: 11.5, color: C.slate, lineSpacingMultiple: 1.1,
  });
  codePanel(s, {
    x: 0.6, y: 2.1, w: 5.55, h: 2.85, fs: 9.3,
    code: 'd = np.array([8.0, 7.5, 9.0, 6.5, 8.5])\nprint("Diem TB:", np.mean(d))\nprint("Cao nhat:", np.max(d))\nprint("Thap nhat:", np.min(d))\nprint("Do lech chuan:", np.std(d))\nprint("So bai >= 8:", np.sum(d >= 8.0), "/", d.size)\nprint("Sau thuong:", d + 0.5)',
  });
  outPanel(s, {
    x: 0.6, y: 5.1, w: 5.55, h: 1.3, fs: 8.6,
    text: "Diem TB: 7.9\nCao nhat: 9.0   Thap nhat: 6.5\nDo lech chuan: 0.8602325267042626\nSo bai >= 8: 3 / 5\nSau thuong: [8.5 8.  9.5 7.  9. ]",
  });
  const stats = [["7.9", "Điểm trung bình"], ["9.0", "Cao nhất"], ["6.5", "Thấp nhất"], ["0.860", "Độ lệch chuẩn"]];
  stats.forEach((st, i) => {
    const x = 6.45 + (i % 2) * 3.18;
    const y = 2.1 + Math.floor(i / 2) * 1.12;
    card(s, { x, y, w: 3.03, h: 1.0 });
    tx(s, st[0], { x: x + 0.18, y: y + 0.12, w: 1.45, h: 0.5, fontSize: 20, bold: true, color: C.teal, fontFace: F.code });
    tx(s, st[1], { x: x + 1.5, y: y + 0.2, w: 1.4, h: 0.6, fontSize: 8.5, color: C.muted, lineSpacingMultiple: 1.05 });
  });
  label(s, "Điểm từng bài và đường trung bình 7.9", { x: 6.45, y: 4.4, w: 6.2, h: 0.24, fontSize: 9.5, bold: true, color: C.slate });
  const bx = 6.7, by = 4.72, bw = 5.6, bh = 1.55, maxV = 10;
  const scores = [8.0, 7.5, 9.0, 6.5, 8.5];
  scores.forEach((v, i) => {
    const h = (v / maxV) * bh;
    const x = bx + i * 1.02;
    s.addShape(p.ShapeType.rect, { x, y: by + bh - h, w: 0.58, h, fill: { color: i === 1 ? C.cyan : C.teal }, line: { color: C.white, width: 0.5 } });
    tx(s, v.toFixed(1), { x: x - 0.08, y: by + bh - h - 0.22, w: 0.74, h: 0.2, fontSize: 8.5, color: C.ink, align: "center", fontFace: F.code });
  });
  const meanY = by + bh - (7.9 / maxV) * bh;
  s.addShape(p.ShapeType.line, {
    x: bx - 0.05, y: meanY, w: 5.2, h: 0,
    line: { color: C.amber, width: 1.25, dashType: "dash" },
  });
  tx(s, "TB 7.9", { x: bx + 4.65, y: meanY - 0.24, w: 0.75, h: 0.2, fontSize: 8, bold: true, color: "B7771B", fontFace: F.code });
  tx(s, "3/5 bài đạt ngưỡng 8.0", { x: 6.45, y: 6.42, w: 6.2, h: 0.24, fontSize: 9.5, bold: true, color: C.green });
  footer(s, 22);
  s.addNotes("Ví dụ thống kê: mean 7.9, max 9.0, min 6.5, std khoảng 0.860. d >= 8.0 tạo mảng boolean, np.sum cộng các True để đếm 3/5. d + 0.5 cộng điểm thưởng nhờ broadcasting.");
}

/* ---------------------------------------------------------------- 23 example zscore */
{
  const s = p.addSlide(); bg(s);
  header(s, "06 · Thực hành", "Ví dụ 2 — Chuẩn hóa và thay vòng lặp");
  const col = (x, title, code, out, take) => {
    card(s, { x, y: 1.6, w: 5.95, h: 4.35 });
    tx(s, title, { x: x + 0.26, y: 1.76, w: 5.4, h: 0.32, fontSize: 13.5, bold: true, color: C.ink });
    codePanel(s, { x: x + 0.22, y: 2.18, w: 5.5, h: 1.72, fs: 9.2, code });
    outPanel(s, { x: x + 0.22, y: 4.02, w: 5.5, h: 1.18, fs: 8.8, text: out });
    tx(s, take, { x: x + 0.26, y: 5.3, w: 5.4, h: 0.5, fontSize: 9.2, italic: true, color: C.muted, lineSpacingMultiple: 1.1 });
  };
  col(0.6, "Chuẩn hóa z-score",
    "x = np.array([2.0, 4.0, 6.0, 8.0])\nz = (x - np.mean(x)) / np.std(x)\nprint(z)\nprint(np.mean(z), np.std(z))",
    "[-1.34164079 -0.4472136\n  0.4472136   1.34164079]\nmean: 0.0  std: 1.0",
    "Hai lần broadcasting với scalar: trừ 5.0 rồi chia 2.236. Kết quả có trung bình 0, độ lệch chuẩn 1.");
  col(6.78, "Vector hóa và lọc dữ liệu",
    "prices = np.array([100, 250, 80, 320])\nnew = prices * 1.1\nprint(new)\nprint(prices > 200)\nprint(prices[prices > 200])",
    "[110. 275.  88. 352.]\n[False  True False  True]\n[250 320]",
    "Một biểu thức thay cho vòng lặp: nhân từng phần tử, tạo mặt nạ boolean, rồi lọc.");
  card(s, { x: 0.6, y: 6.12, w: 12.13, h: 0.62, fill: C.ice, line: "CFE5EE", shadow: false });
  tx(s, "Điểm chung: biểu thức mảng thay cho vòng lặp — ngắn hơn, ít lỗi chỉ số hơn, và đọc như công thức toán.", {
    x: 0.85, y: 6.12, w: 11.6, h: 0.62, fontSize: 11, bold: true, color: C.teal, valign: "mid",
  });
  footer(s, 23);
  s.addNotes("Hai ví dụ cho thấy sức mạnh biểu diễn: chuẩn hóa z-score bằng một biểu thức, và thay vòng lặp bằng phép nhân mảng kết hợp mặt nạ boolean. Kết quả z có mean 0 và std 1.");
}

/* ---------------------------------------------------------------- 24 conclusion */
{
  const s = p.addSlide(); bg(s, C.ink);
  header(s, "Kết luận", "Ba điều cần nhớ về NumPy", { dark: true });
  const items = [
    ["01", "Shape quyết định mọi thứ", "Đọc shape trước khi viết phép toán: mọi lỗi shape đều dẫn tới ValueError hoặc kết quả sai khó hiểu."],
    ["02", "* khác @", "* nhân từng phần tử; @ nhân ma trận theo quy tắc hàng × cột. Hai kết quả hoàn toàn khác nhau."],
    ["03", "Broadcasting so sánh từ phải sang trái", "Tương thích khi bằng nhau hoặc một bên bằng 1; chiều thiếu được coi là 1."],
  ];
  items.forEach((it, i) => {
    const y = 1.65 + i * 1.28;
    tx(s, it[0], { x: 0.62, y: y + 0.05, w: 0.75, h: 0.5, fontSize: 22, bold: true, color: C.amber, fontFace: F.code });
    tx(s, it[1], { x: 1.4, y, w: 10.9, h: 0.36, fontSize: 16.5, bold: true, color: C.white });
    tx(s, it[2], { x: 1.4, y: y + 0.4, w: 10.9, h: 0.5, fontSize: 10.5, color: "A9C6D3", lineSpacingMultiple: 1.12 });
  });
  const cols = [
    ["Nên dùng khi", "Dữ liệu số, đồng nhất kiểu, kích thước lớn; cần thống kê, biến đổi, đại số tuyến tính, xử lý ảnh, tiền xử lý học máy."],
    ["Cân nhắc công cụ khác", "Bảng nhiều kiểu có nhãn → pandas; dữ liệu nhỏ → list; GPU hoặc đạo hàm tự động → PyTorch."],
  ];
  cols.forEach((c, i) => {
    const x = 0.6 + i * 6.13;
    s.addShape(p.ShapeType.roundRect, { x, y: 5.62, w: 6.0, h: 1.05, fill: { color: "0F3A4C" }, line: { color: "1D566B", width: 0.75 }, rectRadius: 0.06 });
    tx(s, c[0], { x: x + 0.24, y: 5.72, w: 5.5, h: 0.24, fontSize: 10, bold: true, color: C.cyan, charSpacing: 0.8 });
    tx(s, c[1], { x: x + 0.24, y: 5.98, w: 5.55, h: 0.62, fontSize: 8.6, color: "B8D2DD", lineSpacingMultiple: 1.08 });
  });
  footer(s, 24, true);
  s.addNotes("Ba điều cần nhớ: shape quyết định mọi thứ, * khác @, và broadcasting so sánh từ phải sang trái. Kết thúc bằng ranh giới công cụ: pandas cho bảng nhiều kiểu, PyTorch cho GPU và autograd.");
}

/* ---------------------------------------------------------------- 25 references */
{
  const s = p.addSlide(); bg(s);
  header(s, "Tài liệu tham khảo", "Nguồn và hướng tìm hiểu tiếp");
  tx(s, "Hướng tìm hiểu tiếp", { x: 0.6, y: 1.55, w: 4.9, h: 0.3, fontSize: 13, bold: true, color: C.ink });
  const next = [
    ["Matplotlib", "Trực quan hóa mảng: đường, cột, phân tán."],
    ["pandas", "Dữ liệu bảng có nhãn cột và hàng."],
    ["numpy.linalg", "Định thức, nghịch đảo, trị riêng, giải hệ."],
    ["Broadcasting nâng cao", "np.newaxis, np.expand_dims."],
    ["Đọc / ghi dữ liệu", "np.loadtxt, np.savetxt, np.save, np.load."],
  ];
  next.forEach((n, i) => {
    const y = 1.98 + i * 0.83;
    card(s, { x: 0.6, y, w: 4.85, h: 0.7 });
    tx(s, n[0], { x: 0.8, y: y + 0.08, w: 1.75, h: 0.26, fontSize: 10, bold: true, color: C.teal, fontFace: F.code });
    tx(s, n[1], { x: 2.5, y: y + 0.06, w: 2.8, h: 0.58, fontSize: 8.3, color: C.slate, lineSpacingMultiple: 1.05 });
  });
  tx(s, "Tài liệu tham khảo", { x: 5.85, y: 1.55, w: 6.8, h: 0.3, fontSize: 13, bold: true, color: C.ink });
  tx(s, "Truy cập: 25/10/2026", { x: 5.85, y: 1.86, w: 3.0, h: 0.2, fontSize: 8.5, color: C.muted, italic: true });
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
    x: 5.85, y: 2.12, w: 6.9, h: 3.95, fontFace: F.body, fontSize: 9.0, color: C.slate,
    margin: 0, valign: "top", lineSpacingMultiple: 1.08, paraSpaceAfter: 6,
  });
  tx(s, "Logo: NumPy Documentation (giấy phép BSD). Các sơ đồ khác được vẽ bằng hình khối PowerPoint. Code và output kiểm chứng trên Python 3.14 + NumPy 2.5.4.", {
    x: 0.6, y: 6.3, w: 12.1, h: 0.35, fontSize: 8.5, italic: true, color: C.muted,
  });
  footer(s, 25);
  s.addNotes("Bảy nguồn chính thức: What is NumPy, absolute beginners, broadcasting, quickstart, array creation, numpy.linalg và Python datastructures. Hướng tiếp: Matplotlib, pandas, numpy.linalg, broadcasting nâng cao và đọc ghi dữ liệu.");
}

p.writeFile({ fileName: "presentation.pptx" }).then(() => console.log("saved presentation.pptx"));
