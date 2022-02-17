import sys
input = sys.stdin.readline

success = "HaruHaru"
fail = "Hing"

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

xx = [0, 1]
yy = [1, 0]

answer = fail

visited = [[0 for i in range(n)]for j in range(n)]


def dfs(x, y):
    global answer
    visited[x][y] = 1
    if x == y == n-1:
        answer = success
    g = graph[x][y]
    if g != 0:
        for i in range(2):
            dx, dy = x+g*xx[i], y+g*yy[i]
            if 0 <= dx < n and 0 <= dy < n and visited[dx][dy] == 0:
                dfs(dx, dy)


dfs(0, 0)
print(answer)
