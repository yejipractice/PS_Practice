from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

a = list(permutations(nums, m))
a.sort()

for i in a:
    print(*i)
