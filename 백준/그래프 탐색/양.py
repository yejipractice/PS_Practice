import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

r, c = map(int, input().split())
graph = []
total_wolf = 0
total_sheep = 0
for _ in range(r):
    line = list(input().rstrip())
    graph.append(line)
    total_sheep += line.count("o")
    total_wolf += line.count("v")


def dfs(x, y):
    global wolf, sheep
    if graph[x][y] == "v":
        wolf += 1
    elif graph[x][y] == "o":
        sheep += 1
    graph[x][y] = "x"
    for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dx, dy = x+xx, y+yy
        if 0 <= dx < r and 0 <= dy < c and graph[dx][dy] != "#" and graph[dx][dy] != "x":
            dfs(dx, dy)


for i in range(r):
    for j in range(c):
        if graph[i][j] != "x" and graph[i][j] != "#":
            wolf, sheep = 0, 0
            dfs(i, j)
            if sheep > wolf:
                total_wolf -= wolf
            else:
                total_sheep -= sheep

print(total_sheep, total_wolf)
