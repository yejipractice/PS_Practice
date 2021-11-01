from itertools import combinations
import sys
input = sys.stdin.readline

while 1:
    nums = list(map(int, input().split()))
    if nums == [0]:
        break
    array = list(combinations(sorted(nums[1:]), 6))
    for a in array:
        print(*a)
    print()
