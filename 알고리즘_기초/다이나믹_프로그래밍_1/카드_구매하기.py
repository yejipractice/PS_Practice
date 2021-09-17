import sys
input = sys.stdin.readline

n = int(input())

memo = [0]+list(map(int, input().split()))

for i in range(2, n+1):
    for j in range(1, i//2+1):
        memo[i] = max(memo[i], memo[i-j]+memo[j])

print(memo[n])
