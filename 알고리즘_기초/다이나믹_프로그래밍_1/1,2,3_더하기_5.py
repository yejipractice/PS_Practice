import sys
input = sys.stdin.readline

INF = 100000
mod = 1000000009

memo = [[0]*4 for _ in range(INF+1)]
memo[1] = [0, 1, 0, 0]
memo[2] = [0, 0, 1, 0]
memo[3] = [0, 1, 1, 1]

for i in range(4, INF+1):
    memo[i][1] = memo[i-1][2] % mod+memo[i-1][3] % mod
    memo[i][2] = memo[i-2][1] % mod+memo[i-2][3] % mod
    memo[i][3] = memo[i-3][1] % mod+memo[i-3][2] % mod

    # mod로 나눠서 저장해야 시간 초과가 안 걸림

n = int(input())
for _ in range(n):
    i = int(input())
    print(sum(memo[i]) % mod)
