import sys
import random

input = sys.stdin.readline

a, b = map(int, input().split())
print(random.randint(a, b))
