import sys
from pathlib import Path

input = sys.stdin.readline

p = Path(input().strip())
if p.suffix.lower() != ".txt":
    sys.exit()
print(p.read_text(encoding="utf-8"), end="")
