from collections import deque

m, n, k = map(int, input().split())

graph = [[0 for i in range(n)]for j in range(m)]

for _ in range(k):  # 까다로운 인덱스 구현
    a, b, c, d = map(int, input().split())
    for x in range(m-d, m-b):
        for y in range(a, c):
            graph[x][y] = 1

cases = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(xx, yy):
    queue = deque()
    queue.append((xx, yy))
    cnt = 0
    while queue:
        now_x, now_y = queue.popleft()
        graph[now_x][now_y] = 1
        cnt += 1
        for case in cases:
            dx, dy = now_x+case[0], now_y+case[1]
            if 0 <= dx < m and 0 <= dy < n and graph[dx][dy] == 0:
                graph[dx][dy] = 1
                queue.append((dx, dy))
    return cnt


answer = []  # 빈공간 bfs
for x in range(m):
    for y in range(n):
        if graph[x][y] == 0:
            answer.append(bfs(x, y))

answer.sort()
print(len(answer))
print(*answer)
