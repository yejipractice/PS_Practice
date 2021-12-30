import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
if sum(nums) == s:
    ans += 1

for i in range(1, len(nums)):
    cases = list(combinations(nums, i))
    for case in cases:
        if sum(case) == s:
            ans += 1

print(ans)
