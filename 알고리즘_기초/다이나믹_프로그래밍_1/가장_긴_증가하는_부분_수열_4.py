import sys
input = sys.stdin.readline

n = int(input())

dp = [1 for i in range(n)]

nums = list(map(int, input().split()))
ans = [i for i in range(n)]

max_idx = 0

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
            ans[i] = j

        if dp[max_idx] < dp[i]:
            max_idx = i

# 역추적
tmp = []
while max_idx != ans[max_idx]:
    tmp.append(nums[max_idx])
    max_idx = ans[max_idx]
tmp.append(nums[max_idx])
tmp.reverse()

print(max(dp))
print(*tmp)
