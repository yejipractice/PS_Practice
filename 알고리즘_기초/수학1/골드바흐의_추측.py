import sys
input = sys.stdin.readline

INF = 1000000

check = [True for _ in range(INF)]

for i in range(2, int(INF ** 0.5)+1):
    if check[i] == True:
        for j in range(i*2, INF, i):
            if check[j] == True:
                check[j] = False

while 1:
    n = int(input())

    if n == 0:
        break
    for i in range(3, INF):
        if check[i] == True:
            if check[n-i] == True:
                print("%d = %d + %d" % (n, i, n-i))
                break
