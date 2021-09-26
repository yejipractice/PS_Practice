from itertools import product, repeat
# 중복 순열 모듈
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]


res = product(nums, repeat=m)

for i in res:
    print(*i)
