import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
for x, cnt in Counter(a).items():
    print(x, cnt)
