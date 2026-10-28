from PIL import Image, ImageDraw
from pathlib import Path

src = Path("render")
files = sorted(src.glob("slide-*.png"))
cols, rows = 5, 5
tw, th = 384, 216
pad = 14
label_h = 20
sheet = Image.new("RGB", (cols * (tw + pad) + pad, rows * (th + label_h + pad) + pad), "#E8EEF2")
d = ImageDraw.Draw(sheet)
for i, f in enumerate(files):
    im = Image.open(f).convert("RGB").resize((tw, th), Image.LANCZOS)
    x = pad + (i % cols) * (tw + pad)
    y = pad + (i // cols) * (th + label_h + pad)
    sheet.paste(im, (x, y))
    d.rectangle([x, y, x + tw - 1, y + th - 1], outline="#B9CBD6")
    d.text((x + 4, y + th + 4), f"Slide {i + 1:02d}", fill="#26414F")
sheet.save(src / "contact.png")
print("contact", sheet.size)
