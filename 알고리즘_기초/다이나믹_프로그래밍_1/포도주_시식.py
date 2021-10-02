import sys
input = sys.stdin.readline

n = int(input())
drinks = [0]
for _ in range(n):
    drinks.append(int(input()))

dp = [0 for i in range(n+1)]

if n <= 2:
    print(sum(drinks[:n+1]))
elif n == 3:
    s = sum(drinks[:n+1])
    dp[3] = max(s-drinks[1], s-drinks[2])
    dp[3] = max(s-drinks[3], dp[3])
    print(dp[3])
else:
    dp[1] = drinks[1]
    dp[2] = drinks[1]+drinks[2]
    s = sum(drinks[:3+1])
    dp[3] = max(s-drinks[1], s-drinks[2])
    dp[3] = max(s-drinks[3], dp[3])
    for i in range(4, n+1):
        dp[i] = max(dp[i-2]+drinks[i], dp[i-1])
        dp[i] = max(dp[i], dp[i-3]+drinks[i-1]+drinks[i])

    print(dp[n])

# 1)  _ 0 x 0
# 2)  0 x 0 0
# 3)  _ _ 0 x
# 세 가지 경우를 고려해야 함
