N = int(input())

for i in range(N):
    result = 0
    x, y = map(int, input().split())
    distance = y - x
    n = int(distance**(1/2))
    if n ** 2 == distance:
        result = 2*n-1
    elif distance > n**2 and distance <= n**2 + n:
        result = 2*n
    else:
        result = 2*n+1

    print(result)

# 1+2+...+(n-1)+n+(n-1)+...+2+1 = n^2
