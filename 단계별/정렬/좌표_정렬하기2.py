import sys
input = sys.stdin.readline

N = int(input())

list = []

for _ in range(N):
    a, b = map(int, input().split())
    list.append([b, a])

list.sort(key=lambda x: (x[0], x[1]))

for i in list:
    print(i[1], i[0])
