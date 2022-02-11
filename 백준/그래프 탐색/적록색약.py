import copy
from collections import deque

n = int(input())

graph = []

cases = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(x, y, char1, char2, graph):
    queue = deque()
    queue.append((x, y))
    while queue:
        now_x, now_y = queue.popleft()
        graph[now_x][now_y] = "O"
        for case in cases:
            dx, dy = now_x+case[0], now_y+case[1]
            if 0 <= dx < n and 0 <= dy < n:
                if graph[dx][dy] == char1 or graph[dx][dy] == char2:
                    queue.append((dx, dy))
                    graph[dx][dy] = "O"


for _ in range(n):
    graph.append(list(map(str, input())))

graph2 = copy.deepcopy(graph)  # 색약을 위한 그래프, visited를 동시에 하기 위해 따로
ans1 = 0
ans2 = 0
for i in range(n):  # 색약 아닌 경우의 bfs
    for j in range(n):
        if graph[i][j] != "O":  # 방문하면 "O" 다른 문자로 갱신
            bfs(i, j, graph[i][j], graph[i][j], graph)
            ans1 += 1

for i in range(n):
    for j in range(n):  # 색약인 경우의 bfs
        if graph2[i][j] == "R" or graph2[i][j] == "G":
            bfs(i, j, "R", "G", graph2)
            ans2 += 1
            continue
        elif graph2[i][j] == "B":
            bfs(i, j, "B", "B", graph2)
            ans2 += 1

print(ans1, ans2)
