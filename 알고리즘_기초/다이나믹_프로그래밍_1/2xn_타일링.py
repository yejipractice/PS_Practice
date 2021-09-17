n = int(input())

if n <= 2:
    print(n)
else:
    memo = [0] * (n+1)
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n+1):
        memo[i] = memo[i-1]+memo[i-2]
    print(memo[n] % 10007)

# 규칙 찾은 후 점화식 사용
# dp 문제에서 메모리제이션할 때, index error 조심
