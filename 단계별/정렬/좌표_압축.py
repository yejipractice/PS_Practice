import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

ranks = sorted(list(set(nums)))

for i in nums:
    print(ranks.index(i), end=" ")

# 시간초과
