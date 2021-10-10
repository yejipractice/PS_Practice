from itertools import product, repeat
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
a = list(product(nums, repeat=m))
a = list(set(a))
a.sort()
for i in a:
    print(*i)
