import sys
input = sys.stdin.readline

n, num = map(int, input().split())
res = []
while 1:
    if n == 0:
        break
    r = n % num
    n = n // num
    if r >= 10:
        r = chr(ord('A')+(r-10))
    res.append(r)

while res:
    print(res.pop(), end="")
