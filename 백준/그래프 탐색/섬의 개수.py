from collections import deque
cases = [[0, 1], [0, -1], [1, 0], [-1, 0],
         [1, 1], [1, -1], [-1, 1], [-1, -1]]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        now_x, now_y = queue.popleft()
        for case in cases:
            dx, dy = now_x+case[0], now_y+case[1]
            if 0 <= dx < h and 0 <= dy < w and graph[dx][dy] == 1:
                graph[dx][dy] = 0
                queue.append((dx, dy))


while 1:
    w, h = map(int, input().split())
    if w+h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
