from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

xx = [0, 0, 1, -1]
yy = [1, -1, 0, 0]


def bfs(start_x, start_y, visited):
    queue = deque()
    queue.append((start_x, start_y, 0))
    visited[start_x][start_y] = True
    result = 0
    while queue:
        now_x, now_y, time = queue.popleft()
        result = max(result, time)
        for idx in range(4):
            next_x, next_y = now_x+xx[idx], now_y+yy[idx]
            if 0 <= next_x < n and 0 <= next_y < m and graph[next_x][next_y] == "L" and visited[next_x][next_y] == False:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, time+1))
    return result


answer = 0
for i in range(n):
    for j in range(m):
        visited = [[False for _ in range(m)] for __ in range(n)]
        if graph[i][j] == "L":
            answer = max(answer, bfs(i, j, visited))

print(answer)
