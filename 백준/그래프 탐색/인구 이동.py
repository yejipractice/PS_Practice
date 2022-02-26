from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


xx = [0, 0, 1, -1]
yy = [1, -1, 0, 0]


def bfs(x, y):
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    total = []
    total.append(graph[x][y])
    nodes = []
    nodes.append((x, y))
    while queue:
        now_x, now_y = queue.popleft()
        for i in range(4):
            dx, dy = now_x+xx[i], now_y+yy[i]
            if 0 <= dx < n and 0 <= dy < n and visited[dx][dy] == 0:
                diff = abs(graph[now_x][now_y]-graph[dx][dy])
                if l <= diff <= r:
                    visited[dx][dy] = 1
                    nodes.append((dx, dy))
                    total.append(graph[dx][dy])
                    queue.append((dx, dy))
    if len(total) == 1:
        return False
    result = sum(total)//len(total)
    for nodex, nodey in nodes:
        graph[nodex][nodey] = result
    return True


time = 0
while 1:
    visited = [[0 for i in range(n)]for j in range(n)]
    isChanged = False
    for i in range(n):  # 모든 국가에 대해 이동이 있는지 시뮬레이션 해보기
        for j in range(n):
            if visited[i][j] == 0:
                res = bfs(i, j)
                if res:
                    isChanged = True
    if isChanged == False:  # 이동이 없음 확인
        print(time)
        break
    time += 1
