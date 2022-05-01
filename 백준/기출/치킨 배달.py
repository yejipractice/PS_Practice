from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

stores = []
houses = []

for i in range(n):
    for j in range(n):
        now = graph[i][j]
        if now == 1:
            houses.append((i, j))
        elif now == 2:
            stores.append((i, j))

INF = float('inf')

answer = INF

for arr in combinations(stores, m):
    sum = 0
    for hx, hy in houses:
        min_len = INF
        for sx, sy in arr:
            len = abs(hx-sx) + abs(hy-sy)
            min_len = min(min_len, len)
        sum += min_len
    answer = min(answer, sum)

print(answer)
