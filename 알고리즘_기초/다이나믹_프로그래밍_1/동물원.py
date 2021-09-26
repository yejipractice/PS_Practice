import sys
input = sys.stdin.readline

n = int(input())

# no, left, right <<로 나눠 생각하는 것이 핵심
dp = [1, 1, 1]
mod = 9901

for i in range(2, n+1):
    d = dp.copy()
    dp[0] = sum(d) % mod
    dp[1] = d[0]+d[2] % mod
    dp[2] = d[0]+d[1] % mod

print(sum(dp) % mod)
