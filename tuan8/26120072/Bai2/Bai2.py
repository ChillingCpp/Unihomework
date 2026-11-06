import sys

input = sys.stdin.readline

m = int(input())
a = [list(map(int, input().split())) for _ in range(m)]
res = [x for row in a for x in row]
print(*res)
