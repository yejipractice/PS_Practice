import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

if n >= 2:
    dp[2] = 3

for i in range(4, n+1, 2):
    dp[i] += dp[i-2]*3
    for j in range(4, i, 2):
        dp[i] += 2*dp[i-j]
    dp[i] += 2

print(dp[-1])

# 점화식 찾기가 어려운 케이스
