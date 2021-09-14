import sys
input = sys.stdin.readline

A, B = map(int, input().split())
idx = int(input())
AList = list(map(int, input().split()))

idx -= 1
res = 0
for a in AList:
    res += a*(A**idx)
    idx -= 1

BList = []
while 1:
    if res <= 0:
        break
    r = res % B
    res = res//B
    BList.append(r)

while BList:
    print(BList.pop(), end=" ")
