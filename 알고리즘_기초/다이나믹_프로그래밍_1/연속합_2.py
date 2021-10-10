import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [[0]*n for _ in range(2)]

dp[0][0], dp[1][0] = nums[0], nums[0]

for i in range(1, n):
    dp[0][i] = max(dp[1][i-1], dp[0][i-1]+nums[i])
    dp[1][i] = max(dp[1][i-1] + nums[i], nums[i])

print(max(max(dp[0]), max(dp[1])))

# 제거할 횟수가 남아있는 배열은 dp[1]에, 제거를 할 횟수가 남아 있지 않은 배열은 dp[0]에 저장
