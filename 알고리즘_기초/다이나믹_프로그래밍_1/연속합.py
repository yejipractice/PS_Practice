import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

max_sum = nums[0]
for i in range(n):
    for j in range(i, n):
        max_sum = max(sum(nums[i:j+1]), max_sum)

print(max_sum)
