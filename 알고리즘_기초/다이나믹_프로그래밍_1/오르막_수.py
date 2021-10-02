import sys
input = sys.stdin.readline

n = int(input())

dp = [1]*(10)
mod = 10007

for i in range(2, n+1):
    d = dp.copy()
    for j in range(10):
        dp[j] = sum(d[:j+1]) % mod

print(sum(dp) % mod)
