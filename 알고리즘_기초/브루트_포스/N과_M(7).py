from itertools import product, repeat
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
a = list(product(nums, repeat=m))

for i in a:
    print(*i)
