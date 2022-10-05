import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

sharks = deque()

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            sharks.append((i, j, 0))
            graph[i][j] = -1

xx = [0, 0, 1, -1, -1, -1, 1, 1]
yy = [1, -1, 0, 0, -1, 1, 1, -1]

while sharks:
    now_x, now_y, dis = sharks.popleft()
    for idx in range(8):
        dx, dy = now_x+xx[idx], now_y+yy[idx]
        if 0<=dx<n and 0<=dy<m:
            if graph[dx][dy]==0 or dis+1 < graph[dx][dy]:
                graph[dx][dy] = dis+1
                sharks.append((dx, dy, dis+1))

res = -1
for g in graph:
    res = max(res, max(g))

print(res)