from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]
result = permutations(nums, m)
for i in result:
    print(*i)
