import sys
input = sys.stdin.readline

n = int(input())
cost = [[0, 0, 0]]
for i in range(n):
    cost.append(list(map(int, input().split())))


dp = [[0]*3 for _ in range(n+1)]
dp[1][0] = cost[1][0]
dp[1][1] = cost[1][1]
dp[1][2] = cost[1][2]

for i in range(2, n+1):
    dp[i][0] = min(dp[i-1][1]+cost[i][0], dp[i-1][2]+cost[i][0])
    dp[i][1] = min(dp[i-1][0]+cost[i][1], dp[i-1][2]+cost[i][1])
    dp[i][2] = min(dp[i-1][1]+cost[i][2], dp[i-1][0]+cost[i][2])

print(min(dp[n]))
