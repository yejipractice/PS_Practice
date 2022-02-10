from collections import deque

cases = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        xx, yy = queue.popleft()
        for case in cases:
            dx, dy = xx+case[0], yy+case[1]
            if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 1:
                graph[dx][dy] = 0
                queue.append((dx, dy))


tc = int(input())
for _ in range(tc):
    m, n, k = map(int, input().split())
    graph = [[0 for i in range(m)] for j in range(n)]
    for vg in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    cnt = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                bfs(x, y)
                cnt += 1
    print(cnt)
