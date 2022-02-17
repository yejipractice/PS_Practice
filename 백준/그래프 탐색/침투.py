import sys
sys.setrecursionlimit(3000000)

m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input())))


def dfs(x, y):
    graph[x][y] = -1
    for xx, yy in ([(0, 1), (0, -1), (1, 0), (-1, 0)]):
        dx, dy = x+xx, y+yy
        if 0 <= dx < m and 0 <= dy < n and graph[dx][dy] == 0:
            dfs(dx, dy)


for i in range(n):
    if graph[0][i] == 0:
        dfs(0, i)

if -1 in graph[-1]:
    print("YES")
else:
    print("NO")
