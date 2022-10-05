import sys
input = sys.stdin.readline

n, m = map(int, input().split())

INF = -float('inf')

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

up = [[INF for i in range(m)]for j in range(n)]

down = [[INF for i in range(m)]for j in range(n)]

# up: (-1, 0) (0, 1)
# down: (1, 0) (0, 1)

up[n-1][0] = graph[n-1][0]
down[n-1][m-1] = graph[n-1][m-1]

# up dp[x][y] = max(dp[x][y-1], dp[x+1][y])+now
for x in range(n-1, -1, -1):
    for y in range(0, m):
        dx1, dy1 = x, y-1
        dx2, dy2 = x+1, y
        if 0<=dx1<n and 0<=dy1<m:
            if 0<=dx2<n and 0<=dy2<m:
                up[x][y] = max(up[dx2][dy2], up[dx1][dy1])+graph[x][y]
            else:
                up[x][y] = up[dx1][dy1]+graph[x][y]
        else:
            if 0<=dx2<n and 0<=dy2<m:
                up[x][y] = up[dx2][dy2]+graph[x][y]

# down dp[x][y] = max(dp[x][y-1], dp[x-1][y])+now
for x in range(n-1, -1, -1):
    for y in range(m-1, -1, -1):
        dx1, dy1 = x, y-1
        dx2, dy2 = x-1, y
        if 0<=dx1<n and 0<=dy1<m:
            if down[dx1][dy1] == INF:
                down[dx1][dy1] = down[x][y]+graph[dx1][dy1]
            else:
                down[dx1][dy1] = max(down[x][y]+graph[dx1][dy1], down[dx1][dy1])
        if 0<=dx2<n and 0<=dy2<m:
            if down[dx2][dy2] == INF:
                down[dx2][dy2] = down[x][y]+graph[dx2][dy2]
            else:
                down[dx2][dy2] = max(down[x][y]+graph[dx2][dy2], down[dx2][dy2]) 

result = INF
for i in range(n):
    for j in range(m):
        result = max(result, up[i][j]+down[i][j])
    
print(result)