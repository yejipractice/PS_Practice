import sys
input = sys.stdin.readline

INF = 1000000
mod = 1000000009
dp = [0 for i in range(INF+1)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, INF+1):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % mod

n = int(input())
for _ in range(n):
    print(dp[int(input())])
