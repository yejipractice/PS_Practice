from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = combinations([i for i in range(1, n+1)], m)

for i in result:
    print(*i)
