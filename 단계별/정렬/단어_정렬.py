import sys
input = sys.stdin.readline

N = int(input())

lists = []
for _ in range(N):
    lists.append(input().strip())
# 개행 문자 제거 strip

lists = list(set(lists))
lists.sort(key=lambda x: (len(x), x))


for i in lists:
    print(i)
