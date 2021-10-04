import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = nums[:]

# 뒤에서부터 앞으로 비교해나감

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+nums[i])

print(max(dp))
