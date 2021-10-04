from itertools import combinations_with_replacement  # 중복 가능 조합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
a = list(combinations_with_replacement(nums, m))

for i in a:
    print(*i)
