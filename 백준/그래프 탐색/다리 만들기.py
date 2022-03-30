from collections import deque
import sys
input = sys.stdin.readline

INF = float('inf')

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

xx = [0, 0, 1, -1]
yy = [1, -1, 0, 0]


def bfs(start_x, start_y, mark):
    queue1 = deque()
    queue1.append((start_x, start_y))
    graph[start_x][start_y] = mark
    while queue1:
        now_x, now_y = queue1.popleft()
        for idx in range(4):
            next_x, next_y = now_x+xx[idx], now_y+yy[idx]
            if 0 <= next_x < n and 0 <= next_y < n and graph[next_x][next_y] == 1:
                graph[next_x][next_y] = mark
                queue1.append((next_x, next_y))


def bfs2(start_x, start_y, visited):
    queue2 = deque()
    queue2.append((start_x, start_y, 0))
    start = graph[start_x][start_y]
    while queue2:
        now_x, now_y, time = queue2.popleft()
        for idx in range(4):
            next_x, next_y = now_x+xx[idx], now_y+yy[idx]
            if 0 <= next_x < n and 0 <= next_y < n:
                if start == graph[next_x][next_y]:
                    continue
                if graph[next_x][next_y] == 0:  # 로직 실수: 조건문에서 and를 사용하면 예외 발생 가능, 차라리 이중 조건
                    if time+1 < visited[next_x][next_y]:
                        queue2.append((next_x, next_y, time+1))
                        visited[next_x][next_y] = time+1
                elif graph[next_x][next_y] != start:
                    visited[next_x][next_y] = min(
                        time, visited[next_x][next_y])


mark = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j, mark)
            mark += 1

visited = [[INF for _ in range(n)]for __ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            bfs2(i, j, visited)

answer = INF
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            answer = min(answer, visited[i][j])

print(answer)

# 핵심은 dp 사용하기
