import pymupdf

# Read the theory PDF
doc1 = pymupdf.open(r"C:\Users\Admin\Desktop\baitap\tuan3\IP-03-Control Flow Statements.pdf")
text1 = ""
for page in doc1:
    text1 += page.get_text()
doc1.close()

# Read the exercises PDF
doc2 = pymupdf.open(r"C:\Users\Admin\Desktop\baitap\tuan3\IP-03-Exercises.pdf")
text2 = ""
for page in doc2:
    text2 += page.get_text()
doc2.close()

# Write to file to avoid encoding issues
with open(r"C:\Users\Admin\Desktop\baitap\pdf_content.txt", "w", encoding="utf-8") as f:
    f.write("=== THEORY PDF ===\n")
    f.write(text1)
    f.write("\n\n=== EXERCISES PDF ===\n")
    f.write(text2)

print("Done! Content written to pdf_content.txt")
