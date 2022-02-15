import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))
xx = [0, 0, 1, -1]
yy = [1, -1, 0, 0]
visited = [[-1 for i in range(n)]for j in range(m)]

# bfs로 구현했다가 망하고 참고. bfs 연습을 더 많이 해서 dfs 적용 연습 부족인 듯
# 이걸 어떻게 생각해내지... ?


def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for i in range(4):
        dx, dy = x+xx[i], y+yy[i]
        if 0 <= dx < m and 0 <= dy < n and graph[dx][dy] < graph[x][y]:
            visited[x][y] += dfs(dx, dy)
    return visited[x][y]


print(dfs(0, 0))
