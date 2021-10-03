from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
a = list(combinations(nums, m))


for i in a:
    print(*i)
