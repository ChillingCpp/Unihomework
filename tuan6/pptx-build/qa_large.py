"""Structural QA for the large-type NumPy deck (stdlib only; lxml is broken here)."""
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}
EMU = 914400
DECK = Path(__file__).with_name("presentation.pptx")
OUT = Path(__file__).with_name("render") / "qa-large.json"


def slide_num(name: str) -> int:
    return int(re.search(r"slide(\d+)\.xml$", name).group(1))


def text_of(el) -> str:
    return "".join(t.text or "" for t in el.findall(".//a:t", NS))


def main() -> int:
    report = {"file": str(DECK), "slides": 0, "notes": 0, "errors": [], "warnings": []}
    with zipfile.ZipFile(DECK) as z:
        bad = z.testzip()
        if bad:
            report["errors"].append(f"ZIP corrupt at {bad}")

        pres = ET.fromstring(z.read("ppt/presentation.xml"))
        size = pres.find("p:sldSz", NS)
        width = int(size.get("cx")) / EMU
        height = int(size.get("cy")) / EMU
        report["size_inches"] = [round(width, 3), round(height, 3)]
        if abs(width - 13.333) > 0.01 or abs(height - 7.5) > 0.01:
            report["errors"].append(f"Unexpected slide size {width:.3f}x{height:.3f}")

        slides = sorted(
            [n for n in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)],
            key=slide_num,
        )
        notes = [n for n in z.namelist() if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", n)]
        report["slides"] = len(slides)
        report["notes"] = len(notes)
        if len(slides) != 25:
            report["errors"].append(f"Expected 25 slides, found {len(slides)}")
        if len(notes) != 25:
            report["errors"].append(f"Expected 25 speaker-note parts, found {len(notes)}")

        sizes = {}
        tables = 0
        pics = 0
        for n in slides:
            root = ET.fromstring(z.read(n))
            idx = slide_num(n)
            all_text = text_of(root)
            font_sizes = []
            for r in root.findall(".//a:r", NS):
                rp = r.find("a:rPr", NS)
                if rp is not None and rp.get("sz"):
                    font_sizes.append(int(rp.get("sz")) / 100)
            sizes[idx] = sorted(set(font_sizes), reverse=True)
            if any(x >= 32 for x in font_sizes):
                pass
            else:
                report["warnings"].append(f"slide {idx}: no run >=32pt")
            if idx > 1 and f"{idx:02d} / 25" not in all_text:
                report["errors"].append(f"slide {idx}: page number missing")
            for sp in root.findall(".//p:sp", NS):
                xfrm = sp.find("p:spPr/a:xfrm", NS)
                if xfrm is None:
                    continue
                off = xfrm.find("a:off", NS)
                ext = xfrm.find("a:ext", NS)
                if off is None or ext is None:
                    continue
                x, y = int(off.get("x")) / EMU, int(off.get("y")) / EMU
                w, h = int(ext.get("cx")) / EMU, int(ext.get("cy")) / EMU
                if x < -0.02 or y < -0.02 or x + w > width + 0.02 or y + h > height + 0.02:
                    report["warnings"].append(
                        f"slide {idx}: shape outside canvas x={x:.2f} y={y:.2f} w={w:.2f} h={h:.2f}"
                    )
            tables += len(root.findall(".//a:tbl", NS))
            pics += len(root.findall(".//p:pic", NS))

        report["tables"] = tables
        report["pictures"] = pics
        report["font_sizes_by_slide"] = sizes

        for n in notes:
            txt = text_of(ET.fromstring(z.read(n))).strip()
            if not txt:
                report["errors"].append(f"empty notes: {n}")

    if report["tables"] < 4:
        report["warnings"].append(f"Expected >=4 native tables, found {report['tables']}")
    if report["pictures"] != 1:
        report["warnings"].append(f"Expected 1 picture (logo), found {report['pictures']}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "font_sizes_by_slide"}, ensure_ascii=False, indent=2))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
