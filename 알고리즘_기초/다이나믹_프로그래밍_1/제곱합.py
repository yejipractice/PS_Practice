import sys
input = sys.stdin.readline

n = int(input())
dp = [i for i in range(n+1)]

for i in range(2, int(n**(1/2)+1)):
    dp[i**2] = 1


for i in range(2, n+1):
    for j in range(i-1, i//2-1, -1):
        if dp[i] > dp[j]+dp[i-j]:
            dp[i] = dp[j]+dp[i-j]

print(dp[-1])

# min보다 if절이 빠름
# min을 사용할 경우 비교한 다음 할당하는데, if를 사용하면 해당하지 않는 경우 바로 넘어가므로.
# 시간 초과 주의
