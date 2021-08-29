import sys
input = sys.stdin.readline

m, n = map(int, input().split())

# 에라토스테네스의 체
sieve = [True] * (n+1)
x = int(n**0.5)

for i in range(2, x+1):
    if sieve[i] == True:
        for j in range(i+i, n+1, i):
            sieve[j] = False

result = [i for i in range(2, n+1) if sieve[i] == True]

for i in result:
    if i >= m:
        print(i)
