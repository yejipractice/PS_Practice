import sys
input = sys.stdin.readline

n = int(input())
dp = [i for i in range(n+1)]

for i in range(2, int(n**(1/2)+1)):
    dp[i**2] = 1


for i in range(2, n+1):
    for j in range(i-1, i//2-1, -1):
        dp[i] = min(dp[i], dp[j]+dp[i-j])

print(dp[-1])
