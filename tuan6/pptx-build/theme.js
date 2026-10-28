const pptxgen = require("pptxgenjs");

const C = {
  ink: "062A3A",
  slate: "415A6B",
  muted: "728694",
  teal: "1B8EA8",
  cyan: "4DB8D4",
  ice: "EAF4F8",
  paper: "F7FAFB",
  white: "FFFFFF",
  amber: "E8A33D",
  coral: "D96C5F",
  green: "2D8C6F",
  code: "0B2230",
  codeBar: "103445",
  codeText: "D6E6EF",
  border: "D7E5EC",
};

let S = null;
const F = { head: "Segoe UI", body: "Segoe UI", code: "Consolas" };
const TOTAL = 25;

// Type scale for the large-print edition.
// Body: 20-22 pt | subheads: 25-26 pt | slide titles: 32 pt.
const TYPE = {
  title: 32,
  cover: 48,
  subhead: 25,
  body: 20,
  lead: 22,
  code: 16,
  table: 18,
  caption: 15,
  source: 12.5,
  footer: 10.5,
  eyebrow: 12,
};

function deck() {
  const p = new pptxgen();
  p.defineLayout({ name: "W16x9", width: 13.333, height: 7.5 });
  p.layout = "W16x9";
  p.author = "26120072";
  p.subject = "Tìm hiểu thư viện NumPy trong Python";
  p.title = "Tìm hiểu thư viện NumPy trong Python";
  p.company = "Nhập môn Công nghệ Thông tin";
  p.lang = "vi-VN";
  p.theme = { headFontFace: F.head, bodyFontFace: F.body, lang: "vi-VN" };
  S = p.ShapeType;
  return p;
}

function tx(s, text, o = {}) {
  s.addText(text, {
    fontFace: F.body,
    color: C.slate,
    margin: 0,
    valign: "top",
    fontSize: TYPE.body,
    ...o,
  });
}

function bg(s, color = C.paper) {
  s.background = { color };
}

function header(s, eyebrow, title, o = {}) {
  const dark = !!o.dark;
  tx(s, eyebrow.toUpperCase(), {
    x: 0.6, y: 0.3, w: 12.13, h: 0.25, fontSize: TYPE.eyebrow, bold: true,
    color: dark ? C.cyan : C.teal, charSpacing: 1.5, fontFace: F.head,
  });
  tx(s, title, {
    x: 0.6, y: 0.52, w: 12.13, h: 0.8, fontSize: o.size || TYPE.title, bold: true,
    color: dark ? C.white : C.ink, valign: "mid", fontFace: F.head,
  });
  s.addShape(S.rect, {
    x: 0.6, y: 1.4, w: 1.0, h: 0.045,
    fill: { color: dark ? C.amber : C.teal },
    line: { color: dark ? C.amber : C.teal, width: 0 },
  });
}

function footer(s, n, dark = false) {
  s.addShape(S.rect, {
    x: 0.6, y: 7.04, w: 12.13, h: 0.01,
    fill: { color: dark ? "1D4657" : C.border },
    line: { color: dark ? "1D4657" : C.border, width: 0 },
  });
  tx(s, "Tìm hiểu thư viện NumPy trong Python", {
    x: 0.6, y: 7.12, w: 8.5, h: 0.22, fontSize: TYPE.footer,
    color: dark ? "8FB0BF" : C.muted,
  });
  tx(s, `${String(n).padStart(2, "0")} / ${TOTAL}`, {
    x: 11.7, y: 7.12, w: 1.03, h: 0.22, fontSize: TYPE.footer,
    color: dark ? "8FB0BF" : C.muted, align: "right",
  });
}

function card(s, o = {}) {
  s.addShape(S.roundRect, {
    x: o.x, y: o.y, w: o.w, h: o.h,
    fill: { color: o.fill || C.white },
    line: { color: o.line || C.border, width: o.lw || 0.75 },
    rectRadius: 0.07,
    shadow: o.shadow === false ? undefined : {
      type: "outer", color: C.ink, opacity: 0.07, blur: 5, offset: 1, angle: 90,
    },
  });
}

function chip(s, text, o = {}) {
  s.addShape(S.roundRect, {
    x: o.x, y: o.y, w: o.w, h: o.h || 0.44,
    fill: { color: o.fill || C.ice },
    line: { color: o.line || "CFE5EE", width: 0.75 },
    rectRadius: 0.5,
  });
  tx(s, text, {
    x: o.x, y: o.y, w: o.w, h: o.h || 0.44, fontSize: o.fs || 15.5,
    bold: o.bold !== false, color: o.color || C.teal,
    align: "center", valign: "mid", fontFace: o.mono ? F.code : F.body,
  });
}

const KW = new Set(["import", "as", "print", "for", "in", "if", "else", "elif", "try", "except",
  "def", "return", "True", "False", "None", "and", "or", "not", "with", "from", "while"]);

function hl(code) {
  const runs = [];
  const lines = code.split("\n");
  lines.forEach((line, li) => {
    const re = /(#.*$)|("[^"]*"|'[^']*')|\b(\d+\.?\d*)\b|\b([A-Za-z_][A-Za-z0-9_]*)\b/g;
    let last = 0;
    let m;
    const parts = [];
    while ((m = re.exec(line)) !== null) {
      if (m.index > last) parts.push({ t: line.slice(last, m.index), c: C.codeText });
      if (m[1]) parts.push({ t: m[1], c: "6F93A3", i: true });
      else if (m[2]) parts.push({ t: m[2], c: C.amber });
      else if (m[3]) parts.push({ t: m[3], c: "F08A7C" });
      else if (m[4]) {
        const w = m[4];
        if (KW.has(w)) parts.push({ t: w, c: "6FD0E4" });
        else if (["np", "numpy"].includes(w)) parts.push({ t: w, c: "8AD9C0" });
        else parts.push({ t: w, c: C.codeText });
      }
      last = re.lastIndex;
    }
    if (last < line.length) parts.push({ t: line.slice(last), c: C.codeText });
    if (parts.length === 0) parts.push({ t: " ", c: C.codeText });
    parts.forEach((p, i) => {
      runs.push({
        text: p.t,
        options: {
          color: p.c,
          italic: !!p.i,
          breakLine: li < lines.length - 1 && i === parts.length - 1,
        },
      });
    });
  });
  return runs;
}

function codePanel(s, o) {
  const fs = o.fs || TYPE.code;
  const bar = 0.34;
  s.addShape(S.roundRect, {
    x: o.x, y: o.y, w: o.w, h: o.h,
    fill: { color: C.code }, line: { color: "163B4C", width: 0.75 }, rectRadius: 0.05,
  });
  s.addShape(S.rect, {
    x: o.x, y: o.y, w: o.w, h: bar,
    fill: { color: C.codeBar }, line: { color: C.codeBar, width: 0 },
  });
  tx(s, o.title || "python", {
    x: o.x + 0.16, y: o.y + 0.07, w: o.w - 1.0, h: 0.22,
    fontSize: 10.5, color: "8FB6C8", fontFace: F.code,
  });
  [C.coral, C.amber, C.green].forEach((col, i) => {
    s.addShape(S.ellipse, {
      x: o.x + o.w - 0.62 + i * 0.17, y: o.y + 0.13, w: 0.09, h: 0.09,
      fill: { color: col }, line: { color: col, width: 0 },
    });
  });
  s.addText(hl(o.code), {
    x: o.x + 0.18, y: o.y + 0.45, w: o.w - 0.32, h: o.h - 0.52,
    fontFace: F.code, fontSize: fs, color: C.codeText, margin: 0,
    valign: "top", lineSpacingMultiple: 1.0, paraSpaceAfter: 0,
  });
}

function outPanel(s, o) {
  s.addShape(S.roundRect, {
    x: o.x, y: o.y, w: o.w, h: o.h,
    fill: { color: C.white }, line: { color: "CFE5EE", width: 0.75 }, rectRadius: 0.05,
  });
  tx(s, o.label || "KẾT QUẢ", {
    x: o.x + 0.16, y: o.y + 0.1, w: o.w - 0.3, h: 0.2,
    fontSize: 10.5, bold: true, color: C.green, charSpacing: 1.1,
  });
  s.addText(o.text, {
    x: o.x + 0.16, y: o.y + 0.38, w: o.w - 0.3, h: o.h - 0.46,
    fontFace: F.code, fontSize: o.fs || TYPE.code, color: o.color || C.ink,
    margin: 0, valign: "top", lineSpacingMultiple: 1.0,
  });
}

function grid(s, o) {
  const cw = o.cw, ch = o.ch;
  const hi = o.hi || {};
  for (let r = 0; r < o.rows; r++) {
    for (let c = 0; c < o.cols; c++) {
      const key = r + "," + c;
      const fill = hi[key] || o.fill || C.ice;
      const tc = hi[key] ? C.white : (o.color || C.ink);
      s.addShape(S.rect, {
        x: o.x + c * cw, y: o.y + r * ch, w: cw, h: ch,
        fill: { color: fill }, line: { color: o.line || "A9CDDB", width: 0.75 },
      });
      tx(s, String(o.vals[r][c]), {
        x: o.x + c * cw, y: o.y + r * ch, w: cw, h: ch,
        align: "center", valign: "mid", fontSize: o.fs || TYPE.table,
        bold: !!o.bold, color: tc, fontFace: F.code,
      });
    }
  }
}

function label(s, text, o = {}) {
  tx(s, text, Object.assign({ fontSize: TYPE.caption, color: C.muted, fontFace: F.body }, o));
}

function arrow(s, x1, y1, x2, y2, o = {}) {
  s.addShape(S.line, {
    x: x1, y: y1, w: x2 - x1, h: y2 - y1,
    line: {
      color: o.color || C.teal, width: o.w || 1.5,
      endArrowType: o.end === false ? "none" : "triangle",
      beginArrowType: o.begin ? "triangle" : "none",
      dashType: o.dash || "solid",
    },
  });
}

function note(s, text, o = {}) {
  tx(s, text, Object.assign({
    x: 0.6, y: 6.35, w: 12.13, h: 0.5, fontSize: TYPE.body,
    italic: true, color: C.muted, valign: "mid",
  }, o));
}

module.exports = {
  pptxgen, C, F, TOTAL, TYPE, deck, tx, bg, header, footer, card, chip,
  codePanel, outPanel, grid, label, arrow, note,
};
