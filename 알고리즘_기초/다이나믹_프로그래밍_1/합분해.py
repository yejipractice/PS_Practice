import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0]*201 for i in range(201)]
mod = 1000000000
# dp[횟수][합]
for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i+1

for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1]+dp[i-1][j]) % mod

print(dp[k][n])

# 예를 들어 3을 3개의 수를 이용해서 만드려면 총 10개의 경우가 나오는데,
# 이는 3을 2개의 숫자로 만드는 경우의 가장 앞에 0을 더해주는 경우와,
# 2를 3개의 숫자로 만드는 경우의 가장 앞에 1을 더해주는 경우의 합이 되는 것이다.
