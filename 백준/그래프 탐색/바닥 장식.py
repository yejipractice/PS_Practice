import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(input().rstrip()))


def dfs(x, y):
    g = graph[x][y]
    if g == "-":
        for xx, yy in [(0, -1), (0, 1)]:
            dx, dy = x+xx, y+yy
    elif g == "|":
        for xx, yy in [(-1, 0), (1, 0)]:
            dx, dy = x+xx, y+yy
    graph[x][y] = -1
    if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == g:
        dfs(dx, dy)


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != -1:
            dfs(i, j)
            cnt += 1
print(cnt)
