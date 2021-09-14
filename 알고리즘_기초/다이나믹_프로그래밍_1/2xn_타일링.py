n = int(input())

memo = [0] * (n+1)
memo[1] = 1
memo[2] = 2
if n <= 2:
    print(memo[n])
else:
    for i in range(3, n+1):
        memo[i] = memo[i-1]+memo[i-2]
    print(memo[n] % 10007)

# 규칙 찾은 후 점화식 사용
