import sys
input = sys.stdin.readline

n = int(input())

memo = [[0 for i in range(10)] for _ in range(101)]
mod = 1000000000

for i in range(1, 10):
    memo[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            memo[i][j] = memo[i-1][j+1]
        elif j == 9:
            memo[i][j] = memo[i-1][j-1]
        else:
            memo[i][j] = memo[i-1][j-1]+memo[i-1][j+1]

print(sum(memo[n]) % mod)
