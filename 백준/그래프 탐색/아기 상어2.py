from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
distance = -1
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

xx = [0, 1, 1, 1, 0, -1, -1, -1]
yy = [1, 1, 0, -1, -1, -1, 0, 1]


def bfs(x, y):
    queue = deque()
    visited = [[False for i in range(m)]for j in range(n)]
    queue.append((x, y, 0))
    while queue:
        now_x, now_y, cnt = queue.popleft()
        if graph[now_x][now_y] == 1:
            return cnt
        for i in range(len(xx)):
            dx, dy = now_x+xx[i], now_y+yy[i]
            if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == False:
                queue.append((dx, dy, cnt+1))
                visited[dx][dy] = True
    return 0


for i in range(n):
    for j in range(m):
        distance = max(bfs(i, j), distance)

print(distance)
