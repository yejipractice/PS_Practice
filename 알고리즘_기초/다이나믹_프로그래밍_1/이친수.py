import sys
input = sys.stdin.readline

n = int(input())

memo = [[0, 0] for _ in range(90+1)]
memo[1][1] = 1

for i in range(2, n+1):
    for j in range(2):
        if j == 1:
            memo[i][j] = memo[i-1][0]
        else:
            memo[i][j] = sum(memo[i-1])

print(sum(memo[n]))
