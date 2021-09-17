import sys
input = sys.stdin.readline

n = int(input())

memo = [0] * (11+1)
memo[1] = 1
memo[2] = 2
memo[3] = 1+1+2
for i in range(4, 11+1):
    memo[i] = memo[i-3]+memo[i-2]+memo[i-1]

for _ in range(n):
    i = int(input())
    print(memo[i])
